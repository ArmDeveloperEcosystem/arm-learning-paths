---
title: Assess the OS kernel and driver for Arm SPE support
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---


### Check whether the OS kernel is built with SPE {#check-kernel-spe}

{{% notice Note %}}
The steps in this section use an AWS Graviton-based Amazon EC2 `c7g.metal` instance running Ubuntu 24.04 LTS. Commands and outputs on other platforms or distributions might differ slightly.
{{% /notice %}}

You need to verify both the kernel and driver layers. Start by checking the kernel version:

```bash
uname -r
```
The output is similar to:

```output
6.17.0-1010-aws
```

The example Amazon EC2 instance is running the standard Ubuntu 24.04 LTS Amazon Machine Image (AMI) provided through AWS Quick Start. The command output shows a Linux 6.17 kernel. The `1010-aws` suffix indicates an AWS-specific build customized for the AWS environment.

Now, check whether the kernel was built with SPE support enabled:

```bash
grep CONFIG_ARM_SPE_PMU /boot/config-$(uname -r) 2>/dev/null || true
```

The possible outputs for a kernel are `y`, `m`, or `n`. The output determines your next step.

- If the output is `y`, the kernel has built-in SPE support. Next, [verify SPE is active with Sysreport](/learning-paths/servers-and-cloud-computing/spe-on-performix/how-to-3/#verify-spe-active).
- If the output is `m`, SPE is available as a loadable kernel module. This is the typical output for cloud instances. Next, [confirm that the kernel module is available](#check-kernel-module).
- If the output is `n`, the kernel was not built with SPE support. Next, [use another operating system or kernel](/learning-paths/servers-and-cloud-computing/spe-on-performix/how-to-4/#try-another-os).

If the command produces no output, the kernel config file might not be present on your system. In this case, [use another operating system or kernel](/learning-paths/servers-and-cloud-computing/spe-on-performix/how-to-4/#try-another-os).

### Confirm that the kernel module is available {#check-kernel-module}

If your OS kernel includes SPE support as a loadable module, you need to confirm that the module file is present on the filesystem before attempting to load it.

Run the following command to check whether the loadable kernel module (driver) is available on the target:

```bash
modinfo arm_spe_pmu 2>/dev/null || echo "arm_spe_pmu not present for this kernel"
```
If you see `arm_spe_pmu not present for this kernel`, the module was not included in your kernel package. Next, [install Linux kernel extra modules](/learning-paths/servers-and-cloud-computing/spe-on-performix/how-to-3/#install-extra-modules).

If you see output similar to the following, the module file exists and is ready to load. Follow the steps in the next section to load the kernel module.

```output
filename:       /lib/modules/6.17.0-1010-aws/kernel/drivers/perf/arm_spe_pmu.ko.zst
license:        GPL v2
author:         Will Deacon <will.deacon@arm.com>
description:    Perf driver for the ARMv8.2 Statistical Profiling Extension
srcversion:     3B6FCB5AD9B37B8BB9FF4A9
...
```

### Load the kernel module {#load-kernel-module}

If a loadable module is available, load the module and confirm it is active:

```bash
sudo modprobe arm_spe_pmu
lsmod | grep arm_spe_pmu
```

`modprobe` loads the module into the running kernel. `lsmod` lists currently loaded modules; a matching line confirms the driver is active. If it loads correctly, the output is similar to:

```output
arm_spe_pmu            24576  0
```

The module is now loaded. Next, [verify SPE is active with Sysreport](/learning-paths/servers-and-cloud-computing/spe-on-performix/how-to-3/#verify-spe-active).

### What you've accomplished and what's next

You've now checked whether your kernel supports Arm SPE, verified whether the `arm_spe_pmu` module file is available, and loaded the module when applicable.

Next, if the module is available and loaded, [verify SPE is active with Sysreport](/learning-paths/servers-and-cloud-computing/spe-on-performix/how-to-3/#verify-spe-active). If your kernel or modules package does not provide SPE support, [use another operating system or kernel](/learning-paths/servers-and-cloud-computing/spe-on-performix/how-to-4/#try-another-os).