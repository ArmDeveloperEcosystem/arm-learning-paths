---
title: Understand where Zephyr sits in the Cortex-A boot chain
description: Learn why Zephyr on a Cortex-A processor is a payload that U-Boot can verify, what a FIT image contains, and how a Cortex-A boot chain hands control to it, with the TI AM62L EVM as the example.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Zephyr is the last stage, not the first

On a microcontroller (MCU), Zephyr runs first, so secure boot means adding a bootloader such as MCUboot. A Cortex-A processor starts in a ROM (read-only memory) inside the SoC (system on chip), and several firmware stages run before your code. Zephyr is the last stage, so the stage before it, usually U-Boot, can check it before starting it.

U-Boot checks images packed with their signature into a FIT (Flattened Image Tree). Signed FIT images are documented for Linux, and secure boot for Zephyr is documented for Cortex-M; this Learning Path covers Zephyr signed on a Cortex-A.

Everything except the board setup works on any Cortex-A board that runs U-Boot. The example board is the TI AM62L EVM (evaluation module); its SDK, SD card layout and boot switches sit in marked sections.

## The boot chain on a Cortex-A board

On an Armv8-A board with U-Boot, the boot chain is: the boot ROM in the SoC, then early firmware, then U-Boot, then the payload. The payload is what U-Boot loads from storage and starts: Linux on most boards, Zephyr here.

The early firmware is usually the SPL (Secondary Program Loader), a small U-Boot that loads the full one, plus TF-A (Trusted Firmware-A) and OP-TEE (Open Portable Trusted Execution Environment), which run in the Secure world. Many SoCs add the vendor's own security firmware, which checks the later stages. You build the SPL with U-Boot; the rest comes prebuilt in the vendor's SDK.

![Diagram of a generic Cortex-A boot chain in four boxes: the boot ROM, the vendor's early boot stages, U-Boot, and Zephyr inside a FIT image. A grey bracket over the early boot stages and U-Boot says the silicon vendor's ROM and firmware check them, against your fused key or, before fusing, with any key passing. A blue bracket over Zephyr says U-Boot checks it with your key, the link this Learning Path adds. Under each checked box the diagram names who checks it: the ROM, the firmware, and U-Boot, which then starts Zephyr with go.#center](images/boot-chain-generic.svg "A Cortex-A boot chain, and the link this Learning Path adds")

### The same chain on the AM62L EVM

On the AM62L, the early stages are two files. `tiboot3.bin` holds TF-A's first stage and TIFS (TI Foundational Security), TI's security firmware; `tispl.bin` holds the rest of TF-A, OP-TEE and the SPL. You build them together with `u-boot.img` when you [build U-Boot](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/5-build-uboot/). The EVM ships as HS-FS, TI's name for the development state described below.

![Diagram of the AM62L boot chain from the boot ROM through tiboot3.bin, tispl.bin and u-boot.img to the Zephyr FIT image. A grey bracket over the three TI files says TI's ROM and TIFS check them, and that on an HS-FS device such as this EVM any key passes. A blue bracket over the FIT says U-Boot checks it with your key. Under each file the diagram names who checks it: the ROM checks tiboot3.bin, TIFS checks tispl.bin and u-boot.img, and U-Boot checks the FIT signature before it starts Zephyr with go.#center](images/boot-chain.svg "The same chain on the AM62L, with TI's file names")

## What a FIT image is

A FIT is U-Boot's container format for boot images. It's a device tree blob (DTB) whose nodes hold images instead of hardware descriptions.

One FIT holds three things:

- The image itself, which is Zephyr's `zephyr.bin` here
- A hash of that image, so U-Boot can tell if a byte changed
- A configuration that names the image to use (`kernel = "kernel-1"`) and carries a signature

`mkimage`, a U-Boot host tool, builds the FIT from a text source file (a `.its` file) and signs it with your private key. On the board, U-Boot's `bootm` command parses the FIT, verifies the signature and the hash, and copies the image to its load address.

This Learning Path uses `sha256,rsa2048`: a SHA-256 hash of the data, signed with a 2048-bit RSA key.

The public key lives inside U-Boot's own device tree, the control device tree, under a `/signature` node. That key node carries `required = "conf"`: every configuration in every FIT must carry a valid signature by this key, or U-Boot refuses to load it. Without `required`, a FIT with no signature at all still boots.

![Diagram of a signed FIT image next to U-Boot's control device tree. The FIT contains an images node with the Zephyr binary and its hash, and a configurations node with a signature. The control device tree contains a /signature node holding the public key with required set to conf. Arrows show the signature covering the configuration and the hash node, and the hash covering the image bytes.#center](images/fit-signature.svg "What the signature and the hash each cover in a FIT image")

The signature does not cover the image bytes: it covers the configuration node plus the hash node, and the hash covers the bytes.

## What this Learning Path adds

This Learning Path adds the last link of the chain: U-Boot verifies the Zephyr FIT and only then jumps to Zephyr with `go`, U-Boot's plain jump-to-an-address command.

This Learning Path doesn't fuse your key into the chip, so the SoC stays in its development state, where the ROM and the vendor's firmware accept boot files signed with any key; U-Boot's check of Zephyr is enforced either way. [Review what is verified and what production needs](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/8-production/) explains the production state.

## What you've learned and what's next

Zephyr is the last stage of a Cortex-A boot chain, so U-Boot can verify it, and `required = "conf"` makes U-Boot refuse any FIT it can't verify. Next, you [set up the host tools and the board's SDK](/learning-paths/embedded-and-microcontrollers/zephyr-signed-fit-uboot-cortex-a/2-set-up-tools/).
