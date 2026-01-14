---
# User change
title: "Transfer Files Over WiFi"

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

1. [Log in to Linux]( {{< relref "2-boot-nxp.md" >}} ) on the board, as a [super user]( {{< relref "3-create-super-user" >}} )

2. [Enable Wifi]( {{< relref "4-enable-wifi.md" >}} ) on the NXP board

3. Note down the NXP board's IP address on your WiFi network:
   ```bash
   ifconfig | grep RUNNING -A 1
   ```

4. Open a terminal window on the machine with the source file

5. Navigate to the source file directory and copy the file to the NXP board's destination directory:
   ```bash
   # On your machine, in the source file directory
   scp <source_file> <nxp_user>@<nxp_ip_address>:/home/nxp_user/path/to/destination/directory/
   ```
   Example:
   ```bash { output_lines = "1" }
   scp install.sh testuser@192.168.1.1:/home/testuser/apps/test_app/
   ```