---
title: Compare CPU maximum-frequency limits
description: Apply CPU frequency caps under the schedutil governor and measure the resulting OpenSSL throughput and SoC energy use.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a frequency-cap script

The frequency-cap experiment uses the `schedutil` governor for every run. The hardware minimum remains unchanged, and the maximum frequency is the only variable.

Create `set-frequency-cap.sh`:

```bash
cat > set-frequency-cap.sh <<'EOF'
#!/usr/bin/env bash
set -eu

target_max=${1:?Usage: $0 MAX_FREQUENCY_KHZ}

case "$target_max" in
    *[!0-9]*|'')
        echo "Frequency must be an integer in kHz" >&2
        exit 1
        ;;
esac

for policy in /sys/devices/system/cpu/cpufreq/policy*; do
    hardware_min=$(cat "$policy/cpuinfo_min_freq")
    hardware_max=$(cat "$policy/cpuinfo_max_freq")

    if [ "$target_max" -lt "$hardware_min" ] || [ "$target_max" -gt "$hardware_max" ]; then
        echo "$target_max is outside the range $hardware_min-$hardware_max for $(basename "$policy")" >&2
        exit 1
    fi
done

for policy in /sys/devices/system/cpu/cpufreq/policy*; do
    hardware_min=$(cat "$policy/cpuinfo_min_freq")

    echo "$hardware_min" | sudo tee "$policy/scaling_min_freq" > /dev/null
    echo "$target_max" | sudo tee "$policy/scaling_max_freq" > /dev/null
    echo schedutil | sudo tee "$policy/scaling_governor" > /dev/null
done

echo "Configured schedutil with a maximum frequency of $target_max kHz"
EOF

chmod +x set-frequency-cap.sh
```

The Thelio Astra used for this Learning Path accepts maximum limits between `1000000` kHz and `2200000` kHz. Other systems can expose a different range.

## Verify an intermediate limit

Apply a `1400000` kHz maximum:

```bash
sudo ./set-frequency-cap.sh 1400000
```

Confirm that every policy accepted the limit:

```bash
grep -h . /sys/devices/system/cpu/cpufreq/policy*/scaling_max_freq \
    | sort -nu
```

The expected output is:

```output
1400000
```

If Linux rounds or rejects the value, select an accepted value within the hardware range and use that value consistently in the remaining steps.

## Run the capped-frequency tests

Run the workload at a `1400000` kHz maximum:

```bash
sleep 60
sudo ./run-openssl.sh cap-1400mhz 90
```

Apply an `1800000` kHz maximum and run the same workload:

```bash
sudo ./set-frequency-cap.sh 1800000
sleep 60
sudo ./run-openssl.sh cap-1800mhz 90
```

Apply the full `2200000` kHz maximum and run the final capped-frequency test:

```bash
sudo ./set-frequency-cap.sh 2200000
sleep 60
sudo ./run-openssl.sh cap-2200mhz 90
```

The `cap-2200mhz` run uses the same limits as the baseline `schedutil` run. The duplicate measurement helps identify normal run-to-run variation.

## Keep the comparison controlled

Use the same conditions for every run:

- Keep the OpenSSL command, worker count, duration, and buffer size unchanged
- Close unrelated CPU-intensive applications
- Leave the fan policy unchanged
- Use the same minimum frequency and governor
- Allow the same idle period before every run
- Keep the system connected to the same power and cooling environment

For publication-quality results, repeat each configuration at least three times and report the median. A single run is sufficient to complete the workflow and check whether the efficiency curves differ.

## Restore the original settings

Restore the CPUFreq settings saved at the beginning:

```bash
./restore-cpufreq.sh
```

Verify the restored governor and limits:

```bash
grep . /sys/devices/system/cpu/cpufreq/policy0/{scaling_governor,scaling_min_freq,scaling_max_freq}
```

The output is similar to:

```output
/sys/devices/system/cpu/cpufreq/policy0/scaling_governor:schedutil
/sys/devices/system/cpu/cpufreq/policy0/scaling_min_freq:1000000
/sys/devices/system/cpu/cpufreq/policy0/scaling_max_freq:2200000
```

## What you've accomplished

You collected OpenSSL and telemetry results under three maximum-frequency limits while keeping the governor fixed. The final page calculates average power, energy, throughput per watt, and joules per gigabyte.

