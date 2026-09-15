---
title: Test that U-Boot refuses a wrong key and a tampered image
description: "Optional: sign a second Zephyr image with a key U-Boot doesn't have, tamper with a copy of the trusted FIT, check both with fit_check_sign on the host, then watch U-Boot refuse both on the AM62L EVM."
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prove the refusal, not only the acceptance

On the previous page, U-Boot verified `zephyr-a.itb` and started Zephyr. So far you've seen the verifier accept. You haven't seen it refuse. You need two images it must refuse: one signed with the wrong key, and one changed after signing. You make both, check them on the host, put them on the card, and watch U-Boot refuse each one at the serial console.

This page is optional. It needs nothing beyond what you already built: the `hello` application, the two key pairs in `$KEYS`, and the `mkimage` and `fit_check_sign` tools. It also reuses the U-Boot you built with `key-a` and the card image in `$WORK`. The `b` and `t` commands you compiled into U-Boot are waiting for the two files this page makes.

Open a terminal and load the environment: `source $HOME/zephyr-secure-boot/env.sh`.

## Build a second Zephyr image

The wrong-key image is a different program on purpose. If U-Boot ever runs it, the console says so in capital letters, and you can't mistake it for the trusted image.

In Workbench for Zephyr, select **Add Application** again. Use the same workspace, toolchain, board and sample as when you [built the trusted image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/3-build-zephyr/), and enter `hello_b` as the **Project Name**. The wizard fills in `zephyrproject/applications/hello_b` as the location. Then give it the same `prj.conf` and the same `src/main.c` as `hello`, with the two banner lines changed:

```c
	printk("#   Hello from ZEPHYR IMAGE B                  #\n");
	printk("#   signed with key-b  (NOT trusted by U-Boot) #\n");
```

The replacement text is the same length as the original, so the box stays aligned. Build `hello_b` the same way, with a right-click on it in the **Applications** view and **Build**. The result is `$WORK/zephyrproject/applications/hello_b/build/primary/zephyr/zephyr.bin`, again about 58 KB. Only the text differs.

## Sign the second image with a key U-Boot doesn't have

`key-b` is the second key pair you created when you [signed the trusted image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/4-sign-zephyr/). It's a real, valid key, but U-Boot never sees its public half. For the wrong-key image, copy the FIT source with `sed`, swapping `key-a` for `key-b` and the `hello` binary for `hello_b`, then sign it the same way:

```bash
sed 's/key-a/key-b/g; s#/hello/#/hello_b/#' $FIT/zephyr-a.its > $FIT/zephyr-b.its
$UBOOT_OUT/tools/mkimage -f $FIT/zephyr-b.its -k $KEYS $FIT/zephyr-b.itb
```

`mkimage` prints a summary like the one for the trusted image; the line to check is `Sign algo:    sha256,rsa2048:key-b`. This image proves that a valid signature isn't enough: U-Boot must refuse a key it doesn't have.

## Make a tampered copy of the trusted image

For the tampered image, copy the trusted `.itb` and overwrite one byte inside the payload:

```bash
cp $FIT/zephyr-a.itb $FIT/zephyr-tampered.itb
printf '\xff' | dd of=$FIT/zephyr-tampered.itb bs=1 seek=32768 conv=notrunc 2>/dev/null
```

`printf '\xff'` produces one byte of value `0xff`. `bs=1` makes `dd` count in bytes, `seek=32768` skips to that offset, and `conv=notrunc` keeps the rest of the file intact. The first `0xe8` (232) bytes of the file belong to the FIT itself, and the 58340-byte Zephyr binary follows; you saw that as `Data Start: 0x900000e8` on the board's console. So offset 32768 (`0x8000`) lands inside Zephyr's code, not in the FIT's own nodes.

Check that the copy now differs from the original:

```bash
cmp $FIT/zephyr-a.itb $FIT/zephyr-tampered.itb
```

The output is similar to:

```output
/home/user/zephyr-secure-boot/fit/zephyr-a.itb /home/user/zephyr-secure-boot/fit/zephyr-tampered.itb differ: byte 32769, line 94
```

`cmp` counts bytes from one, and the line number varies with the build. If `cmp` prints nothing, that byte was already `0xff` in your build; pick another offset inside the payload, for example `seek=32800`, and run the `dd` and `cmp` commands again.

This image proves that U-Boot catches a change made after signing. Expect the signature check to pass and the hash check to fail. `mkimage` signed the configuration node and the `hash-1` node of the image, and the byte you changed is in neither, so the RSA signature still verifies. The payload bytes are covered by `hash-1`, and they no longer match it, so the hash check fails. The signature makes the hash trustworthy, and the hash catches the change.

All three `.itb` files are the same size, 60198 bytes in this build. Size tells you nothing; only verification does.

## Check both images on the host

`fit_check_sign` gives the same verdict as U-Boot on the board; run it as you did when you [built U-Boot](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/), this time on the wrong-key image:

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

The signature still passes and only the hash fails, as you expected when you made the tampered image. You'll see the same `sha256 error!` and `Bad hash value for 'hash-1'` lines on the board.

## Add the two images to the card

The card image from the previous page holds the three boot files and `zephyr-a.itb`. Add the two new FITs to it with `mcopy`, the same tool and the same `@@1048576` volume offset you used when you [built the card image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/6-boot-the-board/), then list the volume:

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

`mdir` shows the long name `zephyr-tampered.itb` at the end of its line and the FAT short name `ZEPHYR~1.ITB` in front; U-Boot's `fatload` finds it by the long name. Six files: the three boot stages and the three FITs. Nothing else on the card changes.

Write the image to the card again, with the same command as on the previous page:

```bash
sudo dd if=$WORK/sdcard.img of=/dev/sdX bs=4M conv=fsync status=progress
```

{{% notice Warning %}}
Replace `/dev/sdX` with your card, for example `/dev/sdb`, never a partition such as `/dev/sdb1`. `dd` erases everything on the target, so a wrong device name erases the wrong disk.
{{% /notice %}}

If the card is easier to reach from a PC, copy `zephyr-b.itb` and `zephyr-tampered.itb` onto its first partition from there instead. The result is the same six files.

## Run the wrong-key test

Move the card to the board, open the console with `picocom` as on the previous page, and power the board on. This time press a key during the three-second countdown to stop autoboot. If you miss it, U-Boot starts image A and doesn't come back; power the board off and on and try again. At the prompt, run the wrong-key test:

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

U-Boot reports two separate failures, the same two that `fit_check_sign` reports on the host. The first line says it found a signature naming `key-b` and has no such key; U-Boot doesn't have the public half of `key-b`. The `Failed to verify required signature 'key-key-a'` line is the `required = "conf"` rule you [built into U-Boot](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/). It says every configuration must carry a valid signature by `key-a`, and this one doesn't. An image with no signature node at all fails that second check in the same way. `Bad Data Hash` and `ERROR -2: can't get kernel image!` close both refusals on this page, so the lines before them are the ones that name the failed check.

Because `bootm start` returns an error, the `&&` chain stops there. `bootm loados` and `go` never run, and the `echo` after the `;` prints the `REFUSED` line. You're back at the U-Boot prompt; image B never ran.

## Run the tampered test

You're still at the prompt. Run the tampered test:

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

This time the signature check passes and the hash check fails. That surprises people at first, and it's exactly what the FIT diagram in [Understand where Zephyr sits in the Cortex-A boot chain](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/1-boot-chain/) shows. The byte you flipped is in the payload, which the signed `hash-1` node covers, not in the nodes the signature covers, as you saw when you made the tampered image. U-Boot stops before `bootm loados` again.

{{% notice Note %}}
If `run b` or `run t` ends with a Zephyr banner instead of the `REFUSED` line, the check isn't failing closed. The two causes seen in practice are a `;` where `&&` belongs in the `zboot` chain of `CONFIG_PREBOOT`, and a `signature.dtsi` without `required = "conf"`. Check both against [Build U-Boot with the public key and a boot command that fails closed](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/), rebuild, and write the card again.
{{% /notice %}}

To boot the trusted image again, type `run a` at the prompt. The output is the same as on the previous page: the `IMAGE A` banner, then the four lines Zephyr prints after it.

## What you've accomplished and what's next

You've watched the three results that make the check credible. `zephyr-a.itb`, signed with the key compiled into U-Boot, verifies and runs. `zephyr-b.itb`, signed with a valid key U-Boot doesn't have, is refused at the signature step. `zephyr-tampered.itb`, signed with the right key and changed afterwards, passes the signature step and is refused at the hash step. In every case a refusal stops the `&&` chain before `go`, so a rejected image never runs.

Next, [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/8-production/) separates what these runs proved from what they didn't, and what still stands between this setup and a production device.
