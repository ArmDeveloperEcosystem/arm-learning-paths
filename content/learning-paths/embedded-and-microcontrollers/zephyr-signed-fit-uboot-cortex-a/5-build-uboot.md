---
title: Build U-Boot with the public key and a boot command that fails closed
description: Build U-Boot with a trusted public key and a boot command that starts Zephyr only after verification, then check the signed FIT on the host.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Check that U-Boot can verify signatures

Open a terminal and load the environment file for your target:

- QEMU: `source $HOME/zephyr-secure-boot/env-qemu.sh`
- AM62L evaluation module (EVM): `source $HOME/zephyr-secure-boot/env-am62l.sh`

Both target default configurations enable Flattened Image Tree (FIT) signature verification. Check the relevant settings in `$UBOOT_OUT/.config`, generated when you built the host tools:

```bash
grep -E '^CONFIG_(FIT|FIT_SIGNATURE|RSA|OF_SEPARATE)=|LEGACY_IMAGE_FORMAT' $UBOOT_OUT/.config
```

For the AM62L EVM, the expected output is:

```output
CONFIG_FIT=y
CONFIG_FIT_SIGNATURE=y
# CONFIG_LEGACY_IMAGE_FORMAT is not set
CONFIG_OF_SEPARATE=y
CONFIG_RSA=y
```

`CONFIG_FIT_SIGNATURE` and `CONFIG_RSA` enable the verifier. `CONFIG_OF_SEPARATE` provides a separate control device tree blob (DTB), which will hold your public key. Legacy images, which carry no signature, are disabled in this configuration.

You'll add the public key and boot command through build configuration, without patching U-Boot source.

For QEMU, `qemu_arm64_defconfig` enables the unsigned legacy image format with `CONFIG_LEGACY_IMAGE_FORMAT=y`. The QEMU configuration fragment disables it and configures a control device tree containing your key.

## Generate the public-key device-tree node

Use a temporary FIT to make `mkimage` write the public key into a scratch DTB. You'll convert the key node to source for the U-Boot build. 

First, create an empty DTB and a placeholder payload in `$WORK`:

```bash
printf '/dts-v1/;\n/ { };\n' | dtc -I dts -O dtb -o $WORK/scratch.dtb
printf 'payload' > $WORK/payload.bin
```

Create `key.its` using the same layout as `zephyr-a.its`, with the placeholder payload:

```bash
cat > $WORK/key.its <<'EOF'
/dts-v1/;
/ {
	description = "carrier used only to emit the public key for key-a";
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

Sign the temporary FIT and convert the scratch DTB to `signature.dtsi`:

```bash
$UBOOT_OUT/tools/mkimage -f $WORK/key.its -k $KEYS -K $WORK/scratch.dtb -r $WORK/key.itb
dtc -I dtb -O dts -q $WORK/scratch.dtb | sed '/^\/dts-v1\/;/d' > $WORK/signature.dtsi
```

`-K` writes the public key into `scratch.dtb`, and `-r` marks the key as required. The `sed` command removes the `/dts-v1/;` header so that the resulting `.dtsi` can be included after the main `.dts` header.

Check the key name and required-signature setting:

```bash
grep -E 'key-name-hint|required' $WORK/signature.dtsi
```

The expected output is:

```output
			required = "conf";
			key-name-hint = "key-a";
```

Confirm that `key-name-hint` is `key-a` and `required` is `conf`. Leave out `key-b` so that U-Boot doesn't trust its signatures.

The build incorporates `signature.dtsi` into the U-Boot control device tree. Use `mkimage -K` only with the scratch DTB. Adding the key directly to a finished `u-boot.dtb` would lose it when `make` rebuilds that file.

## Write a boot command that fails closed

An unverified boot command loads `zephyr.bin` and jumps to it. With your QEMU target values, the command looks like the following:

```console
=> fatload virtio 0:1 0x40000000 zephyr.bin; dcache flush; icache flush; dcache off; icache off; go 0x40000000
```

On the AM62L EVM, the same line reads `fatload mmc 1:1 0x82000000 zephyr.bin` and ends `go 0x82000000`.

The command doesn't verify the image between `fatload` and `go`. Add `bootm` verification before the handover. The verified command chain uses the same QEMU target values and is split into lines for readability:

```text
fatload virtio 0:1 0x48000000 ${fit} &&
bootm start 0x48000000 &&
bootm loados &&
dcache flush && icache flush && dcache off && icache off &&
go 0x40000000;
echo "*** REFUSED: Zephyr was NOT started ***"
```

The command chain loads, verifies, and starts Zephyr:

- `fatload virtio 0:1 0x48000000 ${fit}` reads the FIT named in `${fit}` from `BOOT_DEV` to `FIT_ADDR`. `FIT_ADDR` is separate from `ZEPHYR_ADDR`, so copying the payload won't overwrite the FIT being read.
- `bootm start 0x48000000` parses the FIT, picks `conf-1`, verifies the RSA signature against `/signature/key-key-a`, then verifies the image hash.
- `bootm loados` copies the verified payload to its `load` address, `ZEPHYR_ADDR`.
- The cache commands flush and disable the caches. On arm64, `dcache off` also disables the memory management unit (MMU), preparing the state Zephyr expects at entry.
- `go 0x40000000` jumps to `ZEPHYR_ADDR` without performing verification. Using `bootm start` and `bootm loados` stops before the OS-specific boot code that a plain `bootm` would run.

For QEMU, `BOOT_DEV` is `virtio 0:1`, the File Allocation Table (FAT) partition in the disk image. On the AM62L EVM, it's `mmc 1:1`, the first partition on the SD card. The board loads the FIT at `0x90000000` and copies Zephyr to `0x82000000`.

Failing closed means stopping before Zephyr starts if any command fails. The `&&` operators enforce this condition: `a && b` runs `b` only if `a` succeeds. Separating the commands with `;` would allow execution to continue after a failed check. In this application, `go` doesn't return, so the refusal message prints only when an earlier command fails.

Store the chain in the environment variable `zboot`. Three wrapper commands select which FIT it loads:

| Variable | Definition |
|---|---|
| `zboot` | The chain, with `${fit}` as the file name |
| `a` | `setenv fit zephyr-a.itb; run zboot` |
| `b` | `setenv fit zephyr-b.itb; run zboot` |
| `t` | `setenv fit zephyr-tampered.itb; run zboot` |

`a` boots the trusted image. `b` and `t` select the images that you'll create during the optional [wrong-key and tampered-image tests](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-test-the-checks/).

Autoboot runs `bootcmd` after a countdown. `CONFIG_PREBOOT` defines `zboot` and its wrappers before the countdown, making them available if you interrupt it. `CONFIG_BOOTCOMMAND="run a"` selects the trusted image by default. `CONFIG_BOOTDELAY=3` gives you three seconds to interrupt autoboot.

The commands are compiled into U-Boot rather than stored on the card, where anyone could edit a boot script to skip the check.

## Configure U-Boot

Reset to the default configuration for your target before adding the custom settings:

```bash
make -C $UBOOT_SRC O=$UBOOT_OUT CROSS_COMPILE=$CROSS CC="$UBOOT_CC" $UBOOT_DEFCONFIG
```

Append the boot-command settings to `.config`. The unquoted `EOF` delimiter lets the shell expand `$BOOT_DEV`, `$FIT_ADDR`, and `$ZEPHYR_ADDR`. Escaping `\${fit}` preserves `${fit}` for U-Boot to expand at runtime:

```bash
cat >> $UBOOT_OUT/.config <<EOF
CONFIG_USE_PREBOOT=y
CONFIG_PREBOOT="setenv zboot 'fatload $BOOT_DEV $FIT_ADDR \${fit} && bootm start $FIT_ADDR && bootm loados && dcache flush && icache flush && dcache off && icache off && go $ZEPHYR_ADDR; echo \"*** REFUSED: Zephyr was NOT started ***\"'; setenv a 'setenv fit zephyr-a.itb; run zboot'; setenv b 'setenv fit zephyr-b.itb; run zboot'; setenv t 'setenv fit zephyr-tampered.itb; run zboot'"
CONFIG_USE_BOOTCOMMAND=y
CONFIG_BOOTCOMMAND="run a"
CONFIG_BOOTDELAY=3
EOF
```

Keep the `\"` sequences around the `echo` text. The sequences represent literal quotes inside the Kconfig string. Run `grep ^CONFIG_PREBOOT $UBOOT_OUT/.config` and check that the device and addresses for your target appear in the command.

Follow the instructions for your target to add its device-tree and boot settings:

{{< tabpane-normal >}}
  {{< tab header="QEMU" >}}
QEMU normally supplies the U-Boot device tree at runtime, so `CONFIG_DEVICE_TREE_INCLUDES` has no source tree to modify. Instead, you'll create a control device tree containing your key and pass it to the build.

Add the following settings to enable that approach and disable unsigned legacy images. The settings also enable cache commands and keep the environment from being saved to flash:

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

`CONFIG_OF_BOARD` and `CONFIG_OF_OMIT_DTB` off make U-Boot carry a control device tree of its own, the one your key goes into. `CONFIG_LEGACY_IMAGE_FORMAT` off closes the older image format, which carries no signature. `CONFIG_CMD_CACHE` adds the `dcache` and `icache` commands that the boot command uses. `CONFIG_ENV_IS_NOWHERE` keeps the environment out of flash, so nothing saved at the prompt can replace your boot command.
  {{< /tab >}}
  {{< tab header="AM62L EVM" >}}
TI's U-Boot tree builds its control device tree from source. Set `CONFIG_DEVICE_TREE_INCLUDES` to include your public-key node in that build:

```bash
cat >> $UBOOT_OUT/.config <<EOF
CONFIG_DEVICE_TREE_INCLUDES="$WORK/signature.dtsi"
EOF
```
  {{< /tab >}}
{{< /tabpane-normal >}}

Run `olddefconfig` to resolve the configuration settings:

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

These override warnings are expected because your settings replace default values. The QEMU configuration can produce additional warnings for its target-specific overrides.

## Build U-Boot

Follow the instructions for your target to build U-Boot.

{{< tabpane-normal >}}
  {{< tab header="QEMU" >}}
Export the device tree for the QEMU machine that you'll boot later:

```bash
qemu-system-aarch64 -machine virt,gic-version=3,dumpdtb=$WORK/qemu-virt.dtb -cpu cortex-a53 -m 1G -nographic
```
This keeps the U-Boot drivers, console, and memory sizing consistent with the machine. QEMU writes the file and exits.

Add your public-key node by decompiling the tree, appending `signature.dtsi`, and recompiling it:

```bash
dtc -I dtb -O dts -q $WORK/qemu-virt.dtb > $WORK/uboot-control.dts
cat $WORK/signature.dtsi >> $WORK/uboot-control.dts
dtc -I dts -O dtb -q -o $WORK/uboot-control.dtb $WORK/uboot-control.dts
```
The device tree compiler (`dtc`) merges the repeated root nodes, adding `/signature` to the exported tree.

Build U-Boot with `EXT_DTB` pointing to your control device tree. Specify `u-boot.bin` and `u-boot.dtb` as the build targets:

```bash
make -C $UBOOT_SRC O=$UBOOT_OUT CROSS_COMPILE=$CROSS CC="$UBOOT_CC" -j$(nproc) \
     EXT_DTB=$WORK/uboot-control.dtb u-boot.bin u-boot.dtb
```
The `scripts/check-of.sh` script in U-Boot rejects the default `all` target for this machine, which normally receives its device tree from a prior stage.

The build takes a couple of minutes. Check the two files:

```bash
ls -l $UBOOT_OUT/u-boot.bin $UBOOT_OUT/u-boot.dtb
```

`u-boot.bin` is about 1.4 MB and ends with the bytes of `u-boot.dtb`, the control device tree with your key inside.
  {{< /tab >}}
  {{< tab header="AM62L EVM" >}}
TI's U-Boot tree uses binman, the U-Boot image packaging tool, to package the early stages. Point `BL1`, `BL31`, and `TEE` to the prebuilt TF-A and OP-TEE binaries in the SDK. Set `BINMAN_INDIRS` to the SDK directory containing TI's system firmware:

```bash
make -C $UBOOT_SRC O=$UBOOT_OUT CROSS_COMPILE=$CROSS CC="$UBOOT_CC" -j$(nproc) \
     BL1=$PREBUILT/bl1.bin BL31=$PREBUILT/bl31.bin TEE=$PREBUILT/bl32.bin BINMAN_INDIRS=$PREBUILT
```

The build takes a few minutes. Check the three boot files:

```bash
ls -l $UBOOT_OUT/tiboot3.bin $UBOOT_OUT/tispl.bin $UBOOT_OUT/u-boot.img
```

Expect sizes of about 0.2 MB for `tiboot3.bin`, 1.5 MB for `tispl.bin`, and 1.4 MB for `u-boot.img`. The build also writes the control device tree to `u-boot.dtb` in the same output directory.
  {{< /tab >}}
{{< /tabpane-normal >}}

## Check the embedded key and verify the signed FIT

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

The `rsa,` properties contain the public key for `key-a`. Check that the node includes `required = "conf"`, which makes U-Boot require a valid configuration signature.

Verify the trusted FIT on the host using the key in that DTB. `fit_check_sign` uses the verification code in U-Boot. `-f` selects the FIT, and `-k` selects the DTB containing the public key:

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

Check for `sha256,rsa2048:key-a+`, which confirms that the configuration signature verifies with `key-a`. The `+` indicates success. The final verdict is `Signature check OK`, and the exit code is zero.

The tool also checks for device-tree and ramdisk subimages. The two `Could not find subimage node type` messages are expected because this FIT contains only Zephyr.

## What you've accomplished and what's next

You've built U-Boot with the public key for `key-a` and a boot command that starts Zephyr only after verification succeeds. The trusted FIT passes the host check against the embedded key. 

Next, you'll prepare the boot media and watch U-Boot verify and start Zephyr on your chosen target.
