---
title: Compare Linux CPU frequency governors
description: Measure how the powersave, schedutil, and performance governors change OpenSSL throughput, SoC power, and temperature.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a governor configuration script

The governor experiment keeps the hardware minimum and maximum frequency limits unchanged. Only the governor changes between runs.

Create `set-governor.sh`:

```bash
cat > set-governor.sh <<'EOF'
#!/usr/bin/env bash
set -eu

governor=${1:?Usage: $0 GOVERNOR}

for policy in /sys/devices/system/cpu/cpufreq/policy*; do
    if ! grep -qw "$governor" "$policy/scaling_available_governors"; then
        echo "$governor is not available for $(basename "$policy")" >&2
        exit 1
    fi
done

for policy in /sys/devices/system/cpu/cpufreq/policy*; do
    hardware_max=$(cat "$policy/cpuinfo_max_freq")
    hardware_min=$(cat "$policy/cpuinfo_min_freq")

    echo "$hardware_max" | sudo tee "$policy/scaling_max_freq" > /dev/null
    echo "$hardware_min" | sudo tee "$policy/scaling_min_freq" > /dev/null
    echo "$governor" | sudo tee "$policy/scaling_governor" > /dev/null
done

echo "Configured all CPUFreq policies with the $governor governor"
EOF

chmod +x set-governor.sh
```

The script restores the full hardware frequency range before applying the governor. This prevents a frequency cap from an earlier experiment affecting the result.

## Run the powersave test

Configure the `powersave` governor and verify that all policies changed:

```bash
sudo ./set-governor.sh powersave

grep -h . /sys/devices/system/cpu/cpufreq/policy*/scaling_governor \
    | sort -u
```

The expected output is:

```output
powersave
```

Allow the system to settle, then run OpenSSL:

```bash
sleep 60
sudo ./run-openssl.sh governor-powersave 90
```

## Run the schedutil test

Configure `schedutil` and run the same workload:

```bash
sudo ./set-governor.sh schedutil
sleep 60
sudo ./run-openssl.sh governor-schedutil 90
```

This run repeats the baseline configuration. Keeping it in the governor sequence makes it easier to compare runs collected close together under similar room and system conditions.

## Run the performance test

Configure `performance` and run the workload:

```bash
sudo ./set-governor.sh performance
sleep 60
sudo ./run-openssl.sh governor-performance 90
```

## Inspect the frequency traces

Print the minimum, average, and maximum observed frequency for each run:

```bash
for csv in results/governor-*/telemetry.csv; do
    awk -F, '
        NR == 2 { min = max = $3 }
        NR > 1 {
            total += $3
            count++
            if ($3 < min) min = $3
            if ($3 > max) max = $3
        }
        END {
            printf "%s min=%.0f avg=%.0f max=%.0f kHz\n", FILENAME, min, total / count, max
        }
    ' "$csv"
done
```

The `performance` governor should request the highest permitted performance. The `powersave` governor should request the lowest permitted performance. The `schedutil` governor adjusts the request according to scheduler utilization.

Check the measured frequency instead of assuming each governor behaved as expected. Firmware, platform controls, and thermal limits can affect the actual frequency.

## Restore the default configuration

Return to the original settings after the governor tests:

```bash
./restore-cpufreq.sh
```

## What you've accomplished

You collected equivalent workload and telemetry data for three governors while preserving the full frequency range. Next, keep `schedutil` fixed and change only the maximum permitted frequency.

