---
# User change
title: "Import and build example project"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Before you begin

You should have Arm Development Studio installed and your license configured. Refer to the [Arm Development Studio install guide](/install-guides/armds/) for more information.

## Get started with the IDE

Launch the IDE from the applications menu for your operating system or using the command line. 

To launch from the command line run:

```console
armds_ide
```

If this is your first time opening the workspace, you will be presented with a pane to set some basic workspace configurations. You can click `Finish` to accept the default setup.  

The IDE opens a workspace, a base directory on your host machine is used to store all projects.

Optionally, you can use `File > Switch Workspace` to select a new location.

You can move individual panes around the GUI as you wish, opening other panes with the `+` button visible in the tab bar of panes.

You can select `Window > Perspective > Reset Perspective` from the menu to return to the default set up.

## Import and build an example project

Development Studio provides a number of useful example projects to help you get started. 

To import a project:

1. Click `File > Import... > Arm Development Studio > Examples & Programming Libraries` and click `Next`.

2. Expand `Examples` and expand the example types to see the available examples.

For example, expand `Armv7 Bare-Metal` and select `startup_Cortex-M3_AC6` with a check mark and click `Finish` to import the project into your workspace.

{{% notice  Filter%}}
Enter `m3` (or similar) in the text box at top of pane to easily locate the example project.
{{% /notice %}}

The imported project is now in your workspace, and can be seen in the `Project Explorer` pane.

Expand the project view to see the various source files. Click on any source to view (and edit). A detailed `readme` is provided for each project highlighting key learnings of the selected project. 

Most projects include a `.scat` file. This is a [Scatter loading](https://developer.arm.com/documentation/101754/latest/armlink-Reference/Scatter-loading-Features/The-scatter-loading-mechanism/Overview-of-scatter-loading) description file, which defines the target memory map to the linker.

3. Build the project by clicking the `hammer` icon.

The build output is shown in the `Console` pane.

## Build an example from the command line

You can also build projects from the command line, either via directly invoking the build tools, or by using make tools.

Windows users will find an `Arm DS <version> Command Prompt` in their installation. Linux users can use the supplied `suite_exec` script to set up the path to a compiler. 

To ensure the appropriate compiler is selected, enter:
```console
armclang --version
```

To build the example project above `unzip` the project from the supplied archive:.
```console
unzip <install_dir>/examples/Bare-metal_examples_Armv7.zip "startup_Cortex-M3_AC6/*" .
cd startup_Cortex-M3_AC6
```

Once in the project directory run `make` to build the project:

```console
make
```

## Understanding the compiler options

If invoking the compiler directly, a minimal set of compiler options are needed, specifying whether or not you are compiling for
* AArch32 (`--target=arm-arm-none-eabi`) or
* AArch64 (`--target=arm64-arm-none-eabi`) targets.

You must also specify a specific Arm Architecture (`-march`) or processor (`-mcpu`).

Use the list option (`-march=list` or `-mcpu=list`) to see all valid arguments for these options. For example:

```console
armclang --target=arm-arm-none-eabi -mcpu=list
```

Full details of available command line options are given in the [Arm Compiler for Embedded Reference Guide](https://developer.arm.com/documentation/101754/latest/armclang-Reference/armclang-Command-line-Options).
