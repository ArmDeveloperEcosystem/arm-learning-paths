---
title: Calculate performance and energy efficiency
description: Integrate sampled SoC power, combine it with OpenSSL throughput, and compare performance per watt and joules per gigabyte.
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Record the OpenSSL throughput

Print the saved OpenSSL output for a run:

```bash
cat results/governor-schedutil/openssl-output.txt
```

Find the SHA-256 value for the 16384 byte buffer. OpenSSL normally reports this value in thousands of bytes per second with a trailing `k`.

Record the numeric portion without the trailing `k`. For example, if OpenSSL reports `1234567.89k`, use `1234567.89` as the throughput in kB/s.

## Create the analysis script

Create `analyze-telemetry.py` in `~/perf-per-watt`:

```python
import csv
import statistics
import sys


def usage():
    print(
        f"Usage: {sys.argv[0]} LABEL TELEMETRY_CSV THROUGHPUT_KB_PER_SECOND",
        file=sys.stderr,
    )
    raise SystemExit(1)


if len(sys.argv) != 4:
    usage()

label = sys.argv[1]
telemetry_path = sys.argv[2]

try:
    throughput_kb_per_second = float(sys.argv[3])
except ValueError:
    usage()

with open(telemetry_path, newline="", encoding="utf-8") as telemetry_file:
    rows = list(csv.DictReader(telemetry_file))

if len(rows) < 2:
    raise SystemExit("At least two telemetry samples are needed")

samples = []

for row in rows:
    samples.append(
        {
            "time": float(row["epoch_seconds"]),
            "freq": float(row["avg_freq_khz"]),
            "cpu_power": float(row["cpu_power_w"]),
            "io_power": float(row["io_power_w"]),
            "soc_power": float(row["soc_power_w"]),
            "temperature": float(row["soc_temp_c"]),
            "cpu_fan": float(row["cpu_fan_rpm"]),
            "intake_fan": float(row["intake_fan_rpm"]),
        }
    )

cpu_energy_j = 0.0
io_energy_j = 0.0
soc_energy_j = 0.0

for previous, current in zip(samples, samples[1:]):
    interval = current["time"] - previous["time"]

    if interval <= 0:
        continue

    cpu_energy_j += interval * (previous["cpu_power"] + current["cpu_power"]) / 2
    io_energy_j += interval * (previous["io_power"] + current["io_power"]) / 2
    soc_energy_j += interval * (previous["soc_power"] + current["soc_power"]) / 2

duration_seconds = samples[-1]["time"] - samples[0]["time"]

if duration_seconds <= 0:
    raise SystemExit("Telemetry timestamps don't contain a positive duration")

average_cpu_power_w = cpu_energy_j / duration_seconds
average_io_power_w = io_energy_j / duration_seconds
average_soc_power_w = soc_energy_j / duration_seconds
average_frequency_mhz = statistics.fmean(sample["freq"] for sample in samples) / 1000
peak_temperature_c = max(sample["temperature"] for sample in samples)
average_cpu_fan_rpm = statistics.fmean(sample["cpu_fan"] for sample in samples)
average_intake_fan_rpm = statistics.fmean(sample["intake_fan"] for sample in samples)

throughput_gb_per_second = throughput_kb_per_second / 1_000_000
total_work_gb = throughput_gb_per_second * duration_seconds
throughput_per_watt = throughput_gb_per_second / average_soc_power_w
energy_per_gb = soc_energy_j / total_work_gb

print(
    "label,duration_s,avg_freq_mhz,throughput_gb_s,avg_cpu_power_w,"
    "avg_io_power_w,avg_soc_power_w,soc_energy_j,throughput_gb_s_per_w,"
    "energy_j_per_gb,peak_temp_c,avg_cpu_fan_rpm,avg_intake_fan_rpm"
)

print(
    f"{label},{duration_seconds:.3f},{average_frequency_mhz:.1f},"
    f"{throughput_gb_per_second:.6f},{average_cpu_power_w:.3f},"
    f"{average_io_power_w:.3f},{average_soc_power_w:.3f},"
    f"{soc_energy_j:.3f},{throughput_per_watt:.9f},{energy_per_gb:.6f},"
    f"{peak_temperature_c:.1f},{average_cpu_fan_rpm:.1f},"
    f"{average_intake_fan_rpm:.1f}"
)
```

The script integrates each pair of consecutive power samples using the trapezoidal rule. This method accounts for power changes during the run instead of multiplying one power reading by the total duration.

## Analyze one run

Run the script with the label, telemetry file, and measured OpenSSL throughput, replacing `THROUGHPUT_KB_PER_SECOND` with the numeric OpenSSL value:

```bash
python3 analyze-telemetry.py \
    governor-schedutil \
    results/governor-schedutil/telemetry.csv \
    THROUGHPUT_KB_PER_SECOND
```

The script prints a CSV header followed by one result row. 

Save the output:

```bash
python3 analyze-telemetry.py \
    governor-schedutil \
    results/governor-schedutil/telemetry.csv \
    THROUGHPUT_KB_PER_SECOND \
    > results/governor-schedutil/summary.csv
```

## Build the comparison table

Repeat the analysis for every run and collect the following fields:

| Configuration | Average frequency (MHz) | SHA-256 throughput | Average SoC power | SoC energy | Throughput per watt | Energy per GB | Peak temperature (°C) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `powersave` | 1000 MHz | 39.6 GB/s | 31.7 W | 2837 J | 1.248 GB/s/W | 0.801 J/GB | 41°C |
| `schedutil` | 2199 MHz | 87.4 GB/s | 48.2 W | 4327 J | 1.811 GB/s/W | 0.552 J/GB | 47°C |
| `performance` | 2200 MHz | 87.4 GB/s | 48.4 W | 4340 J | 1.807 GB/s/W | 0.553 J/GB | 47°C |
| `schedutil`, 1.4 GHz cap | 1400 MHz | 55.5 GB/s | 36.1 W | 3244 J | 1.536 GB/s/W | 0.651 J/GB | 43°C |
| `schedutil`, 1.8 GHz cap | 1799 MHz | 71.4 GB/s | 40.8 W | 3631 J | 1.750 GB/s/W | 0.571 J/GB | 44°C |
| `schedutil`, 2.2 GHz cap | 2200 MHz | 87.3 GB/s | 48.3 W | 4338 J | 1.807 GB/s/W | 0.553 J/GB | 47°C |

Use the table to identify the following:

- The configuration that produces the highest SHA-256 throughput
- The configuration that produces the highest throughput per watt
- The configuration that consumes the fewest joules per gigabyte
- Whether the fastest configuration also uses energy the most efficiently
- Whether a lower frequency reduces temperature and fan speed
- How closely the measured average frequency follows the configured limit

For this CPU-bound SHA-256 workload on the Ampere Altra, `schedutil` at the full 2.2 GHz maximum delivers both the highest throughput and the best energy efficiency. Power scales nearly linearly with frequency on this processor. This means running faster finishes the work sooner and uses less total energy. The `powersave` governor draws fewer watts but takes so much longer that it consumes more joules per gigabyte.

## When a frequency cap is useful

The full-speed result doesn't mean frequency caps are never worthwhile. Consider capping frequency when:

- The deployment is thermally constrained: In a dense chassis or passively-cooled edge system, sustained full frequency can cause throttling. Capping at 1.8 GHz delivers 82% of the throughput at 85% of the power and drops peak temperature by 3°C.
- The rack has a fixed power budget: Running more servers at a lower per-server power draw can produce higher aggregate throughput within the same power envelope.
- The workload is latency-insensitive: Overnight batch jobs, log compression, or background indexing don't need the fastest completion time. Lower power extends hardware lifetime and reduces cooling costs.
- The workload is memory-bound or I/O-bound: OpenSSL SHA-256 is fully CPU-bound. Applications that stall on memory or network I/O often show diminishing throughput returns at higher frequencies, while power keeps climbing. Rerun this workflow with your production workload to find its specific efficiency curve.

## Interpret performance per watt

Throughput per watt measures how much SHA-256 work the SoC completes for each watt of average power:

```text
throughput per watt = throughput in GB/s / average SoC power in W
```

A larger value is better.

Energy per gigabyte measures how much SoC energy is used to process one gigabyte:

```text
energy per GB = SoC energy in J / processed data in GB
```

A smaller value is better.

The configuration with the lowest power isn't necessarily the most energy-efficient. A slow configuration can consume fewer watts but run long enough to use more total energy for the same work.

## What you've accomplished

You've now used standard Linux CPUFreq and `hwmon` interfaces to measure an Arm workload under different power-management configurations. You've collected synchronized frequency, CPU power, I/O power, temperature, and fan telemetry, then calculated throughput per watt and joules per gigabyte.

You can reuse the workflow with another sustained workload by replacing the OpenSSL command and providing a meaningful throughput value to the analysis script.
