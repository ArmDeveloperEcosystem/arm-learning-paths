---
title: Introduction to OpenBMC and UEFI
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction to OpenBMC and UEFI

This section explains the roles of OpenBMC and UEFI in the Arm server boot flow, and highlights why simulating their integration is essential for early-stage development.

### OpenBMC

[OpenBMC](https://www.openbmc.org/) is a collaborative open-source firmware stack for Baseboard Management Controllers (BMC), hosted by the Linux Foundation.  
BMCs are embedded microcontrollers on server motherboards that enable both in-band and out-of-band system management.  
Out-of-band access allows remote management even when the host system is powered off or unresponsive, while in-band interfaces support communication with the host operating system during normal operation.

The OpenBMC stack is built using the Yocto Project and includes a Linux kernel, system services, D-Bus interfaces, and support for industry-standard APIs such as Redfish and IPMI. It provides features like hardware monitoring, fan control, power sequencing, sensor telemetry, event logging, BIOS configuration, and more.

Its architecture is modular by design—each board or platform can define its own layers and packages through Yocto recipes, enabling custom extensions to firmware functionality without modifying upstream code.

It is widely adopted by hyperscalers and enterprise vendors to manage servers, storage systems, and network appliances.  
OpenBMC is particularly well-suited to Arm-based server platforms like **[Neoverse RD-V3](https://neoverse-reference-design.docs.arm.com/en/latest/platforms/rdv3.html)**, where it provides early-stage platform control and boot orchestration even before silicon is available.

**Key features of OpenBMC include:**
- **Remote management:** power control, Serial over LAN (SOL), and virtual media  
- **Hardware health monitoring:** sensors, fans, temperature, voltage, and power rails  
- **Firmware update mechanisms:** support for signed image updates and secure boot  
- **Industry-standard APIs:** IPMI, Redfish, PLDM, and MCTP  
- **Modular and extensible design:** device tree-based configuration and layered architecture  

OpenBMC enables faster development cycles, open innovation, and reduced vendor lock-in across data centers, cloud platforms, and edge environments.

In this Learning Path, you’ll simulate how OpenBMC manages the early stage boot process, power sequencing, and remote access for a virtual Neoverse RD-V3 server. You will interact with the BMC console, inspect boot logs, and verify serial-over-LAN and UART communication with the host.

### UEFI

The [Unified Extensible Firmware Interface (UEFI)](https://uefi.org/) is the modern replacement for legacy BIOS, responsible for initializing hardware and loading the operating system.  
UEFI provides a robust, modular, and extensible interface between platform firmware and OS loaders. It supports:

- A modular and extensible architecture  
- Faster boot times and reliable system initialization  
- Large storage device support using GPT (GUID Partition Table)  
- Secure Boot for verifying boot integrity  
- Pre-boot networking and diagnostics via UEFI Shell or applications  

UEFI executes after the platform powers on and before the OS kernel takes over.  
It discovers and initializes system hardware, configures memory and I/O, and launches the bootloader.  
It is governed by the UEFI Forum and is now the standard firmware interface across server-class, desktop, and embedded systems.

In platforms that integrate OpenBMC, the BMC operates independently from the host CPU and manages platform power, telemetry, and recovery.  
During system boot, UEFI and OpenBMC coordinate via mechanisms such as IPMI over KCS, PLDM over MCTP, or shared memory buffers.  

These interactions are especially critical in Arm server-class platforms—like Neoverse RD-V3—for secure boot, remote diagnostics, and system recovery during pre-silicon or bring-up phases.

### Key Interactions Between OpenBMC and UEFI

| **Interaction**           | **Direction**     | **Description**                                                                 |
|---------------------------|-------------------|---------------------------------------------------------------------------------|
| Boot power sequencing     | BMC → Host        | BMC controls host power-on flow, ensuring UEFI starts in the correct sequence.  |
| Boot status reporting     | UEFI → BMC        | UEFI sends boot state and progress via IPMI (KCS) or PLDM.                      |
| Serial-over-LAN (SOL)     | BMC ↔ Host        | BMC bridges host UART console to remote clients over the network.               |
| Pre-boot configuration    | BMC ↔ UEFI        | BMC may inject or read boot config settings via shared memory or commands.      |
| System recovery signaling | UEFI → BMC        | UEFI can request BMC to initiate reboot, NMI, or recovery actions.              |


In this Learning Path, you will build and run the UEFI firmware on the RD-V3 FVP host platform.

You will use OpenBMC to power on the virtual Arm server, access the serial console, and monitor the host boot progress like real hardware platform. By inspecting the full boot log and observing system behavior in simulation, you will gain valuable insights into how BMC and UEFI coordinate during early firmware bring-up.
