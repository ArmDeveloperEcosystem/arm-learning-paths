---
title: Change page size on Ubuntu
weight: 3
### FIXED, DO NOT MODIFY
layout: learningpathall
---

To install a 64 K page size kernel on [Ubuntu 22.04 LTS or later](https://releases.ubuntu.com/22.04/), follow the steps below.

## Verify the current page size

Verify you’re using a 4KB base-page-size kernel by entering the following commands:

```bash
getconf PAGESIZE
uname -r
```

The output should be similar to below. The kernel flavor (the string after the version number) may vary, but the first line should always be 4096.

```output
4096
6.1.0-34-cloud-arm64
```

The 4096 indicates the current page size is 4 KB. If you see a value that is different, you are already using a page size other than 4096 (4K).  On Arm systems, the valid options are 4K, 16K, and 64K.

## Install the required dependencies and the 64K kernel

Run the commands to install the required software:

```bash
sudo apt-get -y update
sudo apt-get -y install git build-essential autoconf automake libtool gdb wget linux-generic-64k
```

Next, run the following command to configure GRUB to load the 64K kernel by default:

```bash
echo "GRUB_FLAVOUR_ORDER=generic-64k" | sudo tee /etc/default/grub.d/local-order.cfg 
```

## Update GRUB and reboot

Commit your changes to GRUB and reboot by entering the following:

```bash
sudo update-grub 
sudo reboot 
```

Upon reboot, check the kernel page size and name to confirm the changes:

```bash
getconf PAGESIZE
uname -r
```

The output shows the 64K kernel is running: 

```output
65536
6.8.0-59-generic-64k
```

This indicates that the current page size is 64K and that you are running the new 64K kernel.  

## Revert to the 4K kernel

To revert to the original 4K kernel, run the following commands:

```bash
echo "GRUB_FLAVOUR_ORDER=generic" | sudo tee /etc/default/grub.d/local-order.cfg 
sudo update-grub 
sudo reboot 
```
Upon reboot, verify you’re on a 4KB pagesize kernel by entering the following commands:

```bash
getconf PAGESIZE
uname -r
```

The output shows the 4K kernel is running: 

```output
4096
6.1.0-34-cloud-arm64
```

The 4096 indicates the current page size has been reverted to 4KB.