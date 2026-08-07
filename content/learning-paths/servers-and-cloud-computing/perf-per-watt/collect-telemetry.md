---
title: Collect synchronized power and thermal telemetry
description: Create a Linux shell script that records CPU frequency, SoC power, temperature, and fan speed in a CSV file.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create the telemetry logger

The logger finds `hwmon` devices and channels by name and label. The use of both name and label keeps the script working if Linux assigns different `hwmon` directory numbers after a reboot.

Create `collect-telemetry.sh` in `~/perf-per-watt`, replacing `ampere_hwmon` and `thelio_hwmon` with the devices for your system:

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

The output is similar to:

```output
timestamp,epoch_seconds,avg_freq_khz,cpu_power_w,io_power_w,soc_power_w,soc_temp_c,cpu_fan_rpm,intake_fan_rpm
2026-08-06T09:47:56-05:00,1786027676.633482916,1109099,12.240000,8.025000,20.265000,36.000,1065,720
2026-08-06T09:47:57-05:00,1786027677.708797530,1031262,12.280000,8.024000,20.304000,36.000,1065,735
2026-08-06T09:47:58-05:00,1786027678.783871620,1018438,12.360000,8.024000,20.384000,36.000,1065,735
2026-08-06T09:47:59-05:00,1786027679.863988207,1025325,12.360000,8.025000,20.385000,36.000,1065,720
2026-08-06T09:48:00-05:00,1786027680.940551795,1006262,12.360000,8.025000,20.385000,36.000,1065,735
```

Your values will differ. Confirm that each row has nine fields and that power, temperature, and fan readings are nonzero.

Count the number of fields in each row:

```bash
awk -F, 'NF != 9 { print "Unexpected field count on line", NR, ":", NF }' telemetry-test.csv
```

No output means every row has the expected number of fields.

## Interpret the recorded values

The logger records the following values:

| Column | Meaning |
| --- | --- |
| `avg_freq_khz` | Mean current frequency across CPUFreq policies |
| `cpu_power_w` | CPU-domain power reported by `apm_xgene` |
| `io_power_w` | I/O-domain power reported by `apm_xgene` |
| `soc_power_w` | Sum of CPU and I/O power |
| `soc_temp_c` | SoC temperature |
| `cpu_fan_rpm` | CPU fan speed |
| `intake_fan_rpm` | Chassis intake fan speed |

The average frequency is a system-wide summary. It doesn't show whether individual CPUs run at different frequencies, but it's sufficient for comparing OpenSSL runs using all cores.

## What you've accomplished and what's next

You've now created and tested a CSV telemetry logger. 

Next, run OpenSSL while the logger records frequency, power, temperature, and fan speed.
