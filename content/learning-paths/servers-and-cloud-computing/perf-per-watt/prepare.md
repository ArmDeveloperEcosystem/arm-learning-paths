---
title: Prepare the Arm Linux system
description: Install the required tools and save the current CPU frequency settings before changing them.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you will measure

You'll measure power reported by the Linux `hwmon` driver of your machine's processor. On the [System76 Thelio Astra](https://system76.com/desktops/thelio-astra) that the Learning Path was tested on, the `apm_xgene` driver exposes separate CPU and I/O power channels. You can apply the same process to other Arm Linux systems.

Adding these channels gives an estimate of system-on-chip (SoC) power. The estimate doesn't include all power drawn by the workstation. Memory, storage, fans, voltage-conversion losses, and the power supply can consume additional power.

Use the results to compare different CPU frequency configurations on the same system. 

## Install the required software on the system

The workload uses OpenSSL, and the analysis script uses Python 3. The Learning Path was tested on Ubuntu 24.04. You can test other Linux distributions as long as you install OpenSSL, Python 3, and `cpupower`.

Install OpenSSL and `cpupower`:

```bash
sudo apt update
sudo apt install -y openssl linux-tools-common linux-tools-$(uname -r)
```

{{% notice Note %}}
You'll use the `cpupower` utility for a summary view in the next section, but the workload and telemetry scripts read and write CPUFreq sysfs files directly. If `cpupower` is difficult to install on your system, you can skip it without affecting the main workflow.

If the `linux-tools-$(uname -r)` package isn't available for your kernel version, look for an existing `cpupower` binary from another installed `linux-tools` package:

```bash
find /usr/lib/linux-*tools* -name cpupower 2>/dev/null
```

If a binary is found, create a symlink so that it's available on the PATH:

```bash
sudo ln -sf $(find /usr/lib/linux-*tools* -name cpupower | head -1) /usr/local/bin/cpupower
```

This situation is common on systems with custom kernels, where the kernel version doesn't match an available `linux-tools` package. For more information about kernel-tools version mismatches, see the [Perf install guide](/install-guides/perf/).
{{% /notice %}}

Confirm that OpenSSL, Python 3, and `cpupower` are available:

```bash
openssl version
python3 --version
cpupower --version
```

The output is similar to:

```output
OpenSSL 3.0.13 30 Jan 2024 (Library: OpenSSL 3.0.13 30 Jan 2024)
Python 3.12.3
cpupower 7.0.12
Report errors and bugs to linux-pm@vger.kernel.org, please.
```

Record the complete OpenSSL build information with the benchmark results:

```bash
openssl version -a
```

The output is similar to:

```output
OpenSSL 3.0.13 30 Jan 2024 (Library: OpenSSL 3.0.13 30 Jan 2024)
built on: Wed Jul 29 16:55:30 2026 UTC
platform: debian-arm64
options:  bn(64,64)
compiler: gcc -fPIC -pthread -Wa,--noexecstack -Wall -fzero-call-used-regs=used-gpr -DOPENSSL_TLS_SECURITY_LEVEL=2 -Wa,--noexecstack -g -O2 -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer -ffile-prefix-map=/build/openssl-s2Z99D/openssl-3.0.13=. -fstack-protector-strong -fstack-clash-protection -Wformat -Werror=format-security -mbranch-protection=standard -fdebug-prefix-map=/build/openssl-s2Z99D/openssl-3.0.13=/usr/src/openssl-3.0.13-0ubuntu3.12 -DOPENSSL_USE_NODELETE -DOPENSSL_PIC -DOPENSSL_BUILDING_OPENSSL -DNDEBUG -Wdate-time -D_FORTIFY_SOURCE=3
OPENSSLDIR: "/usr/lib/ssl"
ENGINESDIR: "/usr/lib/aarch64-linux-gnu/engines-3"
MODULESDIR: "/usr/lib/aarch64-linux-gnu/ossl-modules"
Seeding source: os-specific
CPUINFO: OPENSSL_armcap=0xbd
```

OpenSSL version and build options can affect cryptographic throughput. Keep them unchanged while you compare CPU frequency configurations.

## Create a working directory

Create a directory for the scripts and results:

```bash
mkdir -p ~/perf-per-watt/results
cd ~/perf-per-watt
```

## Save the current CPUFreq settings

CPU frequency changes apply immediately. Save the current governor and frequency limits before running any experiments.

{{% notice Warning %}}
Run the frequency-control commands only on a system you administer. Changing every CPUFreq policy can affect interactive applications and other users until you restore the original settings or reboot.
{{% /notice %}}

Create a script named `save-cpufreq.sh`:

```bash
cat > save-cpufreq.sh <<'EOF'
#!/usr/bin/env bash
set -eu

state_dir=${1:-cpufreq-state}
mkdir -p "$state_dir"

for policy in /sys/devices/system/cpu/cpufreq/policy*; do
    policy_name=$(basename "$policy")
    mkdir -p "$state_dir/$policy_name"

    cat "$policy/scaling_governor" > "$state_dir/$policy_name/scaling_governor"
    cat "$policy/scaling_min_freq" > "$state_dir/$policy_name/scaling_min_freq"
    cat "$policy/scaling_max_freq" > "$state_dir/$policy_name/scaling_max_freq"
done

echo "Saved CPUFreq settings in $state_dir"
EOF

chmod +x save-cpufreq.sh
```

Run the script to save the current settings:

```bash
./save-cpufreq.sh
```

The output is similar to:

```output
Saved CPUFreq settings in cpufreq-state
```

The script saves the current governor and frequency range for each CPUFreq policy. 

Create a second script named `restore-cpufreq.sh`:

```bash
cat > restore-cpufreq.sh <<'EOF'
#!/usr/bin/env bash
set -eu

state_dir=${1:-cpufreq-state}

if [ ! -d "$state_dir" ]; then
    echo "CPUFreq state directory not found: $state_dir" >&2
    exit 1
fi

for policy in /sys/devices/system/cpu/cpufreq/policy*; do
    policy_name=$(basename "$policy")
    saved_policy="$state_dir/$policy_name"

    if [ ! -d "$saved_policy" ]; then
        echo "Saved state is missing for $policy_name" >&2
        exit 1
    fi

    saved_max=$(cat "$saved_policy/scaling_max_freq")
    saved_min=$(cat "$saved_policy/scaling_min_freq")
    saved_governor=$(cat "$saved_policy/scaling_governor")

    echo "$saved_max" | sudo tee "$policy/scaling_max_freq" > /dev/null
    echo "$saved_min" | sudo tee "$policy/scaling_min_freq" > /dev/null
    echo "$saved_governor" | sudo tee "$policy/scaling_governor" > /dev/null
done

echo "Restored CPUFreq settings from $state_dir"
EOF

chmod +x restore-cpufreq.sh
```

You can restore the original settings at any time:

```bash
./restore-cpufreq.sh
```

CPUFreq settings also return to the platform defaults after a reboot unless another service reapplies them.

## What you've accomplished and what's next

You've now installed the required tools and saved the original CPUFreq settings. 

Next, you'll inspect the controls and sensors that Linux exposes on the system.
