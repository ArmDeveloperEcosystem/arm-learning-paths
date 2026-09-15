---
title: Test that U-Boot refuses a wrong key and a tampered image
description: "Optional: sign a second Zephyr image with a key U-Boot doesn't have, tamper with a copy of the trusted FIT, check both with fit_check_sign on the host, then watch U-Boot refuse both on the board."
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prove the refusal, not only the acceptance

On the previous page, U-Boot verified `zephyr-a.itb` and started Zephyr. You've seen the verifier accept; you haven't seen it refuse. This page makes two images it must refuse, one signed with the wrong key and one changed after signing, checks them on the host, and watches U-Boot refuse each one at the serial console.

This page is optional. It reuses the `hello` application, the two key pairs in `$KEYS`, the `mkimage` and `fit_check_sign` tools, the U-Boot you built with `key-a`, and the card image in `$WORK`. The `b` and `t` commands compiled into U-Boot are waiting for the two files this page makes.

Open a terminal and load the environment: `source $HOME/zephyr-secure-boot/env.sh`.

## Build a second Zephyr image

The wrong-key image is a different program on purpose: if U-Boot ever runs it, the console says so in capital letters.

In Workbench for Zephyr, select **Add Application** again. Use the same workspace, toolchain, board and sample as when you [built the trusted image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/3-build-zephyr/), and enter `hello_b` as the **Project Name**. Give it the same `prj.conf` and the same `src/main.c` as `hello`, with the two banner lines changed:

```c
	printk("#   Hello from ZEPHYR IMAGE B                  #\n");
	printk("#   signed with key-b  (NOT trusted by U-Boot) #\n");
```

The replacement text is the same length as the original, so the box stays aligned. Build `hello_b` the same way, with a right-click on it in the **Applications** view and **Build**. The result is `$WORK/zephyrproject/applications/hello_b/build/primary/zephyr/zephyr.bin`, again about 58 KB.

## Sign the second image with a key U-Boot doesn't have

`key-b` is the second key pair you created when you [signed the trusted image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/4-sign-zephyr/). It's a valid key, but U-Boot never sees its public half. Copy the FIT source with `sed`, swapping `key-a` for `key-b` and `hello` for `hello_b`, then sign it:

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

The payload starts at offset `0xe8` (232), the `Data Start` you saw on the board, and is 58340 bytes long, so offset 32768 (`0x8000`) lands inside Zephyr's code, not in the FIT's own structure.

Check that the copy now differs from the original:

```bash
cmp $FIT/zephyr-a.itb $FIT/zephyr-tampered.itb
```

The output is similar to:

```output
/home/user/zephyr-secure-boot/fit/zephyr-a.itb /home/user/zephyr-secure-boot/fit/zephyr-tampered.itb differ: byte 32769, line 94
```

If `cmp` prints nothing, that byte was already `0xff` in your build; pick another offset inside the payload, for example `seek=32800`, and run the `dd` and `cmp` commands again.

This image proves that U-Boot catches a change made after signing. Expect the signature check to pass and the hash check to fail. `mkimage` signed the configuration node and the `hash-1` node of the image, and the byte you changed is in neither, so the RSA signature still verifies. The payload bytes are covered by `hash-1`, and they no longer match it, so the hash check fails. The signature makes the hash trustworthy, and the hash catches the change.

All three `.itb` files are the same size, 60198 bytes in this build; only verification tells them apart.

## Check both images on the host

`fit_check_sign` gives the same verdict as U-Boot on the board. Your `Created` time and the `FIT Image at` address differ; the lines that matter are the same. Run it as you did when you [built U-Boot](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/), first on the wrong-key image:

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

Two checks fail: the `-` after `key-b` is the missing key, and the `Failed to verify required signature` line is the `required = "conf"` rule. The wrong-key test on the board explains both.

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

The signature still passes and only the hash fails, as you expected when you made the tampered image. You'll see the same `sha256 error!` and `Bad hash value for 'hash-1'` lines on the board.

## Add the two images to the card

Add the two new FITs to the card image with `mcopy`, at the same `@@1048576` volume offset you used when you [built the card image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/6-boot-the-board/), then list the volume:

```bash
M=$WORK/sdcard.img@@1048576
mcopy -o -i $M $FIT/zephyr-b.itb $FIT/zephyr-tampered.itb ::
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
zephyr-b itb     60198 2026-09-15  16:49
ZEPHYR~1 ITB     60198 2026-09-15  16:49  zephyr-tampered.itb
        6 files           3 287 838 bytes
                        130 643 968 bytes free
```

`mdir` shows the FAT short name `ZEPHYR~1.ITB` in front and the long name `zephyr-tampered.itb` at the end of its line; U-Boot's `fatload` finds it by the long name. Six files: the boot files from the previous page and the three FITs.

Write the image to the card again with the same `dd` command as on the previous page, taking the same care with `/dev/sdX`:

```bash
sudo dd if=$WORK/sdcard.img of=/dev/sdX bs=4M conv=fsync status=progress
```

## Run the wrong-key test

Move the card to the board, open the console with `picocom` as on the previous page, and power the board on. Press a key during the three-second countdown to stop autoboot. If you miss it, U-Boot starts image A; power the board off and on and try again. At the prompt, run the wrong-key test:

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

**Lines to look for:** `sha256,rsa2048:key-b-  error!`, then `Failed to verify required signature 'key-key-a'`, and last `*** REFUSED: Zephyr was NOT started ***`, printed by the `echo` in your boot command. No `Loading Kernel Image` line and no Zephyr banner.

U-Boot reports two separate failures, the same two that `fit_check_sign` reports on the host. The `sha256,rsa2048:key-b-  error!` line says U-Boot found a signature naming `key-b` and has no such key; U-Boot doesn't have the public half of `key-b`. The `Failed to verify required signature 'key-key-a'` line is the `required = "conf"` rule you [built into U-Boot](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/). It says every configuration must carry a valid signature by `key-a`, and this one doesn't. An image with no signature node at all fails that second check in the same way. `Bad Data Hash` and `ERROR -2: can't get kernel image!` end both refusals on this page and don't say which check failed; the lines before them do.

Because `bootm start` returns an error, the `&&` chain stops there. `bootm loados` and `go` never run, and the `echo` after the `;` prints the `REFUSED` line. You're back at the U-Boot prompt; image B never ran.

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

**Lines to look for:** `sha256,rsa2048:key-a+ OK` (the signature passes), then `sha256 error!` and `Bad hash value for 'hash-1' hash node in 'kernel-1' image node` (the hash fails), then `*** REFUSED: Zephyr was NOT started ***`.

This time the signature check passes and the hash check fails, as the FIT diagram in [Understand where Zephyr sits in the Cortex-A boot chain](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/1-boot-chain/) shows. The byte you flipped is in the payload, which the signed `hash-1` node covers, not in the nodes the signature covers. The `Hash value` line is the hash `mkimage` stored, and the bytes U-Boot just read no longer produce it. `bootm start` fails, so `bootm loados` and `go` never run.

{{% notice Note %}}
If `run b` or `run t` ends with a Zephyr banner instead of the `REFUSED` line, the check isn't failing closed. The two causes seen in practice are a `;` where `&&` belongs in the `zboot` chain of `CONFIG_PREBOOT`, and a `signature.dtsi` without `required = "conf"`. Check both against [Build U-Boot with the public key and a boot command that fails closed](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/), rebuild, and write the card again.
{{% /notice %}}

To boot the trusted image again, type `run a` at the prompt. The output is the same as on the previous page: the `IMAGE A` banner, then the four lines Zephyr prints after it.

## What you've accomplished and what's next

You've watched the three results that make the check credible. `zephyr-a.itb`, signed with the key compiled into U-Boot, verifies and runs. `zephyr-b.itb`, signed with a valid key U-Boot doesn't have, is refused at the signature step. `zephyr-tampered.itb`, signed with the right key and changed afterwards, passes the signature step and is refused at the hash step. In every case a refusal stops the `&&` chain before `go`, so a rejected image never runs.

Next, [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/8-production/) separates what these runs proved from what they didn't, and what still stands between this setup and a production device.
