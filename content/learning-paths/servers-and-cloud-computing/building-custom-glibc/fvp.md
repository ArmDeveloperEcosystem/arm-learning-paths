---
title: Boot Linux on the FVP
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction

During this step, you will set up everything for the FVP to run and then boot the Linux system using the kernel and the root file system that you prepared earlier in the earlier sections.

Arm [Fixed Virtual Platform (FVP)](https://developer.arm.com/downloads/-/arm-ecosystem-fvps) is a model that allows you to access functionality
of Armv8.x or v9.x hardware. You will use the Armv-A Base Rev C Architecture Envelope Model (AEM).

In addition to the model itself, you also need the device tree and the firmware. To simplify
building these components, you will use a tool called [Shrinkwrap](https://gitlab.arm.com/tooling/shrinkwrap).

This tool comes with a detailed [user guide](https://shrinkwrap.docs.arm.com/en/latest/) that covers all of its features and
configuration options. You will also leverage this tool to run and boot the images you prepared on the FVP.

Shrinkwrap can be used in a few different ways. One of the ways is to use a Docker container to facilitate the building of the firmware and
running the FVP. This helps avoid installing all the dependencies on your host system.

## Install Shrinkwrap

First, install prerequisites in a Python virtual environment using Python 3.x:

```bash
cd $HOME
python -m venv ./workspace/venv
source ./workspace/venv/bin/activate
pip install -U pip setuptools wheel
pip install pyyaml termcolor tuxmake
```

Shrinkwrap can be used directly from the source, which can be checked out from its Git
repository. Run this command in the workspace directory:

```bash
git clone https://git.gitlab.arm.com/tooling/shrinkwrap.git
export PATH=${PATH}:$(pwd)/shrinkwrap/shrinkwrap
```

Putting Shrinkwrap's main executable on your `PATH` is all you need to install the tool.
To check that it works, ensure that the Python virtual environment we created earlier
is activated, then run this command to confirm shrinkwrap has been correctly installed.

```bash
shrinkwrap --version
```



## Build firmware for the FVP

Before proceeding, ensure that Docker is installed and usable. Follow the installation
instructions for your distro. Now, you can use the Shrinkwrap tool to build the firmware, the third essential ingredient in our
setup. The following step needs to be done once although you will need to repeat it if you
want to rebuild the firmware:

```bash
shrinkwrap build --overlay=arch/v9.4.yaml ns-edk2.yaml
```

This command uses the `arch/v9.4.yaml` config that enables Armv9.4 hardware features.
This config is included with the Shrinkwrap installation. We also use the `ns-edk2.yaml`
config. This configuration file is also a part of the Shrinkwrap tool. It defines the
settings for building and running the firmware using EDK2 on Arm FVPs. The build
process takes some time. During this step, Shrinkwrap downloads the required Docker
image and starts a container to clone all the required firmware repositories and build
the components including the device tree for the FVP.

## Overlay config

At this point, we have everything required to boot our system. Shrinkwrap uses so called overlay
configuration files. The following file instructs Shrinkwrap to connect all the pieces together
and locate the kernel image, and rootfs. It can also be used to tweak any of the FVP
parameters. Create a file in $HOME/workspace directory called `aarch64.yaml` using a text editor of your choice. Copy the contents shown below into the file. Under the ROOTFS and KERNEL values, replace `user` with the the appropriate value (e.g., ubuntu).

```yaml
run:
  rtvars:
    ROOTFS:
      value: /home/user/workspace/rootfs.img
    CMDLINE:
      value: ip=dhcp kpti=off root=/dev/vda2 console=ttyAMA0
    KERNEL:
      value: /home/user/workspace/linux-build/arch/arm64/boot/Image
  params:
    -C bp.hostbridge.userNetworking: 1
    -C bp.hostbridge.userNetPorts: 8022=22,8123=8123
    -C bp.smsc_91c111.enabled: 1
    -C bp.virtio_net.enabled: 0
    -C cluster0.NUM_CORES: 1
    -C cluster1.NUM_CORES: 0
    -C pctl.CPU-affinities: 0.0.0.0
```

The most important parts in this configuration file are:

 * Paths to the rootfs image and the kernel image.
 * The kernel command line, which contains `root=/dev/vda2`, specifying where to locate
   the filesystem to be mounted at `/`.
 * The port mapping `8022=22`, which is used for SSH access into the guest system.
   You can add more ports as needed.

The FVP has many parameters that can be tweaked in this config by adding a `-C param: value`
line to the `params` section. Refer to the [Fast Models Fixed Virtual Platforms Reference Guide](https://developer.arm.com/documentation/100966/latest/Getting-Started-with-Fixed-Virtual-Platforms/Configuring-the-model).
for more details.

## Run FVP with Shrinkwrap

To run the FVP using Docker, execute the following command:

```bash
shrinkwrap run ns-edk2.yaml --overlay ~/workspace/aarch64.yaml
```

At first, Shrinkwrap starts a Docker container and runs the FVP in it. At the beginning
of the output, you may see a line containing the IP address that you need to use for SSH
access into the guest system:

```
Press '^]' to quit shrinkwrap.
All other keys are passed through.
Environment ip address: 172.17.0.2.
```

It also tells you how to stop the FVP execution: press `Ctrl+]` (more on this later).

Booting the Linux on the FVP takes some time. Look out for the system log messages about
growing the root partition to utilize the empty disk space we created earlier.

```
=> Growing root partition
CHANGED: partition=2 ... old: size=1316864 ... new: size=5511135
```

After a couple of minutes, you should be able to SSH in a different terminal into the
guest OS running on the FVP using the IP address reported by the Shrinkwrap tool and the
port number specified earlier in our overlay config:

```bash
ssh root@172.17.0.2 -p 8022
```

The default password is `voidlinux`.

When you have logged in, check the properties of your guest system, for example:

```bash
uname -a
cat /proc/cpuinfo
```

For example, the following terminal output is observed.

```output
cat /proc/cpuinfoLinux void-live 6.13.0 #1 SMP PREEMPT Fri Mar 21 10:16:33 UTC 2025 aarch64 GNU/Linux
```

## Powering down

You can always press `Ctrl+]` to stop Shrinkwrap in the terminal where Shrinkwrap is
running. However, this abruptly aborts execution of the FVP. This may leave the filesystem
in your rootfs image, used by the guest system, in a broken state, resulting in errors
during the next boot. To avoid this, it is advisable to shut down the guest system gracefully
from the root console of your guest system, for example:

```bash
ssh root@172.17.0.2 -p 8022 poweroff
```

Continue to the next section for additional setup. The remaining steps are optional but it
helps prepare our guest system for running Glibc tests and doing other complex tasks.

