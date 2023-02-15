---
# User change
title: "Create and setup Keil MDK project"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Install appropriate device CMSIS-Pack

This learning path is written for the supplied (Cortex-M4) FVP, however it could be run on any of the 9000+ devices supported by [CMSIS-Pack](https://www.open-cmsis-pack.org/).

This step is not necessary if using the FVP.

If using a different platform, click on `Pack Installer` icon, browse for your device, and install any suggested Device Specific pack.

## Create project in Keil MDK

In the MDK menu, navigate to `Project` > `New uVision Project`, and create a new project (recommend to locate in a new folder).

### Select device

You will then be prompted to `Select Device` for your project. A list of all devices with their CMSIS-Packs installed will be shown.

For this example, we shall select `Arm` > `Arm Cortex-M4` > `ARMCM4`.

## Manage Run-Time Environment

You will first be presented with the `Manage Run-Time Environment` dialog, which allows you to specify the CMSIS software components that will be used in the project.

Under `CMSIS`, select `CORE`, as well as `RTOS2 (API)` > `Keil RTX5`, in `Library` form.

Under `Device`, select `Startup` (`C Startup`).

These are the minimal components needed for such an application. Click `OK`.

## Rename target

A project can contain many `targets`, which refer to the platform that a particular build will run on. The default name is `Target 1`. To give a meaningful name, click `Manage Project Items`, and rename the target (for example, to `FVP`), as well as optionally the `Source Group 1` (to `Source`) that will contain the source code. Arranging code in these folders allows for easy sharing across different target builds.

## Target options

Click `Options for Target`, to open that dialog. This is where build and other settings can be made.

### Set FVP as debug target

Navigate to the `Debug` tab, and select `Models Cortex-M Debugger` from the `Use` pull-down list. Click `Settings`, then the `Command` browse (`...`) button, to locate the `Cortex-M4 FVP` within your Keil MDK installation (`ARM\FVP\MPS2_Cortex-M` folder). Click `OK`.

### Compiler optimization options

Navigate to `C/C++ (AC6)` tab, and (optionally) change optimization level to `-O2` for high performance code.
You may also wish to disable `Warnings`, change language options or other settings.

### Define memory map

We shall use [scatter-loading](https://developer.arm.com/documentation/101754/latest/armlink-Reference/Scatter-loading-Features/The-scatter-loading-mechanism/Overview-of-scatter-loading) to define the memory map.

The memory map for the FVP is given in the [documentation](https://developer.arm.com/documentation/100964/latest/Microcontroller-Prototyping-System-2/MPS2---memory-maps/MPS2---memory-map-for-models-without-the-Armv8-M-additions).

Navigate to the `Linker` tab, and de-select `Use Memory Layout from Target Dialog`. Click the browse (`...`) button and create a text file in the same folder as the project. Click `Edit` to open the file in the IDE. The following is a typical scatter file for the FVP.
```text
LOAD 0x0 0x400000 {
	ROOT 0x0 0x400000 {
		*.o (RESET, +First)
		*(InRoot$$Sections)
		.ANY (+RO)   }

	RAM 0x20000000 0x40000 {
		.ANY (+RW +ZI)     }

	ARM_LIB_HEAP  0x20040000 EMPTY 0x10000 {}

	ARM_LIB_STACK 0x20050000 EMPTY 0x10000 {}
}
```
For more on scatter-loading, see this [learning path](/learning-paths/embedded/bare-metal).

We are now ready to build our example.

## Comments for Arm Development Studio users
* Add required CMSIS-Packs via the `CMSIS Pack Manager` perspective.
* When creating the project navigate the menu to `File` > `New` > `Project...` > `C/C++` > `C Project`, then select `CMSIS C/C++ Project`, using `Arm Compiler for Embedded 6`.
* Run-time environment is managed by the `.rteconfig` file within the project.
* Build settings are in the `Project Properties` (`Alt+Enter`), under `C/C++ Build` > `Settings`.
* Debug configuration will be set later.
