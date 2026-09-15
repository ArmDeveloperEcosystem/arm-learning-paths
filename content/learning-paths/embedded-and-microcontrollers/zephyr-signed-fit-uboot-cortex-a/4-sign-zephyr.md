---
title: Create signing keys and sign the Zephyr image into a FIT
description: Build mkimage from the TI U-Boot tree, generate two RSA keys with OpenSSL, and sign the Zephyr binary into a FIT image that U-Boot can verify.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build U-Boot's host tools first

Open a terminal and load the environment: `source $HOME/zephyr-secure-boot/env.sh`.

`mkimage` builds and signs a FIT image. `fit_check_sign` verifies a signed FIT on the host. Both come from the same U-Boot tree as the board's U-Boot, so signer and verifier match.

The `tools` target needs the board's `.config` first, so select the AM62L EVM defconfig:

```bash
make -C $UBOOT_SRC O=$UBOOT_OUT CROSS_COMPILE=$CROSS CC="${CROSS}gcc --sysroot=$SYSROOT" am62lx_evm_defconfig
```

`CC="${CROSS}gcc --sysroot=$SYSROOT"` gives the SDK's compiler the library path `SYSROOT` from `env.sh`; without it the U-Boot link fails. Keep it on every `make` line, including the three on the next page.

Then build the host tools:

```bash
make -C $UBOOT_SRC O=$UBOOT_OUT CROSS_COMPILE=$CROSS CC="${CROSS}gcc --sysroot=$SYSROOT" tools
```

Check that `mkimage` runs:

```bash
$UBOOT_OUT/tools/mkimage -V
```

The output is similar to:

```output
mkimage version 2026.01-g5fb294342321
```

{{% notice Note %}}
If the `tools` build stops early, the fix depends on where it stops:
- At `pylibfdt` or `swig`: install `swig python3-dev` as described in [Set up the host tools and the TI SDK](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/2-set-up-tools/). If you'd rather not build U-Boot's own `dtc` and `pylibfdt`, add `DTC=$(which dtc)` to the `make` line and install the `python3-libfdt` package, because U-Boot still checks that `import libfdt` works in `python3`
- At `mkeficapsule` with `fatal error: gnutls/gnutls.h: No such file or directory`: install `libgnutls28-dev uuid-dev`, or add the line `# CONFIG_TOOLS_MKEFICAPSULE is not set` to `$UBOOT_OUT/.config`, then run the `tools` step again. You don't need that tool
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

`sha256,rsa2048` is enough for a demo. The production page covers stronger keys and where to keep them.

{{% notice Warning %}}
These are throwaway development keys, generated on the build machine. Production keys are generated and kept elsewhere. See [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/8-production/).
{{% /notice %}}

## Write the FIT source

You describe the FIT from [Understand where Zephyr sits in the Cortex-A boot chain](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/1-boot-chain/) in a `.its` file (image tree source), and `mkimage` compiles and signs it into an `.itb` (image tree blob).

Write the source with a heredoc, so `$WORK` expands to the absolute path of the Zephyr binary you built on the previous page:

```bash
cat > $FIT/zephyr-a.its <<EOF
/dts-v1/;
/ {
	description = "Zephyr RTOS for AM62L Cortex-A53, signed with key-a";
	#address-cells = <1>;
	images {
		kernel-1 {
			description = "Zephyr RTOS image";
			data = /incbin/("$WORK/zephyrproject/applications/hello/build/primary/zephyr/zephyr.bin");
			type = "kernel";
			arch = "arm64";
			os = "u-boot";
			compression = "none";
			load  = <0x82000000>;
			entry = <0x82000000>;
			hash-1 { algo = "sha256"; };
		};
	};
	configurations {
		default = "conf-1";
		conf-1 {
			description = "Zephyr on AM62L Cortex-A53";
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

`type = "kernel"` is the plain label `bootm` accepts for the main image.

`os = "u-boot"` is U-Boot's slot for a standalone program: the payload is verified and copied, nothing else. With `os = "linux"`, U-Boot would look for a device tree in the FIT and parse a Linux kernel header.

`load` and `entry` are `0x82000000`, Zephyr's link address on this board, where U-Boot copies the verified payload.

`hash-1 { algo = "sha256"; }` is the hash of the payload bytes. It sits in the image node, and the signature covers it.

`conf-1` points at the image node with `kernel = "kernel-1"`, and `default` names it so U-Boot picks it without being told.

`signature-1` sits under the configuration, not under the image, because the `required = "conf"` rule you build into U-Boot on the next page demands a valid signature on the configuration it boots. With `sign-images = "kernel"`, `mkimage` signs the configuration node plus the hash node of the kernel image. `key-name-hint = "key-a"` names the key files in `$KEYS` and, later, the key node U-Boot looks up.

Both `description` properties are mandatory. `mkimage` refuses the source without them.

## Sign the image

Compile and sign the FIT. `-k $KEYS` tells `mkimage` where the private key is:

```bash
$UBOOT_OUT/tools/mkimage -f $FIT/zephyr-a.its -k $KEYS $FIT/zephyr-a.itb
```

`mkimage` prints the image contents. Trimmed, the output is similar to:

```output
  Type:         Kernel Image
  ...
  OS:           U-Boot
  Load Address: 0x82000000
  Entry Point:  0x82000000
  Hash algo:    sha256
  ...
  Sign algo:    sha256,rsa2048:key-a
```

Don't use the `mkimage -K` option here: the public key goes into U-Boot's own device tree at build time, on the next page.

Print the same listing for any FIT with:

```bash
$UBOOT_OUT/tools/mkimage -l $FIT/zephyr-a.itb
```

## What you've accomplished and what's next

You've built `mkimage` and `fit_check_sign`, created two RSA key pairs, and signed Zephyr into `$FIT/zephyr-a.itb`. U-Boot can't verify it yet because it doesn't have the key. On the next page, [Build U-Boot with the public key and a boot command that fails closed](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/), you compile `key-a`'s public half into U-Boot's device tree, write the boot command, and check the image offline with `fit_check_sign` before touching the board.
