---
title: Centos Page Size Modification
weight: 5
### FIXED, DO NOT MODIFY
layout: learningpathall
---

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


### Install the kernel-64k package:

   ```bash
   sudo dnf -y install kernel-64k
   ```

### Set the kernel-64k as the default kernel and add necessary kernel arguments:

   ```bash
   k=$(echo /boot/vmlinuz*64k)
   sudo grubby --set-default "$k" \
              --update-kernel "$k" \
              --args "crashkernel=2G-:640M"
   ```

### Reboot the system:

   ```bash
   sudo reboot
   ```

### Verify the page size and kernel version:

   ```bash
   getconf PAGESIZE
   uname -r
   ```

   The output should be:

   ```output
   65536
   5.14.0-583.el9.aarch64+64k
   ```

## Reverting back to the original 4K kernel on CentOS

To revert to the original 4K kernel, run:

```bash
# 1) Get your running kernel (should be something like "5.14.0-583.el9.aarch64+64k")
curr=$(uname -r)

# 2) Strip the "+64k" suffix
base=${curr%+64k}

# 3) Build the full path to the 4K kernel image
k4="/boot/vmlinuz-${base}"

# 4) Sanity‐check that it actually exists
if [[ ! -e "$k4" ]]; then
  echo "Cannot find 4K kernel image at $k4"
  exit 1
fi

echo "Found 4K kernel: $k4"

# 5) (Optional) remove any crashkernel args if you added them earlier
sudo grubby --remove-args="crashkernel=2G-:640M" --update-kernel "$k4"

# 6) Finally, set it as the default
sudo grubby --set-default "$k4"

# Reboot the system
sudo reboot
```

Upon reboot, verify:

```bash
getconf PAGESIZE
uname -r
```

The output should be:

```output
4096
<original-kernel-version>
```