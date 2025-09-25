---
title: System requirements
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

If you are building and testing Windows on Arm software you have a variety of options to run Windows on Arm. You can use local laptops, cloud virtual machines, and CI/CD platforms like GitHub Actions for development tasks.

You can also use a local Arm Linux server to create virtual machines for Windows on Arm software development tasks. This Learning Path explains how to install and use Windows on Arm virtual machines on an Arm Linux system. Two scripts are provided to create and run Windows on Arm virtual machines to make the process easy. 

Before creating a Windows on Arm virtual machine, ensure your Arm Linux system meets the hardware and software requirements. This section covers everything you need to prepare to create a Windows on Arm virtual machine using QEMU and KVM.

## Hardware requirements

You need an Arm Linux system with enough performance, memory, and storage to run a Windows on Arm virtual machine. 

The provided scripts have been tested on a [Thelio Astra](https://system76.com/desktops/thelio-astra-a1.1-n1/configure?srsltid=AfmBOoplXbwXifyxppxFe_oyahYMJHUT0bp2BnIBSH5ADjqgZxB7wW75) running Ubuntu 24.04. 

Thelio Astra is an Arm-based desktop computer designed by System76 for autonomous vehicle development and other general-purpose Arm software development. It uses the Ampere Altra processor, which is based on the Arm Neoverse N1 CPU, and ships with the Ubuntu operating system.

Other Arm Linux systems and other Linux distributions are possible, but have not been tested. General hardware requirements are listed below.

The minimum hardware requirements for the Arm Linux system are:

- 8 cores with hardware virtualization support
- 8 GB RAM
- 50 GB free disk space

The scripts automatically allocate resources as listed below, but the details can be customized for your system.

- CPU: half of available cores (minimum 4 cores)
- Memory: half of available RAM (minimum 4 GB)
- Disk: 40 GB VM disk

## KVM support 

Kernel-based Virtual Machine (KVM) support is required for hardware-accelerated virtualization and good VM performance.

KVM is a virtualization infrastructure built into the Linux kernel that allows you to run virtual machines with near-native performance. It leverages Arm's hardware virtualization extensions to provide efficient CPU virtualization, while QEMU handles device emulation and management. Without KVM, virtual machines run much slower using software emulation.

Verify your system supports KVM by running:

```console
sudo apt install cpu-checker -y
sudo kvm-ok
```

If KVM is available, you will see the messages:

```output
INFO: /dev/kvm exists
KVM acceleration can be used
```

This confirms that:
- Your CPU supports hardware virtualization
- The KVM kernel module is loaded
- The `/dev/kvm` device exists 

## Required software

The scripts require several software packages. 

Install the packages using the Linux package manager.

```console
sudo apt update
sudo apt install qemu-system-arm qemu-utils genisoimage wget curl jq uuid-runtime -y
```

If needed, the [Remmina](https://remmina.org/) remote desktop (RDP) client is automatically installed by the run script so you don't need to install it now, but you can install it using the command below.

```console
sudo apt install remmina remmina-plugin-rdp -y
```

Proceed to the next section to learn about the scripts.

