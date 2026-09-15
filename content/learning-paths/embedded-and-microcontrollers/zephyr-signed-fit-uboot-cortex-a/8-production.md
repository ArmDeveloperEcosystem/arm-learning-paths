---
title: Review what is verified and what production needs
description: Separate what the boot and the optional refusal tests proved from what they didn't, then list what a production device needs before the whole chain can be trusted.
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you've proved

The boot in [Prepare the SD card and boot the board](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/6-boot-the-board/) proved that Zephyr runs only after `bootm start` has verified the signature and the hash. The `## Starting application at 0x82000000` line came from `go`, which sits behind `&&` and so never runs unless `bootm start` says yes.

The [previous page](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-test-the-checks/), if you ran it, proved the two refusals: U-Boot rejects an image signed with a key it doesn't have, and it rejects an image changed after signing.

The three runs give these results:

| Command | Image | What is different | Result |
|---|---|---|---|
| `run a` | `zephyr-a.itb` | Signed with `key-a` | Zephyr starts |
| `run b` | `zephyr-b.itb` | Signed with `key-b`, a key U-Boot doesn't have | Refused: `Failed to verify required signature 'key-key-a'` |
| `run t` | `zephyr-tampered.itb` | Signed with `key-a`, one payload byte changed after signing | Refused: `Bad hash value for 'hash-1' hash node in 'kernel-1' image node` |

You did this without changing a line of U-Boot source: the public key went in through `CONFIG_DEVICE_TREE_INCLUDES` and the boot commands through `CONFIG_PREBOOT`, so both carry to a newer U-Boot without a patch.

## What you haven't proved

Each stage checks the next, so the chain is only as trustworthy as the stage that checked U-Boot.

Most Cortex-A SoCs have the two security states you met in [Understand where Zephyr sits in the Cortex-A boot chain](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/1-boot-chain/): the production state, with the customer's key in eFuses, and the development state, where any key passes. The SPL banner told you this EVM is in the development state, HS-FS in TI's words: `SoC:   AM62LX SR1.0 HS-FS`. On the AM62L EVM, TI's development key signs the three boot files, so the ROM and security-firmware checks run but can't refuse anything, and U-Boot enforces only the last link, U-Boot to Zephyr.

The public half of `key-a` lives inside `u-boot.img`, on an unprotected FAT partition, so anyone who can write the card can replace it with one that carries their own key. The root of trust is in a file on the card, not in silicon.

## What production needs

### Fuse your key and move to the production state

On TI devices the procedure is the keywriter, which burns your key into the eFuses and moves the chip to HS-SE, TI's name for the production state; you then re-sign `tiboot3.bin`, `tispl.bin` and `u-boot.img` with that key. From then on the ROM and the security firmware refuse any boot file that isn't signed with your key, U-Boot included, so the `key-a` public half inside it is itself authenticated. The procedure is vendor-specific and out of scope here.

### Keep the environment built in

`bootcmd` holds the command autoboot runs, and `preboot` holds the one that defined `zboot`, `a`, `b` and `t`. The AM62L configuration ends up with `CONFIG_ENV_IS_NOWHERE=y`, so `saveenv` has nowhere to write and both variables always come from the binary you built. Keep it that way: a writable environment is a writable boot command.

{{% notice Warning %}}
Don't enable `CONFIG_ENV_IS_IN_FAT`, a development convenience that stores the environment in `uboot.env` on the boot media: a saved environment overrides `bootcmd` and `preboot`, so anyone with the card can skip the check.
{{% /notice %}}

### Lock the console

With `CONFIG_BOOTDELAY=3`, anyone with a serial cable can stop the countdown, get the `=>` prompt and type `fatload` and `go` by hand. Set `CONFIG_BOOTDELAY=-2` (no delay, no key check), or use `CONFIG_AUTOBOOT_KEYED` so that only a known string stops autoboot. Both settings only cover the countdown: if `bootcmd` returns, for example after a refused image, U-Boot still drops to the `=>` prompt. On a production build, end `zboot` with `reset` after the `echo`, so a refusal restarts the board instead of opening a prompt.

### Close the other boot paths

Any other boot command compiled into U-Boot can be run instead of `zboot`, and none of them goes through your check. The AM62L configuration turns on several, and most vendor defconfigs do the same:

| Path | Symbols | What it can do |
|---|---|---|
| Standard boot (bootstd, bootflow) | `CONFIG_BOOTSTD=y` (and `CONFIG_BOOTSTD_FULL=y`) | Scans storage for something to boot and starts it |
| EFI | `CONFIG_EFI_LOADER=y`, `CONFIG_CMD_BOOTEFI=y` | Starts an EFI application from the card |
| Raw kernel commands | `CONFIG_CMD_BOOTI=y`, `CONFIG_CMD_BOOTZ=y` | Starts a bare Linux kernel file with no FIT and no signature |
| Network and DFU (Device Firmware Upgrade) | `CONFIG_CMD_NET=y`, `CONFIG_CMD_DFU=y` | Loads an image over Ethernet or USB |

`CONFIG_LEGACY_IMAGE_FORMAT` is already off; keep it off, because that older format carries no signature. Audit the rest and turn off everything your product doesn't use.

### Use real keys and keep them off the build machine

`sha256,rsa2048` is fine for a demo. The AM62L's own boot chain uses `sha512,rsa4096`. To match it, change `rsa_keygen_bits:2048` to `rsa_keygen_bits:4096` in the `openssl genpkey` command from [Create signing keys and sign the Zephyr image into a FIT](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/4-sign-zephyr/), and `algo = "sha256,rsa2048"` to `algo = "sha512,rsa4096"` in `zephyr-a.its` and in the `key.its` carrier; the commands stay the same. Check that `$UBOOT_OUT/.config` has `CONFIG_SHA512=y`: the AM62L configuration turns it on, and another board may need it in the fragment you append. Generate the production key on a hardware security module (HSM), or at least on a machine that isn't the build host.

### Sign in a release step

Running `mkimage -k` on a developer machine is fine for `key-a`. For the production key, signing belongs in the release pipeline, the only place that holds the private key.

## Take it to another Cortex-A board

Every board-specific value sits in the first two blocks of `env.sh`, so porting is a checklist:

- `BOARD` is the Zephyr board identifier, from `west boards` or the Workbench board list. The board needs the two settings from [Build a Zephyr image that U-Boot can start](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/3-build-zephyr/): the Non-secure world and the arm64 image header.
- `ZEPHYR_ADDR` is the start of the memory node that the board's device tree selects as `zephyr,sram`. It is Zephyr's link address, the FIT `load` and `entry`, and the `go` target, so one value serves all three.
- `FIT_ADDR` is any free address clear of `ZEPHYR_ADDR` and of the firmware regions; otherwise `bootm loados` copies Zephyr over the FIT it is still reading.
- `BOOT_DEV` is the U-Boot device and partition that hold the files. `mmc 1:1` is the SD card's first partition on the AM62L EVM, while `mmc 0` is the eMMC; `mmc list` at the U-Boot prompt shows your board's numbering.
- `UBOOT_DEFCONFIG` is the board's U-Boot configuration.
- `SDK`, `UBOOT_SRC`, `PREBUILT`, `CROSS` and `SYSROOT`, the second block, point at the vendor's SDK: its U-Boot source, early firmware, cross compiler and the compiler's sysroot.

Two things sit outside `env.sh`. The `make` line that builds U-Boot takes whatever the vendor's tree expects for its early stages, `BL1`, `BL31`, `TEE` and `BINMAN_INDIRS` on the AM62L, and the SD card page follows the vendor's card layout, switches and console.

The last difference is how the key reaches the control DTB. `CONFIG_DEVICE_TREE_INCLUDES` works on any board that builds its control DTB from source (`CONFIG_OF_SEPARATE=y` or `CONFIG_OF_EMBED=y`). Boards that take the DTB from a prior stage (`CONFIG_OF_BOARD`) need the `/signature` node in that DTB instead, because that is the tree U-Boot reads keys from. `mkimage -K` writes the node into an existing DTB, and the same throwaway `key.its` from [Build U-Boot with the public key and a boot command that fails closed](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/) gives it the key.

Everything else stays the same: the `.its` file, the keys, the `signature.dtsi` recipe, the boot command and the three test images.

## What you've accomplished

You can now say what your board verifies and what it doesn't, and you have a checklist for a production device. Point `data` in `zephyr-a.its` at your own application's `zephyr.bin`, sign it again with `mkimage`, and watch U-Boot refuse anything else. When you move to your own hardware, change the board block in `env.sh` and keep the rest.

Ac6 runs courses on [Zephyr RTOS programming](https://www.ac6-training.com/en/rt5/zephyr-rtos-programming), on [building a secured embedded Linux platform](https://www.ac6-training.com/en/sec8/secured-embedded-linux-platform-build), and on [AI-assisted embedded development](https://www.ac6-training.com/en/ai1/ai-assisted-embedded-development).
