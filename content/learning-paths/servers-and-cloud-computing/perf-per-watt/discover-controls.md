---
title: Discover CPU frequency and power controls
description: Identify the Linux CPUFreq policies and hwmon channels used to control frequency and measure SoC power and temperature.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Inspect CPUFreq policies

Linux represents each independently controlled CPU frequency domain as a policy directory. List the policies:

```bash
find /sys/devices/system/cpu/cpufreq \
    -maxdepth 1 \
    -type d \
    -name 'policy*' \
    -printf '%f\n' | sort -V
```

Compare the number of policies with the number of online CPUs:

```bash
printf 'CPUFreq policies: '
find /sys/devices/system/cpu/cpufreq -maxdepth 1 -type d -name 'policy*' | wc -l

printf 'Online CPUs: '
nproc
```

On the Thelio Astra used for this Learning Path, each CPU has its own policy. Other Arm systems can group several CPUs into one frequency domain.

Display the controls for the first policy:

```bash
for attribute in \
    affected_cpus \
    related_cpus \
    scaling_driver \
    scaling_available_governors \
    scaling_governor \
    scaling_min_freq \
    scaling_max_freq \
    cpuinfo_min_freq \
    cpuinfo_max_freq \
    cpuinfo_cur_freq \
    scaling_cur_freq \
    boost; do
    printf '%-30s ' "$attribute"
    sudo cat "/sys/devices/system/cpu/cpufreq/policy0/$attribute" 2>/dev/null || echo unsupported
done
```

The Thelio Astra example uses the `cppc_cpufreq` driver. It exposes a range from `1000000` kHz to `2200000` kHz and supports these governors:

```output
conservative ondemand userspace powersave performance schedutil
```

The `userspace` governor isn't useful when `scaling_setspeed` reports `unsupported`. This Learning Path uses `powersave`, `schedutil`, and `performance`.

The `boost` attribute reports `0` because Arm Neoverse server CPUs maintain sustained performance across the full frequency range rather than using a temporary boost mode above the configured maximum.

## View a summary with cpupower

The `cpupower` utility provides a concise view of the same CPUFreq information. It was installed in the previous section.

Display the frequency information for the current CPU:

```bash
cpupower frequency-info
```

The output summarizes the driver, governor, frequency range, and hardware limits in one view:

```output
analyzing CPU 43:
  driver: cppc_cpufreq
  CPUs which run at the same hardware frequency: 43
  CPUs which need to have their frequency coordinated by software: 43
  maximum transition latency:  Cannot determine or is not supported.
  hardware limits: 1000 MHz - 2.20 GHz
  available cpufreq governors: conservative ondemand userspace powersave performance schedutil
  current policy: frequency should be within 1000 MHz and 2.20 GHz.
                  The governor "schedutil" may decide which speed to use
                  within this range.
  current CPU frequency: 1.44 GHz (asserted by call to kernel)
  boost state support:
    Active: no
```

Show the same summary for all CPUs:

```bash
cpupower -c all frequency-info
```

The rest of this Learning Path reads and writes sysfs files directly because the telemetry scripts need programmatic access. The `cpupower` output is useful for quick checks between experiments.

## Locate the hwmon devices

The hwmon directory numbers can change after a kernel update or reboot. Identify devices by reading their `name` files instead of assuming fixed numbers:

```bash
for device in /sys/class/hwmon/hwmon*; do
    printf '%s: ' "$device"
    cat "$device/name"
done
```

The output on a Thelio Astra includes:

```output
/sys/class/hwmon/hwmon0: nvme
/sys/class/hwmon/hwmon1: apm_xgene
/sys/class/hwmon/hwmon2: system76_thelio_io
/sys/class/hwmon/hwmon3: hidpp_battery_0
```

Find the directory that contains the Ampere processor sensors:

```bash
for device in /sys/class/hwmon/hwmon*; do
    if [ "$(cat "$device/name" 2>/dev/null)" = "apm_xgene" ]; then
        echo "$device"
    fi
done
```

Print the available labels and values:

```bash
for device in /sys/class/hwmon/hwmon*; do
    if [ "$(cat "$device/name" 2>/dev/null)" = "apm_xgene" ]; then
        grep . "$device"/power*_label "$device"/power*_input \
            "$device"/temp*_label "$device"/temp*_input
    fi
done
```

The output is similar to:

```output
/sys/class/hwmon/hwmon1/power1_label:CPU power
/sys/class/hwmon/hwmon1/power2_label:IO power
/sys/class/hwmon/hwmon1/power1_input:12200000
/sys/class/hwmon/hwmon1/power2_input:8025000
/sys/class/hwmon/hwmon1/temp1_label:SoC Temperature
/sys/class/hwmon/hwmon1/temp1_input:37000
```

The hwmon subsystem reports power in microwatts and temperature in millidegrees Celsius. For the sample values:

- CPU power is 12.2 W
- I/O power is 8.025 W
- SoC temperature is 37°C

## Inspect fan telemetry

The System76 Thelio I/O controller exposes fan speed and pulse-width modulation (PWM) values. Print the labels and current readings:

```bash
for device in /sys/class/hwmon/hwmon*; do
    if [ "$(cat "$device/name" 2>/dev/null)" = "system76_thelio_io" ]; then
        grep . "$device"/fan*_label "$device"/fan*_input "$device"/pwm*
    fi
done
```

The output is similar to:

```output
/sys/class/hwmon/hwmon2/fan1_label:CPU Fan
/sys/class/hwmon/hwmon2/fan2_label:Intake Fan
/sys/class/hwmon/hwmon2/fan3_label:GPU Fan
/sys/class/hwmon/hwmon2/fan4_label:Aux Fan
/sys/class/hwmon/hwmon2/fan1_input:1065
/sys/class/hwmon/hwmon2/fan2_input:735
/sys/class/hwmon/hwmon2/fan3_input:0
/sys/class/hwmon/hwmon2/fan4_input:0
/sys/class/hwmon/hwmon2/pwm1:85
/sys/class/hwmon/hwmon2/pwm2:85
/sys/class/hwmon/hwmon2/pwm3:85
/sys/class/hwmon/hwmon2/pwm4:85
```

Record fan speed during each experiment, but leave the fan policy unchanged. Changing frequency and fan control at the same time makes it difficult to identify which setting caused a temperature or performance difference.

## Check whether the sensors update

Read the processor sensors once per second for 10 seconds:

```bash
sensor_dir=$(for device in /sys/class/hwmon/hwmon*; do
    if [ "$(cat "$device/name" 2>/dev/null)" = "apm_xgene" ]; then
        echo "$device"
        break
    fi
done)

for sample in $(seq 1 10); do
    printf '%s ' "$(date --iso-8601=seconds)"
    grep -h . "$sensor_dir"/power*_input "$sensor_dir"/temp*_input | xargs
    sleep 1
done
```

The values should change as background activity changes. A sensor that never updates isn't suitable for measuring workload energy.

## What you've learned

You identified the CPU frequency policies and the CPU power, I/O power, SoC temperature, and fan sensors. The next page creates a logger that reads these values while OpenSSL runs.
