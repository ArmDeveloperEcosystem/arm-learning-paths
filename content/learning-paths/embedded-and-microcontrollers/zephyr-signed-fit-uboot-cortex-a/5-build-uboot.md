---
title: Build U-Boot with the public key and a boot command that fails closed
description: Compile the public half of key-a into U-Boot's own device tree through Kconfig, add a boot command that starts Zephyr only after bootm verifies it, and prove on the host with fit_check_sign that the trusted FIT verifies against that key.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Where U-Boot keeps its keys

Open a terminal and load the environment: `source $HOME/zephyr-secure-boot/env.sh`.

U-Boot keeps its FIT verification keys in the control device tree, the DTB packed into `u-boot.img`, in a node named `/signature`:

```dts
/ {
	signature {
		key-key-a {
			required = "conf";
			algo = "sha256,rsa2048";
			rsa,r-squared = <...>;
			rsa,modulus = <...>;
			rsa,exponent = <0x00 0x10001>;
			rsa,n0-inverse = <...>;
			rsa,num-bits = <0x800>;
			key-name-hint = "key-a";
		};
	};
};
```

The `rsa,` properties are the public half of `key-a`. `required = "conf"` is the fail-closed rule from [Understand where Zephyr sits in the Cortex-A boot chain](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/1-boot-chain/): no valid signature by this key, no boot.

`am62lx_evm_defconfig` already turns on everything else. Check the symbols that matter in the `$UBOOT_OUT/.config` from the previous page:

```bash
grep -E '^CONFIG_(FIT|FIT_SIGNATURE|RSA|OF_SEPARATE)=|LEGACY_IMAGE_FORMAT' $UBOOT_OUT/.config
```

The expected output is:

```output
CONFIG_FIT=y
CONFIG_FIT_SIGNATURE=y
# CONFIG_LEGACY_IMAGE_FORMAT is not set
CONFIG_OF_SEPARATE=y
CONFIG_RSA=y
```

`CONFIG_FIT_SIGNATURE` and `CONFIG_RSA` are the verifier. `CONFIG_OF_SEPARATE` builds the control DTB from source, so you can add a node to it at build time.

Legacy image support is off: the older uImage format carries no signature, so `bootm` has nothing unsigned to fall back to. [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/8-production/) covers the other boot commands.

Only the key and the boot command are missing. Both are build configuration, so the U-Boot source stays untouched.

## Generate the key node

`mkimage` only writes a public key while it signs something, so you sign a throwaway FIT into an empty scratch DTB and turn that DTB back into source. Create the empty DTB and a tiny payload in `$WORK`:

```bash
printf '/dts-v1/;\n/ { };\n' | dtc -I dts -O dtb -o $WORK/scratch.dtb
printf 'payload' > $WORK/payload.bin
```

Write the throwaway FIT's source, a copy of the `zephyr-a.its` from [Create signing keys and sign the Zephyr image into a FIT](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/4-sign-zephyr/) with placeholders for the payload and the addresses:

```bash
cat > $WORK/key.its <<'EOF'
/dts-v1/;
/ {
	description = "carrier used only to emit key-a's public key";
	#address-cells = <1>;
	images {
		kernel-1 {
			description = "placeholder payload";
			data = /incbin/("payload.bin");
			type = "kernel"; arch = "arm64"; os = "u-boot"; compression = "none";
			load = <0>; entry = <0>;
			hash-1 { algo = "sha256"; };
		};
	};
	configurations {
		default = "conf-1";
		conf-1 {
			kernel = "kernel-1";
			signature-1 { algo = "sha256,rsa2048"; key-name-hint = "key-a"; sign-images = "kernel"; };
		};
	};
};
EOF
```

Both `description` properties must stay, as on the previous page. `dtc` looks for `payload.bin` next to `key.its`.

Sign the throwaway FIT and convert the scratch DTB to `signature.dtsi`:

```bash
$UBOOT_OUT/tools/mkimage -f $WORK/key.its -k $KEYS -K $WORK/scratch.dtb -r $WORK/key.itb
dtc -I dtb -O dts -q $WORK/scratch.dtb | sed '/^\/dts-v1\/;/d' > $WORK/signature.dtsi
```

`-K` writes the public key into `scratch.dtb` and `-r` marks it required. `sed` removes the `/dts-v1/;` header, which a `.dtsi` included after the main `.dts` must not repeat.

Check that the file names the right key and nothing else:

```bash
grep -E 'key-name-hint|required' $WORK/signature.dtsi
```

The expected output is:

```output
			required = "conf";
			key-name-hint = "key-a";
```

`key-b` must not appear: U-Boot never gets its public half.

## Why a .dtsi and not mkimage -K on u-boot.dtb

`mkimage -K` can also write the key straight into `u-boot.dtb`, but every `make` rebuilds the control DTB from source and the injected key is gone. `CONFIG_DEVICE_TREE_INCLUDES` lists extra `.dtsi` files to include in that build, so the key is compiled in every time.

## Write a boot command that fails closed

Zephyr's own board page starts the AM62L EVM from the U-Boot prompt with one unverified line:

```console
=> fatload mmc 1:1 0x82000000 zephyr.bin; dcache flush; icache flush; dcache off; icache off; go 0x82000000
```

Nothing checks the bytes between `fatload` and `go`. The verified version puts `bootm` in front of the same handover. Split over several lines for reading, the chain is:

```text
fatload mmc 1:1 0x90000000 ${fit} &&
bootm start 0x90000000 &&
bootm loados &&
dcache flush && icache flush && dcache off && icache off &&
go 0x82000000;
echo "*** REFUSED: Zephyr was NOT started ***"
```

Each piece has one job:

- `fatload mmc 1:1 0x90000000 ${fit}` reads the FIT named in `${fit}` from partition 1 of the SD card (`mmc 1`; `mmc 0` is the eMMC) to `0x90000000`, clear of `0x82000000`, so `loados` can't copy Zephyr over the FIT it is reading.
- `bootm start 0x90000000` parses the FIT, picks `conf-1`, verifies the RSA signature against `/signature/key-key-a`, then verifies the image hash.
- `bootm loados` copies the verified payload to its `load` address, `0x82000000`.
- The four cache commands hand the CPU over the way Zephyr expects.
- `go 0x82000000` is a jump. It verifies nothing.

Why not a plain `bootm`? A full `bootm` continues past `loados` into OS-specific boot code; stopping after `loados` and jumping with `go` uses U-Boot as a verifier only, not as an OS loader.

`&&` is what makes it fail closed: `a && b` runs `b` only if `a` succeeded, while `a; b` would fall through to `go` after a failed check. `go` never returns, so the `echo` prints only when a step failed.

That chain becomes the environment variable `zboot`, and three one-line wrappers pick the file it loads:

| Variable | Definition |
|---|---|
| `zboot` | The chain, with `${fit}` as the file name |
| `a` | `setenv fit zephyr-a.itb; run zboot` |
| `b` | `setenv fit zephyr-b.itb; run zboot` |
| `t` | `setenv fit zephyr-tampered.itb; run zboot` |

`a` boots the trusted image. `b` and `t` name images that don't exist yet, for [Test that U-Boot refuses a wrong key and a tampered image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-test-the-checks/). `CONFIG_PREBOOT` defines all four before autoboot, U-Boot's countdown to running `bootcmd` on its own, so they exist even after you stop it. `CONFIG_BOOTCOMMAND="run a"` makes the trusted image the default and `CONFIG_BOOTDELAY=3` gives you three seconds to stop it.

The commands are compiled into U-Boot rather than stored on the card, where anyone could edit a boot script to skip the check. TI's default `CONFIG_ENV_IS_NOWHERE=y` gives the environment no storage, so nothing on the card can override them.

## Configure and build

Reset to TI's defconfig so the fragment lands on a known `.config`:

```bash
make -C $UBOOT_SRC O=$UBOOT_OUT CROSS_COMPILE=$CROSS CC="${CROSS}gcc --sysroot=$SYSROOT" am62lx_evm_defconfig
```

Append the fragment to `.config`. The heredoc is unquoted so `$WORK` expands; `\${fit}` keeps `${fit}` in the file for U-Boot to expand at run time:

```bash
cat >> $UBOOT_OUT/.config <<EOF
CONFIG_DEVICE_TREE_INCLUDES="$WORK/signature.dtsi"
CONFIG_USE_PREBOOT=y
CONFIG_PREBOOT="setenv zboot 'fatload mmc 1:1 0x90000000 \${fit} && bootm start 0x90000000 && bootm loados && dcache flush && icache flush && dcache off && icache off && go 0x82000000; echo \"*** REFUSED: Zephyr was NOT started ***\"'; setenv a 'setenv fit zephyr-a.itb; run zboot'; setenv b 'setenv fit zephyr-b.itb; run zboot'; setenv t 'setenv fit zephyr-tampered.itb; run zboot'"
CONFIG_USE_BOOTCOMMAND=y
CONFIG_BOOTCOMMAND="run a"
CONFIG_BOOTDELAY=3
EOF
```

The `\"` around the `echo` text stay: that's how a Kconfig string holds a literal quote.

{{% notice Note %}}
The fresh defconfig starts from a clean `.config`. If the `tools` build on the previous page needed `# CONFIG_TOOLS_MKEFICAPSULE is not set`, add that line to the fragment. If it needed `DTC=$(which dtc)`, add it to both `make` lines that follow.
{{% /notice %}}

Let Kconfig resolve the fragment:

```bash
make -C $UBOOT_SRC O=$UBOOT_OUT CROSS_COMPILE=$CROSS CC="${CROSS}gcc --sysroot=$SYSROOT" olddefconfig
```

The output is similar to:

```output
.config:2355:warning: override: reassigning to symbol DEVICE_TREE_INCLUDES
.config:2356:warning: override: reassigning to symbol USE_PREBOOT
.config:2358:warning: override: reassigning to symbol USE_BOOTCOMMAND
.config:2359:warning: override: reassigning to symbol BOOTCOMMAND
.config:2360:warning: override: reassigning to symbol BOOTDELAY
```

The five warnings are expected: your lines replace values the defconfig already set. The line numbers can differ.

Now build, pointing `BL1`, `BL31`, `TEE` and `BINMAN_INDIRS` at the prebuilt TF-A, OP-TEE and TI firmware from the SDK:

```bash
make -C $UBOOT_SRC O=$UBOOT_OUT CROSS_COMPILE=$CROSS CC="${CROSS}gcc --sysroot=$SYSROOT" -j$(nproc) \
     BL1=$PREBUILT/bl1.bin BL31=$PREBUILT/bl31.bin TEE=$PREBUILT/bl32.bin BINMAN_INDIRS=$PREBUILT
```

The build takes a few minutes. Check the three boot files:

```bash
ls -l $UBOOT_OUT/tiboot3.bin $UBOOT_OUT/tispl.bin $UBOOT_OUT/u-boot.img
```

The sizes are about 0.2 MB, 1.5 MB and 1.4 MB. These are the three files of the boot chain table on the first page.

## Check the key is inside U-Boot

Decompile `$UBOOT_OUT/u-boot.dtb`, the control DTB that went into `u-boot.img`, and print its `/signature` node:

```bash
dtc -I dtb -O dts -q $UBOOT_OUT/u-boot.dtb | sed -n '/signature {/,/^\t};/p'
```

With the long values shortened, the output is similar to:

```output
	signature {
		key-key-a {
			required = "conf";
			algo = "sha256,rsa2048";
			rsa,r-squared = <...>;
			rsa,modulus = <...>;
			rsa,exponent = <0x00 0x10001>;
			rsa,n0-inverse = <...>;
			rsa,num-bits = <0x800>;
			key-name-hint = "key-a";
		};
	};
```

Now verify the trusted FIT on the host against that DTB. `fit_check_sign` runs the same verification code as U-Boot, so its verdict predicts the board's, and a mistake shows up now rather than at the serial console. `-f` names the FIT and `-k` the DTB that holds the keys:

```bash
$UBOOT_OUT/tools/fit_check_sign -f $FIT/zephyr-a.itb -k $UBOOT_OUT/u-boot.dtb
```

The output is similar to:

```output
Verifying Hash Integrity for node 'conf-1'... sha256,rsa2048:key-a+
Verified OK, loading images
## Loading kernel (any) from FIT Image at 7a44a7686000 ...
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
sha256+
OK

   Decrypting Data ...
OK

   Loading Kernel Image to 0
## Loading fdt (any) from FIT Image at 7a44a7686000 ...
   Using 'conf-1' configuration
   Verifying Hash Integrity ...
sha256,rsa2048:key-a+
OK

Could not find subimage node type 'fdt'
## Loading ramdisk (any) from FIT Image at 7a44a7686000 ...
   Using 'conf-1' configuration
   Verifying Hash Integrity ...
sha256,rsa2048:key-a+
OK

Could not find subimage node type 'ramdisk'
Signature check OK
```

**Lines to look for:** the first line, `sha256,rsa2048:key-a+`, is the signature of `conf-1` verified with `key-a`, the `+` being the pass mark, and the last line, `Signature check OK`, is the verdict. The exit code is 0.

Between them the tool walks the FIT the way `bootm` will on the board: it lists `kernel-1`, checks its hash (`sha256+` then `OK`), prints `Loading Kernel Image to 0` (the host tool loads nothing), and reports that the FIT has no `fdt` and no `ramdisk`. That's correct: it holds Zephyr and nothing else. The `FIT Image at` address is the tool's buffer on the host and changes every run, and the host tool breaks `sha256,rsa2048:key-a+ OK` over two lines where the board prints one.

[Test that U-Boot refuses a wrong key and a tampered image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-test-the-checks/) runs the same tool on an image signed with `key-b` and on a tampered copy, and expects it to refuse both.

## What you've accomplished and what's next

You built TI's U-Boot with the public half of `key-a` compiled into its control device tree and a boot command that starts Zephyr only after `bootm` has verified the signature and the hash, without touching the U-Boot source. `fit_check_sign` has shown on the host that the trusted FIT verifies against that key.

Next, you [put the boot files and the trusted FIT on an SD card](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/6-boot-the-board/) and watch U-Boot make the same decisions on the board.
