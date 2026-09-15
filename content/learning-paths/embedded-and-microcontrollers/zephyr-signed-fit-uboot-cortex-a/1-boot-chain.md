---
title: Understand where Zephyr sits in the Cortex-A boot chain
description: Learn why Zephyr on a Cortex-A processor is a payload that U-Boot can verify, what a FIT image contains, and how the TI AM62L boot chain hands control to it.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Zephyr is the last stage, not the first

On a microcontroller (MCU), Zephyr starts at the reset vector and nothing runs before it. There is no earlier stage that could check it. That's why secure boot on Cortex-M means adding a bootloader yourself, such as MCUboot. That bootloader is the root of trust: the first code you trust because nothing checked it.

A Cortex-A processor boots differently. The processor starts in a ROM (read-only memory) inside the SoC (system on chip), and several pieces of firmware run before your code does. On an MCU, your image is the first thing that runs. On a Cortex-A, it is the last.

That order is what makes verification possible. The stage that runs before Zephyr can check Zephyr before it starts it. On a Cortex-A board, that stage is usually U-Boot, the open-source bootloader that many Arm boards use to load an operating system from storage and start it.

U-Boot packs a program and its signature into a FIT (Flattened Image Tree) image; a later section on this page explains what one contains. Everyone documents signed FIT for Linux, and secure boot for Zephyr on Cortex-M. Nobody documents the one you actually need: Zephyr, signed, on a Cortex-A. This Learning Path covers that combination on real hardware, the TI AM62L EVM (TI's evaluation board for the AM62L). The FIT, the keys, the way the key goes into U-Boot and the boot command are generic, so you can move them to any Cortex-A board that runs U-Boot. The SDK, the SD card layout and the boot switches are specific to TI.

## The boot chain on a Cortex-A board

A boot chain is the list of programs that run one after the other, from power-on to your application. On an Armv8-A board with U-Boot, the chain is: the boot ROM in the SoC, then early firmware, then U-Boot, then the payload. The payload is the program U-Boot loads from storage and starts; on most boards that's Linux, and here it's Zephyr.

The early firmware is usually three things. The SPL (Secondary Program Loader) is a cut-down build of U-Boot whose only job is to load the full U-Boot. TF-A (Trusted Firmware-A) is Arm's reference firmware for the Secure world. On a Cortex-A, TrustZone splits the processor into a Secure world and a Non-secure world; TF-A owns the Secure one and starts U-Boot in the Non-secure one. OP-TEE (Open Portable Trusted Execution Environment) is an open-source trusted operating system that also lives in the Secure world.

You build the SPL as part of U-Boot on a later page. TF-A and OP-TEE come prebuilt in the TI SDK, as `bl1.bin`, `bl31.bin` and `bl32.bin`.

Each stage loads the next one into memory and jumps to it. Secure boot means each stage checks the next one before it jumps. A check is a signature verification: the stage holds a public key, and it refuses to run anything that isn't signed by the matching private key. If one link skips the check, everything after that link runs unverified.

On the AM62L, which has only Cortex-A53 cores, the chain that TI's U-Boot documentation for the K3 family describes has four steps. One TI name appears in it: TIFS (TI Foundational Security) is TI's security firmware, and it checks the boot files that the ROM doesn't. The four steps are:

| Step | What loads what | Who checks it |
|---|---|---|
| 1 | The boot ROM loads `tiboot3.bin`, which holds the first stage of TF-A (BL1) and the TIFS firmware | The boot ROM |
| 2 | BL1 loads `tispl.bin`, which holds the TF-A runtime firmware (BL31), OP-TEE and the U-Boot SPL | TIFS |
| 3 | The SPL loads `u-boot.img`, which is U-Boot proper | TIFS |
| 4 | U-Boot loads the payload, normally a Linux FIT image | U-Boot's own FIT check |

In plain words: TI's chip checks the first three files itself, and U-Boot checks the fourth. That fourth check is the one you set up, and Zephyr is the file it checks. You build `tiboot3.bin`, `tispl.bin` and `u-boot.img` when you [build U-Boot](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/) and copy them to the card when you [prepare the SD card](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/6-boot-the-board/).

![Diagram of the AM62L boot chain from the boot ROM through tiboot3.bin, tispl.bin and u-boot.img to the Zephyr FIT image, with an arrow at each step showing which stage checks the next one. Notice that the last arrow, from U-Boot to Zephyr, is the check this Learning Path adds.#center](images/boot-chain.svg "The AM62L boot chain and the check at each step")

## What a FIT image is

A FIT is U-Boot's container format for boot images. It's a device tree blob (DTB), the same binary format as a hardware device tree, but its nodes hold images instead of hardware descriptions.

One FIT holds three things:

- The image itself, which is Zephyr's `zephyr.bin` here
- A hash of that image, so U-Boot can tell if a byte changed
- A configuration that names the image to use and carries a signature

The configuration is the node U-Boot boots from: it names the image (`kernel = "kernel-1"`) and carries the signature.

`mkimage`, a U-Boot host tool, builds the FIT from a text source file (a `.its` file) and signs it with your private key. On the board, U-Boot's `bootm` command, the command that boots an image already in memory, parses the FIT, verifies the signature and the hash, and copies the image to its load address.

The signature uses RSA (Rivest-Shamir-Adleman), the public and private key pair described earlier. This Learning Path uses `sha256,rsa2048`: a SHA-256 hash of the data, signed with a 2048-bit RSA key.

The public key lives inside U-Boot's own device tree, called the control device tree, under a `/signature` node, with one subnode per key. One property of that key node matters most: `required = "conf"`, where `conf` is short for configuration. It means every configuration in every FIT must carry a valid signature by this key, or U-Boot refuses to load it. That property is what makes the check fail closed: when U-Boot can't verify a FIT, nothing boots. Without `required`, the check fails open: a FIT with no signature at all still boots, as if no check existed.

![Diagram of a signed FIT image next to U-Boot's control device tree. The FIT contains an images node with the Zephyr binary and its hash, and a configurations node with a signature. The control device tree contains a /signature node holding the public key with required set to conf. Arrows show the signature covering the configuration and the hash node, and the hash covering the image bytes.#center](images/fit-signature.svg "What the signature and the hash each cover in a FIT image")

The diagram shows one detail that matters later. The signature does not cover the bytes; it covers the hash of the bytes. `mkimage` signs the configuration node plus the hash node of each image the configuration lists. The hash node covers the image bytes. The signature is what makes that hash trustworthy, so between them they cover everything. So if someone flips a byte in the image after signing, the signature still verifies, and the hash check is what fails. You'll see exactly that on the board when you boot a tampered image.

## What this Learning Path adds

What this Learning Path adds is the last link of the chain: U-Boot verifies the Zephyr FIT and only then jumps to Zephyr with `go`, U-Boot's plain jump-to-an-address command. You don't change a line of U-Boot source. Both the public key and the boot command go in as Kconfig options when you build U-Boot, so you can carry them to a newer U-Boot without a patch. U-Boot's job here is to check Zephyr, not to boot an operating system; the page [Build U-Boot with the public key and a boot command that fails closed](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/) shows how the boot command does that.

What this Learning Path doesn't do is put your key into the chip. TI devices hold the owner's key in eFuses, one-time-programmable bits in silicon. A chip with that key fused is called HS-SE (High Security, Security Enforced): it refuses any boot file not signed with the owner's key. A chip without it yet is HS-FS (High Security, Field Securable): the check still runs, but with no key to compare against, any key passes.

The EVM ships as HS-FS, and its first three boot files are signed with TI's development key. So on this board the first three checks run but can't refuse anything, while the fourth, U-Boot checking Zephyr, refuses on HS-FS and HS-SE alike. You see the device type on the serial console when you boot the board.

{{% notice Note %}}
Moving a device to HS-SE, fusing your own key and re-signing the boot files with it, is a separate TI procedure and out of scope here. The page [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/7-production/) lists what that step changes and what else production needs.
{{% /notice %}}

## What you've learned and what's next

You've now learned that Zephyr on a Cortex-A is the last stage of a boot chain, so the stage before it, U-Boot, can verify it. A FIT is a device tree blob holding the image, its hash and a signed configuration. U-Boot keeps the public key in its control device tree, and `required = "conf"` makes it refuse anything it can't verify. On the AM62L EVM, only that last check is enforced today.

Next, you [set up the host tools and the TI SDK](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/2-set-up-tools/), and create the working directory and environment file that every later page uses.
