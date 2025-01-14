---
# User change
title: "Porting methodology" 

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Porting methodology

This Learning Path introduces porting methodologies when migrating applications to Arm. As a practical example, an `x86_64` application running in a Linux environment will be ported to `aarch64`. Emulation, remote hardware, and physical hardware will be used to run the ported application on `aarch64`. Note: access to physical Arm hardware isn't a requirement. 

When starting to migrate to Arm, some research will be necessary. It is important to understand the original platform environment used for developing, building, and running the application to be migrated. 

The questions below address some of these important aspects.
* What is the original platform architecture (`x86_64`)?
* Does the application use hardware acceleration (such as NVIDIA GPU)?
* What operating system does the application run on?
* How is the application deployed (bare metal or virtualized)?
* What is the application's source language(s)?
* Is the application cross-compiled or built natively?
* What are the application's system dependencies?
* Does the application use external libraries?
* How is the application built (configuration) and which tools are used (compilers)?
* Are there any architecture specific functions or libraries?

These questions help draw a picture of the migration process to identify:
* The target platform configuration (hardware acceleration, OS, system dependencies),
* Development tools (compilers and build tools),
* Application requirements and configuration (compiler flags, third-party libraries).

In the next section you will analyze and answer these questions for an example application.