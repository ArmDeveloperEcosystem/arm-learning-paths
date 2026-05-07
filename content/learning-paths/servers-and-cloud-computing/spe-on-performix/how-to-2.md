---
title: Assess OS kernel
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Assess the OS kernel and driver

{{% notice Note %}}
The examples in this section use an AWS `c7g.metal` instance running Ubuntu 24.04 LTS. Commands and outputs on other platforms or distributions may differ slightly.
{{% /notice %}}

### Step 1.0) Check whether the OS kernel is built with SPE

From the Getting Started section, you know you need to verify both the kernel and driver layers. Start by checking the kernel version:

```bash
uname -r
```
The output is similar to:

```output
6.17.0-1010-aws
```

This AWS instance is running the standard Ubuntu 24.04 LTS Amazon Machine Image (AMI) provided through AWS Quick Start. The command output shows a Linux 6.17 kernel, and the `1010-aws` suffix indicates an AWS-specific build customized for the AWS environment.

Now check whether this kernel was built with SPE support enabled:

```bash
grep CONFIG_ARM_SPE_PMU /boot/config-$(uname -r) 2>/dev/null || true
```

The possible outputs are `y`, `m`, or `n`, meaning built-in support, module support, or no support.

- `y` indicates that the kernel was built with SPE support built-in. **Continue to the next page and skip to Step 2.2** to verify whether SPE is active on your system.
- `m` indicates that SPE is available as a loadable kernel module. This is the typical output for cloud instances. **Continue to Step 1.1.**
- `n` means the kernel was **not** built with SPE support. **Skip directly to Step 3.0.**

If the command produces no output, the kernel config file may not be present on your system. In this case, treat it as `n` and continue to Step 3.0.

### Step 1.1) Check whether the kernel module is available

If your output was `CONFIG_ARM_SPE_PMU=m`, as shown below, the OS kernel includes SPE support as a loadable module. You need to confirm that the module file is present on the filesystem before attempting to load it.

```output
CONFIG_ARM_SPE_PMU=m
```

Run the following command to check whether the loadable kernel module (driver) is available on the target:

```bash
modinfo arm_spe_pmu 2>/dev/null || echo "arm_spe_pmu not present for this kernel"
```

If you see output similar to the following, the module file exists and is ready to load. Continue to the `modprobe` step below.

If you see `arm_spe_pmu not present for this kernel`, the module was not included in your kernel package. **Continue to Step 2.0** to install the extra modules package.

```output
filename:       /lib/modules/6.17.0-1010-aws/kernel/drivers/perf/arm_spe_pmu.ko.zst
license:        GPL v2
author:         Will Deacon <will.deacon@arm.com>
description:    Perf driver for the ARMv8.2 Statistical Profiling Extension
srcversion:     3B6FCB5AD9B37B8BB9FF4A9
...
```

Next, load the module and confirm it is active:

```bash
sudo modprobe arm_spe_pmu
lsmod | grep arm_spe_pmu
```

`modprobe` loads the module into the running kernel. `lsmod` lists currently loaded modules; a matching line confirms the driver is active. If it loads correctly, the output is similar to:

```output
arm_spe_pmu            24576  0
```

The module is now loaded. **Continue to the next page and skip to Step 2.2** to verify that SPE is active.
