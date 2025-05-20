---
title: Ubuntu Page Size Modification
weight: 3
### FIXED, DO NOT MODIFY
layout: learningpathall
---

To install a 64K page size kernel on Ubuntu 22.04+, follow these steps:

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

### Install dependencies and 64K kernel
First, update apt

```bash
sudo apt-get -y install git build-essential autoconf automake libtool gdb wget linux-generic-64k
```
Instruct grub to load the 64K kernel by default:

```bash
echo "GRUB_FLAVOUR_ORDER=generic-64k" | sudo tee /etc/default/grub.d/local-order.cfg 
````

### Update grub then reboot

```bash
sudo update-grub 
sudo reboot 
```

Upon reboot, check the kernel page size and name:

```bash
getconf PAGESIZE
uname -r
```

The output should be:

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

Upon reboot, check the kernel page size and name:

```bash
getconf PAGESIZE
uname -r
```

The output should be:

```output
4096
6.11.0-1013-gcp
```
This confirms the current page size is 4KB and you are running the original kernel.