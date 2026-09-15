---
title: Prepare the SD card and boot the board
description: Build a bootable SD card image with mtools, set the AM62L EVM boot switches, and watch U-Boot start the signed Zephyr image and refuse the wrong-key and tampered ones.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build the SD card image from TI's boot partition

Open a terminal and load the environment: `source $HOME/zephyr-secure-boot/env.sh`.

The boot ROM looks for `tiboot3.bin` by name on the first FAT partition of the SD card. It is picky about that partition. Give it a FAT32 volume with 512-byte clusters, for example, and it loads nothing: the console stays empty, with no SPL banner at all.

TI's own SD card image boots. Its first partition starts at sector 2048 and is 262144 sectors long, which is 128 MiB. It is marked bootable, has partition type `0x0c` (the partition-table code for a FAT volume with logical block addressing, LBA), and is formatted FAT16 with four sectors per cluster. So keep that partition byte for byte and replace only the files in it.

Start from the `.wic.xz` you downloaded when you [set up the tools](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/2-set-up-tools/). Extract only the first 1 MiB, which holds the partition table, plus the 128 MiB partition into a new image file:

```bash
xz -dc $WORK/tisdk-default-image.wic.xz | head -c $(( (2048+262144)*512 )) > $WORK/sdcard.img
```

The result is a 129 MiB file. `head -c` stops reading after that many bytes, so you never extract TI's Linux root filesystem, which is the second partition. The partition table still lists that second partition, and it now points past the end of the file. Delete it:

```bash
sfdisk --delete $WORK/sdcard.img 2
```

The output ends with:

```output
The partition table has been altered.
Syncing disks.
```

`sfdisk` edits partition tables in plain files as well as on devices, so you don't need root and you don't need to attach the file as a disk first.

The FAT volume still holds TI's Linux files. Replace them with yours using `mtools`, which reads and writes FAT volumes inside a file. The `@@1048576` suffix tells `mtools` that the volume starts 1 MiB into the file, which is sector 2048. In `mtools` commands, `::` is the root of that volume, so `::EFI` is the `EFI` directory on the card:

```bash
M=$WORK/sdcard.img@@1048576
mdeltree -i $M ::EFI
mdel -i $M ::Image ::uEnv.txt
mcopy -o -i $M $UBOOT_OUT/tiboot3.bin $UBOOT_OUT/tispl.bin $UBOOT_OUT/u-boot.img ::
mcopy -o -i $M $FIT/zephyr-a.itb $FIT/zephyr-b.itb $FIT/zephyr-tampered.itb ::
```

`-i` names the image. `mdeltree` removes a directory and everything in it, `mdel` removes single files, and `mcopy -o` copies files in and overwrites any that already exist.

`uEnv.txt` deserves a word. It is a text file of environment settings that TI's default boot command imports, and it points at Linux. Your build replaced that command with `run a`, so your U-Boot never reads the file. Delete it anyway: a card that still describes a Linux boot only invites doubt about what ran.

List the volume to check the result:

```bash
mdir -i $M ::
```

The output is similar to:

```output
 Volume in drive : is boot
 Volume Serial Number is 40D2-DF89
Directory for ::/

tiboot3  bin    216538 2026-09-11  18:14
tispl    bin   1467919 2026-09-11  18:14
u-boot   img   1422787 2026-09-11  18:14
zephyr-a itb     60198 2026-09-11  18:14
zephyr-b itb     60198 2026-09-11  18:14
ZEPHYR~1 ITB     60198 2026-09-11  18:14  zephyr-tampered.itb
        6 files           3 287 838 bytes
                        130 643 968 bytes free
```

`mdir` shows the long name `zephyr-tampered.itb` at the end of its line and the FAT short name `ZEPHYR~1.ITB` in front; U-Boot's `fatload` finds it by the long name. Six files: the three boot stages you built and the three FITs you signed. Nothing else goes on the card; the boot commands are compiled into `u-boot.img`.

{{% notice Note %}}
If you prefer not to edit the image on the host, flash TI's `.wic.xz` to the card unchanged. balenaEtcher reads `.wic.xz` directly, and on Linux `xz -dc $WORK/tisdk-default-image.wic.xz | sudo dd of=/dev/sdX bs=4M status=progress` does the same. Then open the first partition on any PC, delete `Image`, `uEnv.txt` and the `EFI` directory, and copy the same six files in.
{{% /notice %}}

## Write the card

Run `lsblk`, insert the micro-SD card in your host, and run `lsblk` again. The disk that appeared is the card. Then write the image to the whole card:

```bash
sudo dd if=$WORK/sdcard.img of=/dev/sdX bs=4M conv=fsync status=progress
```

{{% notice Warning %}}
Replace `/dev/sdX` with your card, for example `/dev/sdb`, never a partition such as `/dev/sdb1`. `dd` erases everything on the target, so a wrong device name erases the wrong disk.
{{% /notice %}}

`conv=fsync` makes `dd` wait until the data is on the card before it returns. The image is 129 MiB, so the rest of the card stays unused; the ROM only reads the first partition.

On Windows or macOS, write `sdcard.img` with balenaEtcher.

## Set the boot switches

The boot switches tell the ROM where to look for `tiboot3.bin`. On the AM62L EVM, **ON** means HIGH, with the knob towards the **ON** label on the switch bank.

The EVM has two ways to set the boot mode, both from the [AM62L EVM User's Guide](https://www.ti.com/lit/pdf/SPRUJG8) (SPRUJG8B). The full pincount setting uses all 16 BOOTMODE bits across three switch banks. The reduced pincount setting uses only the four switches of **SW3**. Either one selects the SD card. Start with the reduced setting: four switches leave fewer ways to get it wrong.

The full pincount value is BOOTMODE `0x0E43`: SD card in filesystem mode as the primary boot device, UART as backup, 25 MHz reference clock. Set the three banks like this:

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

Connect the micro-USB port **J7** to your host. The USB-to-serial chip behind it (an FTDI FT4232HL) creates four serial ports: SoC UART0, SoC UART1, WKUP UART0 and SoC UART4. The console is SoC UART0, at 115200 baud, 8 data bits, no parity, one stop bit. On Linux it is usually the first port, `/dev/ttyUSB0`. Open it:

```bash
picocom -b 115200 /dev/ttyUSB0
```

If `picocom` reports a permission error, add your user to the `dialout` group with `sudo usermod -aG dialout $USER`, then log out and back in. To leave `picocom` later, press the `Ctrl` key and `A`, then `Ctrl` and `X`.

Move the SD card from the host to the board, then power the board through a USB-C PD supply on **J17** or **J19**. The console starts printing at once. Early in the log, the line the SPL prints when it starts shows the device type:

```output
SoC:   AM62LX SR1.0 HS-FS
```

`HS-FS` means no customer key is fused in this device yet; [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-production/) explains what that leaves unverified. The check you watch next, U-Boot verifying Zephyr, doesn't depend on it.

## Watch the trusted image boot

U-Boot counts down for three seconds and then runs `bootcmd` on its own. That automatic run is called autoboot, and `bootcmd` is `run a`, the command you [built into U-Boot](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/). It loads `zephyr-a.itb`, verifies it, copies Zephyr to `0x82000000` and jumps there.

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

Three lines carry the proof. `sha256,rsa2048:key-a+ OK` is `bootm start` verifying the RSA signature of `conf-1` with the `key-a` public key compiled into U-Boot. `sha256+ OK` is the same step checking that the image bytes match the signed hash. `Loading Kernel Image to 82000000` is `bootm loados` copying the verified payload to Zephyr's link address. The `+` after a key name or hash algorithm is U-Boot's shorthand for a pass. A failed signature check prints `-` instead, and you'll see one in the next run.

`go`, not `bootm`, prints `## Starting application at 0x82000000 ...`. It is the last line from U-Boot. The program that U-Boot verified a moment earlier prints everything after it, starting with the Zephyr banner.

## Refuse the wrong key

Zephyr is now running and U-Boot is gone, so power the board off and on. This time press a key during the countdown to stop autoboot. At the prompt, run the wrong-key test:

```console
=> run b
```

The expected output is:

```output
...
   Verifying Hash Integrity ... sha256,rsa2048:key-b-  error!
Verification failed for '<NULL>' hash node in 'conf-1' config node
Failed to verify required signature 'key-key-a'
Bad Data Hash
ERROR -2: can't get kernel image!
*** REFUSED: Zephyr was NOT started ***
```

U-Boot reports two separate failures, the same two that `fit_check_sign` reports on the host. The first line says it found a signature naming `key-b` and has no such key; U-Boot doesn't have the public half of `key-b`. The `Failed to verify required signature 'key-key-a'` line is the `required = "conf"` rule you [built into U-Boot](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/). It says every configuration must carry a valid signature by `key-a`, and this one doesn't. An image with no signature node at all fails that second check in the same way.

Because `bootm start` returns an error, the `&&` chain stops there. `bootm loados` and `go` never run, and the `echo` after the `;` prints the `REFUSED` line. You are back at the U-Boot prompt; image B never ran.

## Refuse the tampered image

You are still at the prompt. Run the tampered test:

```console
=> run t
```

The expected output is:

```output
...
   Verifying Hash Integrity ... sha256,rsa2048:key-a+ OK
   Trying 'kernel-1' kernel subimage
     ...
   Verifying Hash Integrity ... sha256 error!
Bad hash value for 'hash-1' hash node in 'kernel-1' image node
Bad Data Hash
ERROR -2: can't get kernel image!
*** REFUSED: Zephyr was NOT started ***
```

This time the signature check passes and the hash check fails. That surprises people at first, and it is exactly what the FIT diagram in [Understand where Zephyr sits in the Cortex-A boot chain](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/1-boot-chain/) shows. `mkimage` signed the configuration node and the `hash-1` node of the image, and neither has changed. The byte you flipped when you [signed the images](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/4-sign-zephyr/) is in the payload, so the payload no longer matches that signed hash. The signature makes the hash trustworthy, and the hash catches the change. U-Boot stops before `bootm loados` again.

To boot the trusted image again, type `run a` at the prompt.

## If nothing prints

If the terminal stays empty, the ROM did not load `tiboot3.bin`. Work down this list, because each step removes one suspect:

1. Open all four serial ports that **J7** creates. Windows doesn't always number SoC UART0 first, and on Linux it isn't always `/dev/ttyUSB0`.
2. Check the boot switches against the tables, or try the other setting.
3. Check the card layout. A FAT32 boot partition with 512-byte clusters gives exactly this symptom; the FAT16 partition from TI's image is the known-good template.
4. Flash TI's unchanged `.wic.xz` to a card and boot it. That image is TI's own and boots as shipped. If it prints nothing either, the cause is the switches, the port, or the power, not your files.
5. If TI's own card boots but yours never shows the SPL banner, copy TI's prebuilt first two stages over yours and write the card again: `mcopy -o -i $M $PREBUILT/tiboot3.bin $PREBUILT/tispl.bin ::`. `u-boot.img` carries the key and the boot command, so the check you are testing doesn't change.

If U-Boot starts Zephyr but the banner is the last line you see, `CONFIG_ARMV8_A_NS` is missing from the [Zephyr build](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/3-build-zephyr/).

## What you've accomplished and what's next

You built a bootable SD card from TI's own boot partition and set the switches. Then you watched U-Boot on real silicon accept the FIT signed with `key-a`, refuse the one signed with `key-b`, and refuse the one changed after signing. U-Boot now enforces the U-Boot to Zephyr link of the boot chain, from an unmodified source tree.

Next, [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-production/) covers what this proves and what it doesn't, and lists what a production device needs on top of it: a fused key, a locked console, and no other boot path.
