---
title: Prepare the SD card and boot the board
description: Build a bootable SD card image with mtools, set the AM62L EVM boot switches, and watch U-Boot verify the signed Zephyr image and start it on the board.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why you start from the vendor's card image

Open a terminal and load the environment: `source $HOME/zephyr-secure-boot/env.sh`.

Some boot ROMs look for the first-stage file by name on a FAT partition, as the AM62L's does; others read it from a fixed offset on the card. That is why you start from the vendor's own card image. On every board, U-Boot's `fatload` then reads `zephyr-a.itb` from the partition in `BOOT_DEV`.

## Build the SD card image from the vendor's boot partition

On the AM62L EVM, the boot ROM reads `tiboot3.bin` from the card's first FAT partition and is picky about its format: TI's FAT16 partition boots, while a FAT32 one with 512-byte clusters leaves the console empty. Keep TI's partition byte for byte and replace only the files; it starts at sector 2048 and is 262144 sectors long, which is where the numbers in the next command come from.

Start from the `.wic.xz` you downloaded. Extract the first 1 MiB, which holds the partition table, plus the 128 MiB partition into a new image file:

```bash
xz -dc $WORK/tisdk-default-image.wic.xz | head -c $(( (2048+262144)*512 )) > $WORK/sdcard.img
```

The result is a 129 MiB file. The partition table still lists TI's second partition, which now points past the end of the file. Delete it:

```bash
sfdisk --delete $WORK/sdcard.img 2
```

The output ends with:

```output
The partition table has been altered.
Syncing disks.
```

Replace TI's Linux files in the FAT volume with yours using `mtools`. The `@@1048576` suffix tells `mtools` that the volume starts 1 MiB into the file, and `::` is the root of that volume:

```bash
M=$WORK/sdcard.img@@1048576
mdeltree -i $M ::EFI
mdel -i $M ::Image ::uEnv.txt
mcopy -o -i $M $UBOOT_OUT/tiboot3.bin $UBOOT_OUT/tispl.bin $UBOOT_OUT/u-boot.img ::
mcopy -o -i $M $FIT/zephyr-a.itb ::
```

List the volume to check the result:

```bash
mdir -i $M ::
```

The output is similar to:

```output
 Volume in drive : is boot
 Volume Serial Number is 40D2-DF89
Directory for ::/

tiboot3  bin    216538 2026-09-15  16:49
tispl    bin   1467919 2026-09-15  16:49
u-boot   img   1422787 2026-09-15  16:49
zephyr-a itb     60198 2026-09-15  16:49
        4 files           3 167 442 bytes
                        130 766 848 bytes free
```

Four files: the three boot stages you built and the FIT you signed.

## Write the card

Run `lsblk`, insert the micro-SD card in your host, and run `lsblk` again. The disk that appeared is the card. Write the image to the whole card:

```bash
sudo dd if=$WORK/sdcard.img of=/dev/sdX bs=4M conv=fsync status=progress
```

{{% notice Warning %}}
Replace `/dev/sdX` with your card, for example `/dev/sdb`, never a partition such as `/dev/sdb1`. `dd` erases everything on the target, so a wrong device name erases the wrong disk.
{{% /notice %}}

On Windows or macOS, write `sdcard.img` with balenaEtcher.

{{% notice Note %}}
If you prefer not to edit the image on the host, write TI's `.wic.xz` to the card unchanged, with balenaEtcher or with `xz -dc $WORK/tisdk-default-image.wic.xz | sudo dd of=/dev/sdX bs=4M status=progress`, taking the same care with `/dev/sdX`. Then open the first partition on any PC, delete `Image`, `uEnv.txt` and the `EFI` directory, and copy the same four files in.
{{% /notice %}}

## Set the AM62L EVM boot switches

Set **SW3** as shown below, the reduced pincount setting from the [AM62L EVM User's Guide](https://www.ti.com/lit/pdf/SPRUJG8), in which the ROM ignores **SW2** and **SW4**. **ON** is towards the **ON** label on the switch bank.

| Switch | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **SW3** | OFF | ON | OFF | ON |

## Connect the console and power on

Connect the micro-USB port **J7** to your host. It creates four serial ports; the console is usually the first one, `/dev/ttyUSB0`, at 115200 baud. Open it:

```bash
picocom -b 115200 /dev/ttyUSB0
```

If `picocom` reports a permission error, add your user to the `dialout` group with `sudo usermod -aG dialout $USER`, then log out and back in. To leave `picocom` later, press **Ctrl+A**, then **Ctrl+X**.

Move the SD card to the board, then power the board through a USB-C PD supply on **J17** or **J19**. The console starts printing at once. Your dates, version strings and countdown differ. The log up to the countdown is similar to:

```output
NOTICE:  Booting Trusted Firmware
NOTICE:  BL1: v2.14.0(release):12.00.00.06-28-gb54338ab6
NOTICE:  BL1: Built : 09:15:06, Jul  8 2026
NOTICE:  BL1: dram_class: 11
NOTICE:  BL1: dram_size: 0x80000000
NOTICE:  DDR init done
NOTICE:  ENTERING WFI - end of bl1
NOTICE:  BL31: v2.14.0(release):12.00.00.06-28-gb54338ab6
NOTICE:  BL31: Built : 09:15:06, Jul  8 2026
NOTICE:  SYSFW ABI: 4.0 (firmware rev 0x000c '12.1.2--v12.01.02 (Clever Cat)')
ERROR:   Agent 0 Protocol 0x10 Message 0x7: not supported

U-Boot SPL 2026.01-ti-g5fb294342321 (Jul 09 2026 - 22:23:09 +0000)
SPL initial stack usage: 1920 bytes
Trying to boot from MMC2
Authentication passed
Authentication passed
ERROR:   Agent 0 Protocol 0x10 Message 0x7: not supported


U-Boot 2026.01-g5fb294342321 (Sep 11 2026 - 18:13:32 +0200)

SoC:   AM62LX SR1.1 HS-FS
Model: Texas Instruments AM62L3 Evaluation Module
DRAM:  2 GiB
ERROR:   Agent 0 Protocol 0x10 Message 0x7: not supported
Core:  89 devices, 34 uclasses, devicetree: separate
MMC:   mmc@fa10000: 0, mmc@fa00000: 1
Loading Environment from nowhere... OK
In:    serial@2800000
Out:   serial@2800000
Err:   serial@2800000
Net:   eth0: ethernet@8000000port@1, eth1: ethernet@8000000port@2
Hit any key to stop autoboot:  3
```

**Lines to look for:** the `NOTICE:  BL1:` and `BL31:` lines are TF-A, from `tiboot3.bin` and `tispl.bin`; `Authentication passed` is TIFS accepting `u-boot.img`; `SoC:   AM62LX SR1.1 HS-FS` says the SoC is in its development state, which TI calls HS-FS; `MMC:` lists the eMMC as device 0 and the SD card as device 1. The `ERROR:` lines come from TI's firmware and are harmless.

This log comes from a board running TI's prebuilt first two stages, so its `U-Boot SPL` line shows TI's build date instead of yours.

## Watch the trusted image boot

After the three-second countdown, autoboot runs `run a`, the command you [built into U-Boot](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/). Your times and hash differ, and on another board so do `FIT_ADDR` and `ZEPHYR_ADDR`. The output is similar to:

```output
60198 bytes read in 1 ms (57.4 MiB/s)
## Loading kernel (any) from FIT Image at 90000000 ...
   Using 'conf-1' configuration
   Verifying Hash Integrity ... sha256,rsa2048:key-a+ OK
   Trying 'kernel-1' kernel subimage
     Description:  Zephyr RTOS image
     Created:      2026-09-11  16:14:00 UTC
     Type:         Kernel Image
     Compression:  uncompressed
     Data Start:   0x900000e8
     Data Size:    58340 Bytes = 57 KiB
     Architecture: AArch64
     OS:           U-Boot
     Load Address: 0x82000000
     Entry Point:  0x82000000
     Hash algo:    sha256
     Hash value:   1d1d375f14c3354579e9e5310986a69b831bcd1944cd6b35aa8e83632b658166
   Verifying Hash Integrity ... sha256+ OK
   Loading Kernel Image to 82000000
## Starting application at 0x82000000 ...
*** Booting Zephyr OS build 4.4.2 ***
Secondary CPU core 1 (MPID:0x1) is up

################################################
#                                              #
#   Hello from ZEPHYR IMAGE A                  #
#   signed with key-a  (TRUSTED by U-Boot)     #
#                                              #
################################################

board            : am62l_evm/am62l3/a53
arch             : arm64
started by       : U-Boot 'go' after FIT signature verification
this image was verified by U-Boot before it ran.
```

**Lines to look for:** `sha256,rsa2048:key-a+ OK` is `bootm start` verifying the signature with the `key-a` public key in U-Boot, and `sha256+ OK` is the image hash matching; `+` means pass. `Loading Kernel Image to 82000000` is `bootm loados` copying Zephyr to its link address, and `## Starting application at 0x82000000 ...` is `go`, the last line from U-Boot. Everything after it comes from Zephyr: its banner, `Secondary CPU core 1 (MPID:0x1) is up` when it starts the second core, and `Hello from ZEPHYR IMAGE A`.

## If nothing prints

If the terminal stays empty, the ROM did not load `tiboot3.bin`. Work down this list:

1. Try all four serial ports that **J7** creates; the console isn't always the first one.
2. Check **SW3**, or switch to the full pincount setting, which uses all three switch banks: BOOTMODE `0x0E43` in the same guide.
3. Check that the card's first partition is still TI's FAT16 partition, not reformatted.
4. Flash TI's unchanged `.wic.xz` to a card and boot it. If it prints nothing either, the cause is the switches, the port, or the power, not your files.
5. If TI's card boots but yours never shows the SPL banner, copy TI's prebuilt first two stages over yours with `mcopy -o -i $WORK/sdcard.img@@1048576 $PREBUILT/tiboot3.bin $PREBUILT/tispl.bin ::`, then write the card again with the same `dd`. `u-boot.img` still carries the key and the boot command.

On another board the same list applies, with your vendor's first-stage file, card image and console port.

If U-Boot starts Zephyr but the banner is the last line you see, `CONFIG_ARMV8_A_NS` is missing from the [Zephyr build](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/3-build-zephyr/).

## What you've accomplished and what's next

You built the SD card and watched U-Boot verify the FIT signed with `key-a` and start Zephyr on the board. Next, the optional [Test that U-Boot refuses a wrong key and a tampered image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-test-the-checks/) proves the refusals; after it, [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/8-production/) lists what a product needs on top.
