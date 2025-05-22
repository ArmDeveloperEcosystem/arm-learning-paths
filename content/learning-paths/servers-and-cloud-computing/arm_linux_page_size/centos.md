---
title: Change page size on CentOS 
weight: 5
### FIXED, DO NOT MODIFY
layout: learningpathall
---

Follow the steps below to install a 64K page size kernel on [CentOS 9  or newer](https://www.centos.org/download/).

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

## Install the 64k kernel package:

Enter the command below to install the 64k kernel:

```bash
sudo dnf -y install kernel-64k
```

You should see a page of output ending with:

```output
...
Installed:
  kernel-64k-5.14.0-583.el9.aarch64                          kernel-64k-core-5.14.0-583.el9.aarch64                         
  kernel-64k-modules-5.14.0-583.el9.aarch64                  kernel-64k-modules-core-5.14.0-583.el9.aarch64                 

Complete!
```

Enter the following to configure the 64K kernel as default and reboot:

```bash
k=$(echo /boot/vmlinuz*64k)
sudo grubby --set-default "$k" --update-kernel "$k"
sudo reboot
```

## Verify the page size and kernel version:

Upon reboot, check the kernel page size and name once again to confirm the changes:

```bash
getconf PAGESIZE
uname -r
```

The output shows the 64k kernel is running: 

```output
65536
5.14.0-583.el9.aarch64+64k
```

## Revert back to the 4K kernel

To revert to the original 4K kernel, enter the following:

```bash
# Get your running kernel (should be something like "5.14.0-583.el9.aarch64+64k")
curr=$(uname -r)

# Strip the "+64k" suffix
base=${curr%+64k}

# Build the full path to the 4K kernel image
k4="/boot/vmlinuz-${base}"

# Sanity‐check that it actually exists
if [[ ! -e "$k4" ]]; then
  echo "Cannot find 4K kernel image at $k4"
  exit 1
fi

echo "Found 4K kernel: $k4"

# remove any crashkernel args
sudo grubby --remove-args="crashkernel=2G-:640M" --update-kernel "$k4"

# set it as the default
sudo grubby --set-default "$k4"

# Reboot the system
sudo reboot
```

Upon reboot, verify you’re on a 4 KB pagesize kernel by entering the following commands:

```bash
getconf PAGESIZE
uname -r
```

The output shows the 4k kernel is running: 

```output
4096
6.1.0-34-cloud-arm64
```

The 4096 indicates the current page size has been reverted to 4KB. 