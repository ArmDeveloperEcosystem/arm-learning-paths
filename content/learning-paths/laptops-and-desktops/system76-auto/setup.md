---
# User change
title: "Set up an automotive development environment"

weight: 3

layout: "learningpathall"
---

## Before you begin

This Learning Path explains how to perform automotive software development using the [System76 Thelio Astra](https://system76.com/arm) Linux desktop computer running Ubuntu. 

Before you begin, install Multipass using the [Multipass install guide](/install-guides/multipass/) for Arm Linux. You can then use Multipass to create a cloud-style virtual machine on your desktop computer. 



## Create a virtual machine using Multipass

A Multipass virtual machine is a good way to create the required automotive development environment and isolate the build and test process. Using Multipass also allows you to split the resources of the Thelio Astra and specify the number of CPUs and the portion of memory and storage for the development environment. It is also easy to delete an existing VM and create a new one whenever required. 

The Arm Automotive Solutions Software Reference Stack requires Ubuntu 20.04 for the build and test machine. The Thelio Astra ships with either Ubuntu 22.04 or 24.04. With Multipass, you can use Ubuntu 20.04 for the development environment, isolate the development from the native operating system, and avoid any compatibility issues.

To get started, create a Multipass virtual machine named `u20-32` with Ubuntu 20.04 and 32 CPUs:

```console
multipass launch 20.04 --name u20-32 --cpus 32 --disk 250G --memory 32G 
```
{{% notice Note %}}
You can adjust the configuration of the setup, by changing the number of CPUs, the allotted memory, and the disk space size. Using more of these resources will speed up the build process.

This Learning Path documents an example using a Thelio Astra with 64 CPUs, 64 GB of RAM, and 1 TB of storage.
{{% /notice %}}
 

Start a bash shell in the Ubuntu 20.04 VM:

```console
multipass shell u20-32 
```

Update the Ubuntu software:

```console
sudo apt update ; sudo apt upgrade -y
```

### Create swap space

Building the automotive software stack requires significant memory resources, so it's good practice to create swap space. Without swap space, some build processes might fail due to lack of memory. 

Create 10 GB of swap space:

```
sudo fallocate -l 10G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

To confirm the swap space has been created, run:

```console
swapon --show
```

The output shows the swap space:

```output
NAME      TYPE SIZE USED PRIO
/swapfile file  10G   0B   -2
```

### Install the required development tools

A number of development tools are required to build the Arm Automotive Solutions Software Reference Stack.

Install the required software:

```console
sudo apt install gawk wget git diffstat unzip texinfo gcc build-essential chrpath socat cpio python3 python3-pip python3-pexpect xz-utils debianutils iputils-ping python3-git python3-jinja2 python3-subunit zstd liblz4-tool file locales libacl1 -y
```

Configure the locale and install [Kas](https://kas.readthedocs.io/en/latest/index.html), a setup tool for [BitBake](https://docs.yoctoproject.org/bitbake/): 

```console
sudo locale-gen en_US.UTF-8
sudo -H pip3 install --upgrade kas==4.3.2 && sudo apt install python3-newt -y
```

You now have a Multipass virtual machine running Ubuntu 20.04 with the required swap space and the required development tools installed. 

Proceed to the next section to build the Arm Automotive Solutions Software Reference Stack.
