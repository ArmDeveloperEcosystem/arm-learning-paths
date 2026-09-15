---
title: Test that U-Boot refuses a wrong key and a tampered image
description: "Optional: sign a second Zephyr image with a key U-Boot doesn't have, tamper with a copy of the trusted FIT, check both with fit_check_sign on the host, then watch U-Boot refuse both on the AM62L EVM."
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

The line to check in the `mkimage` summary is `Sign algo:    sha256,rsa2048:key-b`.

## Make a tampered copy of the trusted image

Copy the trusted `.itb` and overwrite one byte inside the payload:

```bash
cp $FIT/zephyr-a.itb $FIT/zephyr-tampered.itb
printf '\xff' | dd of=$FIT/zephyr-tampered.itb bs=1 seek=32768 conv=notrunc 2>/dev/null
```

The first `0xe8` (232) bytes of the file belong to the FIT itself and the Zephyr binary follows, so offset 32768 (`0x8000`) lands inside Zephyr's code, not in the FIT's own nodes.

Check that the copy now differs from the original:

```bash
cmp $FIT/zephyr-a.itb $FIT/zephyr-tampered.itb
```

The output is similar to:

```output
/home/user/zephyr-secure-boot/fit/zephyr-a.itb /home/user/zephyr-secure-boot/fit/zephyr-tampered.itb differ: byte 32769, line 94
```

If `cmp` prints nothing, that byte was already `0xff` in your build; pick another offset inside the payload, for example `seek=32800`, and run the `dd` and `cmp` commands again.

Expect the signature check to pass and the hash check to fail: the signature covers the configuration node and the `hash-1` node, and `hash-1` covers the payload bytes you changed.

All three `.itb` files are the same size, 60198 bytes in this build; only verification tells them apart.

## Check both images on the host

`fit_check_sign` gives the same verdict as U-Boot on the board. Run it as you did when you [built U-Boot](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/), first on the wrong-key image:

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

Two checks fail: the DTB has no `key-b`, and `required = "conf"` demands a `key-a` signature on every configuration.

Then check the tampered image:

```bash
$UBOOT_OUT/tools/fit_check_sign -f $FIT/zephyr-tampered.itb -k $UBOOT_OUT/u-boot.dtb
```

The output is similar to:

```output
Verifying Hash Integrity for node 'conf-1'... sha256,rsa2048:key-a+
Verified OK, loading images
...
sha256 error!
Bad hash value for 'hash-1' hash node in 'kernel-1' image node
Bad Data Hash
...
Signature check bad (error 1)
```

The signature passes and only the hash fails.

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

`mdir` shows the FAT short name `ZEPHYR~1.ITB` in front and the long name `zephyr-tampered.itb` at the end of its line; U-Boot's `fatload` finds it by the long name. Six files: the three boot stages and the three FITs.

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
...
   Verifying Hash Integrity ... sha256,rsa2048:key-b-  error!
Verification failed for '<NULL>' hash node in 'conf-1' config node
Failed to verify required signature 'key-key-a'
Bad Data Hash
ERROR -2: can't get kernel image!
*** REFUSED: Zephyr was NOT started ***
```

These are the same two failures as on the host: U-Boot found a signature naming `key-b` and has no such key, and the `required = "conf"` rule you [built into U-Boot](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/) demands a valid `key-a` signature on every configuration. `Bad Data Hash` and `ERROR -2: can't get kernel image!` close both refusals on this page; the lines before them name the failed check.

Because `bootm start` returns an error, the `&&` chain stops there: `bootm loados` and `go` never run, and the `echo` after the `;` prints the `REFUSED` line.

## Run the tampered test

Still at the prompt, run the tampered test:

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

This time the signature check passes and the hash check fails, as you expected when you made the tampered image and as the FIT diagram in [Understand where Zephyr sits in the Cortex-A boot chain](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/1-boot-chain/) shows.

{{% notice Note %}}
If `run b` or `run t` ends with a Zephyr banner instead of the `REFUSED` line, the check isn't failing closed. The two causes seen in practice are a `;` where `&&` belongs in the `zboot` chain of `CONFIG_PREBOOT`, and a `signature.dtsi` without `required = "conf"`. Check both against [Build U-Boot with the public key and a boot command that fails closed](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/), rebuild, and write the card again.
{{% /notice %}}

To boot the trusted image again, type `run a` at the prompt.

## What you've accomplished and what's next

`zephyr-a.itb`, signed with the key compiled into U-Boot, runs; `zephyr-b.itb`, signed with a valid key U-Boot doesn't have, is refused at the signature step; `zephyr-tampered.itb`, changed after signing, passes the signature step and is refused at the hash step. In every case the refusal stops the `&&` chain before `go`, so a rejected image never runs.

Next, [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/8-production/) separates what these runs proved from what they didn't, and what still stands between this setup and a production device.
