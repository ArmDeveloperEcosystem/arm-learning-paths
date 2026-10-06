---
title: Learn where Zephyr sits in the Cortex-A boot chain
description: Learn why Zephyr on a Cortex-A processor is a payload that U-Boot can verify, what a FIT image contains, and how the boot chain hands control to it.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Zephyr is the last stage, not the first

On a microcontroller (MCU), Zephyr runs first, so secure boot means adding a bootloader such as MCUboot. A Cortex-A processor starts in a ROM (read-only memory) inside the SoC (system on chip), and several firmware stages run before your code. Zephyr is the last stage, so the stage before it, usually U-Boot, can check it before starting it.

You package Zephyr in a Flattened Image Tree (FIT) with a signature that U-Boot verifies before starting the image.

You can build and boot a verified Zephyr image in QEMU without hardware, or on a TI AM62L evaluation module (EVM). Both targets use the same signing and verification workflow, with separate instructions where setup differs.

## The boot chain on a Cortex-A board

On an Armv8-A board using U-Boot, boot proceeds from the SoC's boot ROM through early firmware to U-Boot. U-Boot then loads and starts the payload: Zephyr in your setup.

The early firmware is usually the SPL (Secondary Program Loader), a small U-Boot that loads the full one, plus TF-A (Trusted Firmware-A) and OP-TEE (Open Portable Trusted Execution Environment), which run in the Secure world. Many SoCs add the vendor's own security firmware, which checks the later stages. You build the SPL with U-Boot; the rest comes prebuilt in the vendor's SDK.

![Cortex-A boot chain from boot ROM through early firmware and U-Boot to a signed Zephyr FIT image. U-Boot verifies Zephyr; trust in the earlier stages depends on the platform's secure-boot configuration.#center](images/boot-chain-generic.svg "U-Boot verifies Zephyr in the Cortex-A boot chain")

## Choose your target

Pick one target now. QEMU is the default and needs nothing but your host; the AM62L EVM shows the same work on real silicon. Every page is written for both, and marks the few steps that differ.

| Requirement or feature | QEMU | AM62L EVM |
|---|---|---|
| Hardware | None | The board, a micro-SD card and reader, a micro-USB cable, a USB-C PD supply |
| Download | U-Boot source, 32 MB | TI Processor SDK, 4.5 GB, unpacks to 11 GB |
| Stages before U-Boot | None: QEMU starts `u-boot.bin` directly | Boot ROM, `tiboot3.bin`, `tispl.bin` |
| Zephyr board | `qemu_cortex_a53` | `am62l_evm/am62l3/a53` |
| Boot media | FAT partition in a 64 MiB disk image, `virtio 0:1` | FAT partition on a micro-SD card, `mmc 1:1` |
| Console | The terminal you start QEMU in | USB serial at 115200 baud |

### The boot chain in QEMU

QEMU's `virt` machine has no boot ROM and no vendor firmware. It loads the file you pass to `-bios` and starts the Cortex-A53 on it, so the chain is two links long:

```output
QEMU -bios u-boot.bin  ->  U-Boot  ->  Zephyr inside a FIT image
```

QEMU runs U-Boot's FIT verifier, but nothing authenticates U-Boot itself.

### The boot chain on the AM62L EVM

On the AM62L, the early stages are two files. `tiboot3.bin` holds TF-A's first stage and TIFS (TI Foundational Security), TI's security firmware; `tispl.bin` holds the rest of TF-A, OP-TEE and the SPL. You build them together with `u-boot.img` in a later step when you build U-Boot. The EVM ships in TI's High Security, Field Securable (HS-FS) development state.

![AM62L boot chain from boot ROM through `tiboot3.bin`, `tispl.bin`, and `u-boot.img` to the Zephyr FIT image. In HS-FS development mode, the early stages accept any signing key; U-Boot verifies Zephyr against your key before starting it.#center](images/boot-chain.svg "The same chain on the AM62L, with TI's file names")

## What a FIT image is

A FIT is U-Boot's container format for boot images. It's a device tree blob (DTB) whose nodes hold images instead of hardware descriptions.

The signed FIT you build contains:

- The image itself, which is Zephyr's `zephyr.bin` here
- A hash of that image, so U-Boot can tell if a byte changed
- A configuration that names the image to use (`kernel = "kernel-1"`) and carries a signature

`mkimage`, a U-Boot host tool, builds the FIT from a text source file (a `.its` file) and signs it with your private key. On the target, U-Boot's `bootm` command parses the FIT, verifies the signature and the hash, and copies the image to its load address.

You sign the FIT configuration with `sha256,rsa2048`, which combines SHA-256 hashing with a 2048-bit RSA key.

The public key lives inside U-Boot's own device tree, the control device tree, under a `/signature` node. That key node carries `required = "conf"`: every configuration in every FIT must carry a valid signature by this key, or U-Boot refuses to load it. Without `required`, a FIT with no signature at all still boots.

![Signed FIT image beside U-Boot's control device tree, which holds the required public key. The signature covers the FIT configuration and payload hash; the hash covers the Zephyr image bytes.#center](images/fit-signature.svg "What the signature and the hash each cover in a FIT image")

The signature does not cover the image bytes: it covers the configuration node plus the hash node, and the hash covers the bytes.

## Verify Zephyr before starting it

You configure U-Boot to verify the Zephyr FIT before starting Zephyr with `go`, U-Boot's command for jumping to an address.

In QEMU there is no key to fuse and nothing checks U-Boot at all. You leave the AM62L EVM in its development state without fusing your key into the chip. In that state, the ROM and vendor firmware accept boot files signed with any key. U-Boot's check of Zephyr is enforced either way. You'll review what a production device needs in the final section of this Learning Path.

## What you've learned and what's next

Zephyr is the last stage of a Cortex-A boot chain, so U-Boot can verify it, and `required = "conf"` makes U-Boot refuse any FIT it can't verify. Next, you set up the host tools for your target.
