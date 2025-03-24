---
title: Build the Root file system
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download and unpack root file system

The root file system (or rootfs for short) is the second essential component that you will need. The root file system is a collection of files that are essential for a Linux system to function. Usually, it also includes various tools that make using your system more convenient.

Since you are providing your own kernel, there isn't much that is required from a rootfs. All you need is for it to be built for the AArch64 target and contain the tools that you require.

To speed things up for this learning path, you will use a readily available rootfs for the [Void Linux](https://voidlinux.org/) distro. There are other options for obtaining a working root file system, but the rest of this learning path assumes that you are using the Void Linux distribution.

Download the image (make sure you download into the directory detailed in the 'Naming Conventions' section)

```bash
wget https://repo-default.voidlinux.org/live/20250202/void-rpi-aarch64-20250202.img.xz
```

Note that at the time when you are reading this, there might be a newer version available.

Let's unpack and resize the image. The added size determines how much free disk space
you will have in your guest system:

```bash
unxz --keep void-rpi-aarch64-20250202.img.xz
mv void-rpi-aarch64-20250202.img rootfs.img
truncate -s +2G rootfs.img
```

Here you added 2 GiB of free space. Of course, the file system in this image is not actually
resized at this point. Void Linux will be able to do it automatically during the first
boot.

Note that when we run our system, the rootfs image file will be modified. If something
goes wrong, the image might be corrupted, and you might not be able to boot from it again.
That's why it's recommended to create a backup copy after the initial setup.

