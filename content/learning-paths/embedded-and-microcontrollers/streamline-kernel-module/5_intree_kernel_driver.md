---
title: Integrate a custom character device driver into the Linux kernel
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview
In the previous steps, you built and profiled an out-of-tree kernel module. Now, you'll learn how to integrate a driver directly into the Linux kernel source tree. By statically linking your driver, you can profile it using Streamline by adding the kernel’s `vmlinux` file in the capture settings. This approach lets you analyze function calls, call paths, and specific kernel code sections that might affect performance, just as you did with the out-of-tree module.

### Create an in-tree simple character device driver

Use the same example character driver you used earlier `mychardrv`. This time, you will be statically linking it to the kernel.

Go to your kernel source directory, which in this case is located in Buildroot's output directory in `$(BUILDROOT_HOME)/output/build/linux-custom`.

Copy the `mychardrv.c` file created earlier to `drivers/char` directory:

```bash
cd drivers/char
cp <mychardrv.c file> ./mychardrv.c
```
Add the following configuration to the bottom of the `Kconfig` file to make the kernel configuration system aware of the the new driver you just added:

```plaintext
config MYCHAR_DRIVER
tristate "My Character Driver"
default y
help
A simple character device driver for testing.
endmenu
```

You also need to modify the `Makefile` in the current directory to make it build the object file for `mychardrv.c`. Add the following line to it:

```Makefile
obj-$(CONFIG_MYCHAR_DRIVER) += mychardrv.o
```

## Rebuild and run the Linux image

You can rebuild the Linux image simply by running the `make` command in your Buildroot directory. This rebuilds the Linux kernel including the new device driver and produces a debuggable `vmlinux` ELF file:

```bash
cd $(BUILDROOT_HOME)
make -j$(nproc)
```

To verify that the driver was compiled into the kernel, run the following command:

```bash
find $(BUILDROOT_HOME) -iname "mychardrv.o"
```

The output gives you the full path to the object file for your character device driver. This confirms that the kernel build process included your driver.

Next, flash the updated `sdcard.img` file to your target's SD card. This step can be confusing at first, but it's essential for running your new kernel with the integrated driver on your Arm device.

{{% notice %}}
To learn how to flash the sdcard.img file to your SD card, see [this helpful article](https://www.ev3dev.org/docs/tutorials/writing-sd-card-image-ubuntu-disk-image-writer/).
{{% /notice %}}

When you integrate your driver into the kernel source tree, it loads automatically each time Linux boots. You don't need to manually insert the module as your character device driver is ready to use as soon as the system starts.
