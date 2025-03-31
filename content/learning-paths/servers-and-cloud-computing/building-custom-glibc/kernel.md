---
title: Build Linux kernel
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Obtain kernel source

The Linux kernel image is the first essential components that you need to build. You are going to build it from source.

There are various ways to obtain the sources for a particular version of the Linux kernel that you want to use. Here, as an example, we obtain a stable
version from the mainline repository.

```bash
git clone  https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
pushd linux
git checkout v6.13 -b release/6.13
popd
```

Note that at the time when you are reading this, there might be a newer version
available.

Using a stable kernel version is a good starting point. When everything is up
and running, you can switch to the version of the kernel that you are actually
interested in running.

## Configure and build kernel

Before moving on, export some environment variables, pointing out some key directories and options.
All the build output, including the binary that you intend to use later, will be put in
the `linux-build` subfolder. Run the following commands in the workspace directory:


```bash
export KBUILD_OUTPUT="$(pwd)/linux-build"
export ARCH=arm64
# Specify cross compiler
export CROSS_COMPILE=aarch64-none-linux-gnu-
````

Next, build the kernel image:
```bash
make -C linux mrproper
make -C linux defconfig
make -C linux Image -j $(nproc)
```

The `mrproper` target is used to clean the build folder. It will also create
this folder if it doesn't exist. The `defconfig` target generates the default
configuration for the selected architecture, `arm64`. At this point, you may
change this configuration if necessary, for example, if the feature that you
are interested in is not enabled by default. To do this, you would usually run
`make menuconfig` in the `linux-build` folder. Finally, building the `Image`
target will produce the binary that we need.

When the build completes, check that the kernel image binary is present:

```bash
ls linux-build/arch/arm64/boot/Image
```

