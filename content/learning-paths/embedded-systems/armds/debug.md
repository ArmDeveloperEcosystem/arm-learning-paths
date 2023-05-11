---
# User change
title: Debug the example

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
Arm Development Studio provides a library of [Fixed Virtual Platforms (FVPs)](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms) to execute (and debug) the example on without the need for any target hardware.

If you have hardware, you may wish to run the example on that. The supplied Cortex-M FVPs are digital twins of the [MPS2+](https://developer.arm.com/Tools%20and%20Software/MPS2%20Plus%20FPGA%20Prototyping%20Board) platform, in this case programmed for Cortex-M3 (`AN385`).

## Debug the example project with FVP

The project contains `startup_Cortex-M3_AC6_FVP.launch` within the project folder. This is a ready-to use debug configuration for the FVP.

1. Double-click on the `.launch` file to inspect. Observe settings in various panes, defining the FVP to connect to, the image to be loaded, and other connection options.

2. Click `Debug` to start the debug session.

{{% notice  %}}
Subsequent debug sessions can be launched directly from the `Debug Control` pane.
{{% /notice %}}

## Debug the example project with MPS2+

The project contains `startup_Cortex-M3_AC6_MPS2.launch` within the project folder.

1. Double-click on the `.launch` file to inspect. Observe settings in various panes, defining the MPS2+ configuration to connect to, the image to be loaded, and other connection options.

2. From the `Target Connection` pulldown, select the debug adapter used to connect to the target. `CMSIS-DAP` is an on-board debug adapter that connects via USB, and so no additional hardware is needed.

3. Click `Browse` to identify your debug adapter, then click `Apply` to save.

4. Click `Debug` to start the debug session.

{{% notice  %}}
Subsequent debug sessions can be launched directly from the `Debug Control` pane.
{{% /notice %}}


## Navigate the GUI

You can control execution (`step`, `continue`, `stop`, etc) from the buttons in the `Debug Control` pane.

The `Commands` pane reflects all actions done in the GUI. The debugger can also be fully controlled by entering [commands](https://developer.arm.com/documentation/101471) in this pane.

Explore the various [views](https://developer.arm.com/documentation/101470/latest/Perspectives-and-Views) to understand how to use the debugger. There are `Register`, `Memory`, `Stack`, `Disassembly`, and many other views available. To open new views, use `Window` > `Show View` menu option, or click the `+` icon alongside already opened views.

Click the disconnect button in the `Debug Control` pane (or use `quit` command) to end the debug session.
