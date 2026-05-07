---
title: Overview of AWS IoT Greengrass and the Arm v9 PAC and BTI instructions

weight: 2

layout: "learningpathall"
---

### AWS IoT Greengrass

AWS IoT Greengrass is an edge runtime and cloud service for building, deploying, and managing software on devices outside the cloud, such as industrial gateways, robots, cameras, and other IoT systems. It lets devices run applications locally for lower latency, reduced bandwidth use, and continued operation when connectivity is limited, while still integrating with AWS services. In Greengrass V2, key features include a modular component model for packaging software, support for Lambda functions, containers, native processes, and custom runtimes, secure communication with AWS IoT Core, local messaging and device state handling, fleet deployments and over-the-air updates, optional stream processing, and edge machine learning inference.


### PAC/BTI Arm v9 instructions

Armv9 Pointer Authentication (PAC) and Branch Target Identification (BTI) are security features designed to make control-flow attacks harder. PAC helps protect return addresses and pointers by adding a cryptographic signature that is checked before the pointer is used, which can detect tampering such as return-oriented programming attempts. BTI complements this by restricting where indirect branches are allowed to land, helping prevent attackers from jumping into unintended instruction sequences. Together, PAC and BTI strengthen software defenses at the instruction-set level, especially for modern operating systems, hypervisors, and applications that need improved resistance to memory-corruption exploits.

### What you've learned and what's next

Next, you'll use AWS IoT Greengrass to create and deploy a custom component to local Arm-based devices and verify each device's PAC/BTI support.