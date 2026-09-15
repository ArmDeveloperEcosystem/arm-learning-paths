---
title: Understand where Zephyr sits in the Cortex-A boot chain
description: Learn why Zephyr on a Cortex-A processor is a payload that U-Boot can verify, what a FIT image contains, and how the TI AM62L boot chain hands control to it.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Zephyr is the last stage, not the first

On a microcontroller (MCU), Zephyr starts at the reset vector and nothing runs before it, so secure boot on Cortex-M means adding a bootloader yourself, such as MCUboot. That bootloader is the root of trust.

A Cortex-A processor starts in a ROM (read-only memory) inside the SoC (system on chip), and several pieces of firmware run before your code does: your image is the last thing that runs, not the first.

That order makes verification possible: the stage before Zephyr can check it before starting it. On a Cortex-A board, that stage is usually U-Boot, the bootloader most Arm boards use.

A U-Boot host tool packs a program and its signature into a FIT (Flattened Image Tree) image, and U-Boot checks it. Signed FIT images are documented for Linux, and secure boot for Zephyr is documented for Cortex-M; this Learning Path covers the combination you ship, Zephyr signed on a Cortex-A, using the TI AM62L EVM (evaluation module). The FIT, the keys, the way the key goes into U-Boot and the boot command are generic, so you can move them to any Cortex-A board that runs U-Boot. The SDK, the SD card layout and the boot switches are specific to TI.

## The boot chain on a Cortex-A board

On an Armv8-A board with U-Boot, the boot chain is: the boot ROM in the SoC, then early firmware, then U-Boot, then the payload. The payload is what U-Boot loads from storage and starts: Linux on most boards, Zephyr here.

The early firmware is usually three things. The SPL (Secondary Program Loader) is a cut-down build of U-Boot whose only job is to load the full U-Boot. TF-A (Trusted Firmware-A) is Arm's reference firmware for the Secure world; it starts U-Boot in the Non-secure world. OP-TEE (Open Portable Trusted Execution Environment) is a trusted operating system that also lives in the Secure world.

You build the SPL as part of U-Boot on a later page. TF-A and OP-TEE come prebuilt in the TI SDK, as `bl1.bin`, `bl31.bin` and `bl32.bin`.

Each stage loads the next one into memory and jumps to it. Secure boot means each stage checks the next one before it jumps: it holds a public key and refuses to run anything that isn't signed by the matching private key. If one link skips the check, everything after that link runs unverified.

![Diagram of a generic Cortex-A boot chain in four boxes: the boot ROM, the vendor's early boot stages, U-Boot, and Zephyr inside a FIT image. The first two arrows are checked by the vendor's ROM and firmware; the last arrow, from U-Boot to Zephyr, is checked by U-Boot with your key and is the link this Learning Path adds.#center](images/boot-chain-generic.svg "A Cortex-A boot chain, and the link this Learning Path adds")

On the AM62L, the chain has four steps. TIFS (TI Foundational Security) is TI's security firmware; it checks the boot files that the ROM doesn't.

| Step | What loads what | Who checks it |
|---|---|---|
| 1 | The boot ROM loads `tiboot3.bin`, which holds the first stage of TF-A (BL1) and the TIFS firmware | The boot ROM |
| 2 | BL1 loads `tispl.bin`, which holds the TF-A runtime firmware (BL31), OP-TEE and the U-Boot SPL | TIFS |
| 3 | The SPL loads `u-boot.img`, which is U-Boot proper | TIFS |
| 4 | U-Boot loads the payload, normally a Linux FIT image | U-Boot's own FIT check |

TI's chip checks the first three files itself, and U-Boot checks the fourth, which is Zephyr here. You build `tiboot3.bin`, `tispl.bin` and `u-boot.img` when you [build U-Boot](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/) and copy them to the card when you [prepare the SD card](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/6-boot-the-board/).

![Diagram of the AM62L boot chain from the boot ROM through tiboot3.bin, tispl.bin and u-boot.img to the Zephyr FIT image. Under each file the diagram names who checks it: the ROM checks tiboot3.bin, TIFS checks tispl.bin and u-boot.img, and U-Boot checks the FIT signature before it starts Zephyr with go.#center](images/boot-chain.svg "The same chain on the AM62L, with TI's file names")

## What a FIT image is

A FIT is U-Boot's container format for boot images. It's a device tree blob (DTB) whose nodes hold images instead of hardware descriptions.

One FIT holds three things:

- The image itself, which is Zephyr's `zephyr.bin` here
- A hash of that image, so U-Boot can tell if a byte changed
- A configuration that names the image to use (`kernel = "kernel-1"`) and carries a signature

`mkimage`, a U-Boot host tool, builds the FIT from a text source file (a `.its` file) and signs it with your private key. On the board, U-Boot's `bootm` command parses the FIT, verifies the signature and the hash, and copies the image to its load address.

This Learning Path uses `sha256,rsa2048`: a SHA-256 hash of the data, signed with a 2048-bit RSA key. RSA is the public-key algorithm whose private half signs and public half verifies.

The public key lives inside U-Boot's own device tree, the control device tree, under a `/signature` node. That key node carries `required = "conf"`: every configuration in every FIT must carry a valid signature by this key, or U-Boot refuses to load it. Without `required`, a FIT with no signature at all still boots.

![Diagram of a signed FIT image next to U-Boot's control device tree. The FIT contains an images node with the Zephyr binary and its hash, and a configurations node with a signature. The control device tree contains a /signature node holding the public key with required set to conf. Arrows show the signature covering the configuration and the hash node, and the hash covering the image bytes.#center](images/fit-signature.svg "What the signature and the hash each cover in a FIT image")

The signature does not cover the image bytes: it covers the configuration node plus the hash node, and the hash covers the bytes. The optional page [Test that U-Boot refuses a wrong key and a tampered image](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-test-the-checks/) shows the difference.

## What this Learning Path adds

This Learning Path adds the last link of the chain: U-Boot verifies the Zephyr FIT and only then jumps to Zephyr with `go`, U-Boot's plain jump-to-an-address command. You don't change a line of U-Boot source: the public key and the boot command go in as Kconfig options. The page [Build U-Boot with the public key and a boot command that fails closed](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/) shows the boot command.

What this Learning Path doesn't do is put your key into the chip. TI devices hold the owner's key in eFuses, one-time-programmable bits in silicon. A chip with that key fused is HS-SE (High Security, Security Enforced): it refuses any boot file not signed with the owner's key. A chip without it yet is HS-FS (High Security, Field Securable): the check runs, but any key passes.

The EVM ships as HS-FS, and its first three boot files are signed with TI's development key, so those checks can't refuse anything. U-Boot's check of Zephyr refuses on HS-FS and HS-SE alike.

{{% notice Note %}}
Moving a device to HS-SE, fusing your own key and re-signing the boot files with it, is a separate TI procedure and out of scope here. The page [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/8-production/) lists what that step changes and what else production needs.
{{% /notice %}}

## What you've learned and what's next

Zephyr on a Cortex-A is the last stage of a boot chain, so U-Boot can verify it before starting it. A FIT holds the image, its hash and a signed configuration, and `required = "conf"` in U-Boot's control device tree makes U-Boot refuse anything it can't verify. On the AM62L EVM, only that last check is enforced today.

Next, you [set up the host tools and the TI SDK](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/2-set-up-tools/), and create the working directory and environment file that every later page uses.
