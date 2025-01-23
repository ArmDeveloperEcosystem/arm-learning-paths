---
# User change
title: "Setting up a Project in Keil Studio (VS Code)" 

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
{{% notice  Note%}}
If using Keil μVision, go to [Setting up a Project in Keil MDK (μVision)](/learning-paths/embedded-and-microcontrollers/asm/setup_mdk5/).
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

Select `CMSIS > Core` and `Device > Startup` (these are likely selected by default).

Close this view to save.

## Configure debug with the FVP

Select `Run and Debug` from the Extensions icon list.

Click the gear icon to open `launch.json`. This is the file that defines the debug instance.

Right-click on `launch.json` and select `Open Run and Debug Configuration`.

From the `Selected Configuration` pull-down, select `New Configuration` > `Launch FVP`. Edit the `Configuration Name` if desired.

From the `Target` > `Configuration Database Entry` pull-down, select `MPS2_Cortex_M4` > `Cortex-M4`.

Other fields can be left as default. Close the file to save. Observe that `launch.json` has been updated.

## Configure scatter file

Return to the `CMSIS` extension. The project is configured to use the `ARMCM4_ac6.sct` file as the scatter description file.

Click the file to create it with the following:

```text
LR_IROM1 0x00000000 0x00040000  {    ; load region size_region
    ER_IROM1 0x00000000 0x00040000  {  ; load address = execution address
        *.o (RESET, +First)
        *(InRoot$$Sections)
        .ANY (+RO)
        .ANY (+XO)
    }
    RW_IRAM1 0x20000000 0x00020000  {  ; RW data
        .ANY (+RW +ZI)
    }
    ARM_LIB_STACK 0x20020000 EMPTY 0x4000 {}
}
```
Close to save.

## main.c

The project automatically creates `main.c` within the `Source Files` group. We will modify this in the [Writing assembly functions](/learning-paths/embedded-and-microcontrollers/asm/coding/) section.

{{% notice  Note%}}
`Next` button below goes to μVision settings. Go to [Writing assembly functions](/learning-paths/embedded-and-microcontrollers/asm/coding/) to skip this section.
{{% /notice %}}
