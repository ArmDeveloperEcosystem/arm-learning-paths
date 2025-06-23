---
title: Modify the device tree for CPU FVPs
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Ensure the device tree matches your FVP model

To run Linux on Arm CPU FVPs, you need to adjust the device tree to match the hardware features of these platforms. This involves removing unsupported nodes - such as the System Memory Management Unit (SMMU) and Peripheral Component Interconnect (PCI) and ensuring that the CPU affinity values are set correctly.

### Remove PCI and SMMU nodes

CPU FVPs don't support PCI or SMMU. If you leave these nodes in the device tree, Linux will crash at boot with a kernel panic.

1. Open the device tree file in a text editor:
```bash
vim linux/arch/arm64/boot/dts/arm/fvp-base-revc.dts
```
2. Remove the following nodes:
- `pci@40000000`
- `iommu@2b400000`

{{% notice warning %}}
If you skip this step, you might get an error like:

```output
Kernel panic - not syncing: Attempted to kill init! exitcode=0x0000000b
```
{{% /notice %}}

### Set CPU affinity values

Each FVP model uses specific CPU affinity values. If these don’t match what’s in the device tree, some CPU cores won’t boot.
1.	Find the correct affinities:
```bash
FVP_Base_Cortex-A55x4 -l | grep pctl.CPU-affinities
```
Example output:

```output
pctl.CPU-affinities=0.0.0.0, 0.0.1.0, 0.0.2.0, 0.0.3.0
```

2.	Convert each to hex for the `reg` field:

```output
0x0, 0x0100, 0x0200, 0x0300
```

3.	Update the CPU nodes in your device tree file to use these `reg` values.

{{% notice Tip %}}
To avoid boot errors such as `psci: failed to boot CPUx (-22)`, make sure every cpu@xxx entry matches the FVP layout.
{{% /notice %}}

### Rebuild Linux

After editing the device tree, rebuild Linux:

```bash
./build-scripts/build-linux.sh -p aemfvp-a -f busybox clean
./build-scripts/build-linux.sh -p aemfvp-a -f busybox build
./build-scripts/aemfvp-a/build-test-busybox.sh -p aemfvp-a package
```

This regenerates the image with the updated device tree, ready for use with your FVP.