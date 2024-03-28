---
title: Build
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build
Now that we have the environment and the source, let us perform a build of the firmware stack. We will follow the [instructions](https://neoverse-reference-design.docs.arm.com/en/latest/platform-boot/busybox-boot.html) to build a busy-box root. This will build a lightweight kernel with shell, giving fast performance on the FVP.

This will test that the firmware implementation builds and boots. It requires `TF-A`, `UEFI`, `SCP` and a lightweight OS loader, to make sure we exercise the UEFI `ExitBootServices` transition. The `busy-box` boot is perfect for this.

Launch the container:
```bash
./container.sh -v /home/ubuntu/rd-infra/ run
```

Perform the build inside the container:
```bash
cd home/ubuntu/rd-infra/
./build-scripts/rdinfra/build-test-busybox.sh -p rdn2 build
```
During the build TF-A, UEFI and SCP firmware are built using their own build systems.

## Package the built images

The build system provides scripts to package the build products into image files that can be consumed by the FVP.

```bash
./container.sh -v /home/ubuntu/rd-infra/ run
./build-scripts/rdinfra/build-test-busybox.sh -p rdn2 package
```

The script first confirmed that the firmware was already built, firmware was marshalled, signing keys generated and firmware signed, firmware image files created and finally a busy-box ramdisk created.

Verify the package was created successfully.

```bash
ls output/rdn2/
```
Should list:
```output
components  grub-busybox.img  ramdisk-busybox.img  rdn2
```
The command:
```
ls output/rdn2/rdn2/ -l
```
Will output similar to:
```output
total 4948
-rw-r--r-- 1 ubuntu ubuntu 5064017 Jan 12 15:35 fip-uefi.bin
lrwxrwxrwx 1 ubuntu ubuntu      25 Jan 12 15:35 Image -> ../components/linux/Image
lrwxrwxrwx 1 ubuntu ubuntu      35 Jan 12 15:35 Image.defconfig -> ../components/linux/Image.defconfig
lrwxrwxrwx 1 ubuntu ubuntu      26 Jan 12 15:35 lkvm -> ../components/kvmtool/lkvm
lrwxrwxrwx 1 ubuntu ubuntu      32 Jan 12 15:35 mcp_ramfw.bin -> ../components/rdn2/mcp_ramfw.bin
lrwxrwxrwx 1 ubuntu ubuntu      32 Jan 12 15:35 mcp_romfw.bin -> ../components/rdn2/mcp_romfw.bin
lrwxrwxrwx 1 ubuntu ubuntu      32 Jan 12 15:35 scp_ramfw.bin -> ../components/rdn2/scp_ramfw.bin
lrwxrwxrwx 1 ubuntu ubuntu      32 Jan 12 15:35 scp_romfw.bin -> ../components/rdn2/scp_romfw.bin
lrwxrwxrwx 1 ubuntu ubuntu      29 Jan 12 15:35 tf-bl1.bin -> ../components/rdn2/tf-bl1.bin
lrwxrwxrwx 1 ubuntu ubuntu      29 Jan 12 15:35 tf-bl2.bin -> ../components/rdn2/tf-bl2.bin
lrwxrwxrwx 1 ubuntu ubuntu      30 Jan 12 15:35 tf-bl31.bin -> ../components/rdn2/tf-bl31.bin
lrwxrwxrwx 1 ubuntu ubuntu      33 Jan 12 15:35 uefi.bin -> ../components/css-common/uefi.bin
```

The `fip-uefi.bin` firmware image will contain the `TF-A BL2` boot loader image which is responsible for unpacking all the rest of the firmware as well as the rest of the firmware that TF-A BL2 unpacks.

This includes the `SCP BL2` (`scp_ramfw.bin`) image that is unpacked by the AP firmware and transferred over to the SCP TCMs using the SCP shared data store module.

Along with the FIP image, the FVP will also need the `TF-A BL1` image and the `SCP BL1` (`scp_romfw.bin`) image files.

