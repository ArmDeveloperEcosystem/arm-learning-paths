---
title: Understand and customize Windows on Arm VM automation scripts

weight: 3

layout: "learningpathall"
---

## Get started with the Windows on Arm VM automation scripts

A GitHub project provides two Bash scripts. Understanding their architecture and design will help you use them effectively and enable you to customize the options for your specific needs.

Start by cloning the project repository from GitHub to your Arm Linux system.

```bash
git clone https://github.com/jasonrandrews/win11arm.git
cd win11arm
```

The remainder of this section explains the structure of the scripts, and the next section provides details to run the scripts to create a Windows virtual machine.

## Project overview

The project includes two Bash scripts. 

- VM create script: `create-win11-vm.sh` handles all VM creation tasks
- VM run script: `run-win11-vm.sh` manages VM execution and connectivity

All configuration is available using command-line options. 

The VM create script also allows you to perform the entire VM creation with a single command or run each individual step to learn and monitor the process. 

This modular approach allows you to understand each component while maintaining the simplicity of automated execution.

## Virtual machine creation

The creation script, `create-win11-vm.sh` is responsible for building a complete Windows 11 on Arm VM from scratch. It handles everything from directory setup to Windows installation, with each step clearly defined and independently executable.

The script handles resource detection and allocation, provides unattended Windows installation, and has a flexible command line to change default values.

Virtual machine creation includes the following steps:

- Download the Windows 11 for Arm ISO from Microsoft
- Configure VirtIO drivers for optimal performance
- Set up automated installation with custom credentials
- Create optimized disk images 

### Virtual machine creation details

The `create-win11-vm.sh` script implements a four-step process that builds a Windows VM incrementally:

### Step 1: Create the VM directory

Step 1 initializes the VM directory structure and configuration. It creates the VM directory, copies initial configuration files, and sets up the basic environment. As a result, the VM directory, configuration files, and connection profiles are created. 

### Step 2: Download Windows and VirtIO drivers

Step 2 downloads the Windows 11 ISO and VirtIO drivers. It downloads the Windows 11 Arm ISO from Microsoft, fetches VirtIO drivers, and prepares unattended installation files. The files created during this step include `installer.iso`, `virtio-win.iso`, and the unattended installation directory. This step takes some time as the Windows ISO download is large, but if you already have the file the script will save time and not repeat the download.

### Step 3: Prepare the VM disk image

Step 3 creates the VM disk image and finalizes the installation setup. It builds the unattended installation ISO, creates the main VM disk image, and configures all installation media. The files created during this step include `disk.qcow2` and `unattended.iso`.

{{% notice Note %}}
The product key used in the scripts is a generic key provided by Microsoft, which allows installation. This key is for testing purposes only and does not activate Windows. If you plan to continue using Windows beyond installation, you should replace it with a genuine product key.
{{% /notice %}}

### Step 4: Boot Windows for the first time

Step 4 executes the Windows installation. It boots the VM with installation media, runs the automated Windows setup, and completes the initial configuration. The result is a fully installed and configured Windows on Arm VM.

Each step builds on the previous one, and you can run them individually for debugging or customization purposes.

## Virtual machine execution

The `run-win11-vm.sh` script runs virtual machines by managing their execution and connectivity. 

The script begins by checking if the VM is already active by validating QEMU processes and PID files. If the VM is running, it skips to establishing an RDP connection; otherwise, it proceeds to start the VM. 

Next, the script launches the VM in headless mode, optimized for RDP access, by configuring QEMU with a headless display, setting up port forwarding, and starting the VM as a background daemon process. 

Once the VM is running, the script waits for the RDP service to become available, configures the Remmina client, and establishes a desktop connection. 

This process ensures seamless access to the VM with proper display scaling and input handling.

## Automatic resource detection and allocation

The scripts try to manage resources based on your system. 

For CPU allocation, `/proc/cpuinfo` is used to determine the total number of CPU cores and use half of the available cores for the VM. A minimum of 2 cores for creation and 4 cores for runtime are required.

For memory allocation, `/proc/meminfo` is used to determine total system RAM and allocate half of the available memory for the VM. A minimum of 2GB is required and memory usage is based on system capacity, with an option to override using a command line parameter. 

For storage, the default VM disk size is 40GB in QCOW2 format. The available disk space is validated before creation.

All settings are customizable using command line arguments. 

## Script integration and workflow

The create and run scripts share the same configuration files. Separating creation from execution enables you to create a VM once and then use the run script repeatedly. 

The next section explains how to create and run a Windows on Arm virtual machine.