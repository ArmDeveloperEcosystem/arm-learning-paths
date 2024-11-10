---
# User change
title: "About the Arm Automotive Solutions Software Reference Stack"

weight: 4

layout: "learningpathall"
---

## Arm Automotive Solutions Software Reference Stack, and Arm Reference Design-1 AE

The Arm Automotive Solutions Software Reference Stack can be run on the Arm Reference Design-1 AE. 

This is a concept hardware design built on the Neoverse V3AE Application Processor (as primary compute) and augmented with an Arm Cortex-R82AE based safety island. 

The system additionally includes a Runtime Security Engine (RSE) used for the secure boot and runtime secure services.

The software stack consists of:

* Firmware.
* Boot loader.
* Hypervisor.
* Linux kernel.
* File system.
* Applications. 

The development environment uses the Yocto Project build framework. 