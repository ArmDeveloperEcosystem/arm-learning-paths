---
# User change
title: "Create and setup Keil MDK project"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
This learning path will introduce the steps to create a basic RTX based RTOS application, making use of the latest features of [CMSIS](https://www.keil.arm.com/cmsis).

For more information on the latest update, see the [CMSIS v6 is here](https://community.arm.com/arm-community-blogs/b/tools-software-ides-blog/posts/cmsis-v6-is-here) blog.

You will use [Keil MDK](/install-guides/mdk) through this Learning Path. If you are using [Arm Development Studio](/install-guides/armds) refer to the appropriate comments.

{{% notice  Note%}}
If using `Arm Keil Studio for Visual Studio Code` please go to [Build an RTX5 RTOS application with Keil Studio (VS Code)](/learning-paths/embedded-and-microcontrollers/cmsis_rtx_vs/).
{{% /notice %}}

## Install (update) to latest CMSIS Packs

Open the 'Pack installer' and install the latest CMSIS packs. At a minimum the following should be installed for this learning path:

* `ARM::CMSIS`
* `ARM::CMSIS-RTX`
* `ARM::CMSIS-View`

{{% notice  Arm Development Studio%}}
Add required `CMSIS-Packs` via the `CMSIS Pack Manager` perspective.
{{% /notice %}}

## Install appropriate device CMSIS-Pack

This Learning Path is written for the supplied (Cortex-M4) Fixed Virtual Platform (FVP), however it could be run on any of the 10000+ devices supported by [CMSIS-Pack](https://www.open-cmsis-pack.org/).

In `Pack Installer` browse for your device, and install any suggested `Device Specific` pack.

## Create project in Keil MDK

In the MDK menu, navigate to `Project` > `New uVision Project`, and create a new project (recommend to locate in a new folder).

{{% notice  Arm Development Studio%}}
When creating the project navigate to `File` > `New` > `Project...` > `C/C++` > `C Project`.

Then select `CMSIS C/C++ Project`, using `Arm Compiler for Embedded 6`.
{{% /notice %}}

### Select device

You will then be prompted to `Select Device` for your project. A list of all devices with their CMSIS-Packs installed will be shown.

For this example, select `Arm` > `Arm Cortex-M4` > `ARMCM4`. Click `OK`.

## Manage Run-Time Environment

You will first be presented with the `Manage Run-Time Environment` dialog, which allows you to specify the CMSIS software components that will be used in the project.

Under `CMSIS`, select `CORE`, as well as `RTOS2 (API)` > `Keil RTX5`, in `Source` form. You will also need to select `CMSIS` > `OS Tick (API)` > `SysTick`.

Under `Device`, select `Startup` (`C Startup`).

These are the minimal components needed for such an application. Click `OK`.

{{% notice  Arm Development Studio%}}
Run-time environment is managed by the `.rteconfig` file within the project.
{{% /notice %}}

## Rename target

A project can contain many targets, which refer to the platform that a particular build will run on. The default name is `Target 1`. To give a meaningful name, click `Manage Project Items`, and rename the target (for example, to `FVP`), as well as optionally the `Source Group 1` (to `Source`) that will contain the source code. Arranging code in these folders allows for easy sharing across different target builds.

Click `OK` to save.

{{% notice  Arm Development Studio%}}
Default `Configuration` names are `Debug` and `Release`.

Name and other settings (see below) are managed in `Project Properties` (`Alt+Enter`), under `C/C++ Build` > `Settings`.
{{% /notice %}}

## Target options

Click `Options for Target`, to open that dialog. This is where build and other settings can be made.

### Set FVP as debug target


### Configure the FVP

In the `Debug` tab, select `Models Cortex-M Debugger`. Click `Settings`, and browse for the FVP provided with MDK in the `Command` pane.
```
Keil_v5/ARM/avh-fvp/bin/models/FVP_MPS2_Cortex-M4_MDK.exe
```

{{% notice  Note%}}
MDK versions 5.37 and earlier will find the FVP at:

`Keil_v5/ARM/FVP/MPS2_Cortex-M/FVP_MPS2_Cortex-M4_MDK.exe`

In 5.38 and 5.39 the FVP is installed at:

`Keil_v5/ARM/VHT/VHT_MPS2_Cortex-M4_MDK.exe`

In 5.40 and later the FVP is installed at:

`Keil_v5/ARM/avh-fvp/bin/models/FVP_MPS2_Cortex-M4_MDK.exe`
{{% /notice %}}

{{% notice  Arm Development Studio%}}
Ignore this step for now. Debug configuration will be set up later.
{{% /notice %}}

### Compiler optimization options

Navigate to `C/C++ (AC6)` tab, and (optionally) change optimization level to `-O2` for high performance code.
You may also wish to disable Warnings, change language options, or other settings.

### Define memory map

Use [scatter-loading](https://developer.arm.com/documentation/101754/latest/armlink-Reference/Scatter-loading-Features/The-scatter-loading-mechanism/Overview-of-scatter-loading) to define the memory map to the linker.

The memory map for the FVP is given in the [documentation](https://developer.arm.com/documentation/100964/latest/Microcontroller-Prototyping-System-2/MPS2---memory-maps/MPS2---memory-map-for-models-without-the-Armv8-M-additions).

Navigate to the `Linker` tab, and de-select `Use Memory Layout from Target Dialog` (as you shall create your own).

Click the browse (`...`) button and create a text file in the same folder as the project.

Click `Edit` to open the file in the IDE. The following is a typical scatter file for the FVP.
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
{{% notice  Arm Development Studio%}}
The IDE recognizes `.sct` files as scatter files, and provides a graphical representation of the layout in a `Memory Map` tab.
{{% /notice %}}
