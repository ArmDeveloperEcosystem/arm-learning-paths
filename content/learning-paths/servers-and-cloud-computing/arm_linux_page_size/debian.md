---
title: Change page size on Debian
weight: 4
### FIXED, DO NOT MODIFY
layout: learningpathall
---

Follow the steps below to install a 64K page size kernel on [Debian 11 “Bullseye” or newer](https://www.debian.org/releases/bullseye/).

Debian does not provide a 64K kernel package, so you will need to compile it from source.  

There are two ways to do this: 
- Download the source from kernel.org.
- Use the Debian source package.

The instructions below use the Debian source package. 

## Verify the current page size

Verify you’re using a 4 KB pagesize kernel by entering the following commands:

```bash
getconf PAGESIZE
uname -r
```

The output should be similar to below. The kernel flavor (the string after the version number) may vary, but the first line should always be 4096.

```output
4096
6.1.0-34-cloud-arm64
```

The 4096 indicates the current page size is 4KB. If you see a value that is different, you are already using a page size other than 4096 (4K).  On Arm systems, the valid options are 4K, 16K, and 64K.

## Install the Debian kernel source package

Follow the steps below to install a 64K kernel using the Debian kernel source package.

First, update, and install the required software:

```bash
sudo apt-get -y update
sudo apt-get -y install git build-essential autoconf automake libtool libncurses-dev bison flex libssl-dev libelf-dev bc debhelper-compat rsync
```

Download the kernel source and cd to its directory:

```bash
# Fetch the actual kernel source
apt source linux
# Change to kernel source dir
cd -- linux*/
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

# Build new kernel config as Debian packages
make -j$(nproc) ARCH=arm64 bindeb-pkg

# install the Debian packages
cd ..
sudo dpkg -i linux-image-*64k*.deb linux-headers-*64k*.deb
```

The system is now ready to reboot:

```bash
sudo reboot
```

Upon reboot, check the kernel page size and name once again to confirm the changes:

```bash
getconf PAGESIZE
uname -r
```

The output shows the 64k kernel is running: 

```output
65536
6.12.22-64k
```

This indicates the current page size is 64K, and you are using the new custom made 64k kernel.  

## Revert back to the 4K kernel

To revert back to the kernel we started with, enter:

```bash
dpkg-query -W -f='${Package}\n' 'linux-image-*-64k*' 'linux-headers-*-64k*' \
  | xargs --no-run-if-empty sudo dpkg -r
sudo update-grub
sudo reboot
```

Upon reboot, verify you’re on a 4 KB pagesize kernel by entering the following commands:

```bash
getconf PAGESIZE
uname -r
```

The output should be similar to below -- the full kernel name may vary, but the first line should always be **4096**:

```output
4096
6.1.0-34-cloud-arm64
```

The 4096 indicates the current page size has been reverted to 4KB. 