---
title: Test that U-Boot refuses a wrong key and a tampered image
description: "Optional: test on the host and target that U-Boot rejects Zephyr FIT images signed with an untrusted key or modified after signing."
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Test rejection of untrusted and tampered images

These tests are optional. Create one FIT signed with an untrusted key and another modified after signing. Check both on the host, then confirm that U-Boot refuses to start them on your target. The `b` and `t` commands are already built into U-Boot to select these images.

Open a terminal and load your target’s environment file:

- **QEMU**: `source $HOME/zephyr-secure-boot/env-qemu.sh`
- **AM62L EVM**: `source $HOME/zephyr-secure-boot/env-am62l.sh`

## Build a second Zephyr image

Give the wrong-key image a distinct banner so you can identify it if it unexpectedly starts.

In Workbench for Zephyr, select **Add Application**. Use the same workspace, toolchain, board, and sample as the [trusted image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/3-build-zephyr/). Enter `hello_b` as the **Project Name**. Copy `prj.conf` and `src/main.c` from `hello`, then replace these two banner lines:

```c
	printk("#   Hello from ZEPHYR IMAGE B                  #\n");
	printk("#   signed with key-b  (NOT trusted by U-Boot) #\n");
```

In the **Applications** view, open the context menu for `hello_b` and select **Build**. The resulting binary is `$WORK/zephyrproject/applications/hello_b/build/primary/zephyr/zephyr.bin`.

## Sign the second image with the untrusted key

Use `key-b`, the second key pair created during [FIT signing](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/4-sign-zephyr/). Copy the FIT source with `sed`, replacing `key-a` with `key-b` and the `hello` application path with `hello_b`. Then sign the new FIT:

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

Check for `Sign algo:    sha256,rsa2048:key-b`. The `Hash value` differs from image A’s because the application banner changed. This FIT has a signature from `key-b`, but U-Boot trusts only `key-a` and must reject it.

## Make a tampered copy of the trusted image

Copy the trusted `.itb` and overwrite one byte inside the payload:

```bash
cp $FIT/zephyr-a.itb $FIT/zephyr-tampered.itb
printf '\xff' | dd of=$FIT/zephyr-tampered.itb bs=1 seek=32768 conv=notrunc 2>/dev/null
```

In the example FITs, offset 32768 (`0x8000`) falls inside the Zephyr payload rather than the FIT metadata. The payload begins a few hundred bytes into the file and is tens of kilobytes long.

Check that the copy now differs from the original:

```bash
cmp $FIT/zephyr-a.itb $FIT/zephyr-tampered.itb
```

The output is similar to:

```output
/home/user/zephyr-secure-boot/fit/zephyr-a.itb /home/user/zephyr-secure-boot/fit/zephyr-tampered.itb differ: byte 32769, line 94
```

If `cmp` prints nothing, the selected byte was already `0xff`. Choose another offset inside the payload, such as `seek=32800`, then repeat the `dd` and `cmp` commands.

Expect the signature check to pass and the payload hash check to fail. The signature covers the unchanged configuration and `hash-1` node. The hash covers the payload bytes you modified.

## Check both images on the host

Your timings, hash values, and `FIT Image at` addresses will differ from these examples. Run `fit_check_sign` with the control device tree from your [U-Boot build](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/). Check the wrong-key image first:

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

Check for `sha256,rsa2048:key-b-` and `Failed to verify required signature 'key-key-a'`. The final verdict, `Signature check bad (error 1)`, confirms rejection. The exit code is one.

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

Check that `sha256,rsa2048:key-a+` reports a valid signature, followed by `sha256 error!` and `Bad hash value for 'hash-1'`. The final verdict is `Signature check bad (error 1)`, and the exit code is one. The modified payload fails verification even though the configuration signature passes.

## Add the two images to the boot media

Copy both test FITs into the `BOOT_IMG` volume used to [prepare the boot media](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/6-boot-the-target/), then list its contents:

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

This example lists the AM62L EVM’s six files: three boot files and three FITs. The QEMU disk image contains only the three FITs.

{{< tabpane-normal >}}
  {{< tab header="QEMU" >}}
Restart QEMU with the same command used to boot the trusted image. QEMU reads the updated `disk.img` directly; no physical media needs to be written.
  {{< /tab >}}
  {{< tab header="AM62L EVM" >}}
Write the updated image to the card. Confirm the card’s device name before replacing `/dev/sdX`; `dd` overwrites the entire selected disk:

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

Check for `sha256,rsa2048:key-b-  error!` and `Failed to verify required signature 'key-key-a'`. The `-` indicates failure: the image’s signature doesn’t satisfy the required `key-a` check.

When `bootm start` fails, the `&&` chain skips `go` and prints `*** REFUSED: Zephyr was NOT started ***`. Confirm that no Zephyr banner appears. `Bad Data Hash` and `ERROR -2: can't get kernel image!` can appear for either rejection test; use the preceding messages to identify which check failed.

## Run the tampered-image test

At the U-Boot prompt, run the tampered-image test:

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

Check that `sha256,rsa2048:key-a+ OK` reports a valid signature. `sha256 error!` and `Bad hash value for 'hash-1'` indicate that the payload no longer matches its stored hash. Confirm that `*** REFUSED: Zephyr was NOT started ***` appears without a Zephyr banner.

{{% notice Note %}}
If `run b` or `run t` starts Zephyr, verification isn’t preventing startup. Check for a `;` where `&&` belongs in `CONFIG_PREBOOT`, and confirm that `signature.dtsi` includes `required = "conf"`. Compare both with the [U-Boot build settings](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/), rebuild, and update the boot media.
{{% /notice %}}

To boot the trusted image again, type `run a`.

## What you've accomplished and what's next

You’ve confirmed that U-Boot rejects the wrong-key image at the signature check and the tampered image at the payload hash check. Neither reaches `go` or starts Zephyr. Next, you’ll review what these tests establish and what a production device still needs.
