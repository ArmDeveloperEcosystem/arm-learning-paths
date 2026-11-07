---
title: Understand the Zena CSS virtual platform
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the Zena CSS virtual platform

In [Innexis ANA](https://www.siemens.com/en-gb/products/ic/hav/innexis/architecture-native-acceleration/), a *chamber* provides the environment in which you create and run a virtual platform. The **Arm-Zena-CSS** vSoC describes the virtual hardware. The [**Arm-Zena-CSS EWAOL Software Stack**](https://arm-zena-css.docs.arm.com/en/v2.2/overview.html) supplies the software images used to boot it.

This Learning Path follows Siemens Innexis ANA **2026.2**. ANA menus, supplied assets, and software behavior may change in later releases. Use the ANA User Guide that matches your chamber version when a screen differs from this tutorial.

Zena CSS has more than one processing area. You will inspect these consoles after starting the virtual platform:

| Console in ANA | What to look for |
| --- | --- |
| **RSE** | Firmware messages associated with the Root of Security for the system. |
| **Safety Island** | SCP firmware messages from the Safety Island. |
| **Primary Compute Secure** | Secure-world and boot-stage messages for the primary-compute system. |
| **Primary Compute** | EWAOL Linux boot messages and the login prompt. |

The RSE starts the boot process on a Cortex-M55. It prepares firmware for the Cortex-R82AE Safety Island and the Primary Compute. SCP firmware on the Safety Island then powers on the Primary Compute.

Trusted Firmware-A (TF-A) and OP-TEE run in the Primary Compute secure world. U-Boot and systemd-boot lead to Linux in the normal world. The two Primary Compute console views show software running on the same Cortex-A720AE cores, not two separate groups of CPUs. See the [Arm Zena CSS boot process](https://arm-zena-css.docs.arm.com/en/latest/design/boot_process.html) for the reference software flow.

The firmware consoles help you see how the virtual system reaches Linux. They do not, by themselves, demonstrate that an application is secure or that a product has passed a security assessment.

For this Learning Path, your first working result is the **EWAOL Linux login prompt on the primary-compute console**. You will then inspect the guest from its shell. You do not need to change firmware or rebuild the software stack.

## Check your understanding

Before continuing, locate **Arm-Zena-CSS** and its **EWAOL Software Stack** in your chamber. If either is absent, ask the chamber administrator which Zena assets are available.
