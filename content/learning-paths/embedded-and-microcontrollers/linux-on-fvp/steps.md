---
title: Configure Trusted Firmware-A build flags to include cpu_ops support
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build TF-A with cpu_ops support

Some Arm Fixed Virtual Platforms (FVPs) require CPU-specific initialization routines to boot Linux successfully. The Trusted Firmware-A `cpu_ops` framework provides these routines.

## What are cpu_ops?
The `cpu_ops` framework in Trusted Firmware-A contains functions to:

- Handle CPU resets
- Manage power states
- Apply errata workarounds

Each CPU type has its own implementation, defined in files such as:
```output
lib/cpus/aarch64/cortex_a55.S
lib/cpus/aarch64/cortex_a53.S
```

## Why are cpu_ops required?

If the firmware is built without the proper cpu_ops, you’ll hit an assertion failure like:

```output
ASSERT: File lib/cpus/aarch64/cpu_helpers.S Line 00035
```

This means that the required CPU operation routines are missing from the build.

## How do I include the correct cpu_ops?

To include the correct `cpu_ops`, you need to set TF-A build options depending on the CPU, using the build flags.

### For the A55 CPU FVP

Add the following line to your TF-A build script:

```output
ARM_TF_BUILD_FLAGS="$ARM_TF_BUILD_FLAGS HW_ASSISTED_COHERENCY=1 USE_COHERENT_MEM=0"
```

These flags enable hardware-assisted cache coherency and disable use of coherent memory, which is typical for Cortex-A55 FVPs.

### For the A78 CPU FVP

Add the following line to your TF-A build script:

```output
ARM_TF_BUILD_FLAGS="$ARM_TF_BUILD_FLAGS HW_ASSISTED_COHERENCY=1 USE_COHERENT_MEM=0 CTX_INCLUDE_AARCH32_REGS=0"
```
{{% notice Note %}}
USE_COHERENT_MEM=1 cannot be used with HW_ASSISTED_COHERENCY=1.
{{% /notice %}}

This configuration disables 32-bit context registers (specific to AArch64-only CPUs like Cortex-A78) and applies the same coherency settings as above.

## Rebuild and package

Run the following commands to rebuild TF-A and integrate it into the BusyBox image:
```bash
./build-scripts/build-arm-tf.sh -p aemfvp-a -f busybox clean
./build-scripts/build-arm-tf.sh -p aemfvp-a -f busybox build
./build-scripts/aemfvp-a/build-test-busybox.sh -p aemfvp-a package
```
Once the build completes, your firmware will include the correct CPU operation routines, allowing Linux to boot correctly on the target FVP.

After packaging, you can boot the updated firmware on your FVP and verify that Linux reaches userspace without triggering early boot assertions.