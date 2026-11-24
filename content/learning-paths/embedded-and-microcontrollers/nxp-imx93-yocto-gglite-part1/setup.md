---
title: "NXP FRDM i.MX 93: Boot and connect the board"
description: "Write the image and verify Ethernet, SSH, clock, and application-core ownership."
weight: 4
layout: "learningpathall"
---

## Write our Yocto image to our microSD card 

On the Linux host with the card reader attached, identify the whole microSD device:

```bash
lsblk -o NAME,SIZE,MODEL,MOUNTPOINTS
```

Writing an image erases that device. Check its model and capacity, unmount its partitions, and replace both placeholders below with the actual WIC artifact and whole device. Keep the factory eMMC image available as a recovery option.

```bash
zstd -d --keep /path/to/nxp-lp-dev-image.rootfs.wic.zst
sudo dd if=/path/to/nxp-lp-dev-image.rootfs.wic of=/dev/sdX   bs=4M conv=fsync status=progress
sync
```

With the board powered off, locate the `SW1` boot configuration switch (the default eMMC setting is `0010`). Set `SW1[3:0]` to `0011` to boot from the SD card, following the bit order in the [FRDM i.MX 93 manual](https://www.nxp.com/webapp/Download?colCode=UM12181). Insert the card and connect the specified power supply. NXP also confirms `SW1 = 0011` in its [FRDM i.MX 93 getting-started guide](https://www.nxp.com/document/guide/getting-started-with-frdm-imx93:GS-FRDM-IMX93).

Connect wired Ethernet to a network with DHCP and Internet access. Connect debug USB port `P16` to your Ubuntu host and open the Cortex-A55 Linux console at 115200 8N1. The second serial port is for the Cortex-M33.

The NXP FRDM i.MX 93 [board guide](https://www.nxp.com/document/guide/getting-started-with-frdm-imx93:GS-FRDM-IMX93) and [manual](https://www.nxp.com/webapp/Download?colCode=UM12181) identify the power, debug, Ethernet, and boot-switch connectors. Use Ethernet networking and the boot-switch positions specified for this board revision.

Apply power to the board to begin its booting from the microSD card.

## Log into the newly booted board and set credentials

On the board's Linux console via the USB serial connection, login. Then set the root password:

```bash
passwd
```

Next, lets find what IP address our board has:

```bash
ip route | grep default | awk '{print $9}'
```

Save off the IP address (we'll replace OUR_BOARD_IP_ADDRESS with this IP address below)

From your Ubuntu host, lets open a SSH shell into our board (with IP address):

```bash
ssh root@OUR_BOARD_IP_ADDRESS
```

Inside our SSH shell, lets get some information about our Yocto image running on our board:

```bash
uname -m
ip -br address
ip route
command -v nxp-mcore
command -v nxp-provision-greengrass
python3 /usr/libexec/nxp-lp/check-greengrass.py
cat /etc/nxp-lp/board.json
nxp-mcore status
```

Expect `aarch64`, the correct NXP FRDM i.MX 93 profile, and an offline application Cortex-M33.

## Verify outbound connectivity

Using the SSH shell into our board, lets check Internet connectivity:

```bash
timedatectl set-ntp true
systemctl status ntpd.service --no-pager -l
ntpq -pn
ntpq -c rv
date -u
timedatectl status
getent hosts amazontrust.com
curl -I https://www.amazontrust.com/repository/AmazonRootCA1.pem
python3 -c 'import sys; print(sys.version)'
```

This image uses `ntpd`. Correct time is required for AWS IoT Greengrass. 

Verify the gateway, DNS, UTC time, HTTPS access, and Python version. The Walnascar image normally uses Python 3.13; record the actual major/minor for Part 3 wheel selection. Part 1's Greengrass services are intentionally not enabled yet. Do not start them until you install the device provisioning information (next section).


## Verify FRDM identity and MCU boot preparation

Reboot your board and stop at U-Boot prompt by pressing `Enter`. Confirm the required configuration:

```bash
printenv bootcmd fdtfile prepare_mcore
```

Output should look like this:

```output
bootcmd=run prepare_mcore; run bsp_bootcmd
fdtfile=imx93-11x11-frdm.dtb
prepare_mcore=setenv mcore_clk clk-imx93.mcore_booted
```

If the output is different, then lets configure it:

```bash
setenv fdtfile imx8mp-frdm.dtb
setenv bootcmd 'run prepare_mcore; run bsp_bootcmd'
saveenv
```

Then reconfirm the configuration:

```bash
printenv bootcmd fdtfile prepare_mcore
```

Output should look like this:

```output
bootcmd=run prepare_mcore; run bsp_bootcmd
fdtfile=imx93-11x11-frdm.dtb
prepare_mcore=setenv mcore_clk clk-imx93.mcore_booted
```

Your board is now ready for the next steps!

## What you have learned

You have learned how to flash and boot the correct NXP FRDM i.MX 93 image, establish SSH over Ethernet, and verify the board profile, application MCU state, and outbound connection before provisioning.
