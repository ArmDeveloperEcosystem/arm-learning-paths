---
title: Run Software Stack
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Firmware and Kernel Images

After adding extra TF-A build options and removing the PCI and MMU nodes from the device tree, you can follow the [Arm Reference Solution Guide](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/blob/master/docs/aemfvp-a/user-guide.rst) to build the software stack.

When the build is complete, you can use the `tree` command to look at the directory structure.

```console
tree output/aemfvp-a/aemfvp-a/
```

The directory structure is similar to: 

```output
output/aemfvp-a/aemfvp-a/
├── Image -> ../components/linux/Image
├── Image.defconfig -> ../components/linux/Image.defconfig
├── fip-uboot.bin
├── fip-uefi.bin
├── fvp-base-revc.dtb -> ../components/linux/fvp-base-revc.dtb
├── tf-bl1.bin -> ../components/fvp/tf-bl1.bin
├── tf-bl2.bin -> ../components/fvp/tf-bl2.bin
├── tf-bl2u.bin -> ../components/fvp/tf-bl2u.bin
├── tf-bl31.bin -> ../components/fvp/tf-bl31.bin
├── uboot.bin -> ../components/aemfvp-a/uboot.bin
└── uefi.bin -> ../components/aemfvp-a/uefi.bin
```

### Run software stack on FVP

After the build of the software stack, you can follow the [guide](https://gitlab.arm.com/arm-reference-solutions/arm-reference-solutions-docs/-/tree/master) to run the software stack on the Armv-A Base AEM FVP platform.

CPU FVP platforms have a fixed number of cores, so you cannot use the model-scripts/aemfvp-a/boot.sh to run the CPU FVP platforms.

To run the software stack in the CPU FVP platform, use a command similar to: 

```console
FVP_Base_Cortex-A55x4 \
-C pctl.startup=0.0.0.0 \
-C bp.secure_memory=0  \
-C cache_state_modelled=0 \
-C bp.ve_sysregs.mmbSiteDefault=0 \
-C bp.ve_sysregs.exit_on_shutdown=1 \
-C bp.pl011_uart0.untimed_fifos=1 \
-C bp.pl011_uart0.unbuffered_output=1 \
-C bp.pl011_uart0.out_file=<PATH_TO_LOG>/uart0.log \
-C bp.pl011_uart1.untimed_fifos=1 \
-C bp.pl011_uart1.unbuffered_output=1 \
-C bp.pl011_uart1.out_file=<PATH_TO_LOG>/uart1.log \
-C bp.secureflashloader.fname=<SRC_PATH>/output/aemfvp-a/aemfvp-a/tf-bl1.bin \
-C bp.flashloader0.fname=<SRC_PATH>/output/aemfvp-a/aemfvp-a/fip-uboot.bin \
-C bp.virtioblockdevice.image_path=<SRC_PATH>/output/aemfvp-a/components/aemfvp-a/grub-busybox.img \
--data cluster0.cpu0=<SRC_PATH>/output/aemfvp-a/aemfvp-a/Image@0x80080000 \
--data cluster0.cpu0=<SRC_PATH>/output/aemfvp-a/aemfvp-a/fvp-base-revc.dtb@0x83000000
```

After the previous command is run, the CPU FVP starts booting Trusted Firmware-A, followed by UEFI/U-Boot, Linux, and BusyBox.

If you use the GUI, you can run it as shown in the following figure:

![GUI #center](FVP.png)

### Alternative running option

On some CPU FVP platforms, you might encounter the following error and the system cannot boot successfully.

```output
Warning: target instance not found: 'FVP_Base_Cortex_A65AEx4_Cortex_A76AEx4.cluster0.cpu0' (data: 'output/aemfvp-a/aemfvp-a/Image')
In file: /tmp/plgbuild/abs_build/1153836_60931/trunk/work/fastsim/Framework/scx/SCXExportedVirtualSubsystem.cpp:358
Warning: target instance not found: 'FVP_Base_Cortex_A65AEx4_Cortex_A76AEx4.cluster0.cpu0' (data: 'output/aemfvp-a/aemfvp-a/fvp-base-revc.dtb')
In file: /tmp/plgbuild/abs_build/1153836_60931/trunk/work/fastsim/Framework/scx/SCXExportedVirtualSubsystem.cpp:358
```

The FVP platform contains multiple CPU instances, and the CPU instance names are different on different CPU FVP platforms.

To load raw data into right CPU instances, use the `––dataoption` to specify correct CPU instance names, according to the CPU FVP platform. For example, on FVP_Base_Cortex-A55x4, the CPU0 instance is cluster0.cpu0:

```console
data cluster0.cpu0=<SRC_PATH>/output/aemfvp-a/aemfvp-a/Image@0x80080000 \
--data cluster0.cpu0=<SRC_PATH>/output/aemfvp-a/aemfvp-a/fvp-base-revc.dtb@0x83000000 
```

Run the FVP to dump the parameters and use `grep` to get the correct CPU0 instance name in the CPU FVP platform.

```console
FVP_Base_Cortex-A65AEx4+Cortex-A76AEx4 -l | grep RVBARADDR | grep cpu0
```

The output is similar to:

```output
cluster0.subcluster0.cpu0.thread0.RVBARADDR=0         # (int   , init-time) default = '0x0'    : Value of RVBAR_ELx register.
cluster0.subcluster0.cpu0.thread1.RVBARADDR=0         # (int   , init-time) default = '0x0'    : Value of RVBAR_ELx register.
cluster0.subcluster1.cpu0.RVBARADDR=0                 # (int   , init-time) default = '0x0'    : Value of RVBAR_ELx register.
```

For another FVP:

```console
FVP_Base_Cortex-A55x4+Cortex-A78x4 -l | grep RVBARADDR | grep cpu0
```

The output is similar to:

```output
cluster0.subcluster0.cpu0.RVBARADDR=0                 # (int   , init-time) default = '0x0'    : Value of RVBAR_ELx register.
cluster0.subcluster1.cpu0.RVBARADDR=0                 # (int   , init-time) default = '0x0'    : Value of RVBAR_ELx register.
```

For FVP_Base_Cortex-A65AEx4+Cortex-A76AEx4, use the –data option like the following to run the FVP:

```console
--data cluster0.subcluster0.cpu0.thread0=<SRC_PATH>/output/aemfvp-a/aemfvp-a/Image@0x80080000 \
--data cluster0.subcluster0.cpu0.thread0=<SRC_PATH>/output/aemfvp-a/aemfvp-a/fvp-base-revc.dtb@0x83000000
```
