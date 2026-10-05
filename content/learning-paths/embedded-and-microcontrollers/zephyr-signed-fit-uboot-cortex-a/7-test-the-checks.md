---
title: Test that U-Boot refuses a wrong key and a tampered image
description: "Optional: sign a second Zephyr image with a key U-Boot doesn't have, tamper with a copy of the trusted FIT, check both with fit_check_sign on the host, then watch U-Boot refuse both on your target."
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prove the refusal, not only the acceptance

This page makes two images U-Boot must refuse, one signed with the wrong key and one changed after signing, checks them on the host, and watches U-Boot refuse each one on your target's console.

This page is optional, and the `b` and `t` commands in your U-Boot are already waiting for its two files.

Open a terminal and load the environment for your target: `source $HOME/zephyr-secure-boot/env-qemu.sh`, or `source $HOME/zephyr-secure-boot/env-am62l.sh` for the AM62L EVM.

## Build a second Zephyr image

The wrong-key image is a different program on purpose: if U-Boot ever runs it, the console says so in capital letters.

In Workbench for Zephyr, select **Add Application** again. Use the same workspace, toolchain, board and sample as when you [built the trusted image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/3-build-zephyr/), and enter `hello_b` as the **Project Name**. Give it the same `prj.conf` and the same `src/main.c` as `hello`, with the two banner lines changed:

```c
	printk("#   Hello from ZEPHYR IMAGE B                  #\n");
	printk("#   signed with key-b  (NOT trusted by U-Boot) #\n");
```

The replacement text is the same length as the original, so the box stays aligned. Build `hello_b` the same way, with a right-click on it in the **Applications** view and **Build**. The result is `$WORK/zephyrproject/applications/hello_b/build/primary/zephyr/zephyr.bin`, the same size as the first image.

## Sign the second image with a key U-Boot doesn't have

`key-b` is the second key pair you created when you [signed the trusted image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/4-sign-zephyr/). Copy the FIT source with `sed`, swapping `key-a` for `key-b` and `hello` for `hello_b`, then sign it:

```bash
sed 's/key-a/key-b/g; s#/hello/#/hello_b/#' $FIT/zephyr-a.its > $FIT/zephyr-b.its
$UBOOT_OUT/tools/mkimage -f $FIT/zephyr-b.its -k $KEYS $FIT/zephyr-b.itb
```

The output is similar to:

```output
FIT description: Zephyr RTOS, signed with key-b
Created:         Fri Sep 11 19:14:00 2026
 Image 0 (kernel-1)
  Description:  Zephyr RTOS image
  Created:      Fri Sep 11 19:14:00 2026
  Type:         Kernel Image
  Compression:  uncompressed
  Data Size:    58340 Bytes = 56.97 KiB = 0.06 MiB
  Architecture: AArch64
  OS:           U-Boot
  Load Address: 0x82000000
  Entry Point:  0x82000000
  Hash algo:    sha256
  Hash value:   42bf9a7ae3d4fe62f6acc09a1ca7abbd803d26c4b12f0dff717acce06e2b6a9b
 Default Configuration: 'conf-1'
 Configuration 0 (conf-1)
  Description:  Zephyr on Cortex-A
  Kernel:       kernel-1
  Sign algo:    sha256,rsa2048:key-b
  Sign value:   6137633e965eee69ee2cc27b1a904330cf056e1b9ec2371abaf26865763117ed...
  Timestamp:    Fri Sep 11 19:14:00 2026
Signature written to '/home/user/zephyr-secure-boot/fit/zephyr-b.itb', node '/configurations/conf-1/signature-1'
```

**Lines to look for:** `Sign algo:    sha256,rsa2048:key-b`, and a `Hash value` that differs from image A's, because `hello_b` is a different binary. This image proves that a valid signature isn't enough: U-Boot must refuse a key it doesn't have.

## Make a tampered copy of the trusted image

Copy the trusted `.itb` and overwrite one byte inside the payload:

```bash
cp $FIT/zephyr-a.itb $FIT/zephyr-tampered.itb
printf '\xff' | dd of=$FIT/zephyr-tampered.itb bs=1 seek=32768 conv=notrunc 2>/dev/null
```

The payload starts at the `Data Start` offset you saw when U-Boot loaded the FIT, a couple of hundred bytes into the file, and is tens of kilobytes long, so offset 32768 (`0x8000`) lands inside Zephyr's code, not in the FIT's own structure.

Check that the copy now differs from the original:

```bash
cmp $FIT/zephyr-a.itb $FIT/zephyr-tampered.itb
```

The output is similar to:

```output
/home/user/zephyr-secure-boot/fit/zephyr-a.itb /home/user/zephyr-secure-boot/fit/zephyr-tampered.itb differ: byte 32769, line 94
```

If `cmp` prints nothing, that byte was already `0xff` in your build; pick another offset inside the payload, for example `seek=32800`, and run the `dd` and `cmp` commands again.

This image proves that U-Boot catches a change made after signing. Expect the signature check to pass and the hash check to fail: the signature covers the configuration and the `hash-1` node, which you didn't touch, and `hash-1` covers the payload bytes, which you changed.

## Check both images on the host

Your times, hash values and `FIT Image at` addresses differ from the outputs on this page. Run `fit_check_sign` as you did when you [built U-Boot](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/), first on the wrong-key image:

```bash
$UBOOT_OUT/tools/fit_check_sign -f $FIT/zephyr-b.itb -k $UBOOT_OUT/u-boot.dtb
```

The output is similar to:

```output
Verifying Hash Integrity for node 'conf-1'... sha256,rsa2048:key-b-
 error!
Verification failed for '(null)' hash node in 'conf-1' config node
Failed to verify required signature 'key-key-a'
Signature check bad (error 1)
```

**Lines to look for:** `sha256,rsa2048:key-b-` followed by `error!`, then `Failed to verify required signature 'key-key-a'`, then `Signature check bad (error 1)`. The exit code is 1.

Then check the tampered image:

```bash
$UBOOT_OUT/tools/fit_check_sign -f $FIT/zephyr-tampered.itb -k $UBOOT_OUT/u-boot.dtb
```

The output is similar to:

```output
Verifying Hash Integrity for node 'conf-1'... sha256,rsa2048:key-a+
Verified OK, loading images
## Loading kernel (any) from FIT Image at 7ae29b84a000 ...
   Using 'conf-1' configuration
   Verifying Hash Integrity ...
sha256,rsa2048:key-a+
OK

   Trying 'kernel-1' kernel subimage
     Description:  Zephyr RTOS image
     Created:      Fri Sep 11 19:14:00 2026
     Type:         Kernel Image
     Compression:  uncompressed
     Data Size:    58340 Bytes = 56.97 KiB = 0.06 MiB
     Architecture: AArch64
     OS:           U-Boot
     Load Address: 0x82000000
     Entry Point:  0x82000000
     Hash algo:    sha256
     Hash value:   1d1d375f14c3354579e9e5310986a69b831bcd1944cd6b35aa8e83632b658166
   Verifying Hash Integrity ...
sha256 error!
Bad hash value for 'hash-1' hash node in 'kernel-1' image node
Bad Data Hash

## Loading fdt (any) from FIT Image at 7ae29b84a000 ...
   Using 'conf-1' configuration
   Verifying Hash Integrity ...
sha256,rsa2048:key-a+
OK

Could not find subimage node type 'fdt'
## Loading ramdisk (any) from FIT Image at 7ae29b84a000 ...
   Using 'conf-1' configuration
   Verifying Hash Integrity ...
sha256,rsa2048:key-a+
OK

Could not find subimage node type 'ramdisk'
Signature check bad (error 1)
```

**Lines to look for:** `sha256,rsa2048:key-a+` on the first line, then `sha256 error!` and `Bad hash value for 'hash-1' hash node in 'kernel-1' image node`, then `Signature check bad (error 1)`. The exit code is 1.

## Add the two images to the boot media

Add the two new FITs with `mcopy`, at the same `BOOT_IMG` volume you used when you [built the boot media](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/6-boot-the-target/), then list the volume:

```bash
mcopy -o -i $BOOT_IMG $FIT/zephyr-b.itb $FIT/zephyr-tampered.itb ::
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
zephyr-b itb     60198 2026-09-15  16:49
ZEPHYR~1 ITB     60198 2026-09-15  16:49  zephyr-tampered.itb
        6 files           3 287 838 bytes
                        130 643 968 bytes free
```

In QEMU the disk image holds the three FITs and nothing else. The listing above is the AM62L EVM's card: six files, the boot files and the three FITs.

{{< tabpane-normal >}}
  {{< tab header="QEMU" >}}
Nothing to write: `disk.img` is the disk. Start QEMU again with the same command as on the previous page; it reads the image fresh at every start.
  {{< /tab >}}
  {{< tab header="AM62L EVM" >}}
Write the image to the card again with the same `dd` command as on the previous page, taking the same care with `/dev/sdX`:

```bash
sudo dd if=$WORK/sdcard.img of=/dev/sdX bs=4M conv=fsync status=progress
```

Move the card to the board, open the console with `picocom`, and power the board on.
  {{< /tab >}}
{{< /tabpane-normal >}}

## Run the wrong-key test

Press a key during the three-second countdown to stop autoboot. If you miss it, U-Boot starts image A; start the target again and try once more. At the prompt, run the wrong-key test:

```console
=> run b
```

The expected output is:

```output
60198 bytes read in 1 ms (57.4 MiB/s)
## Loading kernel (any) from FIT Image at 90000000 ...
   Using 'conf-1' configuration
   Verifying Hash Integrity ... sha256,rsa2048:key-b-  error!
Verification failed for '<NULL>' hash node in 'conf-1' config node
Failed to verify required signature 'key-key-a'
Bad Data Hash
ERROR -2: can't get kernel image!
*** REFUSED: Zephyr was NOT started ***
```

**Lines to look for:** `sha256,rsa2048:key-b-  error!` says the FIT is signed with `key-b`, which U-Boot doesn't have; `-` means fail. `Failed to verify required signature 'key-key-a'` is the `required = "conf"` rule, which an unsigned image fails too. `Bad Data Hash` and `ERROR -2: can't get kernel image!` close both refusals on this page whichever check failed; the lines above them say which one. `bootm start` failed, so the `&&` chain skipped `go` and the `echo` printed `*** REFUSED: Zephyr was NOT started ***`, with no Zephyr banner.

## Run the tampered test

Still at the prompt, run the tampered test:

```console
=> run t
```

The expected output is:

```output
60198 bytes read in 2 ms (28.7 MiB/s)
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
   Verifying Hash Integrity ... sha256 error!
Bad hash value for 'hash-1' hash node in 'kernel-1' image node
Bad Data Hash
ERROR -2: can't get kernel image!
*** REFUSED: Zephyr was NOT started ***
```

**Lines to look for:** `sha256,rsa2048:key-a+ OK` shows the signature passes; `sha256 error!` and `Bad hash value for 'hash-1' hash node in 'kernel-1' image node` show the payload no longer matches the stored `Hash value`; `*** REFUSED: Zephyr was NOT started ***` follows.

{{% notice Note %}}
If `run b` or `run t` ends with a Zephyr banner instead of the `REFUSED` line, the check isn't failing closed. The two causes seen in practice are a `;` where `&&` belongs in the `zboot` chain of `CONFIG_PREBOOT`, and a `signature.dtsi` without `required = "conf"`. Check both against [Build U-Boot with the public key and a boot command that fails closed](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/), rebuild, and put the files on the boot media again.
{{% /notice %}}

To boot the trusted image again, type `run a`.

## What you've accomplished and what's next

U-Boot started the trusted image and stopped the wrong-key image at the signature and the tampered one at the hash, both before `go`. Next, [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/8-production/) separates what these runs proved from what a product still needs.
