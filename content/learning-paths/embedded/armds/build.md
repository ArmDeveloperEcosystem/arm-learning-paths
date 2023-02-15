---
# User change
title: "Import and build example project"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Prerequisites

It is assumed you have installed Arm Development Studio and configured your license. For full instructions see [here](/install-tools/armds/).

## Getting started with the IDE

Launch the IDE (`armds_ide`). If this is the first time launching the IDE, you will be presented with a pane to set some basic visual preferences. The IDE opens into a workspace, a base directory on your host machine from which all projects are located. You can use `File > Switch Workspace` to select a new location.

You can move indivudual panes around the GUI as you wish, opening other panes with the `+` button visible in the tab bar of panes. If ever you are unhappy with the look, you can select `Window > Perspective > Reset Perspective` from the menu to return to the default configuration. 

## Import and build an example project

Development Studio provides a number of useful example projects to help you get started. To import such an example, navigate the menu system to `File > Import... > Arm Development Studio > Examples & Programming Libraries > Examples`, and select an appropriate example project.

Use the text filter to facilitate this. For this example, I select the `startup_Cortex-M3_AC6` example. Click `Finish`, and the project will be imported to your workspace, and can be seen in the `Project Explorer` pane.

There is likely a `.scat` file also provided. This is a [Scatter loading](https://developer.arm.com/documentation/101754/latest/armlink-Reference/Scatter-loading-Features/The-scatter-loading-mechanism/Overview-of-scatter-loading) description file, which defines the target memory map to the linker.

Expand the project view to see the various source files. Click on any source to view (and edit). A detailed `readme` is provided for each project highlighting key learnings of the selected project. With the hammer icon, the project can be (re)built, with build output observed in the `Console` pane.

## Build an example from the command line

Projects and code-bases can also be build directly from the command line, either via directly invoking the build tools, or by using make tools.

Windows users will find an `Arm DS <version> Command Prompt` in their installation. Linux users can use the supplied `suite_exec` script to set up the appropriate compiler pathing.

See the documentation for [Windows](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Register-a-compiler-toolchain/Configure-a-compiler-toolchain-for-the-Arm-DS-command-prompt/Configure-a-compiler-toolchain-for-the-Arm-DS-command-prompt-on-Windows) and [Linux](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Register-a-compiler-toolchain/Configure-a-compiler-toolchain-for-the-Arm-DS-command-prompt/Configure-a-compiler-toolchain-for-the-Arm-DS-command-prompt-on-Linux) as appropriate.

To ensure the appropriate compiler is selected, enter:
```console
armclang --version
```
To build the above imported example project, navigate to workspace directory, and then to the imported project folder. Enter
```console
make
```
to invoke the supplied makefile, and rebuild the project.

## Compiler options

If invoking the compiler directly, a minimal set of compiler options are needed, specifying whether or not you are compiling for
* AArch32 (`--target=arm-arm-none-eabi`) or
* AArch64 (`--target=arm64-arm-none-eabi`) targets.

You must also specify a specific Arm Architecture (`-march`) or processor (`-mcpu`).

Use the list option (`-march=list` or `-mcpu=list`) to see all valid arguments for these options. For example:
```console
armclang --target=arm-arm-none-eabi -mcpu=list
```
Full details of available command line options are given in the [documentation](https://developer.arm.com/documentation/101754).

## Debug the example project

You will find a `<project_name>_FVP.launch` file within the project folder. This defines the debug connection to a supplied [Fixed Virtual Platform](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms) to execute (and debug) the example on.

Click Debug to launch the FVP, load the image (as specified in the `Files` tab), and stop at entry or a particular symbol, most likely `main` (as specified in `Debugger` tab).

Use views to inspect target registers, memory, and other views. You can control executions (step, continue, stop, etc) from the `Debug Control` pane. The `Commands` pane reflects all actions done in the GUI. The debugger can also be fully controlled by entering [commands](https://developer.arm.com/documentation/101471) in this pane.

Click the disconnect button in the `Debug Control` pane to disconnect and terminate the FVP.

Subsequent debug sessions can be launched directly from the `Debug Control` pane.
