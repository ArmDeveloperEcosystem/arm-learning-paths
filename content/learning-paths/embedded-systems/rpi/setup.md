---
# User change
title: "Setup a Raspberry Pi 4 and an Arm cloud instance" 

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Before you begin

A Raspberry Pi 4 running Raspberry Pi OS and an Arm based instance from a cloud service provider are required for this Learning Path. Refer to [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/) to select a cloud provider. 

## Install Raspberry Pi OS 

Install Raspberry Pi OS on your Raspberry Pi 4 using the [Raspberry Pi documentation](https://www.raspberrypi.com/documentation/computers/getting-started.html). There are numerous ways to prepare an SD card, but [Raspberry Pi Imager](https://www.raspberrypi.com/software/) is recommended from a Windows, Linux, or macOS computer with an SD card slot or SD card adapter. 

Make sure to install the 64-bit version of Raspberry Pi OS. This provides compatibility with Arm cloud servers to compare and contrast development tasks.

Insert the SD card into the Raspberry Pi 4 and go through the setup steps to set your country, create a username and password, connect Wi-Fi, and update the software. 

Reboot to start again with the updated settings. 

Open a terminal and use the Raspberry Pi configuration utility to enable SSH. 

```console
sudo raspi-config
```
Select option 3 for Interfacing Options, then select option 2 for SSH.

You should now be able to SSH to the Raspberry Pi. 

If you need to find the IP address of your Raspberry Pi use the `ifconfig` command at the terminal prompt. 

If `ifconfig` is not found, install it using the package manager. 

```console
sudo apt-get install net-tools
```

If you want to SSH from outside of your local network, read [Access remote computers with remote.it](/learning-paths/cross-platform/remoteit/). 

## Create an Arm cloud server

Use a cloud service provider of your choice and create a virtual machine. The recommended operating system is `Ubuntu 20.04` or `Ubuntu 22.04`. These are available from all cloud service providers which offer Arm instances. 

Confirm you can SSH to the cloud server and confirm the Arm architecture before moving to the next section. 

On both the Raspberry Pi and the cloud server, confirm the Arm 64-bit architecture by running the `uname` command on each computer.

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

The next section identifies the hardware of each machine.
