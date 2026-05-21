---
title: Learn about PAC/BTI security features and OpenJDK support
weight: 2

layout: "learningpathall"
---

## Google Cloud C4A: Arm Neoverse-V2 virtual machines

Google Axion C4A is a family of Arm-based VMs built on Google's custom Axion processors, which use Arm Neoverse-V2 cores. These VMs deliver high performance with improved energy efficiency for modern cloud workloads such as CI/CD pipelines, microservices, media processing, and general-purpose applications.

To learn more about Google Axion, see the Google blog [Introducing Google Axion Processors, our new Arm-based CPUs](https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu).

## OpenJDK and the PAC/BTI Armv9 instructions

OpenJDK is the open-source reference implementation of Java Platform, Standard Edition (Java SE). It provides the core compiler, runtime, and class libraries you use to build and run Java applications across operating systems and hardware platforms. OpenJDK forms the basis for most modern Java distributions, while different vendors package and support their own builds.

Armv9 Pointer Authentication (PAC) and Branch Target Identification (BTI) are security features designed to make control-flow attacks harder.

PAC helps protect return addresses and pointers by adding a cryptographic signature that's checked before the pointer is used, which can detect tampering such as return-oriented programming attempts.

BTI complements this by restricting where indirect branches can land, helping prevent attackers from jumping into unintended instruction sequences. 

Together, PAC and BTI strengthen software defenses at the instruction-set level, especially for modern operating systems, hypervisors, and applications that need improved resistance to memory-corruption exploits.

### How PAC/BTI protects Java applications

PAC and BTI protection in a Java application comes from two layers working together.

The first layer is the system libraries. Native code linked into the JVM process — including the C runtime (`libc`), cryptographic libraries, and other shared libraries — can be compiled with PAC/BTI support. When the OS loads these libraries, the kernel enforces BTI landing-pad checks and validates PAC signatures on return addresses. This protects the native portions of the JVM process even before any Java bytecode runs.

The second layer is the JVM itself. OpenJDK's JIT compiler (C2) generates native machine code at runtime for hot Java methods. When you build the JVM with PAC/BTI support, the JIT emits `PACIASP`/`AUTIASP` instructions to sign and authenticate return addresses in JIT-compiled frames, and marks valid branch targets with `BTI` landing-pad instructions. This extends hardware-enforced control-flow integrity into the dynamically generated code that runs your Java application.

The result is that a fully protected deployment needs both: system libraries compiled with PAC/BTI, and a JVM binary that was itself built with PAC/BTI enabled. You can verify both conditions on a running JVM, which is what the next steps of this Learning Path cover.

## What you've learned and what's next

You now have the background on Google Cloud C4A, OpenJDK, and Armv9 PAC/BTI features.

Next, you'll create an Arm-based Google Cloud VM, install OpenJDK, and validate PAC/BTI readiness in the installed JVM.
