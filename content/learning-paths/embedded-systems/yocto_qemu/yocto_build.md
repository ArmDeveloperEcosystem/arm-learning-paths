---
# User change
title: "How do I get started with Yocto Linux on Qemu?" 

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## What is the Yocto Project?

The [Yocto Project](https://www.yoctoproject.org/) is an open-source project with a build system that allows software developers to create custom embedded Linux OS distributions regardless of the hardware architecture. 
Developers can configure their custom builds of Yocto using a set of recipes. In this Learning Path you will learn the steps to build a minimal Yocto Linux image for a 64-bit Arm target and run it on [QEMU](https://www.qemu.org/). 

## How do I build a minimal Yocto Linux image for a 64-bit Arm target?

Poky is a reference distribution of the Yocto Project. It is a great starting point to build your own custom distribution as it contains both the build system and the the baseline functional distribution. Along with containing recipes for real target boards, it also contains the recipes for building the image, for example 64-bit Arm machines supported in QEMU. The example 64-bit machine emulated by QEMU does not emulate any particular board but is a great starting point to learn and try the basics of running this distribution.

The first step is to install the packages required to build and run Yocto:

```bash
sudo apt update
sudo apt-get install -y gawk wget git-core diffstat unzip texinfo build-essential chrpath socat cpio python3 python3-pip python3-pexpect xz-utils debianutils iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev pylint xterm python3-subunit mesa-common-dev lz4
```
Now download the Poky reference distribution and checkout the branch/tag you wish to build. You will build `yocto-4.0.6` in this example.

```bash
git clone git://git.yoctoproject.org/poky
cd poky
git checkout tags/yocto-4.0.6 -b yocto-4.0.6-local
```
Next source the script as shown below to initialize your build environment for your 64-bit Arm example machine QEMU target:

```bash
source oe-init-build-env build-qemu-arm64
```
The output is shown below:

```output
You had no conf/local.conf file. This configuration file has therefore been
created for you with some default values. You may wish to edit it to, for
example, select a different MACHINE (target hardware). See conf/local.conf
for more information as common configuration options are commented.

You had no conf/bblayers.conf file. This configuration file has therefore been
created for you with some default values. To add additional metadata layers
into your configuration please add entries to conf/bblayers.conf.

The Yocto Project has extensive documentation about OE including a reference
manual which can be found at:
    https://docs.yoctoproject.org

For more information about OpenEmbedded see their website:
    https://www.openembedded.org/


### Shell environment set up for builds. ###

You can now run 'bitbake <target>'

Common targets are:
    core-image-minimal
    core-image-full-cmdline
    core-image-sato
    core-image-weston
    meta-toolchain
    meta-ide-support

You can also run generated qemu images with a command like 'runqemu qemux86'

Other commonly useful commands are:
 - 'devtool' and 'recipetool' handle common recipe tasks
 - 'bitbake-layers' handles common layer tasks
 - 'oe-pkgdata-util' handles common target package tasks
```

You will now be in the `build-qemu-arm64` directory which is your build directory and where the images for your target are built. As the output from running the command above indicates, you will now need to select the target hardware MACHINE in the conf/local.conf file. To do this, run `sed` to uncomment `MACHINE ?= "qemuarm64"` in conf/local.conf file.

```bash { cwd="poky" }
sed -i '/qemuarm64/s/^#//g' conf/local.conf
```
With the right machine now selected, proceed to building the minimal core image for your target.

```bash { cwd="poky",env_source="poky/oe-init-build-env build-qemu-arm64" }
bitbake core-image-minimal
```

Depending on your machine, this build step can take an hour or more to complete.

After the build is complete, the images are in the `build-qemu-arm64/tmp/deploy/images/qemuarm64` directory.

## How do I run the image on the 64-bit Arm QEMU target?

QEMU is installed on your machine as part of cloning the Poky repository and sourcing the environment script. 

You can now run the command below to launch run the image you built on the 64-bit Arm Qemu target

```console
runqemu qemuarm64 nographic
```

You will see Linux booting on your console. 

Enter `root` when presented with the login prompt.

Run `uname` to check the Linux distribution and the target hardware architecture:

```console
uname -a
```
You will see the output below:

```output
Linux qemuarm64 5.15.78-yocto-standard #1 SMP PREEMPT Wed Nov 16 14:17:41 UTC 2022 aarch64 GNU/Linux
```

To exit QEMU enter `Control-a` followed by `x` and you will return to the shell prompt. 

Congratulations! You have successfully built and run a minimal Yocto Linux image on an example 64-bit Arm machine running in QEMU.
