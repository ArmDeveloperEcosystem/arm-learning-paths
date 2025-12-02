---
title: Check system requirements
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Prepare your system for Windows on Arm virtual machines

To build and test Windows on Arm software, choose from several flexible options: run Windows on Arm locally, use cloud-based virtual machines, or leverage CI/CD platforms like GitHub Actions. For hands-on development, set up a Windows on Arm virtual machine directly on your Arm Linux server.

In this Learning Path, you'll install and use Windows on Arm virtual machines on an Arm Linux system. Two easy-to-use scripts are included to streamline the creation and management of your virtual machines. Before you get started, make sure your Arm Linux system meets the hardware and software requirements. In this section, you'll set up everything you need to create a Windows on Arm virtual machine using QEMU and KVM.

## Check hardware requirements

You need an Arm Linux system with enough performance, memory, and storage to run a Windows on Arm virtual machine. You can use the scripts on a [Thelio Astra](https://system76.com/desktops/thelio-astra-a1.1-n1/configure?srsltid=AfmBOoplXbwXifyxppxFe_oyahYMJHUT0bp2BnIBSH5ADjqgZxB7wW75) running Ubuntu 24.04, where they have been tested successfully.

Thelio Astra is an Arm-based desktop computer designed by System76 for autonomous vehicle development and other general-purpose Arm software development. It uses the Ampere Altra processor, which is based on the Arm Neoverse N1 CPU, and ships with the Ubuntu operating system.
You can try these scripts on other Arm Linux systems or distributions, but only the configuration above has been tested. Check the general hardware requirements below before you continue.

The minimum hardware requirements for the Arm Linux system are:

- 8 cores with hardware virtualization support
- 8 GB RAM
- 50 GB free disk space

Customize CPU cores, memory, and disk size by editing the variables at the top of each script file (`create-vm.sh` and `run-vm.sh` in the project directory) to match your system's capabilities.

For this Learning Path, add the following information:

- CPU: half of available cores (minimum 4 cores)
- Memory: half of available RAM (minimum 4 GB)
- Disk: 40 GB VM disk

## Verify KVM support

Kernel-based Virtual Machine (KVM) support is required for hardware-accelerated virtualization and optimal virtual machine (VM) performance on Arm systems. Without KVM, your VMs run significantly slower because they rely on software emulation instead of using Arm's hardware virtualization features.

KVM is a virtualization infrastructure built into the Linux kernel that allows you to run virtual machines with near-native performance. It leverages Arm's hardware virtualization extensions to provide efficient CPU virtualization, while QEMU handles device emulation and management. Without KVM, virtual machines run much slower using software emulation.

Verify your system supports KVM by running:

```console
sudo apt install cpu-checker -y
kvm-ok
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

Add your user account to the KVM group:

```console
sudo usermod -a -G kvm $USER
newgrp kvm
```

## Install required software

The scripts require several software packages. 

Install the packages using the Linux package manager.

```console
sudo apt update
sudo apt install qemu-system-arm qemu-utils genisoimage wget curl jq uuid-runtime seabios -y
```

If needed, the [Remmina](https://remmina.org/) remote desktop (RDP) client is automatically installed by the run script so you don't need to install it now, but you can install it using this command:

```console
sudo apt install remmina remmina-plugin-rdp -y
```

You’ve verified your system requirements and you’re now ready to move on and start working with Windows on Arm virtual machines. 
