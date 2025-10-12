---
title: Build in-tree kernel driver
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build an in-tree Linux kernel driver

Now that we have learned how to build and profile an out-of-tree kernel module, we will move on to building a driver statically into the Linux kernel. We will then profile it by adding the kernel’s vmlinux file as an image in Streamline’s capture settings. This allows us to view function calls and call paths as before, and also inspect specific sections of the kernel code that may be contributing to performance issues.

### Creating an in-tree simple character device driver

We will use the same example character driver we used earlier `mychardrv` except that this time we will be statically linking it to the kernel.

1. Go to your kernel source directory, in our case, it's located in Buildroot's output directory in `<buildroot-dir>/output/build/linux-custom`.

2. Copy the `mychardrv.c` file created earlier to `drivers/char` directory.

    ```bash
    cd drivers/char
    cp <mychardrv.c file> ./mychardrv.c
    ```

3. Add the following configuration to the bottom of the `Kconfig` file to make the kernel configuration system aware of the the new driver we just added.

    ```plaintext
    config MYCHAR_DRIVER
        tristate "My Character Driver"
        default y
        help
          A simple character device driver for testing.
    endmenu
    ```

4. We also need to modify the `Makefile` in the current directory to make it build the object file for `mychardrv.c`, so we'll add the following line to it.

    ```Makefile
    obj-$(CONFIG_MYCHAR_DRIVER) += mychardrv.o
    ```

### Rebuild and Run the Linux Image

You can rebuild the Linux image simply by running the **make** command in your Buildroot directory. This rebuilds the Linux kernel including our new device driver and produce a debuggable `vmlinux` ELF file.

```bash
cd <buildroot-dir>
make -j$(nproc)
```

To verify that our driver was compiled into the kernel, you can run the following command:

```bash
find <buildroot-dir> -iname "mychardrv.o"
```

This should return the full path of the object file produced from compiling our character device driver.

Now you can flash the new `sdcard.img` file produced to your target's SD card. To learn how to flash the sdcard.img file to your SD card, you can look at [this helpful article](https://www.ev3dev.org/docs/tutorials/writing-sd-card-image-ubuntu-disk-image-writer/). This time our driver will be automatically loaded when Linux is booted.
