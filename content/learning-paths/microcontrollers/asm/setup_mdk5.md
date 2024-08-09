---
# User change
title: "Setting up a Project in Keil MDK (μVision)"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Create MDK Project

The first thing to do is set up a new project. Go to 'Project' > 'New μVision Project'.

Select an appropriate place and name for the project.

### Configure CMSIS options

A window will show up requesting you to select the target device for the project. Use the `Search` to locate `ARMCM4`. Select and click `OK`.

You will next be prompted to select software components that you wish to include in your project. Select `CMSIS > Core` and `Device > Startup`. Click `OK`.

### Configure the FVP

Click the `Options for target` icon.

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

### Configure build settings

In the `C/C++` tab, set the `Optimization` level to `-O1`.

In the `Linker` tab, deselect `Use Memory Layout from Target Dialog`. and a `Scatter File` will be created.

Click the `Edit` button to open in the background.

Click `OK` to save all `Options`.

In this scatter file, add a region `ARM_LIB_STACK`. The C library initialization code will initialize the stack at the top of this region.
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
### Rename Project items (optional)

Rename `Target 1` and `Source Group 1` to more meaningful names, via the `Project > Manage... > Project Items` menu.

## Basic functionality

### New C source file

Right-click `Source Group 1` and select `Add New Item`. Select `C file (.c)`.

### Build

Save all files, and click the `Build` button (`F7`).

### Debug

Click the `Debug` button (`Ctrl+F5`) to load the example to the FVP. The code will stop at `main()`.
