---
title: Introduction the Arm RD‑V3 Platform
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction to the Arm RD‑V3 Platform

This module introduces the foundational architecture behind Arm’s RD-V3 platform. You’ll learn how Neoverse CSS-V3 is designed for scalable server-class systems and how to develop and validate firmware using a fully virtual environment—before any hardware is available.

Arm Neoverse is designed to meet the demanding requirements of data center and edge computing, delivering high performance and efficiency. Widely adopted in servers, networking, and edge devices, the Neoverse architecture provides a solid foundation for modern infrastructure.

### Neoverse CSS-V3 Platform Overview

[Neoverse CSS-V3](https://www.arm.com/products/neoverse-compute-subsystems/css-v3) (Compute Subsystem Version 3) is the core subsystem architecture underpinning the Arm RD-V3 platform. It is specifically optimized for high-performance server and data center applications, providing a highly integrated solution combining processing cores, memory management, and interconnect technology.

CSS V3 forms the key building block for specialized computing systems. It reduces design and validation costs for the general-purpose compute subsystem, allowing partners to focus on their specialization and acceleration while reducing risk and accelerating time to deployment. 

CSS‑V3 is available in configurable subsystems, supporting up to 64 Neoverse V3 cores per die. It also enables integration of high-bandwidth DDR5/LPDDR5 memory (up to 12 channels), PCIe Gen5 or CXL I/O (up to 64 lanes), and high-speed die-to-die links with support for UCIe 1.1 or custom PHYs. Designs can be scaled down to smaller core-count configurations, such as 32-core SoCs, or expanded through multi-die integration.

Key features of CSS-V3 include:

* High-performance CPU clusters: Optimized for server workloads and data throughput.

* Advanced memory management: Efficient handling of data across multiple processing cores.

* Interconnect technology: Enabling high-speed, low-latency communication within the subsystem.


### RD‑V3 Platform Introduction

The RD‑V3 platform is a comprehensive reference design built around Arm’s [Neoverse V3](https://www.arm.com/products/silicon-ip-cpu/neoverse/neoverse-v3) CPUs, along with [Cortex-M55](https://www.arm.com/products/silicon-ip-cpu/cortex-m/cortex-m55) and [Cortex-M7](https://www.arm.com/products/silicon-ip-cpu/cortex-m/cortex-m7) microcontrollers. This platform enables efficient high-performance computing and robust platform management:


| Component     | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| Neoverse V3   | The primary application processor responsible for executing OS and payloads |
| Cortex‑M7     | Implements the System Control Processor (SCP) for power, clocks, and init   |
| Cortex‑M55    | Hosts the Runtime Security Engine (RSE), providing secure boot and runtime integrity |

These subsystems work together in a coordinated architecture, communicating through shared memory regions, control buses, and platform protocols. This enables multi-stage boot processes and robust secure boot implementations.



### Develop and Validate Without Hardware

In traditional development workflows, system validation cannot begin until silicon is available—often introducing risk and delay. 

To address this, Arm provides the Fixed Virtual Platform ([FVP](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms)) —a  complete simulations model that emulates full Arm SoC behavior on a host machine. The CSS‑V3 platform is available in multiple FVP configurations, allowing developers to select the model that best fits their specific development and validation needs.


Key Capabilities of FVP:
* Multi-core CPU simulation with SMP boot
* Multiple UART interfaces for serial debug and monitoring
* Compatible with TF‑A, UEFI, GRUB, and Linux kernel images
* Provides boot logs, trace outputs, and interrupt event visibility for debugging

FVP enables developers to verify boot sequences, debug firmware handoffs, and even simulate RSE behaviors—all before first silicon.

### Comparing different version of RD-V3 FVP

To support different use cases and levels of platform complexity, Arm offers three virtual models based on the CSS‑v3 architecture: RD‑V3, RD-V3-Cfg1, and RD‑V3‑R1. While they share a common foundation, they differ in chip count, system topology, and simulation flexibility.

| Model       | Description                                                      | Recommended Use Cases                                              |
|-------------|------------------------------------------------------------------|--------------------------------------------------------------------|
| RD‑V3       | Standard single-die platform with full processor and security blocks | Ideal for newcomers, firmware bring-up, and basic validation        |
| RD‑V3‑R1    | Dual-die platform simulating chiplet-based architecture          | Suitable for multi-node, interconnect, and advanced boot tests     |
| CFG1        | Lightweight model with reduced control complexity for fast startup | Best for CI pipelines, unit testing, and quick validations         |


This Learning Path begins with RD‑V3 as the primary platform for foundational exercises, guiding you through the process of building the software stack and simulating it on FVP to verify the boot sequence.
In later modules, you’ll transition to RD‑V3‑R1 for more advanced system validation and scalability exploration.
