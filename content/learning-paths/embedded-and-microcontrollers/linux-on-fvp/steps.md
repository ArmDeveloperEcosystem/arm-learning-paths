---
title: Use Trusted Firmware-A build options to include cpu_ops support
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build TF-A with cpu_ops support

Some Arm Fixed Virtual Platforms (FVPs) require CPU-specific initialization routines to boot Linux successfully. These routines are provided by the Trusted Firmware-A `cpu_ops` framework.

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

## Why do I need cpu_ops?

If the firmware is built without proper cpu_ops, you’ll hit an assertion failure like:

```output
ASSERT: File lib/cpus/aarch64/cpu_helpers.S Line 00035
```

This means the required CPU operation routines are missing from the build.

## Add TF-A build flags

To include the correct `cpu_ops`, you need to set TF-A build options depending on the CPU.

### A55 CPU FVP

Add the following line to your TF-A build script:

```output
ARM_TF_BUILD_FLAGS="$ARM_TF_BUILD_FLAGS HW_ASSISTED_COHERENCY=1 USE_COHERENT_MEM=0"
```

### A78 CPU FVP
```output
ARM_TF_BUILD_FLAGS="$ARM_TF_BUILD_FLAGS HW_ASSISTED_COHERENCY=1 USE_COHERENT_MEM=0 CTX_INCLUDE_AARCH32_REGS=0"
```
{{% notice Note %}}
USE_COHERENT_MEM=1 cannot be used with HW_ASSISTED_COHERENCY=1.
{{% /notice %}}

## Rebuild and package

Run the following commands to rebuild TF-A and integrate it into the BusyBox image:
```bash
./build-scripts/build-arm-tf.sh -p aemfvp-a -f busybox clean
./build-scripts/build-arm-tf.sh -p aemfvp-a -f busybox build
./build-scripts/aemfvp-a/build-test-busybox.sh -p aemfvp-a package
```
Once the build completes, your firmware will include the correct CPU operation routines, allowing Linux to boot correctly on the target FVP.