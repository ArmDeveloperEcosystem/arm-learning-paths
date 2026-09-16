---
title: Create signing keys and sign the Zephyr image into a FIT
description: Build mkimage from the board's U-Boot tree, generate two RSA keys with OpenSSL, and sign the Zephyr binary into a FIT image that U-Boot can verify.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build U-Boot's host tools first

Open a terminal and load the environment: `source $HOME/zephyr-secure-boot/env.sh`.

`mkimage` builds and signs a FIT image. `fit_check_sign` verifies a signed FIT on the host. Both come from the same U-Boot tree as the board's U-Boot, so signer and verifier match.

The `tools` target needs the board's `.config` first, so run the defconfig target named by `UBOOT_DEFCONFIG` in `env.sh`:

```bash
make -C $UBOOT_SRC O=$UBOOT_OUT CROSS_COMPILE=$CROSS CC="${CROSS}gcc --sysroot=$SYSROOT" $UBOOT_DEFCONFIG
```

`CC="${CROSS}gcc --sysroot=$SYSROOT"` gives the SDK's compiler the library path `SYSROOT` from `env.sh`; on the AM62L SDK the U-Boot link fails without it. Keep it on every `make` line, including the three on the next page.

Then build the host tools:

```bash
make -C $UBOOT_SRC O=$UBOOT_OUT CROSS_COMPILE=$CROSS CC="${CROSS}gcc --sysroot=$SYSROOT" tools
```

Both tools land in `$UBOOT_OUT/tools/`. Check that `mkimage` runs:

```bash
$UBOOT_OUT/tools/mkimage -V
```

The output is similar to:

```output
mkimage version 2026.01-g5fb294342321
```

{{% notice Note %}}
If the `tools` build stops at `pylibfdt`, `swig` or `gnutls/gnutls.h`, a package is missing: run the `apt install` command from [Set up the host tools and the board's SDK](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/2-set-up-tools/) again, then the `tools` step.
{{% /notice %}}

## Create two signing keys

The private key signs and stays on the host. Only the public key goes into U-Boot, on the next page.

You create two pairs. `key-a` is the key U-Boot trusts. `key-b` is a valid key U-Boot never sees. You use it on the optional test page, [Test that U-Boot refuses a wrong key and a tampered image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-test-the-checks/), to prove that U-Boot refuses a key it doesn't know.

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

`mkimage -k <dir>` expects this layout. `<name>.key` holds the private key, `<name>.crt` is a self-signed certificate wrapping the public key, and `<name>` is the `key-name-hint` you write in the FIT source.

These 2048-bit keys, generated on the build machine, are fine for a demo; [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/8-production/) covers production keys.

## Write the FIT source

You describe the FIT in a `.its` file (image tree source), and `mkimage` compiles and signs it into an `.itb` (image tree blob). Write the source; the heredoc is unquoted, so `$WORK` and `$ZEPHYR_ADDR` expand:

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

Three parts of this file matter:

- `os = "u-boot"` marks Zephyr as a standalone program, so U-Boot verifies and copies it without looking for a Linux kernel header or device tree.
- `signature-1` sits under the configuration, because the `required = "conf"` rule checks the configuration U-Boot boots. With `sign-images = "kernel"`, the signature also covers the image's `hash-1` node, and `key-name-hint` names the key in `$KEYS`.
- `load` and `entry` are `ZEPHYR_ADDR`, where U-Boot copies the verified payload and where `go` jumps.

## Sign the image

Compile and sign the FIT. `-k $KEYS` tells `mkimage` where the private key is:

```bash
$UBOOT_OUT/tools/mkimage -f $FIT/zephyr-a.its -k $KEYS $FIT/zephyr-a.itb
```

`mkimage` prints the image contents. Your timestamps, `Hash value` and `Sign value` differ, and the `Sign value` is shortened here. The output is similar to:

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

**Lines to look for:** `Sign algo:    sha256,rsa2048:key-a` and the last line, `Signature written to ... node '/configurations/conf-1/signature-1'`, say that `mkimage` found `key-a` in `$KEYS` and wrote its signature into `conf-1`. `Hash value` is the SHA-256 of `zephyr.bin`, which U-Boot recomputes on the board.

Don't use the `mkimage -K` option here: the public key goes into U-Boot's own device tree at build time, on the next page.

## What you've accomplished and what's next

You've built the U-Boot host tools, created two key pairs and signed Zephyr into `$FIT/zephyr-a.itb`. Next, you [build U-Boot with the public key and a boot command that fails closed](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/).
