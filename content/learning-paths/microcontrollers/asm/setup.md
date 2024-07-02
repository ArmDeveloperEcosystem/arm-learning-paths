---
# User change
title: "Setting Up A Project In Keil MDK" 

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
Though Cortex-M processors have been designed so that all operations can be programmed with C/C++ code, it can be useful to also understand how to create assembler level code, which can be more efficient than compiler generated code.

You will write assembly level functions conforming to the [Arm Procedure Call Standard](https://github.com/ARM-software/abi-aa/blob/main/aapcs32/aapcs32.rst).

[Keil MDK](https://www2.keil.com/mdk5) is used as the toolchain. For installation instructions, refer to the [Keil MDK install guide](/install-guides/mdk/).

## Efficient Embedded Systems Education Kit

This Learning Path is based on examples from the [Efficient Embedded Systems Education Kit](https://github.com/arm-university/Efficient-Embedded-Systems-Design-Education-Kit), which uses the [Nucleo-F401RE](https://www.st.com/en/evaluation-tools/nucleo-f401re.html) development board.

You will use the Cortex-M4 Fixed Virtual Platform provided with MDK.

## Create MDK Project

The first thing to do is set up a new project. Go to 'Project' > 'New uVision Project'.

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
MDK versions before 5.37 will find the FVP at

`Keil_v5/ARM/FVP/MPS2_Cortex-M/FVP_MPS2_Cortex-M4_MDK.exe`

and in 5.38, 5.39 it is available at

`Keil_v5/ARM/VHT/VHT_MPS2_Cortex-M4_MDK.exe`
{{% /notice %}}

### Configure build settings

In the `C/C++` tab, set the `Optimization` level to `-O1`.

In the `Linker` tab, deselect `Use Memory Layout from Target Dialog`. and a `Scatter File` will be created. Click the `Edit` button to open in the background. Click `OK` to save all `Options`.

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
