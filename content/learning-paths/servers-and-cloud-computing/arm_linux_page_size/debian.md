---
title: Change page size on Debian
weight: 4
### FIXED, DO NOT MODIFY
layout: learningpathall
---

You can install a packaged 16K page size kernel on Debian 12 or later. Debian doesn't provide a 64K kernel package, so you need to compile a 64K kernel from source.

## Verify the current page size

Verify that you're using a 4 KB page size kernel:

```bash
getconf PAGESIZE
uname -r
```

The output is similar to the following. The kernel flavor (the string after the version number) can vary, but the first line is always 4096:

```output
4096
6.1.0-34-cloud-arm64
```

The 4096 indicates the current page size is 4 KB. If you see a different value, you're already using a page size other than 4 KB. On Arm systems, the valid options are 4 KB, 16 KB, and 64 KB.

## Install a packaged 16K kernel

Debian provides the [`linux-image-arm64-16k` package](https://packages.debian.org/linux-image-arm64-16k) for Debian 13 (Trixie) and through backports for Debian 12 (Bookworm).

Check your Debian release codename:

```bash
. /etc/os-release
echo "$VERSION_CODENAME"
```

The output is either `trixie` for Debian 13 or `bookworm` for Debian 12.

### Install on Debian 13

On Debian 13, install the 16K kernel directly from the standard package repositories:

```bash
sudo apt-get update
sudo apt-get install linux-image-arm64-16k
```

### Install on Debian 12

On Debian 12, add the official Bookworm Backports repository by following the [Debian Backports configuration format](https://backports.debian.org/Instructions/):

```bash
sudo tee /etc/apt/sources.list.d/debian-backports.sources > /dev/null <<'EOF'
Types: deb
URIs: http://deb.debian.org/debian
Suites: bookworm-backports
Components: main
Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg
EOF
```

Update the package index and install the 16K kernel from backports:

```bash
sudo apt-get update
sudo apt-get install -t bookworm-backports linux-image-arm64-16k
```

Reboot the system to load the new kernel:

```bash
sudo reboot
```

After the system restarts, verify the page size and running kernel:

```bash
getconf PAGESIZE
uname -r
```

The first command returns `16384`, and the kernel name ends in `arm64-16k`.

If you want to test a 64K page size instead, continue with the source-build instructions.

## Install a 64K kernel from source

You can build a 64K kernel from the Debian source package. Another option is to download the source from kernel.org, but these instructions use the Debian source package.

First, update the package index and install the required software:

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

## Build and install the 64K kernel

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

This indicates the current page size is 64 KB, and you're using the new custom-built 64K kernel.

## Revert from the 16K kernel

Boot into the original 4K kernel from the bootloader's advanced options. Then remove the 16K kernel packages:

```bash
dpkg-query -W -f='${Package}\n' 'linux-image-*16k*' 'linux-headers-*16k*' 2>/dev/null \
  | xargs --no-run-if-empty sudo apt-get purge -y
sudo update-grub
sudo reboot
```

After the system restarts, verify that `getconf PAGESIZE` returns `4096`.

## Revert from the 64K kernel

To revert to the kernel we started with, enter:

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

The 4096 indicates the current page size has been reverted to 4 KB.
