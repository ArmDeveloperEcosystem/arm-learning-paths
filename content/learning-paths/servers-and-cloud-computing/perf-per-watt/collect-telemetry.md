---
title: Collect synchronized power and thermal telemetry
description: Create a Linux shell script that records CPU frequency, SoC power, temperature, and fan speed in a CSV file.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create the telemetry logger

The logger finds hwmon devices and channels by name and label. This keeps the script working if Linux assigns different `hwmon` directory numbers after a reboot.

Create `collect-telemetry.sh` in `~/perf-per-watt`:

```bash
cat > collect-telemetry.sh <<'EOF'
#!/usr/bin/env bash
set -eu

output_file=${1:-telemetry.csv}
interval=${2:-1}

find_hwmon() {
    wanted_name=$1

    for device in /sys/class/hwmon/hwmon*; do
        if [ "$(cat "$device/name" 2>/dev/null)" = "$wanted_name" ]; then
            echo "$device"
            return 0
        fi
    done

    return 1
}

find_labeled_input() {
    directory=$1
    sensor_type=$2
    wanted_label=$3

    for label_file in "$directory"/"$sensor_type"*_label; do
        [ -e "$label_file" ] || continue

        if [ "$(cat "$label_file")" = "$wanted_label" ]; then
            echo "${label_file%_label}_input"
            return 0
        fi
    done

    return 1
}

to_watts() {
    awk -v value="$1" 'BEGIN { printf "%.6f", value / 1000000 }'
}

to_celsius() {
    awk -v value="$1" 'BEGIN { printf "%.3f", value / 1000 }'
}

ampere_hwmon=$(find_hwmon apm_xgene) || {
    echo "The apm_xgene hwmon device was not found" >&2
    exit 1
}

thelio_hwmon=$(find_hwmon system76_thelio_io) || {
    echo "The system76_thelio_io hwmon device was not found" >&2
    exit 1
}

cpu_power_file=$(find_labeled_input "$ampere_hwmon" power "CPU power")
io_power_file=$(find_labeled_input "$ampere_hwmon" power "IO power")
soc_temp_file=$(find_labeled_input "$ampere_hwmon" temp "SoC Temperature")
cpu_fan_file=$(find_labeled_input "$thelio_hwmon" fan "CPU Fan")
intake_fan_file=$(find_labeled_input "$thelio_hwmon" fan "Intake Fan")

printf '%s\n' \
    'timestamp,epoch_seconds,avg_freq_khz,cpu_power_w,io_power_w,soc_power_w,soc_temp_c,cpu_fan_rpm,intake_fan_rpm' \
    > "$output_file"

while true; do
    timestamp=$(date --iso-8601=seconds)
    epoch_seconds=$(date +%s.%N)

    avg_freq_khz=$(awk '
        { total += $1; count++ }
        END {
            if (count > 0) {
                printf "%.0f", total / count
            } else {
                print "0"
            }
        }
    ' /sys/devices/system/cpu/cpufreq/policy*/cpuinfo_cur_freq)

    cpu_power_w=$(to_watts "$(cat "$cpu_power_file")")
    io_power_w=$(to_watts "$(cat "$io_power_file")")
    soc_power_w=$(awk -v cpu="$cpu_power_w" -v io="$io_power_w" \
        'BEGIN { printf "%.6f", cpu + io }')
    soc_temp_c=$(to_celsius "$(cat "$soc_temp_file")")
    cpu_fan_rpm=$(cat "$cpu_fan_file")
    intake_fan_rpm=$(cat "$intake_fan_file")

    printf '%s,%s,%s,%s,%s,%s,%s,%s,%s\n' \
        "$timestamp" \
        "$epoch_seconds" \
        "$avg_freq_khz" \
        "$cpu_power_w" \
        "$io_power_w" \
        "$soc_power_w" \
        "$soc_temp_c" \
        "$cpu_fan_rpm" \
        "$intake_fan_rpm" \
        >> "$output_file"

    sleep "$interval"
done
EOF

chmod +x collect-telemetry.sh
```

The script samples every second by default. One-second sampling captures sustained changes without spending excessive time reading sysfs files.

## Test the logger

Start the logger in the background, collect five samples, and stop it:

```bash
sudo ./collect-telemetry.sh telemetry-test.csv &
logger_pid=$!
sleep 5
sudo kill "$logger_pid"
wait "$logger_pid" 2>/dev/null || true
```

Inspect the first records:

```bash
head telemetry-test.csv
```

The output uses this format:

```output
timestamp,epoch_seconds,avg_freq_khz,cpu_power_w,io_power_w,soc_power_w,soc_temp_c,cpu_fan_rpm,intake_fan_rpm
<ISO timestamp>,<epoch seconds>,<average frequency>,<CPU power>,<I/O power>,<SoC power>,<SoC temperature>,<CPU fan>,<intake fan>
```

Your values will differ. Confirm that each row has nine fields and that power, temperature, and fan readings are nonzero.

Count the number of fields in each row:

```bash
awk -F, 'NF != 9 { print "Unexpected field count on line", NR, ":", NF }' telemetry-test.csv
```

No output means every row has the expected number of fields.

## Interpret the recorded values

The logger records these values:

| Column | Meaning |
| --- | --- |
| `avg_freq_khz` | Mean current frequency across CPUFreq policies |
| `cpu_power_w` | CPU-domain power reported by `apm_xgene` |
| `io_power_w` | I/O-domain power reported by `apm_xgene` |
| `soc_power_w` | Sum of CPU and I/O power |
| `soc_temp_c` | SoC temperature |
| `cpu_fan_rpm` | CPU fan speed |
| `intake_fan_rpm` | Chassis intake fan speed |

The average frequency is a system-wide summary. It doesn't show whether individual CPUs ran at different frequencies, but it is sufficient for comparing all-core OpenSSL runs.

## What you've accomplished

You created and tested a CSV telemetry logger. Next, run OpenSSL while the logger records frequency, power, temperature, and fan speed.
