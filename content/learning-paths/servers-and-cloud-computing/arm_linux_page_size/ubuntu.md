---
title: Ubuntu Page Size Modification
weight: 3
### FIXED, DO NOT MODIFY
layout: learningpathall
---

To install a 64K page size kernel on Ubuntu 22.04+, follow these steps:

### Verify current page size
Verify you’re on a 4 KB pagesize kernel by entering the following commands:

```bash
getconf PAGESIZE
uname -r
```
The output should be similar to below -- the full kernel name may vary, but the first line should always be **4096**:

```output
4096
6.1.0-34-cloud-arm64
```

The 4096 indicates the current page size is 4KB. If you see a value that is different, you are already using a page size other than 4096 (4K).  On Arm systems, the valid options are 4K, 16K, and 64K.

### Install dependencies and 64K kernel
Run the below command to update apt:

```bash
sudo apt-get -y update
sudo apt-get -y install git build-essential autoconf automake libtool gdb wget linux-generic-64k
```
Then run the following command to have grub to load the 64K kernel by default:

```bash
echo "GRUB_FLAVOUR_ORDER=generic-64k" | sudo tee /etc/default/grub.d/local-order.cfg 
````

### Update grub then reboot

Commit your changes to grub, then reboot by entering the following:
```bash
sudo update-grub 
sudo reboot 
```

Upon reboot, check the kernel page size and name once again to confirm the changes:

```bash
getconf PAGESIZE
uname -r
```

The output should be similar to below -- like before, the full kernel name may vary, but the first line should always be **65536**:

```output
65536
6.8.0-59-generic-64k
```

This indicates the current page size is 64K and you are running the new 64K kernel.  

### Reverting back to the original 4K kernel

To revert back to the original 4K kernel, run the following commands:

```bash
echo "GRUB_FLAVOUR_ORDER=generic" | sudo tee /etc/default/grub.d/local-order.cfg 
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