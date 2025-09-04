---
# User change
title: "Transfer Files Over USB"

weight: 7 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

1. [Log in to Linux]( {{< relref "2-boot-nxp.md" >}} ) on the board, as a [super user]( {{< relref "3-create-super-user" >}} )

2. On your machine with the source file, copy the source file to a USB-A thumb drive:

3. Insert the thumb drive into the NXP board's USB-A port
  
4. Mount the thumb drive and then copy the files to the board:
   ```bash { output_lines = "1" }
   # Execute these commands on the board
   mount /dev/sda1 /mnt
   cp /mnt/<source_file> /path/to/destination/directory/
   ```

   Example:
   ```bash { output_lines = "1" }
   cp /mnt/install.sh ./apps/test_app/
   ```

5. [optional] Unmount the thumbdrive and then remove it from the NXP board
   ```bash
   umount /mnt
   ```