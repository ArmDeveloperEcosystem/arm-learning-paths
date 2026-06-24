---
# User change
title: "Create csolution project"
description: Create a csolution project in Keil Studio for VS Code and configure CMSIS components for an RTX5 application.

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
You'll create a basic RTX-based RTOS application using [CMSIS](https://www.keil.arm.com/cmsis) and [Keil Studio for VS Code](/install-guides/keilstudio_vs/).

The steps use the **Cortex-M4 Fixed Virtual Platform (FVP)**, but you can follow along with any of the 10,000+ devices supported by [CMSIS-Pack](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/index.html/).

{{% notice  Note%}}
If using `Arm Keil μVision IDE` or Arm Development Studio, refer to the [Build an RTX5 RTOS application with Keil μVision](/learning-paths/embedded-and-microcontrollers/cmsis_rtx/) guide.
{{% /notice %}}

## Create a new project

Keil Studio projects are based on the [CMSIS Solution](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/blob/main/docs/YML-Input-Format.md) standard.

1. Open VS Code and select **File** > **New File**. When prompted for the file type, select **New Solution** (**Arm CMSIS Solution**).
2. The **Create New Solution** dialog opens. Select the **Target Device** drop-down and search for `ARMCM4`.
3. From the **Templates, Reference Applications, and Examples** drop-down, select **Blank Solution**.
4. Ensure **Arm Compiler 6** is the selected compiler.
5. Enter an appropriate **Solution Name**. This defines the folder name the project is created into. You can also change the folder location if necessary.
6. Select **Create**. You'll be prompted to open the solution in the current window or a new window.

## Configure the solution environment

VS Code allows complete configurability of all aspects of the project.

- Locate `vcpkg-configuration.json` within the project. This file defines the components used.
- Right-click on this file and select **Configure Arm Tools Environment** to open the configuration panel.

From the dropdown menus, make sure to select the most up-to-date versions of the following:

- Arm CMSIS-Toolbox
- Arm Compiler for Embedded
- Arm Debugger
- Arm Virtual Hardware for Cortex-M based on Fast Models
- Kitware's CMake tool
- Ninja Build

Set all other tools to **None** as they are not needed for this example.

If you open `vcpkg-configuration.json` in the text editor, you’ll see these selections reflected. Close the file to save your changes.

All necessary components will be downloaded and installed as necessary (if not already installed).

## Configure CMSIS options

1. Select **CMSIS** from the Extensions icon list in VS Code. You'll see the project structure.
2. Hover over the top-level project and select **Manage Software Components** to add CMSIS software packs to your project.

Enable the following components:
* `CMSIS > Core`
* `CMSIS > OSTick > SysTick`
* `CMSIS > RTOS2 > Keil RTX`
* `Device > Startup`

You may need to select **Software packs: All packs** from the drop-down.

If prompted in the **Validation** pane, select the latest available version for each. Use the `CMSIS-RTX` pack if others are shown.

Close this view to save.

## Define the memory map

Use [scatter-loading](https://developer.arm.com/documentation/101754/latest/armlink-Reference/Scatter-loading-Features/The-scatter-loading-mechanism/Overview-of-scatter-loading) to define the memory map to the linker.

The memory map for the FVP is given in the [documentation](https://developer.arm.com/documentation/100964/latest/Microcontroller-Prototyping-System-2/MPS2---memory-maps/MPS2---memory-map-for-models-without-the-Armv8-M-additions).

The project should be configured to use `ARMCM4_ac6.sct` as the scatter file. Locate this file in the CMSIS Extension view and select it to create.

Populate with the following.

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

## Configure debug with the FVP

1. Select **Run and Debug** from the Extensions icon list.
2. Select the gear icon to open `launch.json`. This file defines the debug instance.
3. Right-click on `launch.json` and select **Open Run and Debug Configuration**.

From the **Selected Configuration** drop-down, select **New Configuration** > **Launch FVP**. Edit the **Configuration Name** if desired.

From the **Target** > **Configuration Database Entry** drop-down, select **MPS2_Cortex_M4** > **Cortex-M4**.

Leave other fields as default. Observe that `launch.json` has been updated.

Close the file to save your configuration.
