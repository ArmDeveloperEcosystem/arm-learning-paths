---
title: Understand Azure Cobalt 100, OpenJDK, and Armv9 PAC/BTI

weight: 2

layout: "learningpathall"
---

## Azure Cobalt 100 Arm-based processor

Azure Cobalt 100 is Microsoft's first-generation Arm-based processor, built on Arm Neoverse N2. It allocates a dedicated physical core for each vCPU, which provides consistent and predictable performance for cloud-native, scale-out Linux workloads. These characteristics make Cobalt 100 well suited for Java application servers and security-sensitive workloads where PAC/BTI hardware support is available and beneficial.

To learn more, see the Microsoft blog [Announcing the preview of new Azure VMs based on the Azure Cobalt 100 processor](https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353).

## OpenJDK and Armv9 PAC/BTI security features

OpenJDK is the open-source reference implementation of Java Platform, Standard Edition (Java SE). It provides the core compiler, runtime, and class libraries you use to build and run Java applications across operating systems and hardware platforms. OpenJDK forms the basis for most modern Java distributions, while different vendors package and support their own builds.

Armv9 Pointer Authentication (PAC) and Branch Target Identification (BTI) are security features designed to make control-flow attacks harder. PAC helps protect return addresses and pointers by adding a cryptographic signature that is checked before the pointer is used, which can detect tampering such as return-oriented programming attempts. BTI complements this by restricting where indirect branches are allowed to land, helping prevent attackers from jumping into unintended instruction sequences. Together, PAC and BTI strengthen software defenses at the instruction-set level, especially for modern operating systems, hypervisors, and applications that need improved resistance to memory-corruption exploits. When OpenJDK is compiled with branch protection enabled, the JVM binary and its native libraries are built with these protections, extending the security benefit to Java workloads running on the platform.

## What you've learned and what's next

You now have the background on Azure Cobalt 100, OpenJDK, and Armv9 PAC/BTI features.

Next, you'll create an Arm-based Azure VM, build OpenJDK with branch protection, and validate PAC/BTI readiness in the installed JVM.
