---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Multipass
description: Install Multipass on Apple Silicon macOS or Arm Linux and create Ubuntu virtual machine instances for local Arm cloud-style development.

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- cloud
- vm
- virtual machine
- linux
- containers
- container
- docker

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 30

author: Jason Andrews

### Link to official documentation
official_docs: https://canonical.com/multipass/docs/
ecosystem_dashboard: https://developer.arm.com/ecosystem-dashboard/linux?package=Canonical%20Multipass

test_images:
- ubuntu:latest
test_maintenance: false

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

[Multipass](https://canonical.com/multipass) provides cloud-style virtual machines (VMs) for local development and testing. This guide installs Multipass on macOS with Apple Silicon or on Arm Linux, such as a Raspberry Pi 5, and verifies it by launching an Ubuntu instance.

Multipass provides a clear command line interface (CLI) to easily start virtual machine instances, do development tasks, and clean the VMs from your computer. 

Multipass uses the terms virtual machine and instance synonymously. In this guide, you'll learn how to create a compatible Ubuntu Linux environment for working on cloud instances.

A Mac with Apple Silicon or an Arm Linux computer with Kernel-based Virtual Machine (KVM) enabled is required. The macOS installation also requires an account with administrator privileges.

## Download Multipass for macOS

Download Multipass for macOS from GitHub:

{{% notice Note %}}
The following commands use Multipass version 1.17.0. The same commands work with other versions. Replace the file used in these steps with the file for your version of choice. To find the latest version, see [Multipass releases](https://github.com/canonical/multipass/releases).
{{% /notice %}}

```console
curl -fL -o multipass-1.17.0+mac-Darwin.pkg https://github.com/canonical/multipass/releases/download/v1.17.0/multipass-1.17.0%2Bmac-Darwin.pkg
```

## Install Multipass on macOS

Install the downloaded package:

```console
sudo installer -pkg multipass-1.17.0+mac-Darwin.pkg -target /
```

To upgrade an existing installation, run the new installer in the same way. Existing instances are preserved.

The following instructions use the command line interface. If you prefer the graphical interface, open Multipass from **Applications**. You can use it to create, start, and stop virtual machines.

![Screenshot of the Multipass graphical interface showing the Welcome to Multipass window with cards for Ubuntu Server, Ubuntu Core, Fedora, and Debian, each with Launch and Configure buttons alt-text#center](/install-guides/_images/multipass-gui.png "The Multipass graphical interface on macOS")

### Select the macOS virtualization driver

Multipass 1.17.0 introduces a preview driver based on the Apple Virtualization framework, selected with the name `applevz`. QEMU remains the default driver. To try the new driver before creating an instance, run:

```console
multipass set local.driver=applevz
```

Confirm the selected driver:

```console
multipass get local.driver
```

The expected output is:

```output
applevz
```

{{% notice Note %}}
Instances belong to the driver that created them. Switching drivers hides existing instances until you switch back; it does not migrate them. See [Canonical's driver setup guide](https://canonical.com/multipass/docs/latest/how-to-guides/customise-multipass/set-up-the-driver/) for details.
{{% /notice %}}

If you prefer to use QEMU instead of the preview driver, run the following command. Skip it to continue with `applevz`:

```console
multipass set local.driver=qemu
```

Multipass is now installed. Continue with [Get started with Multipass](#getstarted).

## Install Multipass on Arm Linux

Multipass can be used on Arm Linux computers such as the Raspberry Pi 5.

Running Multipass on Linux requires KVM acceleration. Use a physical Arm Linux computer, or a virtual machine whose host exposes nested virtualization.

The following instructions have been tested on a Raspberry Pi 5 running Raspberry Pi OS and Ubuntu.

### Check if KVM is available

Install and run the `kvm-ok` command to confirm KVM is available.

Install `kvm-ok` on Debian-based Linux distributions:

```bash
sudo apt update
sudo apt install cpu-checker -y
```

To check if KVM is available, run:

```console
sudo kvm-ok
```

If KVM is available, the output is similar to:

```output
INFO: /dev/kvm exists
KVM acceleration can be used
```

If KVM is not available, the output is similar to:

```output
INFO: /dev/kvm does not exist
HINT:   sudo modprobe kvm
INFO: For more detailed results, you should run this as root
HINT:   sudo /usr/sbin/kvm-ok
```

If KVM is available, proceed with the install.

### Install the Snap daemon on Arm Linux

You might need to install the Snap daemon, `snapd`, before installing Multipass.

If you aren't sure if it is running, execute the command:

```console
snap version
```

If the output includes versions for both `snap` and `snapd`, the Snap daemon is available.

If you need to install `snapd`, run:

```bash
sudo apt install snapd -y
```

For distribution-specific setup, including Raspberry Pi OS, follow the [snapd installation instructions](https://snapcraft.io/docs/installing-snapd). Log out and back in, or restart the computer, after installing `snapd` so that its paths and services are available.

The following command installs the latest stable Multipass release. Snap updates it automatically. Use `snap info multipass` to inspect the versions available in other channels; beta and edge builds are intended for testing.

```bash
sudo snap install multipass
```

## Get started with Multipass {#getstarted}

Multipass is now installed. You can try it out. 

### Confirm Multipass is installed

To confirm Multipass is installed, run:

```bash
multipass version
```

The expected output for the macOS package above is:

```output
multipass   1.17.0+mac
multipassd  1.17.0+mac
```

On Linux, if the `multipass` command is not found, add `/snap/bin` to the shell search path:

```bash
export PATH="$PATH:/snap/bin"
```

### List available Ubuntu images

Multipass 1.17 supports Ubuntu, Debian, and Fedora images. This guide uses Ubuntu. Blueprints, including the Docker environment with Portainer, were removed in version 1.17.

To see the images available for your host architecture, run the `find` command. Use an image name or alias from the list when creating an instance.

```bash
multipass find
```

The output is similar to the following. Image versions and available releases change over time:

```output
Image             Aliases                     Version          Description
22.04             jammy                       20261020         Ubuntu 22.04 LTS
24.04             noble                       20261017         Ubuntu 24.04 LTS
26.04             resolute,lts,ubuntu         20261016         Ubuntu 26.04 LTS
26.10             stonking                    20261019         Ubuntu 26.10
core:core22                                   current          Ubuntu Core 22
core:core24                                   current          Ubuntu Core 24
core:core26                                   current          Ubuntu Core 26
debian            trixie                      20261001         Debian 13
fedora                                        20260422         Fedora 44
```

### Launch a Multipass instance

The default values for launching instances allocate 1 CPU, 5 GB of disk space, and 1 GB of memory. By default, the name of the instance is automatically assigned.

Use the following command to launch the latest Ubuntu LTS image with 4 CPUs, 16 GB of disk space, and 4 GB of memory. Make sure your host has these resources available.

```console
multipass launch lts --name m1u --cpus 4 --disk 16G --memory 4G
```

The first launch downloads the image and waits for Ubuntu initialization to complete, which can take several minutes. When it finishes, the output is similar to:

```output
Launched: m1u in zone1
```

The command prompt returns and the instance runs in the background. Multipass assigns an availability zone automatically, so the zone name can differ.

### Connect to a Multipass instance

Use the `list` command to identify created instances. Note the instance names as the name is used in other commands.

```console
multipass list
```

To start a command line shell on a running instance, use the `shell` command:

```console
multipass shell m1u
```

Run `exit` to return to your host shell before running the remaining `multipass` commands.

### Execute a command on a Multipass instance

To run a specific command from the host on the instance, use the `exec` command. The command to be run comes after the ``--``:

```console
multipass exec m1u -- uname -m
```

The expected output on an Arm host is:

```output
aarch64
```

### Print instance information

The `info` command prints information about the instance, including the IP address.

```console
multipass info m1u
```

The output is similar to the following. The zone, IP address, image hash, release, and resource usage depend on your instance:

```output
Name:           m1u
State:          Running
Zone:           zone1
Snapshots:      0
IPv4:           192.168.252.3
Release:        Ubuntu 26.04.1 LTS
Image hash:     8eb876c2ccc4 (Ubuntu 26.04 LTS)
CPU(s):         4
Load:           0.17 0.08 0.02
Disk usage:     2.5GiB out of 15.4GiB
Memory usage:   410.7MiB out of 3.8GiB
Mounts:         --
```

### Mount a host directory into a Multipass instance

To access a large number of files on the host machine without copying or transferring them into the instance, use the `mount` command. This command makes a host directory visible in the instance and all files can be accessed. Modifications made from inside the instance will directly change the files on the host.

For example, create a host directory called `scratch` if it does not exist, then use the `mount` command:

```console
mkdir -p scratch
multipass mount scratch m1u:/home/ubuntu/scratch
```

{{% notice Note %}}
If accessing mounted files returns `Permission denied`, check the ownership of both the host directory and its files. Files owned by a group other than your primary host group can require an explicit `--gid-map` mapping. Use `--uid-map` and `--gid-map` to map host IDs to the Ubuntu user's IDs. See the [mount command reference](https://canonical.com/multipass/docs/stable/reference/command-line-interface/mount/) for the syntax.
{{% /notice %}}

### Unmount a host directory from a Multipass instance

Use the `umount` command to unmount the directory:

```console
multipass umount m1u:/home/ubuntu/scratch
```

Directories can be dynamically mounted and unmounted without stopping the instance.

### Stop and start a Multipass instance

Multipass instances can be stopped and started quickly.

Stop the instance:

```console
multipass stop m1u
```

After stopping the instance, the state will change to Stopped on the list command.

Start the instance:

```console
multipass start m1u
```

### Clean up Multipass instances

Use the `delete` command to delete the instance:

```console
multipass delete m1u
```
After deletion, the state will change to Deleted. There is one extra level of protection to recover deleted instances before they are fully deleted. 

Use the `recover` command to recover the deleted instance:

```console
multipass recover m1u
```
Use the `purge` command to permanently remove all deleted instances:

```console
multipass purge
```

You're now ready to use Multipass.
