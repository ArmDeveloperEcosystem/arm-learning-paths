---
# User change
title: "Set up Code Coverage"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Prerequisites

You must have [Keil MDK](/install-guides/mdk/) installed.

Code coverage can be performed on any project that runs on a suitable target. You shall use one of the standard RTX examples that runs on the supplied Cortex-M FVP.

## Import and build the example project

Open the uVision IDE, and click to open the Pack Installer ![Pack Installer Icon](images/b_uv4_packinst.png)

In the `Devices` tree, select `ARM` > `ARM Cortex M3` > `ARMCM3` (use search text box if necessary).

With this `Device` selected, click on the `Examples` tab, and `Copy` the `CMSIS-RTOS2 Blinky (uVision Simulator)` example.

Open the project in MDK, and build.

## Set up debug with FVP

By default, this project uses the legacy simulator provided with MDK, which does not support code coverage.

To run on the FVP, open Options for Target ![Options for Target Icon](images/b_target_options.png), navigate to `Debug` pane, and select `Models Cortex-M Debugger` from the `Use:` pull-down.

Click `Settings`, and under `Command`, browse for one of the supplied FVPs in the `Keil_v5/ARM/avh-fvp/bin/models` folder of your MDK installation (eg `FVP_MPS2_Cortex-M3_MDK.exe`).

{{% notice Older MDK versions %}}
Depending on the version of MDK you have installed the path to FVP executable may differ.

MDK versions before 5.37: Keil_v5/ARM/FVP

MDK versions 5.38, 5.39: Keil_v5/ARM/VHT

MDK version 5.40 or later: Keil_v5/ARM/avh-fvp/bin/models
{{% /notice %}}

Specify a `Coverage File`, and enable `Load` and `Store` of that file. Because of the way that the data is created, code coverage cannot be updated in real-time.

{{% notice Real hardware %}}
If using real hardware, no such coverage file is needed. The data will be generated directly from the hardware. The coverage will be updated in real-time.
{{% /notice %}}

Click `OK` to save settings, then start a debug session (`Ctrl+F5`).

If not already open, navigate to `View` > `Analysis Windows` > `Code Coverage` to enable that view.

Run the application for a few seconds, going through a number of iterations of the LEDs turning on and off. Observe that the Code Coverage data is not updated (with FVP). Close the debug session, and start a new one to load the coverage data. Code coverage data is now displayed in the `Code Coverage` window.

## Investigate the code coverage output

Observe the report, detailing the percentage of instructions that have been executed for each function. Browse for an 'interesting' record, for example `osRtxThreadDelayTick`, within `rtx_thread.c`. You should see less than 100% of the instructions executed, including one or more instructions not fully executed.

Click on that function (in the `Code Coverage` window) to put the source and disassembly views in focus on that function.

Code that has been fully executed is highlighted in green.

Code that has not been executed (such as some of the switch-cases) are not highlighted.

Code that has not been fully executed is highlighted in orange or blue. What this means is, for example, a conditional branch instruction where only one of the true and false conditions have been met, and so the other branch path of that instruction has not been tested by that run. Orange means that the branch is never taken, blue that it has always been taken.

It is also possible to output the code coverage information on the MDK command line. To show all, simply use:
```command
coverage
```
You can also filter the report by source file or function. In the `Code Coverage` view by the `Module` pulldown, else on the command line with, for example:
```command
coverage \blinky.c
coverage \blinky.c\main
```
