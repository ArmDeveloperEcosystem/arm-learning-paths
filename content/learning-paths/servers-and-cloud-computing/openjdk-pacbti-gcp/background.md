---
title: Understand Google Cloud C4A Axion processors, OpenJDK, and Armv9 PAC/BTI

weight: 2

layout: "learningpathall"
---

## Explore Google Cloud C4A instances

Google Axion C4A is a family of Arm-based VMs built on Google's custom Axion processors, which use Arm Neoverse-V2 cores. These VMs deliver high performance with improved energy efficiency for modern cloud workloads such as CI/CD pipelines, microservices, media processing, and general-purpose applications.

The C4A series provides an Arm-based alternative to x86 VMs, enabling developers to evaluate cost, performance, and efficiency trade-offs in Google Cloud. For Kubernetes users, C4A instances provide a practical way to run Arm-native clusters and validate tooling such as Helm on modern cloud infrastructure.

To learn more about Google Axion, see the Google blog [Introducing Google Axion Processors, our new Arm-based CPUs](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu).

## OpenJDK and the PAC/BTI Arm v9 instructions

OpenJDK is the open-source reference implementation of Java Platform, Standard Edition (Java SE). It provides the core compiler, runtime, and class libraries you use to build and run Java applications across operating systems and hardware platforms. OpenJDK forms the basis for most modern Java distributions, while different vendors package and support their own builds.

Armv9 Pointer Authentication (PAC) and Branch Target Identification (BTI) are security features designed to make control-flow attacks harder. PAC helps protect return addresses and pointers by adding a cryptographic signature that is checked before the pointer is used, which can detect tampering such as return-oriented programming attempts. BTI complements this by restricting where indirect branches are allowed to land, helping prevent attackers from jumping into unintended instruction sequences. Together, PAC and BTI strengthen software defenses at the instruction-set level, especially for modern operating systems, hypervisors, and applications that need improved resistance to memory-corruption exploits.

## What you've learned and what's next

You now have the background on Google Cloud C4A, OpenJDK, and Armv9 PAC/BTI features.

Next, you'll create an Arm-based Google Cloud VM, install OpenJDK, and validate PAC/BTI readiness in the installed JVM.
