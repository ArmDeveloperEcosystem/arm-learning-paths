---
title: Build U-Boot with the public key and a boot command that fails closed
description: Compile the public half of key-a into U-Boot's own device tree through Kconfig, add a boot command that starts Zephyr only after bootm verifies it, and prove on the host with fit_check_sign that the trusted FIT verifies against that key.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Check that U-Boot can verify signatures

Open a terminal and load the environment for your target: `source $HOME/zephyr-secure-boot/env-qemu.sh`, or `source $HOME/zephyr-secure-boot/env-am62l.sh` for the AM62L EVM.

The target's defconfig must turn on the verifier, and both of these do. Check the symbols that matter in the `$UBOOT_OUT/.config` from the previous page:

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

`CONFIG_FIT_SIGNATURE` and `CONFIG_RSA` are the verifier, `CONFIG_OF_SEPARATE` builds the control DTB from source so you can add a node to it, and legacy images, which carry no signature, are off. Only the key and the boot command are missing, and both are build configuration, so the U-Boot source stays untouched.

In QEMU one line differs: `qemu_arm64_defconfig` prints `CONFIG_LEGACY_IMAGE_FORMAT=y`, leaving that unsigned format on. The QEMU tab of the fragment below turns it off.

## Generate the key node

`mkimage` only writes a public key while it signs something, so you sign a throwaway FIT into an empty scratch DTB and turn that DTB back into source. Create the empty DTB and a tiny payload in `$WORK`:

```bash
printf '/dts-v1/;\n/ { };\n' | dtc -I dts -O dtb -o $WORK/scratch.dtb
printf 'payload' > $WORK/payload.bin
```

Write the throwaway FIT's source, the same layout as `zephyr-a.its` with a placeholder payload:

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

`mkimage` refuses the file without its two `description` properties, and `dtc` looks for `payload.bin` next to `key.its`.

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

`key-b` must not appear: U-Boot never gets its public half. The build compiles this file into U-Boot's control device tree, which is why `mkimage -K` is not used here: it writes the key into a finished `u-boot.dtb`, and the next `make` rebuilds that file without it.

## Write a boot command that fails closed

Zephyr's board documentation usually gives a one-line U-Boot command to start Zephyr, with no verification anywhere in it. Filled in with the QEMU values from your environment file, it is:

```console
=> fatload virtio 0:1 0x40000000 zephyr.bin; dcache flush; icache flush; dcache off; icache off; go 0x40000000
```

On the AM62L EVM the same line reads `fatload mmc 1:1 0x82000000 zephyr.bin` and ends `go 0x82000000`.

Nothing checks the bytes between `fatload` and `go`. The verified version puts `bootm` in front of the same handover. Split over several lines for reading, still with the QEMU values filled in, the chain is:

```text
fatload virtio 0:1 0x48000000 ${fit} &&
bootm start 0x48000000 &&
bootm loados &&
dcache flush && icache flush && dcache off && icache off &&
go 0x40000000;
echo "*** REFUSED: Zephyr was NOT started ***"
```

Each piece has one job:

- `fatload virtio 0:1 0x48000000 ${fit}` reads the FIT named in `${fit}` from `BOOT_DEV` to `FIT_ADDR`. In QEMU, `virtio 0:1` is the FAT partition of the disk image; on the AM62L EVM the same chain reads `mmc 1:1`, partition 1 of the SD card (`mmc 0` is the eMMC), at `0x90000000` and `0x82000000`. `FIT_ADDR` is clear of `ZEPHYR_ADDR`, so `loados` can't copy Zephyr over the FIT it is reading.
- `bootm start 0x48000000` parses the FIT, picks `conf-1`, verifies the RSA signature against `/signature/key-key-a`, then verifies the image hash.
- `bootm loados` copies the verified payload to its `load` address, `ZEPHYR_ADDR`.
- The four cache commands flush and turn off the caches, and on arm64 `dcache off` also turns the MMU off, the state Zephyr expects at entry.
- `go 0x40000000` jumps to `ZEPHYR_ADDR` and verifies nothing. Stopping after `bootm loados` keeps U-Boot a verifier, not an OS loader; a plain `bootm` would go on into OS-specific boot code.

`&&` is what makes it fail closed: `a && b` runs `b` only if `a` succeeded, while `a; b` would fall through to `go` after a failed check. `go` never returns, so the `echo` prints only when a step failed.

That chain becomes the environment variable `zboot`, and three one-line wrappers pick the file it loads:

| Variable | Definition |
|---|---|
| `zboot` | The chain, with `${fit}` as the file name |
| `a` | `setenv fit zephyr-a.itb; run zboot` |
| `b` | `setenv fit zephyr-b.itb; run zboot` |
| `t` | `setenv fit zephyr-tampered.itb; run zboot` |

`a` boots the trusted image. `b` and `t` name images that don't exist yet, for [Test that U-Boot refuses a wrong key and a tampered image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-test-the-checks/). Autoboot is U-Boot's countdown to running `bootcmd` on its own. `CONFIG_PREBOOT` defines all four before that countdown starts, so they exist even after you stop it. `CONFIG_BOOTCOMMAND="run a"` makes the trusted image the default and `CONFIG_BOOTDELAY=3` gives you three seconds to stop it.

The commands are compiled into U-Boot rather than stored on the card, where anyone could edit a boot script to skip the check.

## Configure and build

Reset to the board's defconfig so the fragment lands on a known `.config`:

```bash
make -C $UBOOT_SRC O=$UBOOT_OUT CROSS_COMPILE=$CROSS CC="$UBOOT_CC" $UBOOT_DEFCONFIG
```

Append the fragment to `.config`. The heredoc is unquoted, so the target values `$BOOT_DEV`, `$FIT_ADDR` and `$ZEPHYR_ADDR` expand; `\${fit}` keeps `${fit}` in the file for U-Boot to expand at run time:

```bash
cat >> $UBOOT_OUT/.config <<EOF
CONFIG_USE_PREBOOT=y
CONFIG_PREBOOT="setenv zboot 'fatload $BOOT_DEV $FIT_ADDR \${fit} && bootm start $FIT_ADDR && bootm loados && dcache flush && icache flush && dcache off && icache off && go $ZEPHYR_ADDR; echo \"*** REFUSED: Zephyr was NOT started ***\"'; setenv a 'setenv fit zephyr-a.itb; run zboot'; setenv b 'setenv fit zephyr-b.itb; run zboot'; setenv t 'setenv fit zephyr-tampered.itb; run zboot'"
CONFIG_USE_BOOTCOMMAND=y
CONFIG_BOOTCOMMAND="run a"
CONFIG_BOOTDELAY=3
EOF
```

The `\"` around the `echo` text stay: that's how a Kconfig string holds a literal quote. Run `grep ^CONFIG_PREBOOT $UBOOT_OUT/.config` to check that the target values, not the variable names, landed in the file.

Then add the lines that get the key into the control device tree and turn on what your target's defconfig leaves off:

{{< tabpane-normal >}}
  {{< tab header="QEMU" >}}
QEMU hands U-Boot a device tree at run time, so `qemu_arm64_defconfig` builds none of its own and `CONFIG_DEVICE_TREE_INCLUDES` would have nothing to add to. Instead you build the control device tree yourself in the next step and pass it to the build. These lines turn that on, and close two gaps the AM62L defconfig doesn't have:

```bash
cat >> $UBOOT_OUT/.config <<'EOF'
CONFIG_OF_SEPARATE=y
# CONFIG_OF_BOARD is not set
# CONFIG_OF_OMIT_DTB is not set
# CONFIG_LEGACY_IMAGE_FORMAT is not set
CONFIG_CMD_CACHE=y
# CONFIG_ENV_IS_IN_FLASH is not set
CONFIG_ENV_IS_NOWHERE=y
EOF
```

`CONFIG_OF_BOARD` and `CONFIG_OF_OMIT_DTB` off make U-Boot carry a control device tree of its own, the one your key goes into. `CONFIG_LEGACY_IMAGE_FORMAT` off closes the older image format, which carries no signature. `CONFIG_CMD_CACHE` adds the `dcache` and `icache` commands the boot command uses, and `CONFIG_ENV_IS_NOWHERE` keeps the environment out of flash, so nothing saved at the prompt can replace your boot command.
  {{< /tab >}}
  {{< tab header="AM62L EVM" >}}
TI's tree builds its control device tree from source at every `make`, so one line is enough. `CONFIG_DEVICE_TREE_INCLUDES` is the list of extra `.dtsi` files the build compiles into that tree:

```bash
cat >> $UBOOT_OUT/.config <<EOF
CONFIG_DEVICE_TREE_INCLUDES="$WORK/signature.dtsi"
EOF
```
  {{< /tab >}}
{{< /tabpane-normal >}}

Let Kconfig resolve the fragment:

```bash
make -C $UBOOT_SRC O=$UBOOT_OUT CROSS_COMPILE=$CROSS CC="$UBOOT_CC" olddefconfig
```

The output is similar to:

```output
.config:2355:warning: override: reassigning to symbol DEVICE_TREE_INCLUDES
.config:2356:warning: override: reassigning to symbol USE_PREBOOT
.config:2358:warning: override: reassigning to symbol USE_BOOTCOMMAND
.config:2359:warning: override: reassigning to symbol BOOTCOMMAND
.config:2360:warning: override: reassigning to symbol BOOTDELAY
```

The warnings are expected: your lines replace values the defconfig already set. In QEMU there are a few more, one for each extra line in the target block.

### Build U-Boot

{{< tabpane-normal >}}
  {{< tab header="QEMU" >}}
First get the device tree QEMU builds for the machine you boot later, so U-Boot's drivers, console and memory sizing match it. QEMU writes the file and exits:

```bash
qemu-system-aarch64 -machine virt,gic-version=3,dumpdtb=$WORK/qemu-virt.dtb -cpu cortex-a53 -m 1G -nographic
```

Add your key node to it. `dtc` merges repeated root nodes, so decompiling that tree, appending `signature.dtsi` and compiling the two together gives the same tree with `/signature` added:

```bash
dtc -I dtb -O dts -q $WORK/qemu-virt.dtb > $WORK/uboot-control.dts
cat $WORK/signature.dtsi >> $WORK/uboot-control.dts
dtc -I dts -O dtb -q -o $WORK/uboot-control.dtb $WORK/uboot-control.dts
```

Build U-Boot with that file as its control device tree. `EXT_DTB` is the make variable that hands it over, and the two targets are named explicitly because U-Boot's `scripts/check-of.sh` refuses the default `all` target on a machine that normally takes its device tree from a prior stage:

```bash
make -C $UBOOT_SRC O=$UBOOT_OUT CROSS_COMPILE=$CROSS CC="$UBOOT_CC" -j$(nproc) \
     EXT_DTB=$WORK/uboot-control.dtb u-boot.bin u-boot.dtb
```

The build takes a couple of minutes. Check the two files:

```bash
ls -l $UBOOT_OUT/u-boot.bin $UBOOT_OUT/u-boot.dtb
```

`u-boot.bin` is about 1.4 MB and ends with the bytes of `u-boot.dtb`, the control device tree with your key inside.
  {{< /tab >}}
  {{< tab header="AM62L EVM" >}}
TI's U-Boot tree packs the early stages itself, with binman, U-Boot's image packaging tool. Point `BL1`, `BL31` and `TEE` at the prebuilt TF-A and OP-TEE, and `BINMAN_INDIRS` at the directory that holds TI's system firmware, all from the SDK:

```bash
make -C $UBOOT_SRC O=$UBOOT_OUT CROSS_COMPILE=$CROSS CC="$UBOOT_CC" -j$(nproc) \
     BL1=$PREBUILT/bl1.bin BL31=$PREBUILT/bl31.bin TEE=$PREBUILT/bl32.bin BINMAN_INDIRS=$PREBUILT
```

The build takes a few minutes. Check the three boot files:

```bash
ls -l $UBOOT_OUT/tiboot3.bin $UBOOT_OUT/tispl.bin $UBOOT_OUT/u-boot.img
```

The sizes are about 0.2 MB, 1.5 MB and 1.4 MB, and the control device tree lands beside them as `u-boot.dtb`.
  {{< /tab >}}
{{< /tabpane-normal >}}

## Check the key is inside U-Boot

Decompile `$UBOOT_OUT/u-boot.dtb`, the control device tree that went into U-Boot, and print its `/signature` node:

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

The `rsa,` properties are the public half of `key-a`, and `required = "conf"` is the rule U-Boot enforces with it.

Now verify the trusted FIT on the host against that DTB. `fit_check_sign` runs the same verification code as U-Boot, so its verdict predicts the target's. `-f` names the FIT and `-k` the DTB that holds the keys:

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

The lines in between are the tool walking the FIT the way `bootm` does; the two `Could not find subimage node type` lines are expected, because the FIT holds only Zephyr.

## What you've accomplished and what's next

You built U-Boot with `key-a`'s public half and a boot command that starts Zephyr only after `bootm` verifies it, and `fit_check_sign` confirmed on the host that the trusted FIT passes. Next, you [put the boot files and the trusted FIT on the boot media](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/6-boot-the-target/) and boot the target.
