---
title: Prepare the SD card and boot the board
description: Build a bootable SD card image with mtools, set the AM62L EVM boot switches, and watch U-Boot verify the signed Zephyr image and start it on the board.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build the SD card image from TI's boot partition

Open a terminal and load the environment: `source $HOME/zephyr-secure-boot/env.sh`.

The boot ROM looks for `tiboot3.bin` by name on the first FAT partition of the SD card, and it is picky about that partition: a FAT32 volume with 512-byte clusters loads nothing, and the console stays empty.

TI's own SD card image boots. Its first partition starts at sector 2048, is 262144 sectors (128 MiB) long, is marked bootable with partition type `0x0c`, and is formatted FAT16 with four sectors per cluster. Keep that partition byte for byte and replace only the files in it.

Start from the `.wic.xz` you downloaded when you [set up the tools](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/2-set-up-tools/). Extract the first 1 MiB, which holds the partition table, plus the 128 MiB partition into a new image file:

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

`uEnv.txt` is TI's Linux boot environment; your U-Boot never reads it, but delete it so nothing on the card describes a Linux boot.

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

{{% notice Note %}}
If you prefer not to edit the image on the host, flash TI's `.wic.xz` to the card unchanged. balenaEtcher reads `.wic.xz` directly, and on Linux `xz -dc $WORK/tisdk-default-image.wic.xz | sudo dd of=/dev/sdX bs=4M status=progress` does the same. Then open the first partition on any PC, delete `Image`, `uEnv.txt` and the `EFI` directory, and copy the same four files in.
{{% /notice %}}

## Write the card

Run `lsblk`, insert the micro-SD card in your host, and run `lsblk` again. The disk that appeared is the card. Write the image to the whole card:

```bash
sudo dd if=$WORK/sdcard.img of=/dev/sdX bs=4M conv=fsync status=progress
```

{{% notice Warning %}}
Replace `/dev/sdX` with your card, for example `/dev/sdb`, never a partition such as `/dev/sdb1`. `dd` erases everything on the target, so a wrong device name erases the wrong disk.
{{% /notice %}}

On Windows or macOS, write `sdcard.img` with balenaEtcher.

## Set the boot switches

The boot switches tell the ROM where to look for `tiboot3.bin`. On the AM62L EVM, **ON** means HIGH, with the knob towards the **ON** label on the switch bank.

The [AM62L EVM User's Guide](https://www.ti.com/lit/pdf/SPRUJG8) (SPRUJG8B) gives two ways to select the SD card. The full pincount setting uses all 16 BOOTMODE bits across three switch banks; the reduced pincount setting uses only the four switches of **SW3**. Start with the reduced setting.

The full pincount value is BOOTMODE `0x0E43`: SD card in filesystem mode as the primary boot device, UART as backup, 25 MHz reference clock:

| Bank | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| **SW4** (BOOTMODE 0-7) | ON | ON | OFF | OFF | OFF | OFF | ON | OFF |
| **SW2** (BOOTMODE 8-11) | OFF | ON | ON | ON | | | | |
| **SW3** (BOOTMODE 12-15) | OFF | OFF | OFF | OFF | | | | |

The reduced pincount setting uses only **SW3**; the ROM ignores **SW2** and **SW4**:

| Bank | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **SW3** | OFF | ON | OFF | ON |

## Connect the console and power on

Connect the micro-USB port **J7** to your host. The FTDI FT4232HL behind it creates four serial ports: SoC UART0, SoC UART1, WKUP UART0 and SoC UART4. The console is SoC UART0, at 115200 baud, 8 data bits, no parity, one stop bit, usually `/dev/ttyUSB0` on Linux. Open it:

```bash
picocom -b 115200 /dev/ttyUSB0
```

If `picocom` reports a permission error, add your user to the `dialout` group with `sudo usermod -aG dialout $USER`, then log out and back in. To leave `picocom` later, press `Ctrl` and `A`, then `Ctrl` and `X`.

Move the SD card to the board, then power the board through a USB-C PD supply on **J17** or **J19**. The console starts printing at once. Early in the log, the SPL shows the device type:

```output
SoC:   AM62LX SR1.0 HS-FS
```

`HS-FS` means no customer key is fused in this device yet; [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/8-production/) explains what that leaves unverified. The check you watch next, U-Boot verifying Zephyr, doesn't depend on it.

## Watch the trusted image boot

U-Boot counts down for three seconds and then autoboot runs `bootcmd`, which is `run a`, the command you [built into U-Boot](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/). It loads `zephyr-a.itb`, verifies it, copies Zephyr to `0x82000000` and jumps there.

Your `Created` time, `Hash value` and read time differ; the lines that matter are the same. The output is similar to:

```output
60198 bytes read in 7 ms (8.2 MiB/s)
## Loading kernel (any) from FIT Image at 90000000 ...
   Using 'conf-1' configuration
   Verifying Hash Integrity ... sha256,rsa2048:key-a+ OK
   Trying 'kernel-1' kernel subimage
     Description:  Zephyr RTOS image
     Created:      2026-09-11  14:40:50 UTC
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

**Lines to look for:** `sha256,rsa2048:key-a+ OK`, `sha256+ OK` and `Loading Kernel Image to 82000000` are the verification; `## Starting application at 0x82000000 ...` is the jump; `Hello from ZEPHYR IMAGE A` is the verified program running.

Three lines carry the proof. `sha256,rsa2048:key-a+ OK` is `bootm start` verifying the RSA signature of `conf-1` with the `key-a` public key compiled into U-Boot. `sha256+ OK` is the same step checking that the image bytes match the signed hash. `Loading Kernel Image to 82000000` is `bootm loados` copying the verified payload to Zephyr's link address. The `+` after a key name or hash algorithm is U-Boot's shorthand for a pass. A failed signature check prints `-` instead, and [Test that U-Boot refuses a wrong key and a tampered image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-test-the-checks/) shows one.

`go`, not `bootm`, prints `## Starting application at 0x82000000 ...`. It is the last line from U-Boot. The program that U-Boot verified a moment earlier prints everything after it, starting with the Zephyr banner.

## If nothing prints

If the terminal stays empty, the ROM did not load `tiboot3.bin`. Work down this list:

1. Open all four serial ports that **J7** creates; SoC UART0 isn't always the first one.
2. Check the boot switches against the tables, or try the other setting.
3. Check the card layout against TI's FAT16 partition.
4. Flash TI's unchanged `.wic.xz` to a card and boot it. If it prints nothing either, the cause is the switches, the port, or the power, not your files.
5. If TI's card boots but yours never shows the SPL banner, copy TI's prebuilt first two stages over yours and write the card again: `mcopy -o -i $M $PREBUILT/tiboot3.bin $PREBUILT/tispl.bin ::`. `u-boot.img` still carries the key and the boot command.

If U-Boot starts Zephyr but the banner is the last line you see, `CONFIG_ARMV8_A_NS` is missing from the [Zephyr build](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/3-build-zephyr/).

## What you've accomplished and what's next

You built a bootable SD card from TI's boot partition and watched U-Boot on real silicon verify the FIT signed with `key-a` and start Zephyr. Next, the optional [Test that U-Boot refuses a wrong key and a tampered image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-test-the-checks/) proves both refusals on the board. After it, [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/8-production/) lists what a production device needs on top: a fused key, a locked console, and no other boot path.
