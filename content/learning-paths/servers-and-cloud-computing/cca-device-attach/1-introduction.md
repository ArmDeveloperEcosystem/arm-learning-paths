---
title: "About CCA Realms"
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is Arm’s Confidential Computing Architecture (CCA) and Realm Management Extension (RME)?

Arm Confidential Computing Architecture (CCA) is a security framework introduced in the Armv9-A architecture. It defines a set of hardware-enforced isolation features that enable the creation of secure execution environments, which are designed to protect sensitive data while it’s being processed. CCA is the foundation of Confidential Computing on Arm platforms, ensuring that even privileged software like operating systems and hypervisors can’t access protected data.

To support CCA, Arm introduced the Realm Management Extension (RME). RME adds new architectural mechanisms to enforce memory isolation and resource separation at the hardware level. It provides the features and properties required to implement CCA-compliant systems, enabling the creation of Realms, which are trusted, isolated execution environments managed independently of the operating system.

Together, CCA and RME deliver the infrastructure needed to build Confidential Computing solutions on Arm, minimizing the need to trust system-level software and strengthening end-to-end security.

## What is a Realm?

A **Realm** is a protected execution environment enabled by RME.  It operates independently from both the **Normal World** - where operating systems and user applications run - and the **Secure World**, which hosts trusted firmware and trusted execution environments (TEEs). 

Realms allow lower-privileged software, such as an application or a virtual machine, to protect its content and execution from attacks by higher-privileged software, such as an OS or a hypervisor. Realms provide an environment for confidential computing, without requiring the Realm owner to trust the software components that manage the resources that the Realm uses.

While Realms are isolated by design, they still need to interact with external components to be practical - for example, accessing a network interface or communicating with a peripheral device. 

This Learning Path explains how devices can be securely attached to and used by Realms without compromising their isolation guarantees.

