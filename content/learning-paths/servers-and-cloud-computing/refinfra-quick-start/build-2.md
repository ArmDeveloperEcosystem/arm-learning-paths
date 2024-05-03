---
title: Build the software stack
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build
Now that you have the environment and the source set up, you can build the firmware stack. You follow the [instructions](https://neoverse-reference-design.docs.arm.com/en/latest/platform-boot/busybox-boot.html) to build a busybox root filesystem. This builds a lightweight kernel with shell.
You will test that the firmware implementation builds and boots on a FVP. The firmware stack requires `TF-A`, `UEFI`, `SCP` and a lightweight OS loader, to make sure you exercise the UEFI `ExitBootServices` transition. The `busy-box` boot is perfect for this.

Launch the container:
```bash 
./container-scrits/container.sh -v /home/ubuntu/rd-infra/ run
```

Perform a build inside the container:
```bash 
./build-scripts/rdinfra/build-test-busybox.sh -p rdn2 build
```

 During the build you will see that TF-A, UEFI and SCP firmware are built using their own build systems. The build finishes with the following output:
```output
output/bin/grub-mkimage: info: kernel_img=0x7f366cf65010, kernel_size=0x1a000.
output/bin/grub-mkimage: info: the core size is 0xa2a98.
output/bin/grub-mkimage: info: writing 0xa5000 bytes.
Execute build for build-grub.sh on rdn2[rdn2][busybox] done.
-----------------------------------
***********************************
Execute build for build-target-bins.sh on rdn2[rdn2][busybox]
~/rd-infra ~/rd-infra
~/rd-infra
Build
Execute build for build-target-bins.sh on rdn2[rdn2][busybox] done.
-----------------------------------
```

Because your `rd-infra` workspace is mounted into the container from outside, you should normally be able to find the output of the build in our host filesystem - you don't have to extract it from the container.

## Package the built images

The build system provides scripts to package the build products into image files that can be consumed by the FVP.
```bash 
./build-scripts/rdinfra/build-test-busybox.sh -p rdn2 package
```

The script confirms that the firmware has been built, firmware was marshalled, signing keys generated, firmware signed, firmware image files created, and finally a busy-box ramdisk created.

Verify that the package has been created successfully:
```bash 
ls output/rdn2/
```

The output contents should look like:
```output
components  grub-busybox.img  ramdisk-busybox.img  rdn2
```

Examine the full build directory with:
```bash 
ls output/rdn2/rdn2/ -l
```

The output should look like:
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

The `fip-uefi.bin` firmware image will contain the `TF-A BL2` boot loader image which is responsible for unpacking the rest of the firmware as well as the firmware that TF-A BL2 unpacks. This includes the `SCP BL2` (`scp_ramfw.bin`) image that is unpacked by the AP firmware and transferred over to the SCP TCMs using the SCP shared data store module. Along with the FIP image, the FVP also needs the `TF-A BL1` image and the `SCP BL1` (`scp_romfw.bin`) image files.

