---
title: Boot your QEMU or TI AM62L EVM target
description: Prepare boot media for QEMU or the TI AM62L EVM and confirm that U-Boot verifies the signed Zephyr FIT before starting the application.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What your target boots from

Open a terminal and load your target's environment file:

- QEMU: `source $HOME/zephyr-secure-boot/env-qemu.sh`
- AM62L evaluation module (EVM): `source $HOME/zephyr-secure-boot/env-am62l.sh`

The AM62L boot ROM reads the first-stage file from a File Allocation Table (FAT) partition on the SD card. Start with TI's card image to preserve the expected layout. QEMU loads `u-boot.bin` from the command line, so its disk image needs only the signed Flattened Image Tree (FIT).

On either target, U-Boot's `fatload` reads `zephyr-a.itb` from the partition selected by `BOOT_DEV`.

## Build the boot media

Follow the instructions for your target to build the boot media.

{{< tabpane-normal >}}
  {{< tab header="QEMU" >}}
Create a 64 MiB disk image with one FAT16 partition starting at sector 2048. Use a master boot record (MBR) partition table and partition type `0x0e`, which specifies FAT16 with logical block addressing (LBA). These commands don't need root privileges:

```bash
truncate -s 64M $WORK/disk.img
printf 'label: dos\nstart=2048, size=129024, type=e\n' | sfdisk $WORK/disk.img
mkfs.vfat --offset 2048 -F 16 -n ZEPHYRFIT $WORK/disk.img
```

Copy the signed FIT into the partition and list its contents. `BOOT_IMG` includes `@@1048576`, telling `mtools` that the volume starts 1 MiB into the image. `::` identifies the volume's root directory:

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

Confirm that the volume contains `zephyr-a.itb`. The partition is accessed as `virtio 0:1`, matching `BOOT_DEV` in `env-qemu.sh`.
  {{< /tab >}}
  {{< tab header="AM62L EVM" >}}
The boot ROM reads `tiboot3.bin` from the card's first FAT partition. Preserve TI's FAT16 partition layout and replace its files. The supplied partition starts at sector 2048 and spans 262144 sectors. These values determine the extraction size in the command.

Start from the `.wic.xz` that you downloaded. Extract the first 1 MiB, which holds the partition table, plus the 128 MiB partition into a new image file:

```bash
xz -dc $WORK/tisdk-default-image.wic.xz | head -c $(( (2048+262144)*512 )) > $WORK/sdcard.img
```

The result is a 129 MiB image. Its partition table still lists TI's second partition, which points past the end of the extracted image. Remove that partition-table entry:

```bash
sfdisk --delete $WORK/sdcard.img 2
```

The output ends with:

```output
The partition table has been altered.
Syncing disks.
```

Use `mtools` to remove TI's Linux files and copy your boot files and signed FIT into the FAT volume. `BOOT_IMG` includes `@@1048576`, selecting the volume 1 MiB into the image. `::` identifies its root directory:

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

Confirm that the volume contains the three boot files and `zephyr-a.itb`.
  {{< /tab >}}
{{< /tabpane-normal >}}

## Start the target

Follow the instructions for your target to start the target.

{{% notice Warning %}}
The AM62L EVM steps write to a whole disk with `dd`. Replace `/dev/sdX` with your card, for example `/dev/sdb`, never a partition such as `/dev/sdb1`. `dd` erases everything on the target, so a wrong device name erases the wrong disk.
{{% /notice %}}

{{< tabpane-normal >}}
  {{< tab header="QEMU" >}}
Start QEMU with the U-Boot binary and disk image you prepared. `-bios` selects the binary, and `-nographic` displays the serial console in your terminal. The `-drive` and `-device` options attach `disk.img` as the virtio device containing `virtio 0:1`:

```bash
qemu-system-aarch64 -machine virt,gic-version=3 -cpu cortex-a53 -m 1G -nographic -no-reboot \
    -bios $UBOOT_OUT/u-boot.bin \
    -drive if=none,file=$WORK/disk.img,format=raw,id=hd0 \
    -device virtio-blk-device,drive=hd0
```

Use the same `-machine`, `-cpu`, and `-m` settings as the device-tree export used to [build U-Boot](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/). U-Boot should begin printing in the terminal. To exit QEMU, press **Ctrl+A**, then **X**.
  {{< /tab >}}
  {{< tab header="AM62L EVM" >}}
Run `lsblk` before and after inserting the micro-SD card. Identify the newly listed disk and confirm its size matches the card. Replace `/dev/sdX` with that disk's device name and write the image to the whole card:

```bash
sudo dd if=$WORK/sdcard.img of=/dev/sdX bs=4M conv=fsync status=progress
```

If you transfer the prepared image to Windows or macOS, you can write `sdcard.img` with balenaEtcher. Alternatively, write TI's unchanged `.wic.xz` image to the card. Open its first partition, remove `Image`, `uEnv.txt`, and the `EFI` directory, then copy in the three boot files and `zephyr-a.itb`.

Set **SW3** using the table. This is the reduced pin-count setting from the [AM62L EVM User's Guide](https://www.ti.com/lit/pdf/SPRUJG8), where the ROM ignores **SW2** and **SW4**. The **ON** position is toward the **ON** label on the switch bank.

| Switch | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **SW3** | OFF | ON | OFF | ON |

Connect the micro-USB port **J7** to your host. It creates four serial ports. The console is usually `/dev/ttyUSB0` and uses 115200 baud. Open the console:

```bash
picocom -b 115200 /dev/ttyUSB0
```

If `picocom` reports a permission error, add your user to the `dialout` group with `sudo usermod -aG dialout $USER`, then log out and back in. To leave `picocom` later, press **Ctrl+A**, then **Ctrl+X**.

Move the SD card to the board, then connect a USB-C Power Delivery (PD) supply to **J17** or **J19**. Boot messages should appear in the console.
  {{< /tab >}}
{{< /tabpane-normal >}}

In QEMU, the log starts with U-Boot because no TF-A or Secondary Program Loader (SPL) stage runs first. The messages `Bloblist at 0 not found (err=-2)` and `Warning: Unexpected devicetree source (not from a prior stage)` are consistent with this setup. `Loading Environment from nowhere... OK` indicates that U-Boot is using its built-in environment.

The AM62L EVM also prints messages from its early firmware stages. Its log up to the autoboot countdown is similar to the following example. Your dates, version strings, and countdown will differ:

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

Use the following messages to identify the boot stages and selected devices:

- `NOTICE:  BL1:` and `BL31:` identify TF-A running from `tiboot3.bin` and `tispl.bin`.
- `Authentication passed` reports successful authentication by TI's security firmware.
- `SoC:   AM62LX SR1.1 HS-FS` identifies the SoC's development state.
- `MMC:` lists the eMMC as device zero and the SD card as device one.

The `Agent 0 Protocol 0x10 Message 0x7: not supported` errors appear in this successful boot log. They don't prevent Zephyr from starting.

This log comes from a board running TI's prebuilt first two stages, so its `U-Boot SPL` line shows TI's build date instead of yours.

## Watch the trusted image boot

After the three-second countdown, autoboot runs `run a`, the trusted-image command built into U-Boot. The following example output shows the AM62L EVM. Your timings and hash values will differ. QEMU uses different load addresses and image sizes. The output is similar to:

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

Confirm verification and startup using the following messages:

- `sha256,rsa2048:key-a+ OK` confirms that the signature verifies with U-Boot's embedded public key.
- `sha256+ OK` confirms that the payload hash matches.
- `Loading Kernel Image to 82000000` shows `bootm loados` copying Zephyr to its link address.
- `## Starting application at 0x82000000 ...` shows `go` handing control to Zephyr.

Zephyr then prints its boot banner and `Hello from ZEPHYR IMAGE A`. On the AM62L EVM, `Secondary CPU core 1 (MPID:0x1) is up` also reports startup of the second core.

For QEMU, expect `FIT Image at 48000000`, `Data Size: 37040 Bytes`, `Loading Kernel Image to 40000000`, and `board : qemu_cortex_a53/qemu_cortex_a53`. Its board configuration starts one core, so there's no secondary-core startup message.

## Troubleshoot boot and console output

Consider the following guidance to troubleshoot issues with your target.

{{< tabpane-normal >}}
  {{< tab header="QEMU" >}}
Check the symptom and try the corresponding step:

1. Nothing prints, or startup hangs after the banner: Check that the control device tree matches the machine. Rebuild it from a fresh `dumpdtb` with the same `-machine`, `-cpu`, and `-m` used to start QEMU.
2. `Failed to load 'zephyr-a.itb'`: U-Boot found the volume but not the file. List it on the host with `mdir -i $BOOT_IMG ::`.
3. `** Bad device specification virtio 0 **`: Check the partition type with `sfdisk -l $WORK/disk.img`. If it isn't `0x0e`, rebuild the disk image with the specified type.
4. `Unknown command 'dcache'`: `CONFIG_CMD_CACHE` didn't make it into `.config`. Add it and build U-Boot again.
  {{< /tab >}}
  {{< tab header="AM62L EVM" >}}
If the terminal stays empty, check the console connection and whether the ROM loads `tiboot3.bin`:

1. Try all four serial ports that **J7** creates. The console isn't always the first one.
2. Check **SW3**, or switch to the full pincount setting, which uses all three switch banks. BOOTMODE `0x0E43` in the same guide.
3. Check that the card's first partition is still TI's FAT16 partition, not reformatted.
4. Flash TI's unchanged `.wic.xz` to a card and boot it. If that also produces no output, check the boot switches, serial port, and power supply before investigating your custom boot files.
5. If TI's card boots but yours never shows the SPL banner, copy TI's prebuilt first two stages over yours with `mcopy -o -i $BOOT_IMG $PREBUILT/tiboot3.bin $PREBUILT/tispl.bin ::`. Then, write the card again with the same `dd`. `u-boot.img` still carries the key and the boot command.

  {{< /tab >}}
{{< /tabpane-normal >}}

If Zephyr prints its boot banner but no application output, check that the [Zephyr build configuration](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/3-build-zephyr/) includes `CONFIG_ARMV8_A_NS=y`.

## What you've accomplished and what's next

You've prepared the boot media and watched U-Boot verify the FIT signed with `key-a` before starting Zephyr. 

Next, you can run the optional [wrong-key and tampered-image tests](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-test-the-checks/) to confirm that verification failures prevent startup. You can also skip to review [the trust boundary and the additional work needed for production](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/8-production/).
