---
# User change
title: "Arm Automotive Solutions Software Reference Stack"

weight: 4

layout: "learningpathall"
---

## About Arm Automotive Solutions Software Reference Stack, and Arm Reference Design-1 AE

The Arm Automotive Solutions Software Reference Stack can be run on the Arm Reference Design-1 AE (RD-1 AE). 

RD-1 AE is a concept hardware design, for the Automotive segment, and built on the Neoverse V3AE Application Processor as primary compute, and augmented with an Arm Cortex-R82AE based Safety Island. 

The system additionally includes a Runtime Security Engine (RSE) used for the secure boot of the system elements and runtime Secure Services.

The software stack consists of:

* Firmware.
* Boot loader.
* Hypervisor.
* Linux kernel.
* File system.
* Applications. 

The development environment uses the Yocto Project build framework. 