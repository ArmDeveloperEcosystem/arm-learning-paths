---
title: Understanding the CSS V3 Boot Flow and Firmware Stack
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Firmware Stack Overview and Boot Sequence Coordination

To ensure the platform transitions securely and reliably from power-on to operating system launch, this module introduces the roles and interactions of each firmware component within the RD‑V3 boot process.
You’ll learn how each module contributes to system initialization and how control is systematically handed off across the boot chain.

In the RD‑V3 platform, each subsystem—such as TF‑A, RSE, SCP, LCP, and UEFI—operates independently but cooperates through a well-defined sequence. 
Each module is delivered as a separate firmware image, yet they coordinate tightly through a structured boot flow and inter-processor signaling.

The following diagram from the [Neoverse Reference Design Documentation](https://neoverse-reference-design.docs.arm.com/en/latest/shared/boot_flow/rdv3_single_chip.html?highlight=boot) illustrates the progression of component activation from initial reset to OS handoff:

![img1 alt-text#center](rdf_single_chip.png "Boot Flow for RD-V3 Single Chip")


### TF-A: Trusted Firmware-A (BL1 / BL2)

TF‑A is the entry point of the boot chain and is responsible for establishing the system’s root of trust.
* BL1 (Boot Loader Stage 1): Executes from ROM, initializing minimal hardware such as clocks and serial interfaces, and loads BL2.
* BL2 (Boot Loader Stage 2): Validates and loads SCP, RSE, and UEFI images, setting up secure handover to later stages.

TF‑A ensures all downstream components are authenticated and loaded from trusted sources, laying the foundation for a secure boot.


### Example: Walking Through the Full Boot Process on FVP

To illustrate this process end to end, let's walk through a practical example using the RD‑V3 FVP to boot a custom Linux kernel.

* System Power-On (BL1): The platform powers on via FVP. BL1 executes from ROM, sets up clocks and UART, and loads BL2.

* Secure Boot Begins (BL2 → RSE): BL2 loads RSE and other firmware components. RSE performs secure boot validation and releases authorization only if all images pass authentication.

* Platform Initialization (SCP): SCP is loaded next and initializes DRAM, clocks, and power domains. It enables the application cores and signals readiness.

* Firmware Handoff (AP → UEFI): The application processor takes over and runs TF-A BL31, which launches UEFI. UEFI scans boot devices and passes control to GRUB.

* OS Launch (GRUB → Kernel): GRUB selects the custom Linux image and launches it. The kernel initializes and prints Welcome to Arm RD-V3 Linux via UART.

If successful, you’ll see the BusyBox shell prompt like this:

```
Welcome to Arm RD-V3 Linux
```

This flow demonstrates how each component enables and secures the next—entirely within a virtual environment, without requiring physical silicon.


### RSE: Runtime Security Engine (Cortex‑M55)

RSE firmware runs on the Cortex‑M55 and plays a critical role in platform attestation and integrity enforcement.
* Authenticates BL2, SCP, and UEFI firmware images (Secure Boot)
* Records boot-time measurements (e.g., PCRs, ROT)
* Releases boot authorization only after successful validation

RSE acts as the second layer of the chain of trust, maintaining a monitored and secure environment throughout early boot.


### SCP: System Control Processor (Cortex‑M7)

SCP firmware runs on the Cortex‑M7 core and performs early hardware initialization and power domain control.
* Initializes clocks, reset controllers, and system interconnect
* Manages DRAM setup and enables power for the application processor
* Coordinates boot readiness with RSE via MHU (Message Handling Unit)

SCP is central to bring-up operations and ensures the AP starts in a stable hardware environment.


### LCP: Low Power Controller (Optional Component)

If present in the configuration, LCP handles platform power management at a finer granularity:
* Implements sleep/wake transitions
* Controls per-core power gating
* Manages transitions to ACPI power states (e.g., S3, S5)

LCP support depends on the FVP model and may be omitted in simplified virtual setups.


### UEFI / GRUB / Linux Kernel

After SCP powers on the application processor, control passes to the main bootloader and operating system:
* UEFI (EDK2): Provides firmware abstraction, hardware discovery, and ACPI table generation
* GRUB: Selects and loads the Linux kernel image
* Linux Kernel: Initializes the OS, drivers, and launches the userland (e.g., BusyBox)

On the FVP, you can observe this process via UART logs, helping validate each stage’s success.


### Coordination and Handoff Logic

The RD‑V3 boot sequence follows a multi-stage, dependency-driven handshake model, where each firmware module validates, powers, or authorizes the next.

| Stage | Dependency Chain     | Description                                                             |
|-------|----------------------|-------------------------------------------------------------------------|
| 1     | RSE ← BL2            | RSE is loaded and triggered by BL2 to begin security validation         |
| 2     | SCP ← BL2 + RSE      | SCP initialization requires both BL2 and authorization from RSE         |
| 3     | AP ← SCP + RSE       | The application processor starts only after SCP sets power and RSE permits |
| 4     | UEFI → GRUB → Linux  | UEFI launches GRUB, which loads the kernel and enters the OS            |


{{% notice Note %}}
In the table above, arrows (←) represent **dependency relationships**—the component on the left **depends on** the component(s) on the right to be triggered or authorized.  
For example, `RSE ← BL2` means that RSE is loaded and triggered by BL2;  
`AP ← SCP + RSE` means the application processor can only start after SCP has initialized the hardware and RSE has granted secure boot authorization.  
These arrows do not represent execution order but indicate **which component must be ready for another to begin**.
{{% /notice %}}

{{% notice Note %}}
Once the firmware stack reaches UEFI, it performs hardware discovery and launches GRUB.  
GRUB then selects and boots the Linux kernel. Unlike the previous dependency arrows (←), this is a **direct execution path**—each stage passes control directly to the next.
{{% /notice %}}

This layered approach supports modular testing, independent debugging, and early-stage simulation—all essential for secure and robust platform bring-up.


In this module, you have:

* Explored the full boot sequence of the RD‑V3 platform, from power-on to Linux login
* Understood the responsibilities of key firmware components such as TF‑A, RSE, SCP, LCP, and UEFI
* Learned how secure boot is enforced and how each module hands off control to the next
* Interpreted boot dependencies using FVP simulation and UART logs

In the next module, you’ll set up your development environment, fetch the source code, and build the firmware stack used on RD‑V3.  
You’ll simulate the full bring-up process and validate the results using a fully virtualized platform—before any hardware is required.
