---
title: Understanding the CSS V3 Boot Flow and Firmware Stack
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Firmware Stack Overview and Boot Sequence Coordination

To ensure the platform transitions securely and reliably from power-on to operating system launch, this module introduces the roles and interactions of each firmware component within the RD‑V3 boot process.
You’ll learn how each module contributes to system initialization and how control is systematically handed off across the boot chain.


## How the System Wakes Up

In the RD‑V3 platform, each subsystem—such as TF‑A, RSE, SCP, LCP, and UEFI—operates independently but cooperates through a well-defined sequence. 
Each module is delivered as a separate firmware image, yet they coordinate tightly through a structured boot flow and inter-processor signaling.

The following diagram from the [Neoverse Reference Design Documentation](https://neoverse-reference-design.docs.arm.com/en/latest/shared/boot_flow/rdv3_single_chip.html?highlight=boot) illustrates the progression of component activation from initial reset to OS handoff:

![img1 alt-text#center](rdf_single_chip.png "Boot Flow for RD-V3 Single Chip")

### Stage 1. Security Validation Starts First (RSE)

The first firmware module triggered after BL2 is the Runtime Security Engine (RSE), executing on Cortex‑M55.RSE authenticates all critical firmware components—including SCP, UEFI, and kernel images—using secure boot mechanisms.It performs cryptographic measurements and builds a Root of Trust before allowing any other processors to start.

RSE acts as the platform’s security gatekeeper.

### Stage 2. Early Hardware Initialization (SCP / MCP)

Once RSE completes verification, the System Control Processor (SCP) and Management Control Processor (MCP) are released from reset.

These controllers perform essential platform bring-up:
* Initialize clocks, reset lines, and power domains
* Prepare DRAM and interconnect
* Enable the application cores and signal readiness to TF‑A

SCP/MCP are the ground crew bringing hardware systems online.

### Stage 3. Secure Execution Setup (TF‑A)

Once the AP is released, it begins executing Trusted Firmware‑A (TF‑A) at EL3.
TF‑A configures the secure world, sets up exception levels, and prepares for handoff to UEFI.

TF‑A is the ignition controller, launching the next stages securely.

### Stage 4. Firmware and Bootloader (EDK2 / GRUB)

TF‑A hands off control to UEFI firmware (EDK2), which performs device discovery and launches GRUB.

Responsibilities:
* Detect and initialize memory, PCIe, and boot devices
* Generate ACPI and platform configuration tables
* Locate and launch GRUB from storage or flash

EDK2 and GRUB are like the first- and second-stage rockets launching the payload.

### Stage 5. Linux Kernel Boot

GRUB loads the Linux kernel and passes full control to the OS.

Responsibilities:
* Initialize device drivers and kernel subsystems
* Mount the root filesystem
* Start user-space processes (e.g., BusyBox)

The Linux kernel is the spacecraft—it takes over and begins its mission.

## Firmware Module Responsibilities in Detail

Now that we’ve examined the high-level boot stages, let’s break down each firmware module’s role in more detail.

Each stage of the boot chain is backed by a dedicated component—either a secure bootloader, platform controller, or operating system manager—working together to ensure a reliable system bring-up.

### RSE: Runtime Security Engine (Cortex‑M55) (Stage 1: Security Validation)

RSE firmware runs on the Cortex‑M55 and plays a critical role in platform attestation and integrity enforcement.
* Authenticates BL2, SCP, and UEFI firmware images (Secure Boot)
* Records boot-time measurements (e.g., PCRs, ROT)
* Releases boot authorization only after successful validation

RSE acts as the second layer of the chain of trust, maintaining a monitored and secure environment throughout early boot.


### SCP: System Control Processor (Cortex‑M7) (Stage 2: Early Hardware Bring-up)

SCP firmware runs on the Cortex‑M7 core and performs early hardware initialization and power domain control.
* Initializes clocks, reset controllers, and system interconnect
* Manages DRAM setup and enables power for the application processor
* Coordinates boot readiness with RSE via MHU (Message Handling Unit)

SCP is central to bring-up operations and ensures the AP starts in a stable hardware environment.

### TF-A: Trusted Firmware-A (BL1 / BL2) (Stage 3: Secure Execution Setup)

TF‑A is the entry point of the boot chain and is responsible for establishing the system’s root of trust.
* BL1 (Boot Loader Stage 1): Executes from ROM, initializing minimal hardware such as clocks and serial interfaces, and loads BL2.
* BL2 (Boot Loader Stage 2): Validates and loads SCP, RSE, and UEFI images, setting up secure handover to later stages.

TF‑A ensures all downstream components are authenticated and loaded from trusted sources, laying the foundation for a secure boot.


### UEFI / GRUB / Linux Kernel (Stage 4–5: Bootloader and OS Handoff)

After SCP powers on the application processor, control passes to the main bootloader and operating system:
* UEFI (EDK2): Provides firmware abstraction, hardware discovery, and ACPI table generation
* GRUB: Selects and loads the Linux kernel image
* Linux Kernel: Initializes the OS, drivers, and launches the userland (e.g., BusyBox)

On the FVP, you can observe this process via UART logs, helping validate each stage’s success.


### LCP: Low Power Controller (Optional Component)

If present in the configuration, LCP handles platform power management at a finer granularity:
* Implements sleep/wake transitions
* Controls per-core power gating
* Manages transitions to ACPI power states (e.g., S3, S5)

LCP support depends on the FVP model and may be omitted in simplified virtual setups.


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

With the full boot flow and firmware responsibilities now clear, you're ready to move from theory to practice.

In the next module, you'll clone the RD‑V3 source tree, build the firmware stack, and prepare your own pre-silicon virtual platform using Arm FVP.
