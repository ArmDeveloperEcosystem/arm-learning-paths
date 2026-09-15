---
title: Review what is verified and what production needs
description: Separate what the trusted boot proved, and what the optional refusal tests add, from what neither proved, then list the changes a production device needs before the whole chain can be trusted.
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What you've proved

Two pages gave you the evidence, and each proved a different thing.

The boot in [Prepare the SD card and boot the board](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/6-boot-the-board/) proved that Zephyr runs only after `bootm start` has verified the signature and the hash. The `## Starting application at 0x82000000` line came from `go`, and `go` sits behind `&&`, so it never runs unless `bootm start` says yes.

The [previous page](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-test-the-checks/), if you ran it, proved the two refusals: U-Boot rejects an image signed with a valid key it doesn't have, and it rejects an image changed after signing. All three images went through the same `zboot` command. `a`, `b` and `t` only set the file name, so the result depends on the signature and the hash, not on which of the three you typed.

Put together, the three runs give these results; the first row comes from the boot page and the other two from the test page:

| Command | Image | What is different | Result |
|---|---|---|---|
| `run a` | `zephyr-a.itb` | Signed with `key-a` | Zephyr starts |
| `run b` | `zephyr-b.itb` | Signed with `key-b`, a key U-Boot doesn't have | Refused: `Failed to verify required signature 'key-key-a'` |
| `run t` | `zephyr-tampered.itb` | Signed with `key-a`, one payload byte changed after signing | Refused: `Bad hash value for 'hash-1' hash node in 'kernel-1' image node` |

So on the AM62L EVM, Zephyr runs only if its FIT is signed by the key compiled into U-Boot, and any change to the image after signing is caught.

You did this without changing a line of U-Boot source. The public key went into the control device tree through `CONFIG_DEVICE_TREE_INCLUDES`, and the boot commands went in through `CONFIG_PREBOOT`. Both are build configuration, so you can carry them to a newer TI U-Boot without maintaining a patch.

Most of what you built is not tied to TI. The section *Take it to another Cortex-A board* on this page separates the generic parts from the board-specific ones.

## What you haven't proved

Each stage checks the next, so the whole chain is only as trustworthy as the stage that checked U-Boot. Your check lives in U-Boot; the question is who checked U-Boot.

TI K3 devices come in two security states, which you met in [Understand where Zephyr sits in the Cortex-A boot chain](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/1-boot-chain/). On an HS-SE device the customer's key is burned into eFuses, and the device refuses any boot file that isn't signed with it.

An HS-FS device is the same silicon before the key is burned. The check still runs, but there is no customer key to compare against, so a file signed with any key passes.

The EVM ships as HS-FS. The SPL banner told you so: `SoC:   AM62LX SR1.0 HS-FS`. TI signs `tiboot3.bin`, `tispl.bin` and `u-boot.img` with a development key that ships in the U-Boot source. On HS-FS, the ROM and TIFS accept it.

So the checks on `tiboot3.bin`, `tispl.bin` and `u-boot.img` run on your board, but they can't refuse anything. U-Boot enforces only the last link, U-Boot to Zephyr.

Why this matters: the public half of `key-a` lives inside `u-boot.img`, and `u-boot.img` sits on an unprotected FAT partition. Anyone who can write the card can replace `u-boot.img` with one that carries their own key, or a key node without the `required` property. So the root of trust, the key everything else is checked against, is in a file on the card, not yet in silicon.

## What production needs

Each of the following changes closes one gap left open by the demo setup.

### Fuse your key and move to HS-SE

TI's keywriter procedure burns your key into the eFuses, and you re-sign `tiboot3.bin`, `tispl.bin` and `u-boot.img` with it. From then on the ROM and TIFS refuse any `u-boot.img` that isn't signed with your key, so the `key-a` public half it carries is itself authenticated and the root of trust is in silicon. The procedure is TI-specific and out of scope here.

### Keep the environment built in

U-Boot's environment is its set of named variables. `bootcmd` holds the command autoboot runs, and `preboot` holds the one that defined `zboot`, `a`, `b` and `t`. `saveenv` writes the variables to storage. TI's configuration ends up with `CONFIG_ENV_IS_NOWHERE=y` (the default when no environment storage is chosen), so `saveenv` has nowhere to write and both variables always come from the binary you built. Keep it that way, because a writable environment is a writable boot command.

{{% notice Warning %}}
Don't enable `CONFIG_ENV_IS_IN_FAT` on a production build. It stores the environment in a `uboot.env` file on the boot media (the SD card with `CONFIG_ENV_FAT_DEVICE_AND_PART="1:1"`; TI's default `"0:1"` is the eMMC), and a saved environment overrides `bootcmd` and `preboot`. Anyone with the card can then set `bootcmd` to `fatload` and `go` and skip the check. It's a development convenience only.
{{% /notice %}}

### Lock the console

With `CONFIG_BOOTDELAY=3`, anyone with a serial cable can press a key during the countdown, get the `=>` prompt and type `fatload` and `go` by hand. Set `CONFIG_BOOTDELAY=-2` (autoboot with no delay and no check for a key press), or use `CONFIG_AUTOBOOT_KEYED` so that only a known string stops autoboot. Both settings only cover the countdown. If `bootcmd` returns, for example after a refused image, U-Boot still drops to the `=>` prompt. On a production build, end `zboot` with `reset` after the `echo`, so a refusal restarts the board instead of opening a prompt.

### Close the other boot paths

Every boot command compiled into U-Boot is one that someone at the prompt, or a boot script on the card, can run instead of `zboot`, and none of them goes through your check. TI's configuration turns on several:

| Path | Symbols | What it can do |
|---|---|---|
| Standard boot (bootstd, bootflow) | `CONFIG_BOOTSTD_FULL=y` | Scans storage for something to boot and starts it |
| EFI | `CONFIG_EFI_LOADER=y`, `CONFIG_CMD_BOOTEFI=y` | Starts an EFI application from the card |
| Raw kernel commands | `CONFIG_CMD_BOOTI=y`, `CONFIG_CMD_BOOTZ=y` | Starts a bare Linux kernel file with no FIT and no signature |
| Network and DFU (Device Firmware Upgrade) | `CONFIG_CMD_NET=y`, `CONFIG_CMD_DFU=y` | Loads an image over Ethernet or USB |

`CONFIG_LEGACY_IMAGE_FORMAT` is already off, which is right, because that older single-image format carries no signature. Audit the rest and turn off everything your product doesn't use.

### Use real keys and keep them off the build machine

`sha256,rsa2048` is fine for a demo. TI's own K3 flow uses `sha512,rsa4096`. To match it, change `rsa_keygen_bits:2048` to `rsa_keygen_bits:4096` in the `openssl genpkey` command from [Create signing keys and sign the Zephyr image into a FIT](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/4-sign-zephyr/), and `algo = "sha256,rsa2048"` to `algo = "sha512,rsa4096"` in `zephyr-a.its` and in the `key.its` carrier; the commands stay the same. Generate the production key on a hardware security module (HSM), or at least on a machine that isn't the build host. The `key-a` and `key-b` pairs you generated there in `$KEYS` are throwaway.

### Sign in a release step

Running `mkimage -k` on a developer machine is fine for `key-a`. For the production key, signing belongs in the release pipeline, the only place that holds the private key. No developer machine ever sees it.

## Take it to another Cortex-A board

The board-specific parts are few, and most of them sit on one line of the boot command. Three things change.

The first is the load address. `0x82000000` is the start of the memory node that the AM62L board device tree selects as `zephyr,sram`, so it is Zephyr's link address, the FIT `load` and `entry`, and the `go` target. On another board, take the start of that node from its device tree source (DTS) and use it in all three places. Load the FIT itself at a different address, as you did with `0x90000000`; otherwise `bootm loados` copies Zephyr over the FIT it is still reading.

The second is the storage device and partition in `fatload`. `mmc 1:1` means MMC device 1, partition 1: on the AM62L EVM that is the SD card's FAT partition, while `mmc 0` is the eMMC. On your board both numbers can differ.

The third is how the key reaches the control DTB. `CONFIG_DEVICE_TREE_INCLUDES` works on any board that builds its control DTB from source (`CONFIG_OF_SEPARATE=y` or `CONFIG_OF_EMBED=y`). Some boards take the DTB from a prior stage instead (`CONFIG_OF_BOARD`). On those, the `/signature` node has to go into that DTB, because that is the tree U-Boot reads keys from. `mkimage -K` writes the node into an existing DTB, and the same `key.its` carrier from the [U-Boot page](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/) gives it the key.

What doesn't change is the `.its` file apart from the addresses, the keys, and the `signature.dtsi` recipe. The shape of the boot command, `bootm start && bootm loados && ... go`, and the three test images also stay the same. U-Boot's FIT signature check is generic code, not board code, so it behaves the same everywhere.

## What you've accomplished

You can now say what your board verifies and what it doesn't, and you have a checklist of the changes between a working demo and a production device. The signing flow, the way the public key goes into U-Boot, and the boot command are generic. Point `data` in `zephyr-a.its` at your own application's `zephyr.bin`, sign it again with `mkimage`, and watch U-Boot refuse anything else. When you move to your own hardware, change the three board-specific items and keep the rest.

To go further with a trainer, Ac6 runs courses on [Zephyr RTOS programming](https://www.ac6-training.com/en/rt5/zephyr-rtos-programming) and on [building a secured embedded Linux platform](https://www.ac6-training.com/en/sec8/secured-embedded-linux-platform-build), which covers the U-Boot and TF-A side of this chain. There is also a course on [AI-assisted embedded development](https://www.ac6-training.com/en/ai1/ai-assisted-embedded-development).
