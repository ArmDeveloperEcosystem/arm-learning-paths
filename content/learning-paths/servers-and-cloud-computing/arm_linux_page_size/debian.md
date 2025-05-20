---
title: Debian Page Size Modification
weight: 4
### FIXED, DO NOT MODIFY
layout: learningpathall
---

Debian does not provide a 64K kernel via apt, so you will need to compile it from source.  There are two ways to do this: 1) download the source from the kernel.org website, or 2) use the Debian source package.  This guide will use the Debian source package.

### Verify current page size
Verify you’re on a 4 KB pagesize kernel:

```bash
getconf PAGESIZE
uname -r
```
The output should be similar to (the important part is the 4096 value):

```output
4096
6.1.0-34-cloud-arm64
```

This indicates the current page size is 4KB. If you see a value that is different, you are already using a page size other than 4096 (4K).  On Arm systems, the valid options are 4K, 16K, and 64K.


### Install from Debian Source Package (Easiest, Not Customizable)

To install a 64K page size kernel via package manager, follow these steps:

First, install dependencies:

```bash
sudo apt-get -y install git build-essential autoconf automake libtool libncurses-dev bison flex libssl-dev libelf-dev bc debhelper-compat rsync
```

Download the kernel and cd to its directory:
```bash

# Fetch the actual kernel source
apt source linux
# Change to kernel source dir
cd -- */
```

## Build and install the kernel

Now that you have the kernel source, follow these steps to build and install the kernel:
```bash
# Use running config as template for new config
cp /boot/config-$(uname -r) .config 

# Modify config to enable 64K page size
sed -i 's/^CONFIG_ARM64_4K_PAGES=y/# CONFIG_ARM64_4K_PAGES is not set/' .config
sed -i 's/^# CONFIG_ARM64_64K_PAGES is not set/CONFIG_ARM64_64K_PAGES=y/' .config
echo '# CONFIG_ARM64_16K_PAGES is not set' >> .config

# Build the kernel 
make ARCH=arm64 olddefconfig

# Set 64 for kernel name suffix
sed -i 's/^EXTRAVERSION =.*/EXTRAVERSION = -64k/' Makefile

# Build Debian packages
make -j$(nproc) ARCH=arm64 bindeb-pkg

# 8. Install
cd ..
sudo dpkg -i linux-image-*64k*.deb linux-headers-*64k*.deb
```

The system is now ready to reboot:
```bash
sudo reboot
```
After reboot, check the kernel page size:
```bash
getconf PAGESIZE
uname -r
```
The output should be:

```output
65536
6.12.22-64k
```
This indicates the current page size is 64K, and you are using the new customer made 64k kernel.  

## Reverting back to the original 4K kernel

To revert back to the kernel we started with:

```bash
dpkg-query -W -f='${Package}\n' 'linux-image-*-64k*' 'linux-headers-*-64k*' \
  | xargs --no-run-if-empty sudo dpkg -r
sudo update-grub
sudo reboot
```
The system will now reboot into the original 4K kernel.  To check the page size, run the following command:
```bash
getconf PAGESIZE
uname -r
``` 

The output should be:

```output
4096
6.1.0-34-cloud-arm64
```
This indicates the current page size is 4KB and you are using the kernel you started with.