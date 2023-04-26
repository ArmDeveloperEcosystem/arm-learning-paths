---
# User change
title: "Porting methodology" 

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Porting methodology

This learning path introduces porting methodologies when migrating applications to Arm. As a practical example an `x86_64` application running in a Linux environment will be ported to `aarch64`. Emulation, remote hardware and physical hardware will be used to run the ported application on `aarch64`. Note: access to physical Arm hardware isn't a requirement for following this learning path.

When starting to migrate to Arm, some research will be necessary. It is important to understand the original platform environment used for developing, building and running the application which will be migrated. The questions below address some of these important aspects.
* What is the original platform architecture (e.g. x86_64)?
* Does the application use hardware acceleration (e.g. NVIDIA GPU)?
* What OS does the application run on?
* How is the application deployed (e.g., bare metal or virtualized)?
* What is the application's source language(s)?
* Is the application cross-compiled or built natively?
* What are the application's system dependencies?
* Does the application use external libraries?
* How is the application built (e.g. configuration) and which tools are used (e.g. compilers)?
* Are there any architecture specific functions or libraries?

These questions help draw a picture of the migration process to identify:
* the target platform configuration (e.g. hardware acceleration, OS, system dependencies),
* development tools (e.g. compilers),
* application requirements and configuration (e.g. compiler flags, third-party libraries).

In the next section we will analyze and answer these questions, which are applicable, based on an suitable example application.