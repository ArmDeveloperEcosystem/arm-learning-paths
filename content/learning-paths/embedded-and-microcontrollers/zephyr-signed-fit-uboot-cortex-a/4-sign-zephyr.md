---
title: Create signing keys and sign the Zephyr image into a FIT
description: Build U-Boot’s signing tools, generate RSA key pairs with OpenSSL, and package Zephyr in a signed FIT image for U-Boot to verify.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build U-Boot’s host tools

Open a terminal and load your target’s environment file:

- **QEMU**: `source $HOME/zephyr-secure-boot/env-qemu.sh`
- **AM62L EVM**: `source $HOME/zephyr-secure-boot/env-am62l.sh`

Build `mkimage` to create and sign FIT images, and `fit_check_sign` to verify them on the host. Use your target’s U-Boot source tree so the host tools match the U-Boot version you’ll run.

Before building the tools, generate `.config` from your target’s default configuration. Run the target named by `UBOOT_DEFCONFIG` in your environment file:

```bash
make -C $UBOOT_SRC O=$UBOOT_OUT CROSS_COMPILE=$CROSS CC="$UBOOT_CC" $UBOOT_DEFCONFIG
```

`UBOOT_CC` stores the compiler command. For QEMU, it names the cross compiler installed from Ubuntu. For the AM62L EVM, it also includes `--sysroot` to locate the SDK’s headers and libraries. Keep `CC="$UBOOT_CC"` on every `make` command, including when you build U-Boot later.

Then build the host tools:

```bash
make -C $UBOOT_SRC O=$UBOOT_OUT CROSS_COMPILE=$CROSS CC="$UBOOT_CC" tools
```

Both tools are written to `$UBOOT_OUT/tools/`. Check that `mkimage` runs:

```bash
$UBOOT_OUT/tools/mkimage -V
```

The output is similar to:

```output
mkimage version 2026.01-g5fb294342321
```

The version string identifies your U-Boot source tree. This example uses the AM62L EVM’s TI tree, version 2026.01. For the QEMU setup, expect `mkimage version 2025.07`.

{{% notice Note %}}
If the tools build reports a missing `pylibfdt` dependency, `swig`, or `gnutls/gnutls.h`, check the packages installed during [host-tool setup](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/2-set-up-tools/). Run the shared `apt install` command again, then retry the tools build.
{{% /notice %}}

## Create two signing key pairs

Use the private key to sign the image and keep it on the host. You’ll embed only the public key in U-Boot during the next lesson.

Create two key pairs. You’ll configure U-Boot to trust `key-a` and leave out the public key for `key-b`. The optional [wrong-key and tampered-image tests](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-test-the-checks/) use `key-b` to demonstrate rejection of an image signed with an untrusted key.

Generate both pairs with OpenSSL:

```bash
cd $KEYS
for k in key-a key-b; do
  openssl genpkey -algorithm RSA -quiet -out $k.key \
      -pkeyopt rsa_keygen_bits:2048 -pkeyopt rsa_keygen_pubexp:65537
  openssl req -batch -new -x509 -key $k.key -out $k.crt -subj "/CN=$k" -days 3650
done
ls $KEYS
```

The expected output is:

```output
key-a.crt  key-a.key  key-b.crt  key-b.key
```

`mkimage -k <dir>` expects these files in the key directory:

- `<name>.key` holds the private key
- `<name>.crt` is a self-signed certificate containing the public key
- The shared file-name stem, `<name>`, matches `key-name-hint` in the FIT source

These 2048-bit keys are generated on the build host for this demonstration. [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/8-production/) covers production key handling.

## Write the FIT source

Describe the FIT in an image tree source (`.its`) file. `mkimage` compiles and signs it to produce an image tree blob (`.itb`). Create the source with this command. The unquoted `EOF` delimiter lets the shell expand `$WORK` and `$ZEPHYR_ADDR`:

```bash
cat > $FIT/zephyr-a.its <<EOF
/dts-v1/;
/ {
	description = "Zephyr RTOS, signed with key-a";
	#address-cells = <1>;
	images {
		kernel-1 {
			description = "Zephyr RTOS image";
			data = /incbin/("$WORK/zephyrproject/applications/hello/build/primary/zephyr/zephyr.bin");
			type = "kernel";
			arch = "arm64";
			os = "u-boot";
			compression = "none";
			load  = <$ZEPHYR_ADDR>;
			entry = <$ZEPHYR_ADDR>;
			hash-1 { algo = "sha256"; };
		};
	};
	configurations {
		default = "conf-1";
		conf-1 {
			description = "Zephyr on Cortex-A";
			kernel = "kernel-1";
			signature-1 {
				algo = "sha256,rsa2048";
				key-name-hint = "key-a";
				sign-images = "kernel";
			};
		};
	};
};
EOF
```

The FIT source defines how U-Boot handles the payload:

- `os = "u-boot"` marks Zephyr as a standalone program, so U-Boot verifies and copies it without looking for a Linux kernel header or device tree.
- `signature-1` sits under the configuration, because the `required = "conf"` rule checks the configuration U-Boot boots. With `sign-images = "kernel"`, the signature also covers the image's `hash-1` node, and `key-name-hint` names the key in `$KEYS`.
- `load` and `entry` are `ZEPHYR_ADDR`, where U-Boot copies the verified payload and where `go` jumps.

## Sign the image

Compile and sign the FIT. `-k $KEYS` tells `mkimage` where the private key is:

```bash
$UBOOT_OUT/tools/mkimage -f $FIT/zephyr-a.its -k $KEYS $FIT/zephyr-a.itb
```

`mkimage` prints the FIT contents. Your timestamps, `Hash value`, and `Sign value` will differ. This example shortens `Sign value` for readability. The output is similar to:

```output
FIT description: Zephyr RTOS, signed with key-a
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
  Hash value:   1d1d375f14c3354579e9e5310986a69b831bcd1944cd6b35aa8e83632b658166
 Default Configuration: 'conf-1'
 Configuration 0 (conf-1)
  Description:  Zephyr on Cortex-A
  Kernel:       kernel-1
  Sign algo:    sha256,rsa2048:key-a
  Sign value:   6d5f9933722189a0dcee58791243429d0bf28fe0dce96ac093da23c1f24ead70...
  Timestamp:    Fri Sep 11 19:14:00 2026
Signature written to '/home/user/zephyr-secure-boot/fit/zephyr-a.itb', node '/configurations/conf-1/signature-1'
```

Check `Sign algo:    sha256,rsa2048:key-a` and the final `Signature written to ...` line. They confirm that `mkimage` used `key-a` and wrote its signature into `conf-1`. `Hash value` is the SHA-256 hash of `zephyr.bin`, which U-Boot recomputes during verification.

This example uses the AM62L EVM build. For the QEMU build, expect `Data Size: 37040 Bytes` and `Load Address: 0x40000000`.

Omit `mkimage -K` when signing this FIT. You’ll add the public key to U-Boot’s control device tree during the U-Boot build.

## What you've accomplished and what's next

You’ve built the U-Boot host tools, created two key pairs, and packaged Zephyr in the signed FIT `$FIT/zephyr-a.itb`. Next, you’ll build U-Boot with the trusted public key and a boot command that starts Zephyr only after verification succeeds.
