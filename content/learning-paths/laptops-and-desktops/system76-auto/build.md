---
# User change
title: "Build the Arm Automotive Solutions Software Reference Stack"

weight: 3

layout: "learningpathall"
---

The Arm Automotive Solutions Software Reference Stack can be run on the Arm Reference Design-1 AE. 

This is a concept hardware design built on the Neoverse V3AE Application Processor (as primary compute) and augmented with an Arm Cortex-R82AE based safety island. 

The system additionally includes a Runtime Security Engine (RSE) used for the secure boot and runtime secure services.

The software stack consists of firmware, boot loader, hypervisor, Linux kernel, file system, and applications. 

The development environment uses the Yocto Project build framework. 

## Build the automotive software stack

The Thelio Astra makes it possible to build the complete software stack on an Arm-based local machine, instead of alternatives such as an Arm-based cloud instances or a non-Arm desktop computer.

You can build the Using the Arm Automotive Solutions Software Reference Stack from the command line of the Ubuntu 20.04 Multipass virtual machine. 

Create a new directory and clone the repository:

```console
mkdir -p ~/arm-auto-solutions
cd ~/arm-auto-solutions
git clone https://git.gitlab.arm.com/automotive-and-industrial/arm-auto-solutions/sw-ref-stack.git --branch v1.1
```

Open the configuration menu:

```console
kas menu sw-ref-stack/Kconfig
```

Use the space bar and arrow keys to select the three components show in the screen capture below:
- Accept the END USER LICENSE AGREEMENT
- Safety Island Actuation Demo
- Baremetal 

![configuration #center](configure.png)

{{% notice Note %}}
To build and run you much accept the EULA. 
{{% /notice %}}

Use tab to navigate to the `Build` button and press enter to start the build.

The build will take some time, depending on the number of CPUs in your virtual machine.

