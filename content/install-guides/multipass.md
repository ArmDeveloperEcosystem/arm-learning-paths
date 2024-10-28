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

author_primary: Jason Andrews

### Link to official documentation
official_docs: https://multipass.run/docs

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---
{{% notice Note %}}
A computer running macOS with Apple Silicon or an Arm Linux computer with KVM enabled is required to complete the installation.
{{% /notice %}}

[Multipass](https://multipass.run/) provides cloud style virtual machines (VMs). Multipass is popular among developers for efficient, local testing. When run on macOS with Apple Silicon or on Linux with a Raspberry Pi 5, Multipass provides a similar experience to cloud instances. A local, software compatible equivalent of an Arm cloud instance on your desk with good performance is an important option for developers. 

Multipass provides a clear CLI to easily start virtual machine instances, do development tasks, and clean the VMs from your computer.

## Before you begin

Multipass runs on a variety of platforms and host operating systems. The information below covers running Multipass on macOS with Apple Silicon and Arm Linux with the goal of creating a compatible Ubuntu Linux environment for developers working on cloud instances. 

Multipass uses the terms virtual machine and instance synonymously. 

## Installation on macOS

### Download  {#download}

Download Multipass for macOS.

```console
wget https://github.com/canonical/multipass/releases/download/v1.14.1-rc1/multipass-1.14.1-rc1+mac.14+gf2381bfe9.mac-Darwin.pkg
```

### Install

Install the download using the package command.

```console
sudo installer -pkg multipass-1.14.1-rc1+mac.14+gf2381bfe9.mac-Darwin.pkg -target /
```

The getting started instructions below use the command line interface. If you prefer to use the graphical interface start it from the macOS Launchpad, the initial screen is shown below. You can use the UI to create, start, and stop virtual machines. 

![Connect #center](/install-guides/_images/multipass-gui.png)

Multipass is now installed. Proceed to [Get Started with Multipass](#getstarted).

## Installation on Arm Linux 

Multipass can be used on Arm Linux computers such as the Raspberry Pi 5. 

Running Multipass on Linux requires the KVM hypervisor. KVM does not typically work on virtual machines, it requires bare metal.

The instructions have been tested on a Raspberry Pi 5 running Raspberry Pi OS and Ubuntu.

### Check KVM

Install and run the `kvm-ok` command to confirm KVM is available.

Install `kvm-ok` on Debian based Linux distributions using:

```console
sudo apt install cpu-checker -y
```

To check if KVM is available run:

```console
kvm-ok
```

If KVM is available the output will be similar to:

```output
INFO: /dev/kvm exists
KVM acceleration can be used
```

If KVM is not available the output will be similar to:

```output
INFO: /dev/kvm does not exist
HINT:   sudo modprobe kvm
INFO: For more detailed results, you should run this as root
HINT:   sudo /usr/sbin/kvm-ok
```

If KVM is available, proceed with the install. 

### Install 

You may need to install the Snap daemon, `snapd`, before installing Multipass. 

If you are not sure if it is running, execute the command:

```console
snap version
```

If the command is found and version information is printed, then `snapd` is running. 

If you need to install `snapd` run:

```console
sudo apt install snapd -y
```

LXD is also required for Multipass.

```console
sudo snap install lxd
```

{{% notice Note %}}
You can select from three Multipass releases: stable, beta, or edge. The default version is stable. 
Add `--beta` or `--edge` to the install command below to select these more recent versions.
{{% /notice %}}

```console
sudo snap install multipass
```

Multipass is now installed.

## Get started with Multipass {#getstarted}

To confirm multipass is installed run the `version` command.

```console
multipass version
```

If the `multipass` command is not found, you can add `/snap/bin` to the Bash search path using:

```console
export PATH=$PATH:/snap/bin
```

Multipass runs Ubuntu images. The last three LTS (long-term support) versions are available. A Docker environment with Portainer is also available as well as a few other images.

To see the available images run the `find` command. Any of the listed images can be used to create a new instance.

```console
multipass find 
```
The output from `find` will be similar to the below.

```output
Image                       Aliases           Version          Description
20.04                       focal             20240821         Ubuntu 20.04 LTS
22.04                       jammy             20241002         Ubuntu 22.04 LTS
24.04                       noble,lts         20241004         Ubuntu 24.04 LTS
daily:24.10                 oracular,devel    20241009         Ubuntu 24.10

Blueprint                   Aliases           Version          Description
anbox-cloud-appliance                         latest           Anbox Cloud Appliance
charm-dev                                     latest           A development and testing environment for charmers
docker                                        0.4              A Docker environment with Portainer and related tools
jellyfin                                      latest           Jellyfin is a Free Software Media System that puts you in control of managing and streaming your media.
minikube                                      latest           minikube is local Kubernetes
ros-noetic                                    0.1              A development and testing environment for ROS Noetic.
ros2-humble                                   0.1              A development and testing environment for ROS 2 Humble.
```

### Launching instances

The default values for launching instances allocate 1 CPU, create a small disk (5 Gb), and limited memory (1 Gb). By default, the name of the instance is automatically assigned. 

Most developers are likely to want to modify the defaults. 

Use the command below to launch a virtual machine instance with non-default values.

```console
multipass launch lts --name m1u --cpus 4 --disk 16G --memory 4G
```

Once launched, the command prompt returns and the instance is running in the background.

### Connect and use instances

Use the `list` command to identify created instances. Make note of the instance names as the name is used in other commands.

```console
multipass list
```

To start a command line shell on a running instance use the `shell` command.

```console
multipass shell m1u
```

To run a specific command from the host on the instance use the `exec` command. The command to be run comes after the ``--``

```console
multipass exec m1u -- uname -a
```

The `uname` output will look similar to:

```output
Linux m1u 6.8.0-36-generic #36-Ubuntu SMP PREEMPT_DYNAMIC Mon Jun 10 13:20:23 UTC 2024 aarch64 aarch64 aarch64 GNU/Linux
```

### Print information

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

### Mount a host directory

To access a large number of files on the host machine without copying or transferring them into the instance use the `mount` command. This command makes a host directory visible in the instance and all files can be accessed. Modifications made from inside the instance will directly change the files on the host.

For example, to mount a host directory called `dev` and have it appear in the instance use the `mount` command.

```console
multipass mount dev m1u:/home/ubuntu/dev
```

There are also options to adjust the user and group IDs as needed to avoid permission problems. 

Use the `umount` command to unmount the directory.

```console
multipass umount m1u:/home/ubuntu/dev
```

Directories can be dynamically mounted and unmounted without stopping the instance.

### Stop and Start

Multipass instances can be stopped and started quickly. 

To stop the instance.

```console
multipass stop m1u
```

Following the stop the state will change to Stopped on the list command.

To start the instance.

```console
multipass start m1u
```

### Cleanup

Multipass instances are easy to delete. There is one extra level of protection to recover deleted instances before they are fully deleted. 

Use the `delete` command to delete. 

```console
multipass delete m1u
```
After delete, the state will change to Deleted, but it is still recoverable.

```console
multipass recover m1u
```
Use the `purge` command to permanently remove all deleted instances.

```console
multipass purge 
```
{{% notice Note %}}
Purged instances are no longer recoverable.
{{% /notice %}}
