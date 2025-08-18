---
title: Introduction to OpenBMC and UEFI
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

OpenBMC and UEFI are foundational components in Arm-based server platforms. In this module, you’ll learn what they are, how they interact, and why simulating their integration on a pre-silicon reference design like RD-V3 is valuable for early-stage development and testing.

## Introduction to OpenBMC

[OpenBMC](https://www.openbmc.org/) is a collaborative open-source firmware stack for Baseboard Management Controllers (BMC), hosted by the Linux Foundation.  
BMCs are embedded microcontrollers on server motherboards that enable both in-band and out-of-band system management.  
Out-of-band access allows remote management even when the host system is powered off or unresponsive, while in-band interfaces support communication with the host operating system during normal operation.

The OpenBMC stack is built using the Yocto Project and includes a Linux kernel, system services, D-Bus interfaces, Redfish/IPMI APIs, and support for hardware monitoring, fan control, power sequencing, and more.

It is widely adopted by hyperscalers and enterprise vendors to manage servers, storage systems, and network appliances.  
OpenBMC is particularly well-suited to Arm-based server platforms like **Neoverse RD-V3**, where it provides early-stage platform control and boot orchestration even before silicon is available.

**Key features of OpenBMC include:**
- **Remote management:** power control, Serial over LAN (SOL), and virtual media  
- **Hardware health monitoring:** sensors, fans, temperature, voltage, and power rails  
- **Firmware update mechanisms:** support for signed image updates and secure boot  
- **Industry-standard APIs:** IPMI, Redfish, PLDM, and MCTP  
- **Modular and extensible design:** device tree-based configuration and layered architecture  

OpenBMC enables faster development cycles, open innovation, and reduced vendor lock-in across data centers, cloud platforms, and edge environments.

**In this Learning Path**, you’ll simulate how OpenBMC manages the early-stage boot process, power sequencing, and remote access for a virtual Neoverse RD-V3 server. You will interact with the BMC console, inspect boot logs, and verify serial-over-LAN and UART communication with the host.

## Introduction to UEFI

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

**In this Learning Path**, you will build and run UEFI firmware on the RD-V3 FVP host platform, observe boot log output, and simulate how UEFI coordinates with OpenBMC via shared interfaces to complete system initialization.

