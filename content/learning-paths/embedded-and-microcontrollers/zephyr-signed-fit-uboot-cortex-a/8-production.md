---
title: Review the Zephyr FIT verification boundary and production needs
description: Review the trust boundary for Zephyr FIT verification in U-Boot and the key provisioning, boot controls, and release signing needed for production.
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the verification boundary

You've configured U-Boot to verify the Zephyr payload, the last link in the boot chain. U-Boot reads `zephyr-a.itb` and verifies `conf-1` with the embedded public key for `key-a`. It checks the payload hash before jumping to `ZEPHYR_ADDR`.

If you ran the optional [refusal tests](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-test-the-checks/), you also confirmed two rejection cases. The wrong-key Flattened Image Tree (FIT) fails with `Failed to verify required signature 'key-key-a'`. The modified payload fails with `Bad hash value for 'hash-1'`. Neither starts Zephyr.

The earlier stages aren't authenticated against your key in either setup. QEMU loads `u-boot.bin` directly, without a boot ROM, security firmware, or eFuses to authenticate it.

The AM62L evaluation module (EVM) has those earlier stages, but you've left it in TI's High Security, Field Securable (HS-FS) development state. In this state, the ROM and vendor firmware check boot files but accept any signing key. The U-Boot banner identifies it as `SoC:   AM62LX SR1.1 HS-FS`. Provisioning your key into the one-time-programmable eFuses moves the device to High Security, Security Enforced (HS-SE).

On the EVM, the trusted public key is inside `u-boot.img` on an unprotected File Allocation Table (FAT) partition. Anyone who can replace that file can replace the key and boot command. Production needs an authenticated U-Boot and controls that prevent bypassing its verification step.

## What you need for production

For production, ensure that you complete the following steps:

### Fuse your key and move to the production state

TI's one-time-programmable (OTP) Keywriter tool, called Keywriter Lite on the AM62L, burns the public-key hash into the eFuses and moves the chip to HS-SE. You then re-sign `tiboot3.bin`, `tispl.bin`, and `u-boot.img` with that key.

The ROM and security firmware then require boot files signed with your key, including U-Boot. This authenticates the U-Boot image containing the FIT public key. Key provisioning is vendor-specific and isn't covered in these steps.

### Keep the environment built in

`bootcmd` selects the autoboot command. `preboot` defines `zboot` and the `a`, `b`, and `t` wrappers before autoboot starts.

Both builds use `CONFIG_ENV_IS_NOWHERE=y`: you added it for QEMU, and the AM62L default configuration supplies it. This prevents `saveenv` from writing a persistent environment, so boot settings are loaded from the binary that you built. Check that the `.config` for your board includes the same setting.

{{% notice Warning %}}
Don't enable `CONFIG_ENV_IS_IN_FAT` for this boot configuration. It stores the environment in `uboot.env` on the boot media. A saved environment can override `bootcmd` and `preboot`, allowing someone with write access to the card to bypass verification.
{{% /notice %}}

### Lock the console

With `CONFIG_BOOTDELAY=3`, someone with serial-console access can interrupt autoboot and run `fatload` and `go` without verification. Set `CONFIG_BOOTDELAY=-2` to remove the delay and keyboard check, or use `CONFIG_AUTOBOOT_KEYED` to require a known string to interrupt autoboot.

These settings cover only the countdown. If `bootcmd` returns after rejecting an image, U-Boot still opens the `=>` prompt. In a production build, add `reset` after the refusal `echo` in `zboot`. This ensures that a failed boot restarts the board instead of opening the console.

### Protect production keys and sign during release

You used `sha256,rsa2048`. The boot chain of the AM62L uses `sha512,rsa4096`. To use the latter for your FIT:

- Generate keys with `rsa_keygen_bits:4096`.
- Set `algo = "sha512,rsa4096"` in both `zephyr-a.its` and `key.its`.
- Confirm that `$UBOOT_OUT/.config` includes `CONFIG_SHA512=y`, adding it to the configuration fragment if needed.

Generate production keys in a hardware security module (HSM), or at least away from the build host. Sign during the release process and restrict private-key access to that process.

## Adapt the workflow to another Cortex-A board

If you want to use another Cortex-A board, start by updating the target values and paths in your environment file:

- `BOARD` is the Zephyr board identifier, from `west boards` or the Workbench board list. The board needs the two settings from [Build a Zephyr image that U-Boot can start](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/3-build-zephyr/): the Non-secure world and the arm64 image header.
- `ZEPHYR_ADDR` is the start of the memory node that the device tree of the board selects as `zephyr,sram`. It's the link address of Zephyr, the FIT `load` and `entry`, and the `go` target, so one value serves all three.
- `FIT_ADDR` is any free address clear of `ZEPHYR_ADDR` and of the firmware regions. Otherwise, `bootm loados` copies Zephyr over the FIT it's still reading.
- `BOOT_DEV` is the U-Boot device and partition that hold the files. `mmc 1:1` is the first partition of the SD card on the AM62L EVM, while `mmc 0` is the eMMC. `mmc list` at the U-Boot prompt shows the numbering of your board.
- `UBOOT_DEFCONFIG` selects the U-Boot default configuration of the board. Check for `CONFIG_FIT=y`, `CONFIG_FIT_SIGNATURE=y`, and `CONFIG_RSA=y`. Add missing settings to the [U-Boot configuration fragment](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/). Disable legacy images with `# CONFIG_LEGACY_IMAGE_FORMAT is not set`.
- `UBOOT_SRC`, `CROSS`, and `UBOOT_CC` point at the U-Boot source and the compiler that builds it. `SDK`, `PREBUILT`, and `SYSROOT` are added when they come from a vendor SDK, as on the AM62L.
- `BOOT_IMG` is the boot volume that `mcopy` writes into: the card image on the EVM, the disk image in QEMU, each with the `@@` offset of its FAT partition.

Also adapt the U-Boot build command and boot-media preparation. The build inputs depend on the target: `EXT_DTB` for QEMU, or `BL1`, `BL31`, `TEE`, and `BINMAN_INDIRS` for the AM62L EVM. Output names also vary, often including `u-boot.img` or `u-boot.itb` and a Secondary Program Loader (SPL) file. Follow the requirements of the target for media layout, boot switches, and console access.

Check how the target obtains its control device tree. `CONFIG_DEVICE_TREE_INCLUDES` adds the key node when the tree is built from source with `CONFIG_OF_SEPARATE=y` or `CONFIG_OF_EMBED=y`, as on the AM62L EVM.

For a board using a tree from a prior stage (`CONFIG_OF_BOARD=y`), follow the QEMU approach: merge `signature.dtsi` into an exported tree and pass it to the build with `EXT_DTB=`.

Reuse the FIT signing and verification workflow, adapting the target values in the FIT source and boot command as needed.

## What you've accomplished

You've established verification of the Zephyr payload and learned how you can extend the workflow to production and to another Cortex-A board. 

Before using this approach in production, authenticate the earlier boot stages. Also protect the boot environment and console and move signing into a controlled release process.

To sign your own application for the same target, point `data` in `zephyr-a.its` to its `zephyr.bin` and sign the FIT again. To use another Cortex-A board, adapt the environment, build inputs, and boot media using the checklist in this section.
