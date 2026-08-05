---
title: Establish an OpenSSL performance and power baseline
description: Run a repeatable all-core SHA-256 workload while collecting synchronized SoC power and thermal telemetry.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Use SHA-256 as the workload

The OpenSSL `speed` command measures cryptographic throughput without downloading a dataset or building an application. SHA-256 provides a CPU-intensive server workload with a direct result in bytes processed per second.

Use a fixed `16384`-byte buffer so every run performs the same operation. Use one OpenSSL worker per online CPU to load the full processor.

## Create the workload runner

Create `run-openssl.sh` in `~/perf-per-watt`:

```bash
cat > run-openssl.sh <<'EOF'
#!/usr/bin/env bash
set -eu

label=${1:?Usage: $0 LABEL [SECONDS]}
duration=${2:-90}
result_dir="results/$label"

mkdir -p "$result_dir"

policy=/sys/devices/system/cpu/cpufreq/policy0
cat "$policy/scaling_driver" > "$result_dir/scaling_driver.txt"
cat "$policy/scaling_governor" > "$result_dir/scaling_governor.txt"
cat "$policy/scaling_min_freq" > "$result_dir/scaling_min_freq.txt"
cat "$policy/scaling_max_freq" > "$result_dir/scaling_max_freq.txt"
openssl version -a > "$result_dir/openssl-version.txt"

echo "Warming up all CPUs for 30 seconds"
openssl speed \
    -elapsed \
    -seconds 30 \
    -multi "$(nproc)" \
    -bytes 16384 \
    -evp sha256 \
    > /dev/null 2>&1

echo "Collecting telemetry for $duration seconds"
./collect-telemetry.sh "$result_dir/telemetry.csv" &
logger_pid=$!

cleanup() {
    kill "$logger_pid" 2>/dev/null || true
    wait "$logger_pid" 2>/dev/null || true
}

trap cleanup EXIT INT TERM

openssl speed \
    -elapsed \
    -seconds "$duration" \
    -multi "$(nproc)" \
    -bytes 16384 \
    -evp sha256 \
    2>&1 | tee "$result_dir/openssl-output.txt"

echo "Results saved in $result_dir"
EOF

chmod +x run-openssl.sh
```

The runner performs a 30-second warm-up before collecting results. The warm-up loads OpenSSL code and data, raises CPU activity, and reduces the effect of starting from an idle state.

## Confirm the baseline settings

The initial run uses the current CPUFreq settings. Confirm that the first policy still uses the `schedutil` governor and full frequency range:

```bash
grep . /sys/devices/system/cpu/cpufreq/policy0/{scaling_driver,scaling_governor,scaling_min_freq,scaling_max_freq}
```

On the Thelio Astra example, the baseline is:

```output
scaling_driver:cppc_cpufreq
scaling_governor:schedutil
scaling_min_freq:1000000
scaling_max_freq:2200000
```

If the values differ, restore the saved settings:

```bash
./restore-cpufreq.sh
```

## Run the baseline workload

Allow the system to remain idle for 60 seconds before the run:

```bash
sleep 60
sudo ./run-openssl.sh baseline-schedutil 90
```

The final OpenSSL table contains the aggregate SHA-256 throughput for the `16384`-byte buffer size. Keep the complete output file because OpenSSL output formatting can vary between versions.

List the files captured for the run:

```bash
find results/baseline-schedutil -maxdepth 1 -type f -printf '%f\n' | sort
```

The expected files are:

```output
openssl-output.txt
openssl-version.txt
scaling_driver.txt
scaling_governor.txt
scaling_max_freq.txt
scaling_min_freq.txt
telemetry.csv
```

## Check the telemetry duration

The logger should contain about one sample per second. Count the samples:

```bash
awk 'END { print NR - 1, "telemetry samples" }' results/baseline-schedutil/telemetry.csv
```

A 90-second run should produce approximately 90 samples. A small difference is normal because process startup and shutdown don't align exactly with the sampling interval.

## What you've accomplished

You collected a baseline OpenSSL throughput result and synchronized telemetry using the default CPUFreq configuration. Next, change only the governor and compare its effect.

