---
title: Review what is verified and what production needs
description: See what U-Boot checks with your key on the target you built, what the stages below it accept, and what a production device needs before the whole chain can be trusted.
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Summary

U-Boot verifies the last link of the chain, and only that one. It read `zephyr-a.itb` from the boot media, checked `conf-1` against the `key-a` node built into its own device tree, checked the hash of the payload, and only then jumped to `ZEPHYR_ADDR`. The optional [refusal tests](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-test-the-checks/) show the two ways it stops instead: a FIT signed with `key-b` fails at `Failed to verify required signature 'key-key-a'`, and a FIT with one byte changed after signing fails at `Bad hash value for 'hash-1'`. Zephyr never starts in either case.

Below that link, nothing is checked against your key. Most Cortex-A SoCs hold the customer's key in eFuses, one-time-programmable bits in silicon. Until that key is fused, the SoC is in its development state: the ROM and the vendor's firmware still check the boot files, but any key passes. TI calls the two states HS-FS (High Security, Field Securable) and HS-SE (High Security, Security Enforced), and U-Boot's banner on the EVM read `SoC:   AM62LX SR1.1 HS-FS`. In QEMU there is less still: no ROM, no security firmware and no eFuses, and you hand `u-boot.bin` to the machine on the command line.

So the key that matters, the public half of `key-a`, travels inside `u-boot.img` on an unprotected FAT partition, where anyone who can write the boot media can swap it for their own. Your chain of trust starts on the card, not in the silicon. Moving it there is what the rest of this page is about.

## What production needs

### Fuse your key and move to the production state

On TI devices the procedure is the keywriter, which burns your key into the eFuses and moves the chip to HS-SE; you then re-sign `tiboot3.bin`, `tispl.bin` and `u-boot.img` with that key. From then on the ROM and the security firmware refuse any boot file that isn't signed with your key, U-Boot included, so the `key-a` public half inside it is itself authenticated. The procedure is vendor-specific and out of scope here.

### Keep the environment built in

`bootcmd` holds the command autoboot runs, and `preboot` holds the one that defined `zboot`, `a`, `b` and `t`. Both builds end up with `CONFIG_ENV_IS_NOWHERE=y`, the AM62L from its defconfig and QEMU from the target block you added, so `saveenv` has nowhere to write and both variables always come from the binary you built. Check your board's `.config` for the same line, and keep it that way: a writable environment is a writable boot command.

{{% notice Warning %}}
Don't enable `CONFIG_ENV_IS_IN_FAT`, a development convenience that stores the environment in `uboot.env` on the boot media: a saved environment overrides `bootcmd` and `preboot`, so anyone with the card can skip the check.
{{% /notice %}}

### Lock the console

With `CONFIG_BOOTDELAY=3`, anyone with a serial cable can stop the countdown, get the `=>` prompt and type `fatload` and `go` by hand. Set `CONFIG_BOOTDELAY=-2` (no delay, no key check), or use `CONFIG_AUTOBOOT_KEYED` so that only a known string stops autoboot. Both settings only cover the countdown: if `bootcmd` returns, for example after a refused image, U-Boot still drops to the `=>` prompt. On a production build, end `zboot` with `reset` after the `echo`, so a refusal restarts the board instead of opening a prompt.

### Use real keys and sign in a release step

`sha256,rsa2048` is fine for a demo; the AM62L's own boot chain uses `sha512,rsa4096`. To match it, generate the keys with `rsa_keygen_bits:4096`, set `algo = "sha512,rsa4096"` in `zephyr-a.its` and `key.its`, and check that `$UBOOT_OUT/.config` has `CONFIG_SHA512=y`, adding it to the `.config` fragment if it doesn't. Generate the production key on a hardware security module (HSM), or at least off the build host, and sign in the release pipeline, the only place that holds the private key.

## Take it to another Cortex-A board

Every target-specific value sits in the `# Target values` block of your environment file and the paths under it, so porting is a checklist:

- `BOARD` is the Zephyr board identifier, from `west boards` or the Workbench board list. The board needs the two settings from [Build a Zephyr image that U-Boot can start](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/3-build-zephyr/): the Non-secure world and the arm64 image header.
- `ZEPHYR_ADDR` is the start of the memory node that the board's device tree selects as `zephyr,sram`. It is Zephyr's link address, the FIT `load` and `entry`, and the `go` target, so one value serves all three.
- `FIT_ADDR` is any free address clear of `ZEPHYR_ADDR` and of the firmware regions; otherwise `bootm loados` copies Zephyr over the FIT it is still reading.
- `BOOT_DEV` is the U-Boot device and partition that hold the files. `mmc 1:1` is the SD card's first partition on the AM62L EVM, while `mmc 0` is the eMMC; `mmc list` at the U-Boot prompt shows your board's numbering.
- `UBOOT_DEFCONFIG` is the board's U-Boot configuration. It must enable `CONFIG_FIT`, `CONFIG_FIT_SIGNATURE` and `CONFIG_RSA`: add any that is missing as `CONFIG_<NAME>=y` to the `.config` fragment in [Build U-Boot with the public key and a boot command that fails closed](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/), and if the board has `CONFIG_LEGACY_IMAGE_FORMAT=y`, add `# CONFIG_LEGACY_IMAGE_FORMAT is not set` too.
- `UBOOT_SRC`, `CROSS` and `UBOOT_CC` point at the U-Boot source and the compiler that builds it, with `SDK`, `PREBUILT` and `SYSROOT` added when they come from a vendor SDK, as on the AM62L.
- `BOOT_IMG` is the boot volume `mcopy` writes into: the card image on the EVM, the disk image in QEMU, each with the `@@` offset of its FAT partition.

Two things sit outside the environment file. The `make` line that builds U-Boot takes whatever the target's tree expects: `BL1`, `BL31`, `TEE` and `BINMAN_INDIRS` on the AM62L, `EXT_DTB` in QEMU, and the tree names its own outputs, often `u-boot.img` or `u-boot.itb` plus an SPL file. The boot page follows the target's own media, switches and console.

The last difference is how the key reaches the control device tree. `CONFIG_DEVICE_TREE_INCLUDES` works on any board that builds that tree from source (`CONFIG_OF_SEPARATE=y` or `CONFIG_OF_EMBED=y`), as the AM62L does. A board that takes its device tree from a prior stage (`CONFIG_OF_BOARD=y`) has no tree of its own to add a node to; the QEMU option shows the way around it, merging `signature.dtsi` into a dump of that tree and building with `EXT_DTB=`.

Everything else stays the same: the `.its` file, the keys, the `signature.dtsi` recipe, the boot command and the three test images.

## Where to go from here

To run your own application, point `data` in `zephyr-a.its` at its `zephyr.bin` and sign it again; nothing else in the chain changes. To move to another Cortex-A board, work through the checklist above.

The next page lists the further reading, including U-Boot's FIT signature documentation and the board pages for both targets. Ac6, where this Learning Path was written, runs courses on [Zephyr RTOS programming](https://www.ac6-training.com/en/rt5/zephyr-rtos-programming) and on [building a secured embedded Linux platform](https://www.ac6-training.com/en/sec8/secured-embedded-linux-platform-build), which covers the fusing and release-signing steps above.
