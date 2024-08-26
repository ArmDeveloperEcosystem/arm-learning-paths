---
# User change
title: "Create csolution project"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
This learning path will introduce the steps to create a basic RTX based RTOS application, making use of the latest features of [CMSIS](https://www.keil.arm.com/cmsis).

For more information on the latest update, see the [CMSIS v6 is here](https://community.arm.com/arm-community-blogs/b/tools-software-ides-blog/posts/cmsis-v6-is-here) blog.

You will use [Keil Studio for VS Code](/install-guides/keilstudio_vs) in this Learning Path.

This Learning Path is written for the supplied (Cortex-M4) Fixed Virtual Platform (FVP), however it could be run on any of the 10000+ devices supported by [CMSIS-Pack](https://www.open-cmsis-pack.org/).

{{% notice  Note%}}
If using `Arm Keil μVision IDE` (or `Arm Development Studio`) please go to [Build an RTX5 RTOS application with Keil μVision](/learning-paths/microcontrollers/cmsis_rtx/).
{{% /notice %}}

## Create a new project (csolution)

Keil Studio projects are based on the [CMSIS Solution](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/blob/main/docs/YML-Input-Format.md) standard.

Open the `VS Code` IDE, and select `File` > `New File` from the `File` menu. (`Ctrl`+`Alt`+`Windows`+`N`). You will be prompted for the type of file. Select `New Solution` (`Arm CMSIS Solution`).

The `Create New Solution` window will open. Click the `Target Device` pulldown, and search for `ARMCM4`.

From the `Templates, Reference Applications, and Examples` pulldown, select `Blank Solution`.

Ensure `Arm Compiler 6` is the selected compiler.

Enter an appropriate `Solution Name`. This will define the folder name that the project will be created into. You can also change the folder location if necessary.

Click `Create`. You will be prompted to open the solution in the current window, or open a new window.

## Configure solution environment

VS Code allows complete configurability of all aspects of the project.

Locate `vcpkg-configuration.json` within the project. This file defines the components used.

Right-click on this file, and select `Configure Arm Tools Environment` to open the configuration panel.

From the various pull-downs, ensure that the most up to date versions of the following are selected:

* Arm CMSIS-Toolbox
* Arm Compiler for Embedded
* Arm Debugger
* Arm Virtual Hardware for Cortex-M based on Fast Models
* Kitware's cmake tool
* Ninja Build

Others can be set as `None` as they are not needed for this example.

If you open `vcpkg-configuration.json` in the text editor you will see these set as selected. Close the file to save.

All necessary components will be downloaded and installed as necessary (if not already installed).

## Configure CMSIS options

Select `CMSIS` from the Extensions icon list. You will see the project structure.

Move cursor over the top-level `Project`, and click on `Manage Software Components`. This is the view to add CMSIS Software Packs to your project.

Enable the following components:
* `CMSIS > Core`
* `CMSIS > OSTick > SysTick`
* `CMSIS > RTOS2 > Keil RTX`
* `Device > Startup`

You may need to select `Software packs: All packs` from the pull down.

If prompted in the `Validation` pane, select the latest available version for each. Use the `CMSIS-RTX` pack if others are shown.

Close this view to save.

## Define memory map

Use [scatter-loading](https://developer.arm.com/documentation/101754/latest/armlink-Reference/Scatter-loading-Features/The-scatter-loading-mechanism/Overview-of-scatter-loading) to define the memory map to the linker.

The memory map for the FVP is given in the [documentation](https://developer.arm.com/documentation/100964/latest/Microcontroller-Prototyping-System-2/MPS2---memory-maps/MPS2---memory-map-for-models-without-the-Armv8-M-additions).

The project should be configured to use `ARMCM4_ac6.sct` as the scatter file. Locate this file in the CMSIS Extension view, and click to create.

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

Select `Run and Debug` from the Extensions icon list.

Click the gear icon to open `launch.json`. This is the file that defines the debug instance.

Right-click on `launch.json` and select `Open Run and Debug Configuration`.

From the `Selected Configuration` pull-down, select `New Configuration` > `Launch FVP`. Edit the `Configuration Name` if desired.

From the `Target` > `Configuration Database Entry` pull-down, select `MPS2_Cortex_M4` > `Cortex-M4`.

Other fields can be left as default. Observe that `launch.json` has been updated.

Close the file to save.
