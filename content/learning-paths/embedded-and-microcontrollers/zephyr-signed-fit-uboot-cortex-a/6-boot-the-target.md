---
title: Boot the target
description: Build the boot media for your target, start the board or QEMU, and watch U-Boot verify the signed Zephyr image before it starts it.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What your target boots from

Open a terminal and load the environment for your target: `source $HOME/zephyr-secure-boot/env-am62l.sh`, or `source $HOME/zephyr-secure-boot/env-qemu.sh` for QEMU.

Some boot ROMs look for the first-stage file by name on a FAT partition, as the AM62L's does; others read it from a fixed offset on the card. That is why you start from the vendor's own card image on a board. QEMU has no boot ROM: it takes `u-boot.bin` on the command line, so its disk carries nothing but the FIT. On both, U-Boot's `fatload` then reads `zephyr-a.itb` from the partition in `BOOT_DEV`.

## Build the boot media

{{< tabpane-normal >}}
  {{< tab header="AM62L EVM" >}}
The boot ROM reads `tiboot3.bin` from the card's first FAT partition and is picky about its format: TI's FAT16 partition boots, while a FAT32 one with 512-byte clusters leaves the console empty. Keep TI's partition byte for byte and replace only the files; it starts at sector 2048 and is 262144 sectors long, which is where the numbers in the next command come from.

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

Replace TI's Linux files in the FAT volume with yours using `mtools`. `BOOT_IMG` from your environment file is the image plus the `@@1048576` suffix, which tells `mtools` that the volume starts 1 MiB into the file, and `::` is the root of that volume:

```bash
mdeltree -i $BOOT_IMG ::EFI
mdel -i $BOOT_IMG ::Image ::uEnv.txt
mcopy -o -i $BOOT_IMG $UBOOT_OUT/tiboot3.bin $UBOOT_OUT/tispl.bin $UBOOT_OUT/u-boot.img ::
mcopy -o -i $BOOT_IMG $FIT/zephyr-a.itb ::
mdir -i $BOOT_IMG ::
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
  {{< /tab >}}
  {{< tab header="QEMU" >}}
There is no boot ROM to satisfy and no vendor image to copy, so you build the disk from nothing. Create a 64 MiB file, give it one MBR partition of type `0x0e` (FAT16 with LBA addressing) starting at sector 2048, and format that partition. None of it needs root:

```bash
truncate -s 64M $WORK/disk.img
printf 'label: dos\nstart=2048, size=129024, type=e\n' | sfdisk $WORK/disk.img
mkfs.vfat --offset 2048 -F 16 -n ZEPHYRFIT $WORK/disk.img
```

Copy the FIT in. `BOOT_IMG` from your environment file is the image plus the `@@1048576` suffix, which tells `mtools` that the volume starts 1 MiB into the file, and `::` is the root of that volume:

```bash
mcopy -o -i $BOOT_IMG $FIT/zephyr-a.itb ::
mdir -i $BOOT_IMG ::
```

The output is similar to:

```output
 Volume in drive : is ZEPHYRFIT
 Volume Serial Number is B4EA-EA2A
Directory for ::/

zephyr-a itb     38742 2026-09-17  22:11
        1 file              38 742 bytes
                         65 871 872 bytes free
```

One file: the FIT you signed. `type=e` is what makes U-Boot's DOS partition driver present this volume as `virtio 0:1`, the `BOOT_DEV` in `env-qemu.sh`.
  {{< /tab >}}
{{< /tabpane-normal >}}

## Start the target

{{% notice Warning %}}
The AM62L EVM steps write to a whole disk with `dd`. Replace `/dev/sdX` with your card, for example `/dev/sdb`, never a partition such as `/dev/sdb1`. `dd` erases everything on the target, so a wrong device name erases the wrong disk.
{{% /notice %}}

{{< tabpane-normal >}}
  {{< tab header="AM62L EVM" >}}
Run `lsblk`, insert the micro-SD card in your host, and run `lsblk` again. The disk that appeared is the card. Write the image to the whole card:

```bash
sudo dd if=$WORK/sdcard.img of=/dev/sdX bs=4M conv=fsync status=progress
```

On Windows or macOS, write `sdcard.img` with balenaEtcher. If you prefer not to edit the image on the host, write TI's `.wic.xz` to the card unchanged instead, then open the first partition on any PC, delete `Image`, `uEnv.txt` and the `EFI` directory, and copy the same four files in.

Set **SW3** as shown below, the reduced pincount setting from the [AM62L EVM User's Guide](https://www.ti.com/lit/pdf/SPRUJG8), in which the ROM ignores **SW2** and **SW4**. **ON** is towards the **ON** label on the switch bank.

| Switch | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **SW3** | OFF | ON | OFF | ON |

Connect the micro-USB port **J7** to your host. It creates four serial ports; the console is usually the first one, `/dev/ttyUSB0`, at 115200 baud. Open it:

```bash
picocom -b 115200 /dev/ttyUSB0
```

If `picocom` reports a permission error, add your user to the `dialout` group with `sudo usermod -aG dialout $USER`, then log out and back in. To leave `picocom` later, press **Ctrl+A**, then **Ctrl+X**.

Move the SD card to the board, then power the board through a USB-C PD supply on **J17** or **J19**. The console starts printing at once.
  {{< /tab >}}
  {{< tab header="QEMU" >}}
Start the machine. `-bios` hands QEMU the U-Boot you built, `-nographic` puts the serial console in your terminal, and the `-drive` and `-device` pair attaches `disk.img` as the virtio block device U-Boot sees as `virtio 0:1`:

```bash
qemu-system-aarch64 -machine virt,gic-version=3 -cpu cortex-a53 -m 1G -nographic -no-reboot \
    -bios $UBOOT_OUT/u-boot.bin \
    -drive if=none,file=$WORK/disk.img,format=raw,id=hd0 \
    -device virtio-blk-device,drive=hd0
```

The machine must match the one you dumped the device tree from when you [built U-Boot](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/): same `-machine`, same `-cpu`, same `-m`. U-Boot starts printing at once. To leave QEMU, press **Ctrl+A**, then **X**.
  {{< /tab >}}
{{< /tabpane-normal >}}

On the AM62L EVM the log up to the countdown is similar to the one below. Your dates, version strings and countdown differ.

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

In QEMU there is no TF-A and no SPL, so the log starts at U-Boot's own banner and is about ten lines long. Three of them are worth knowing: `Bloblist at 0 not found (err=-2)` and `Warning: Unexpected devicetree source (not from a prior stage)` are QEMU telling you that nothing ran before U-Boot, which is exactly the case, and `Loading Environment from nowhere... OK` is the environment you compiled in.

## Watch the trusted image boot

After the three-second countdown, autoboot runs `run a`, the command you [built into U-Boot](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/). Your times and hash differ, and on another target so do `FIT_ADDR` and `ZEPHYR_ADDR`. The output is similar to:

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

In QEMU the same block reads `FIT Image at 48000000`, `Data Size: 37040 Bytes`, `Loading Kernel Image to 40000000` and `board : qemu_cortex_a53/qemu_cortex_a53`, and there is no `Secondary CPU core 1` line, because that board configuration starts one core.

## If nothing prints

{{< tabpane-normal >}}
  {{< tab header="AM62L EVM" >}}
If the terminal stays empty, the ROM did not load `tiboot3.bin`. Work down this list:

1. Try all four serial ports that **J7** creates; the console isn't always the first one.
2. Check **SW3**, or switch to the full pincount setting, which uses all three switch banks: BOOTMODE `0x0E43` in the same guide.
3. Check that the card's first partition is still TI's FAT16 partition, not reformatted.
4. Flash TI's unchanged `.wic.xz` to a card and boot it. If it prints nothing either, the cause is the switches, the port, or the power, not your files.
5. If TI's card boots but yours never shows the SPL banner, copy TI's prebuilt first two stages over yours with `mcopy -o -i $BOOT_IMG $PREBUILT/tiboot3.bin $PREBUILT/tispl.bin ::`, then write the card again with the same `dd`. `u-boot.img` still carries the key and the boot command.

On another board the same list applies, with your vendor's first-stage file, card image and console port.
  {{< /tab >}}
  {{< tab header="QEMU" >}}
QEMU always prints something, so read what it says:

1. Nothing at all, or a hang after the banner: the control device tree does not match the machine. Rebuild it from a fresh `dumpdtb` with the same `-machine`, `-cpu` and `-m` you start QEMU with.
2. `Failed to load 'zephyr-a.itb'`: U-Boot found the volume but not the file. List it on the host with `mdir -i $BOOT_IMG ::`.
3. `** Bad device specification virtio 0 **`: the partition type is not `0x0e`. Check with `sfdisk -l $WORK/disk.img` and build the image again.
4. `Unknown command 'dcache'`: `CONFIG_CMD_CACHE` did not make it into `.config`; add it and build U-Boot again.
  {{< /tab >}}
{{< /tabpane-normal >}}

If U-Boot starts Zephyr but the banner is the last line you see, `CONFIG_ARMV8_A_NS` is missing from the [Zephyr build](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/3-build-zephyr/).

## What you've accomplished and what's next

You built the boot media and watched U-Boot verify the FIT signed with `key-a` and start Zephyr on your target. Next, the optional [Test that U-Boot refuses a wrong key and a tampered image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-test-the-checks/) proves the refusals; after it, [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/8-production/) lists what a product needs on top.
