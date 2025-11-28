---
title: Build the in-tree kernel driver
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build an in-tree Linux kernel driver

Now that you have learned how to build and profile an out-of-tree kernel module, you'll move on to building a driver statically into the Linux kernel. You will then profile it by adding the kernel’s `vmlinux` file as an image in Streamline’s capture settings, rather than the kernel object itself. This allows you to view function calls and call paths as before, and also inspect specific sections of the kernel code that might be contributing to performance issues.

### Create an in-tree simple character device driver

Use the same example character driver you used earlier `mychardrv`. This time, you will be statically linking it to the kernel.

Go to your kernel source directory, in our case, it's located in Buildroot's output directory in `$(BUILDROOT_HOME)/output/build/linux-custom`.

Copy the `mychardrv.c` file created earlier to `drivers/char` directory.

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

You can rebuild the Linux image simply by running the **make** command in your Buildroot directory. This rebuilds the Linux kernel including our new device driver and produce a debuggable `vmlinux` ELF file.

```bash
cd $(BUILDROOT_HOME)
make -j$(nproc)
```

To verify that our driver was compiled into the kernel, you can run the following command:

```bash
find $(BUILDROOT_HOME) -iname "mychardrv.o"
```

This should return the full path of the object file produced from compiling our character device driver.

Now you can flash the new `sdcard.img` file produced to your target's SD card. 

{{% notice %}}
To learn how to flash the sdcard.img file to your SD card, see [this helpful article](https://www.ev3dev.org/docs/tutorials/writing-sd-card-image-ubuntu-disk-image-writer/).
{{% /notice %}}

This time your driver will be automatically loaded when Linux is booted.
