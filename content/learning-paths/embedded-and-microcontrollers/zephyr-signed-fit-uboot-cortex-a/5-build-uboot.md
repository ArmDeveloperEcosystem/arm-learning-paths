---
title: Build U-Boot with the public key and a boot command that fails closed
description: Compile the public half of key-a into U-Boot's own device tree through Kconfig, add a boot command that starts Zephyr only after bootm verifies it, and prove on the host with fit_check_sign that only the trusted FIT verifies.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Where U-Boot keeps its keys

Open a terminal and load the environment: `source $HOME/zephyr-secure-boot/env.sh`.

U-Boot keeps its FIT verification keys in the control device tree, the DTB packed into `u-boot.img` that you met on the first page, in a node named `/signature`.

The node U-Boot needs looks like this:

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

The `rsa,` properties are the public half of `key-a`, in the layout U-Boot's RSA code reads. `required = "conf"` is the fail-closed rule from [Understand where Zephyr sits in the Cortex-A boot chain](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/1-boot-chain/): every configuration in every FIT must carry a valid signature by this key, or U-Boot refuses to load it. It applies to configuration signatures, the kind you wrote on the previous page.

The configuration that `am62lx_evm_defconfig` produces already turns on everything else. Check the symbols that matter in the `$UBOOT_OUT/.config` from the previous page:

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

`CONFIG_FIT_SIGNATURE` and `CONFIG_RSA` are the verifier. `CONFIG_OF_SEPARATE` means the control DTB is built from source into a separate `u-boot.dtb`, which binman, U-Boot's image packaging tool, packs into `u-boot.img`, so you can add a node to it at build time.

Legacy image support is off: that older single-file format (uImage) carries no signature, so `bootm` has nothing unsigned to fall back to. Other boot commands still exist; [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-production/) covers them.

The only things missing are the key and the boot command. Both are build configuration, so the U-Boot source stays untouched.

## Generate the key node

`mkimage` only writes a public key while it signs something, so you sign a throwaway FIT into an empty scratch DTB and turn that DTB back into source. Create the empty DTB and a tiny payload in `$WORK`:

```bash
printf '/dts-v1/;\n/ { };\n' | dtc -I dts -O dtb -o $WORK/scratch.dtb
printf 'payload' > $WORK/payload.bin
```

Write the throwaway FIT's source: the `zephyr-a.its` you wrote when you [signed the Zephyr image into a FIT](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/4-sign-zephyr/), with placeholders for the payload and the addresses:

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

Both `description` properties must stay; `mkimage` refuses the file without them. `dtc` looks for `payload.bin` next to `key.its`.

Sign the throwaway FIT and convert the scratch DTB to `signature.dtsi`:

```bash
$UBOOT_OUT/tools/mkimage -f $WORK/key.its -k $KEYS -K $WORK/scratch.dtb -r $WORK/key.itb
dtc -I dtb -O dts -q $WORK/scratch.dtb | sed '/^\/dts-v1\/;/d' > $WORK/signature.dtsi
```

`-K` writes the public key into `scratch.dtb` and `-r` marks it required, which produces the `required = "conf"` property. `sed` removes the `/dts-v1/;` header, because a `.dtsi` included after the main `.dts` must not repeat it.

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

`mkimage -K` can also write the key straight into an existing `u-boot.dtb`. On TI's U-Boot that is fragile: every `make` rebuilds the control DTB from source and binman packs it again, so an injected key is gone at the next build.

`CONFIG_DEVICE_TREE_INCLUDES` is a Kconfig string that lists extra `.dtsi` files to include when the control DTB is built. Point it at `signature.dtsi` and the key is compiled in on every build. No file in the U-Boot tree changes.

## Write a boot command that fails closed

Zephyr's own board page starts the AM62L EVM from the U-Boot prompt with one unverified line:

```console
=> fatload mmc 1:1 0x82000000 zephyr.bin; dcache flush; icache flush; dcache off; icache off; go 0x82000000
```

`fatload` reads the file from the SD card and `go` jumps to it. Nothing checks the bytes in between. The verified version keeps the same handover (the cache commands and `go`) and puts `bootm` in front of it. Split over several lines for reading, the chain is:

```text
fatload mmc 1:1 0x90000000 ${fit} &&
bootm start 0x90000000 &&
bootm loados &&
dcache flush && icache flush && dcache off && icache off &&
go 0x82000000;
echo "*** REFUSED: Zephyr was NOT started ***"
```

Each piece has one job:

- `fatload mmc 1:1 0x90000000 ${fit}` reads the FIT named in `${fit}` from partition 1 of the SD card (`mmc 1`; `mmc 0` is the eMMC) to `0x90000000`, clear of `0x82000000`, so the next steps can't copy Zephyr over the FIT they are reading.
- `bootm start 0x90000000` parses the FIT, picks `conf-1`, verifies the RSA signature against `/signature/key-key-a`, then verifies the image hash. All the checking happens here.
- `bootm loados` copies the verified payload to its `load` address, `0x82000000`.
- The four cache commands hand the CPU over the way Zephyr expects. On arm64, `dcache off` also turns the MMU (memory management unit) off, which Zephyr's memory setup expects on entry.
- `go 0x82000000` is a jump. It verifies nothing.

Why not a plain `bootm`? A full `bootm` runs a sequence of named steps and continues past `loados` to the step that boots an operating system. You stop after `loados`, so no OS-specific code runs, and `go` does the jump instead. U-Boot is used as a verifier, not as an OS loader.

Why `&&` and not `;`? In U-Boot's shell, `a && b` runs `b` only if `a` succeeded; `a; b` runs `b` either way, so a failed check would fall through to `go` and boot the image anyway. The `&&` is what makes it fail closed. `go` never returns, so the `echo` after the final `;` prints only when a step failed.

That chain becomes the environment variable `zboot`, and three one-line wrappers pick the image to test:

| Variable | Definition |
|---|---|
| `zboot` | The chain, with `${fit}` as the file name |
| `a` | `setenv fit zephyr-a.itb; run zboot` |
| `b` | `setenv fit zephyr-b.itb; run zboot` |
| `t` | `setenv fit zephyr-tampered.itb; run zboot` |

`CONFIG_PREBOOT` defines all four: it's a command string U-Boot runs before the autoboot countdown, so the variables exist even after you stop autoboot. `CONFIG_BOOTCOMMAND="run a"` makes the trusted image the default and `CONFIG_BOOTDELAY=3` gives you three seconds to stop it.

You compile them into U-Boot rather than store them on the card, on purpose: anyone with the card could edit a boot script or environment file on the unprotected FAT partition to skip the check. TI's default `CONFIG_ENV_IS_NOWHERE=y` gives the environment no storage, so nothing on the card can override them.

## Configure and build

Reset to TI's defconfig, so the fragment lands on a known `.config` whatever the previous page's `tools` build left behind:

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

Let Kconfig resolve the fragment against the rest of the configuration:

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

The five warnings are expected: your lines replace the values the defconfig already set for the same symbols. The line numbers can differ.

Now build. `BL1`, `BL31` and `TEE` name the prebuilt firmware from the SDK: `bl1.bin` and `bl31.bin` are TF-A stages, `bl32.bin` is OP-TEE. `BINMAN_INDIRS` tells binman where to find TI's firmware when it packs the boot files:

```bash
make -C $UBOOT_SRC O=$UBOOT_OUT CROSS_COMPILE=$CROSS CC="${CROSS}gcc --sysroot=$SYSROOT" -j$(nproc) \
     BL1=$PREBUILT/bl1.bin BL31=$PREBUILT/bl31.bin TEE=$PREBUILT/bl32.bin BINMAN_INDIRS=$PREBUILT
```

One `make` builds the SPL, U-Boot proper and the control DTB, then binman packs the three boot files. `bl1.bin` and TI's firmware go into `tiboot3.bin`; `bl31.bin`, `bl32.bin` and the SPL go into `tispl.bin`; U-Boot proper goes into `u-boot.img`. It takes a few minutes. Check the results:

```bash
ls -l $UBOOT_OUT/tiboot3.bin $UBOOT_OUT/tispl.bin $UBOOT_OUT/u-boot.img
```

The sizes are about 0.2 MB, 1.5 MB and 1.4 MB. These are the three files of the boot chain table on the first page: the ROM loads `tiboot3.bin`, `tispl.bin` carries TF-A, OP-TEE and the SPL, and `u-boot.img` is U-Boot proper.

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

Now verify the three FITs on the host against that DTB. `fit_check_sign` runs the same verification code as U-Boot, so its verdict predicts the board's, and a mistake shows up now rather than at the serial console. `-f` names the FIT and `-k` the DTB that holds the keys. Start with the trusted image:

```bash
$UBOOT_OUT/tools/fit_check_sign -f $FIT/zephyr-a.itb -k $UBOOT_OUT/u-boot.dtb
```

The output is similar to:

```output
Verifying Hash Integrity for node 'conf-1'... sha256,rsa2048:key-a+
Verified OK, loading images
...
Signature check OK
```

The lines cut with `...` list `kernel-1`, check its hash (`sha256+ OK`), print `Loading Kernel Image to 0` (the host tool loads nothing) and report that the FIT has no `fdt` and no `ramdisk`. That's correct: it holds Zephyr and nothing else. The exit code is 0.

Next, check the wrong-key image:

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

Finally, check the tampered image:

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

The signature still passes and only the hash fails, as you expected when you [made the tampered image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/4-sign-zephyr/). You'll see the same two lines on the board.

## What you've accomplished and what's next

You built TI's U-Boot with the public half of `key-a` compiled into its control device tree. Its boot command starts Zephyr only after `bootm` has verified the signature and the hash. The U-Boot source is unchanged: the key is a `.dtsi` and the commands are a `.config` fragment. `fit_check_sign` has shown on the host that the trusted FIT verifies and that it refuses the other two.

Next, you [put the boot files and the three FITs on an SD card](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/6-boot-the-board/) and watch U-Boot make the same decisions on the board.
