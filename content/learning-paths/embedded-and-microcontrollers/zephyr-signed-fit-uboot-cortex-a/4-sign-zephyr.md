---
title: Create signing keys and sign the Zephyr image into a FIT
description: Build mkimage from the TI U-Boot tree, generate two RSA keys with OpenSSL, and sign the Zephyr binary into a FIT image, plus the wrong-key and tampered images that U-Boot must refuse.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build U-Boot's host tools first

Open a terminal and load the environment: `source $HOME/zephyr-secure-boot/env.sh`.

`mkimage` is the U-Boot host tool that builds and signs a FIT image. `fit_check_sign` is its companion that verifies a signed FIT on the host. Both come out of the same U-Boot source tree as the U-Boot that checks the FIT on the board, so the tool that signs and the code that verifies match.

The `tools` target needs the board's `.config` first, so select the AM62L EVM defconfig:

```bash
make -C $UBOOT_SRC O=$UBOOT_OUT CROSS_COMPILE=$CROSS CC="${CROSS}gcc --sysroot=$SYSROOT" am62lx_evm_defconfig
```

The `CC="${CROSS}gcc --sysroot=$SYSROOT"` part is the sysroot fix from the set-up page. Keep it on every `make` line, including the three on the next page.

Then build the host tools. This step doesn't build U-Boot itself yet:

```bash
make -C $UBOOT_SRC O=$UBOOT_OUT CROSS_COMPILE=$CROSS CC="${CROSS}gcc --sysroot=$SYSROOT" tools
```

The result is `$UBOOT_OUT/tools/mkimage` and `$UBOOT_OUT/tools/fit_check_sign`. Check that `mkimage` runs:

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

RSA is the public-key algorithm U-Boot's FIT code verifies with. An RSA key pair has a private half that signs and a public half that verifies. The private key stays on the host. Only the public key goes into U-Boot, on the next page.

You create two pairs. `key-a` is the key U-Boot trusts. `key-b` exists only to be rejected: it's a real, valid key, but U-Boot never sees its public half. A key U-Boot doesn't know must fail exactly like no signature at all, and `key-b` is how you prove that on the board.

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

`mkimage -k <dir>` expects exactly this layout. `<name>.key` holds the private key. `<name>.crt` is a certificate, a standard wrapper file for a public key; it's self-signed because no authority needs to vouch for it here. `<name>` is the key name you'll write as `key-name-hint` in the FIT source in the next section. The `-subj "/CN=$k"` and `-batch` options let `openssl req` run without questions.

The algorithm here is `sha256,rsa2048`, which is enough for a demo. The production page covers stronger keys and where to keep them.

{{% notice Warning %}}
These are throwaway development keys, generated on the build machine. Production keys are generated and kept elsewhere. See [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-production/).
{{% /notice %}}

## Write the FIT source

A FIT is a device tree blob that packs the payload, a hash of it, and a configuration that carries the signature. You describe it in a `.its` file (image tree source) and `mkimage` compiles and signs it into an `.itb` (image tree blob).

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
			data = /incbin/("$WORK/build/hello/zephyr/zephyr.bin");
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

A few properties decide how U-Boot treats this image.

`bootm` is the U-Boot command that verifies and unpacks a FIT. It accepts two labels for the main image, `kernel` and `kernel_noload`, and `type = "kernel"` is the plain one. Zephyr is the kernel here, so the label is right.

`os = "u-boot"` is the property that makes this work. U-Boot has no `zephyr` value for `os`. With `os = "linux"`, U-Boot would treat the payload as a Linux kernel: look for a device tree in the FIT, patch it, and parse the kernel header. `u-boot` is U-Boot's slot for a standalone program: the payload is verified and copied, nothing else. That's why the FIT needs no device tree and Zephyr needs no Linux boot protocol.

`load` and `entry` are both `0x82000000`, Zephyr's link address on this board. After the checks pass, U-Boot copies the verified payload there; on the next page that copy is the `bootm loados` step of the boot command.

`hash-1 { algo = "sha256"; }` is the hash of the payload bytes. It sits in the image node, and the signature covers it.

`configurations` lists the ways to boot this FIT. There is one, `conf-1`; `kernel = "kernel-1"` points it at the image node, and `default` names it so U-Boot picks it without being told.

`signature-1` sits under the configuration, not under the image, because that's what U-Boot checks: the `required = "conf"` rule you build into U-Boot on the next page demands a valid signature on the configuration it boots. With `sign-images = "kernel"`, `mkimage` signs the configuration node plus the hash node of the kernel image. `key-name-hint = "key-a"` names the key files in `$KEYS` and, later, the key node U-Boot looks up. A signature placed here is called a configuration signature, and it is the only kind this Learning Path uses.

Both `description` properties are mandatory. `mkimage` refuses the source without them.

## Sign the image

Compile and sign the FIT. `-k $KEYS` tells `mkimage` where the private key is:

```bash
$UBOOT_OUT/tools/mkimage -f $FIT/zephyr-a.its -k $KEYS $FIT/zephyr-a.itb
```

`mkimage` ends by printing the contents of the image it made. Trimmed to the lines that matter, the output is similar to:

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

`mkimage` also has a `-K` option that writes the public key into a device tree blob. Don't use it here. The public key goes into U-Boot's own device tree at build time, on the next page. Signing the image and giving U-Boot the key are two separate steps.

You can print the same listing for any FIT at any time:

```bash
$UBOOT_OUT/tools/mkimage -l $FIT/zephyr-a.itb
```

The listing is the same one `mkimage` printed when it signed the file.

## Make the two images that must fail

A verifier you've only seen accept images isn't proven. You need two images it must refuse: one signed with the wrong key, and one changed after signing.

For the wrong-key image, copy the source with `sed`, swapping `key-a` for `key-b` and the `hello` binary for `hello_b`, then sign it the same way:

```bash
sed 's/key-a/key-b/g; s#/hello/#/hello_b/#' $FIT/zephyr-a.its > $FIT/zephyr-b.its
$UBOOT_OUT/tools/mkimage -f $FIT/zephyr-b.its -k $KEYS $FIT/zephyr-b.itb
```

The listing now shows `Sign algo:    sha256,rsa2048:key-b`. This image proves that a valid signature isn't enough: U-Boot must refuse a key it doesn't have. The payload is the `IMAGE B` program, so if it ever ran, the console would say so.

For the tampered image, copy the trusted `.itb` and overwrite one byte inside the payload:

```bash
cp $FIT/zephyr-a.itb $FIT/zephyr-tampered.itb
printf '\xff' | dd of=$FIT/zephyr-tampered.itb bs=1 seek=32768 conv=notrunc 2>/dev/null
```

`bs=1` makes `dd` count in bytes, `seek=32768` skips to that offset, and `conv=notrunc` keeps the rest of the file intact. The first `0xe8` bytes of the file belong to the FIT itself, and the 58340-byte Zephyr binary follows; you'll see that as `Data Start: 0x900000e8` on the board's console. So offset 32768 (`0x8000`) lands inside Zephyr's code, not in the FIT's own nodes.

Check that the copy now differs from the original:

```bash
cmp $FIT/zephyr-a.itb $FIT/zephyr-tampered.itb
```

The output is similar to:

```output
/home/user/zephyr-secure-boot/fit/zephyr-a.itb /home/user/zephyr-secure-boot/fit/zephyr-tampered.itb differ: byte 32769, line 94
```

`cmp` counts bytes from 1, and the line number varies with the build. If `cmp` prints nothing, that byte was already `0xff` in your build; pick another offset inside the payload, for example `seek=32800`, and run the `dd` and `cmp` commands again.

This image proves that U-Boot catches a change made after signing. The signature still verifies and the hash fails, for the reason the boot-chain page gave: the signature covers the hash of the bytes, not the bytes. You'll watch both steps on the board.

All three `.itb` files are the same size, 60198 bytes in this build. Size tells you nothing; only verification does.

## What you've accomplished and what's next

You've built `mkimage` and `fit_check_sign` from the TI U-Boot tree, created two RSA key pairs, and signed Zephyr into `$FIT/zephyr-a.itb`. You've also made the two images that must fail, `zephyr-b.itb` and `zephyr-tampered.itb`.

You can't verify any of them yet: U-Boot doesn't have the key. On the next page, [Build U-Boot with the public key and a boot command that fails closed](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/), you compile `key-a`'s public half into U-Boot's device tree and write the boot command. You then check all three images offline with `fit_check_sign` before touching the board.
