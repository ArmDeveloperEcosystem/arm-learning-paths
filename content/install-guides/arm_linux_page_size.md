---
additional_search_terms:
- linux
- cloud

layout: installtoolsall
minutes_to_complete: 30
author: Geremy Cohen
multi_install: false
multitool_install_part: false
title: Increasing Linux Kernel Page Size on Arm-based Systems
weight: 1
---


{{% notice Backup and Test before trying in Production%}}
Modifying the Linux kernel page size can lead to system instability or failure. It is recommended to backup your system and test the changes in a non-production environment before applying to production systems.
{{% /notice %}}


## Overview
Most Linux distributions ship with a default kernel page size of 4KB. When running on Arm, your options for pagesize are 4K, 16K, or 64K; this install guide walks you through  install a 64K page size kernel on Arm-based Linux systems.

## Common Steps

1. Check the current page size:

```bash
getconf PAGESIZE
```
The output should be:

```output
4096
```

This indicates the current page size is 4KB. If you see a value that is different, you are already using a page size other than 4096 (4K).  On Arm systems, the valid options are 4K, 16K, and 64K.


## Instructions for Ubuntu 22.04+

To install a 64K page size kernel on Ubuntu 22.04+, follow these steps:

1. Install dependencies and 64K kernel:

```bash
sudo apt-get -y update 
sudo apt-get -y install git build-essential autoconf automake libtool gdb wget linux-generic-64k
```
2. Instruct grub to load the 64K kernel by default:

```bash
echo "GRUB_FLAVOUR_ORDER=generic-64k" | sudo tee /etc/default/grub.d/local-order.cfg 
````

3. Update grub then reboot:

```bash
sudo update-grub 
sudo reboot 
```

4. Upon reboot, check the kernel page size:

```bash
getconf PAGESIZE
```

The output should be:

```output
65536
```

This indicates the current page size is 64KB.  To revert back to the original 4K kernel, run the following commands:

```bash
echo "GRUB_FLAVOUR_ORDER=generic" | sudo tee /etc/default/grub.d/local-order.cfg 
sudo update-grub 
sudo reboot 
```


## Instructions for Debian 11+

Unlike Ubuntu, Debian does not provide a 64K kernel via apt, so you will need to compile it from source.  There are two ways to do this: 1) download the source from the kernel.org website, or 2) use the Debian source package.  This guide will use the Debian source package.

### Install from Debian Source Package (Easiest, Not Customizable)

To install a 64K page size kernel via package manager, follow these steps:

1. Download the kernel and cd to its directory:
```bash

# Fetch the actual kernel source
apt source linux
# Go into the source dir
cd linux-6.1.*
```

### Install from kernel.org (Advanced, More Customizable)

{{% notice Yo %}}
If you already completed the step of installing from a Debian Source Package, you can skip this section.
{{% /notice %}}

1. Visit https://cdn.kernel.org/pub/linux/kernel/v6.x/ and download the .tar.gz of the kernel version you want to install. 
2. Untar/gzip the file to its own directory.
3. Cd into the directory.

### Common Installer Steps 

Now that you have the kernel source, follow these steps to build and install the kernel. From within the source directory, run the following commands:
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
sed -i 's/^EXTRAVERSION =.*/EXTRAVERSION = -64K/' Makefile

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
```
The output should be:

```output
65536
```
This indicates the current page size is 64KB.  To revert back to the original 4K kernel, run the following commands:

```bash
# Revert to original kernel
sudo apt-get -y install linux-generic
sudo update-grub
sudo reboot
```
The system will now reboot with the original 4K kernel.  To check the page size, run the following command:
```bash
getconf PAGESIZE
``` 

The output should be:

```output
4096
```
This indicates the current page size is 4KB.
## Conclusion
You have successfully installed a 64K page size kernel on your Arm-based Linux system. You can now take advantage of the larger page size for improved performance in certain workloads. If you need to revert back to the original 4K kernel, you can do so by following the steps outlined above.

## Additional Resources
- [Kernel.org](https://kernel.org)
- [Debian Kernel Source](https://www.debian.org/doc/manuals/debian-reference/ch05.en.html#_kernel_source)
- [Ubuntu Kernel Source](https://wiki.ubuntu.com/Kernel/BuildYourOwnKernel)

