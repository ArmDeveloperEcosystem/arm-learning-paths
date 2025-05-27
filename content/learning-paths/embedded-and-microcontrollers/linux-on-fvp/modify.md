---
title: Modify device tree for Linux
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Modify the Device Tree for CPU FVPs

To run Linux on Arm CPU FVPs, you need to adjust the device tree to match the hardware features of these platforms. This involves removing unsupported nodes (like SMMU (System Memory Management Unit)and PCI (Peripheral Component Interconnect)) and ensuring CPU affinity values are set correctly.

### Step 1: Remove PCI and SMMU Nodes

CPU FVPs don't support PCI and SMMU. If you don't remove these nodes, Linux will crash at boot with a kernel panic.

1. Open the device tree file in a text editor:
```bash
vim linux/arch/arm64/boot/dts/arm/fvp-base-revc.dts
```
2.	Delete the following two blocks:
- `pci@40000000`
- `iommu@2b400000`

{{% notice warning %}}
If you skip this, you’ll get an error like:

```output
Kernel panic - not syncing: Attempted to kill init! exitcode=0x0000000b
```
{{% /notice %}}

### Step 2: Set CPU Affinity Values

Each FVP model uses specific CPU affinity values. If these don’t match what’s in the device tree, some CPU cores won’t boot.
1.	Find the correct affinities:
```bash
FVP_Base_Cortex-A55x4 -l | grep pctl.CPU-affinities
```
Example output:

```output
pctl.CPU-affinities=0.0.0.0, 0.0.1.0, 0.0.2.0, 0.0.3.0
```

2.	Convert each to hex for the reg field:

```output
0x0, 0x0100, 0x0200, 0x0300
```

3.	Update the CPU nodes in your device tree file to use these reg values.

{{% notice tip %}}
To avoid boot errors like psci: failed to boot CPUx (-22), make sure every cpu@xxx entry matches the FVP layout.
{{% /notice %}}

### Step 3: Rebuild Linux

After editing the device tree, rebuild Linux:

```bash
./build-scripts/build-linux.sh -p aemfvp-a -f busybox clean
./build-scripts/build-linux.sh -p aemfvp-a -f busybox build
./build-scripts/aemfvp-a/build-test-busybox.sh -p aemfvp-a package
```

This regenerates the image with the updated device tree, ready for use with your FVP.