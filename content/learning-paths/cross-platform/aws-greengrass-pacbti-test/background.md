---
title: Understand AWS IoT Greengrass and Armv9 PAC/BTI security features

weight: 2

layout: "learningpathall"
---

## AWS IoT Greengrass

IoT Greengrass is an edge runtime and cloud service provided by Amazon Web Services (AWS) for building, deploying, and managing software on devices outside the cloud. These devices include industrial gateways, robots, cameras, and other IoT systems. AWS IoT Greengrass lets devices run applications locally for lower latency, reduced bandwidth use, and continued operation when connectivity is limited, while still integrating with AWS services. In Greengrass V2, key features include:

- A modular component model for packaging software
- Support for Lambda functions, containers, native processes, and custom runtimes
- Secure communication with AWS IoT Core
- Local messaging and device state handling
- Fleet deployments and over-the-air updates
- Optional stream processing
- Edge machine learning inference


## PAC/BTI security features

Pointer Authentication (PAC) and Branch Target Identification (BTI) are Arm security features designed to make control-flow attacks harder. PAC was introduced as an optional feature in Armv8.3-A and BTI in Armv8.5-A. Both are mandatory in Armv9-A, which is why Armv9 devices reliably support them while older Armv8 devices might not.

PAC protects return addresses and function pointers by embedding a cryptographic signature that is verified before the pointer is used. This can detect tampering such as return-oriented programming (ROP) attempts. BTI complements PAC by restricting where indirect branches are allowed to land, preventing attackers from jumping into unintended instruction sequences. Together, PAC and BTI strengthen software defenses at the instruction-set level, particularly for operating systems, hypervisors, and applications that need improved resistance to memory-corruption exploits.

## What you've learned and what's next

You now know about AWS IoT Greengrass and its key features. You also learned about PAC/BTI, and how they secure software at the instruction-set level.

Next, you'll use AWS IoT Greengrass to create and deploy a custom component to local Arm-based devices and verify each device's PAC/BTI support.