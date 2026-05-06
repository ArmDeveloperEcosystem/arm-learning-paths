---
title: Install and load driver
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install and load the SPE kernel module

### Step 2.0) Install Linux kernel extra modules

To keep kernel images smaller and tuned for different platforms, many distributions ship extra kernel modules in a separate package. Follow this step if your system returned the following from Step 1.1, indicating the module file was not included in your kernel package. If you arrived here with `CONFIG_ARM_SPE_PMU=y`, or already loaded the module in Step 1.1, skip directly to **Step 2.2**.

```output
arm_spe_pmu not present for this kernel
```

Run the following commands, replacing `apt` with your distribution's package manager if needed. This searches your package index for the extra modules package that matches your kernel version:

```bash
sudo apt update
apt search "linux-modules-extra-$(uname -r)"
```

This example shows two prebuilt packages: a default version and one with `64 KB` page sizes.

```output
Sorting... Done
Full Text Search... Done
linux-modules-extra-6.17.0-1010-aws/noble-security,noble-updates,now 6.17.0-1010.10~24.04.1 arm64 [installed]
  Linux kernel extra modules for version 6.17.0 on DESC

linux-modules-extra-6.17.0-1010-aws-64k/noble-security,noble-updates 6.17.0-1010.10~24.04.1 arm64
  Linux kernel extra modules for version 6.17.0 on DESC
```

Install the package that matches your system. In this example, regular page sizes are used.

```bash
sudo apt install linux-modules-extra-6.17.0-1010-aws -y 
```

Run the check again to confirm that the kernel module is installed:

```bash
modinfo arm_spe_pmu 2>/dev/null || echo "arm_spe_pmu module not present"
```

The output should be similar to:

```output
filename:       /lib/modules/6.17.0-1010-aws/kernel/drivers/perf/arm_spe_pmu.ko.zst
license:        GPL v2
author:         Will Deacon <will.deacon@arm.com>
description:    Perf driver for the ARMv8.2 Statistical Profiling Extension
...
```

### Step 2.1) Load the kernel module

If you installed the extra modules package in Step 2.0, load the module now:

```bash
sudo modprobe arm_spe_pmu
lsmod | grep arm_spe_pmu
```

If it loads correctly, the output is similar to:

```output
arm_spe_pmu            24576  0
```

{{% notice Tip %}}

To load the `arm_spe_pmu` kernel module automatically at boot, create a `.conf` file in `/etc/modules-load.d/`. The `systemd-modules-load` service reads files in that directory at boot and loads the listed modules. Restarting the service applies the change immediately without requiring a reboot. 

```bash
echo arm_spe_pmu | sudo tee /etc/modules-load.d/arm_spe_pmu.conf
sudo systemctl restart systemd-modules-load.service
```


You do not need to reboot now, but after the next reboot the module should load automatically. You can confirm with:

```bash
sudo dmesg | grep "arm_spe_pmu"
[    2.261719] arm_spe_pmu arm,spe-v1: probed SPEv1.1 for CPUs 0-63 [max_record_sz 64, align 64, features 0x17]
```

{{% /notice %}}

### Step 2.2) Verify SPE is active with Sysreport

All paths converge here. Whether the driver is built into your kernel (`y`), was already loaded in Step 1.1, or has just been loaded in Step 2.1, run Sysreport now to confirm SPE is active.

Follow the setup steps in the [Get ready for performance analysis with Sysreport guide](/learning-paths/servers-and-cloud-computing/sysreport/), then run:

```bash
python src/sysreport.py
```

Look for the `perf sampling` field in the output. If SPE is active, you should see:

```output
  perf sampling:       SPE
```

Return to Performix. The `Memory Access` recipe should now show `All checks passing!`.

![Screenshot of the Arm Performix memory access recipe showing all prerequisite checks passing, confirming that SPE is correctly enabled and the arm_spe_pmu module is loaded#center](./memory-access-passing.png "Arm Performix memory access recipe with all checks passing")

If `perf sampling` still shows `None`, check the KPTI section below if your system is Neoverse V1. For all other systems, see Step 3.0 for alternative approaches.

#### For Neoverse V1-based systems: adjust Kernel Page Table Isolation (KPTI)

On some Neoverse V1 systems (for example AWS Graviton3), SPE buffer mapping can fail when Kernel Page Table Isolation (KPTI) is enabled. This issue has been observed on Neoverse V1 and is not known to affect other Neoverse cores. Use the `CPU types:` line in `sysreport.py` to confirm whether your instance is Neoverse V1.

If all of the following conditions are met:

- The system is based on Neoverse V1.
- The kernel includes SPE PMU support.
- The platform exposes the SPE PMU.
- `sysreport` still reports `perf sampling: None`.


Use your preferred editor to update `GRUB_CMDLINE_LINUX` in `/etc/default/grub` and add `kpti=off`, as shown below.

![Screenshot of a terminal text editor showing /etc/default/grub with GRUB_CMDLINE_LINUX updated to include kpti=off, the change required to allow SPE buffer mapping to succeed on Neoverse V1 systems#center](./grub_config_change.png "GRUB_CMDLINE_LINUX set to kpti=off in /etc/default/grub")

{{% notice Note %}}

Disabling KPTI has security implications and should only be done on trusted systems.

{{% /notice %}}

Run the following commands to update the GRUB configuration and reboot. `update-grub` regenerates the bootloader configuration from `/etc/default/grub`. Ensure it completes without errors before rebooting.

```bash
sudo update-grub
sudo reboot
```