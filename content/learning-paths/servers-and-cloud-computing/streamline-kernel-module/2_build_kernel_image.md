---
title: Build Linux image
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build a debuggable kernel image

For this learning path we will be using [Buildroot](https://github.com/buildroot/buildroot) to build a Linux image for Raspberry Pi 3B+ with a debuggable Linux kernel. We will profile Linux kernel modules built out-of-tree and Linux device drivers built in the Linux source code tree.  

1. Clone the Buildroot Repository and initialize the build system with the default configurations.

      ```bash
      git clone https://github.com/buildroot/buildroot.git
      cd buildroot
      make raspberrypi3_64_defconfig
      make menuconfig
      make -j$(nproc)
      ```

2. Change Buildroot configurations to enable debugging symbols and SSH access.

    ```plaintext
    Build options  --->
        [*] build packages with debugging symbols
            gcc debug level (debug level 3)
        [*] build packages with runtime debugging info
            gcc optimization level (optimize for debugging)  --->
    
    System configuration  --->
        [*] Enable root login with password
            (****) Root password    # Choose root password here
        
    Kernel  --->
        Linux Kernel Tools  --->
            [*] perf
    
    Target packages  --->
        Networking applications  --->
            [*] openssh
                [*]   server
                [*]   key utilities
    ```

    You might also need to change your default `sshd_config` file according to your network settings. To do that, you need to modify System configuration→ Root filesystem overlay directories to add a directory that contains your modified `sshd_config` file.

3. By default the Linux kernel images are stripped so we will need to make the image debuggable as we'll be using it later.

    ```bash
    make linux-menuconfig
    ```

    ```plaintext
    Kernel hacking  --->
        -*- Kernel debugging
        Compile-time checks and compiler options  --->
            Debug information (Rely on the toolchain's implicit default DWARF version)
        [ ] Reduce debugging information #un-check
    ```

4. Now we can build the Linux image and flash it to the the SD card to run it on the Raspberry Pi.

    ```bash
    make -j$(nproc)
    ```

It will take some time to build the Linux image. When it completes, the output will be in `<buildroot dir>/output/images/sdcard.img`
For details on flashing the SD card image, see [this helpful article](https://www.ev3dev.org/docs/tutorials/writing-sd-card-image-ubuntu-disk-image-writer/).
Now that we have a target running Linux with a debuggable kernel image, we can start writing our kernel module that we want to profile.
