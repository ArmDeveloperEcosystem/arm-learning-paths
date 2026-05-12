---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Multipass

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
official_docs: https://documentation.ubuntu.com/multipass/en/latest/
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

[Multipass](https://multipass.run/) provides cloud-style virtual machines (VMs) on a variety of platforms and host operating systems. Multipass is popular among developers for efficient local testing. When run on macOS with Apple Silicon or on Linux with a Raspberry Pi 5, Multipass provides a similar experience to cloud instances. A local, software-compatible equivalent of an Arm cloud instance with good performance is an important option for developers.

Multipass provides a clear command line interface (CLI) to easily start virtual machine instances, do development tasks, and clean the VMs from your computer. 

Multipass uses the terms virtual machine and instance synonymously. In this guide, you'll learn how to create a compatible Ubuntu Linux environment for working on cloud instances.

{{% notice Note %}}
A computer running macOS with Apple Silicon or an Arm Linux computer with Kernel-based Virtual Machine (KVM) enabled is required to complete the installation.
{{% /notice %}}

## Download Multipass for macOS {#download}

Download Multipass for macOS from GitHub:

{{% notice Note %}}
The following commands use Multipass version 1.16.2. The same commands work with other versions. Replace the file used in these steps with the file for your version of choice. To find the latest version, see [Multipass releases](https://github.com/canonical/multipass/releases).
{{% /notice %}}

```console
wget https://github.com/canonical/multipass/releases/download/v1.16.2/multipass-1.16.2+mac-Darwin.pkg
```

## Install Multipass on macOS

Install the download using the package command:

```console
sudo installer -pkg multipass-1.16.2+mac-Darwin.pkg -target /
```

The following getting started instructions use the command line interface. If you prefer to use the graphical interface, start it from the macOS Launchpad. The following image shows the initial screen. You can use the UI to create, start, and stop virtual machines.

![Connect #center](/install-guides/_images/multipass-gui.png)

Multipass is now installed. You can now [get Started with Multipass](#getstarted).

## Install Multipass on Arm Linux

Multipass can be used on Arm Linux computers such as the Raspberry Pi 5.

Running Multipass on Linux requires the KVM hypervisor. KVM does not typically work on virtual machines. It requires bare metal.

The following instructions have been tested on a Raspberry Pi 5 running Raspberry Pi OS and Ubuntu.

### Check if KVM is available

Install and run the `kvm-ok` command to confirm KVM is available.

Install `kvm-ok` on Debian-based Linux distributions:

```bash
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

If the command is found and version information is printed, then `snapd` is running.

If you need to install `snapd`, run:

```bash
sudo apt install snapd -y
```

{{% notice Note %}}
You can select from three Multipass releases: stable, beta, or edge. The default version is stable.
Add `--beta` or `--edge` to the following install command to select these more recent versions.
{{% /notice %}}

```bash
sudo snap install multipass
```

## Get started with Multipass {#getstarted}

Multipass is now installed. You can try it out. 

### Confirm Multipass is installed

To confirm multipass is installed, run:

```bash
multipass version
```

If the `multipass` command is not found, add `/snap/bin` to the Bash search path:

```bash
export PATH=$PATH:/snap/bin
```

### List available Ubuntu images

Multipass runs Ubuntu images. The last three long-term support (LTS) versions are available. A Docker environment with Portainer is also available, as well as a few other images.

To see the available images, run the `find` command. Any of the listed images can be used to create a new instance.

```bash
multipass find
```

The output from `find` is similar to:

```output
Image                       Aliases           Version          Description
22.04                       jammy             20251001         Ubuntu 22.04 LTS
24.04                       noble,lts         20251001         Ubuntu 24.04 LTS
25.04                       plucky            20251003         Ubuntu 25.04
daily:25.10                 questing,devel    20251015         Ubuntu 25.10

Blueprint (deprecated)      Aliases           Version          Description
anbox-cloud-appliance                         latest           Anbox Cloud Appliance
charm-dev                                     latest           A development and testing environment for charmers
docker                                        0.4              A Docker environment with Portainer and related tools
jellyfin                                      latest           Jellyfin is a Free Software Media System that puts you in control of managing and streaming your media.
minikube                                      latest           minikube is local Kubernetes
ros2-humble                                   0.1              A development and testing environment for ROS 2 Humble.
ros2-jazzy                                    0.1              A development and testing environment for ROS 2 Jazzy.
```

### Launch a Multipass instance

The default values for launching instances allocate 1 CPU, create a small disk (5 Gb), and limited memory (1 Gb). By default, the name of the instance is automatically assigned.

Use the following command to launch a virtual machine instance with non-default values.

```console
multipass launch lts --name m1u --cpus 4 --disk 16G --memory 4G
```

After the instance is launched, the command prompt returns and the instance is running in the background.

### Connect to a Multipass instance

Use the `list` command to identify created instances. Note the instance names as the name is used in other commands.

```console
multipass list
```

To start a command line shell on a running instance, use the `shell` command:

```console
multipass shell m1u
```

### Execute a command on a Multipass instance

To run a specific command from the host on the instance, use the `exec` command. The command to be run comes after the ``--``:

```console
multipass exec m1u -- uname -a
```

The `uname` output is similar to:

```output
Linux m1u 6.8.0-36-generic #36-Ubuntu SMP PREEMPT_DYNAMIC Mon Jun 10 13:20:23 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux
```

### Print instance information

The `info` command prints information about the instance, including the IP address.

```console
multipass info m1u
```

The output is similar to:

```output
Name:           m1u
State:          Running
Snapshots:      0
IPv4:           192.168.73.29
Release:        Ubuntu 24.04.1 LTS
Image hash:     e380b683b0c4 (Ubuntu 24.04 LTS)
CPU(s):         4
Load:           0.00 0.03 0.01
Disk usage:     2.0GiB out of 15.4GiB
Memory usage:   355.3MiB out of 3.8GiB
Mounts:         --
```

### Mount a host directory into a Multipass instance

To access a large number of files on the host machine without copying or transferring them into the instance, use the `mount` command. This command makes a host directory visible in the instance and all files can be accessed. Modifications made from inside the instance will directly change the files on the host.

For example, to mount a host directory called `dev` and have it appear in the instance, use the `mount` command:

```console
multipass mount dev m1u:/home/ubuntu/dev
```

There are also options to adjust the user and group IDs as needed to avoid permission problems.

### Unmount a host directory from a Multipass instance

Use the `umount` command to unmount the directory:

```console
multipass umount m1u:/home/ubuntu/dev
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
{{% notice Note %}}
Purged instances are no longer recoverable.
{{% /notice %}}

You're now ready to use Multipass.