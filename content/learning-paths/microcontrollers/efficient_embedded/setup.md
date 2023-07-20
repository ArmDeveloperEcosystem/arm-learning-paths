---
# User change
title: "Set up a project in Keil MDK" 

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

In this exercise, you will execute assembly code on the `Nucleo-F401RE` board using the `Keil MDK Debugger` to examine its execution at the processor level.

This exercise is from the [Efficient Embedded Systems Education Kit](https://github.com/arm-university/Efficient-Embedded-Systems-Design-Education-Kit).

Please make sure to read and go through the [Getting Started with MDK](https://developer.arm.com/documentation/KGS1/latest/) documentation or [Learning Path](../../uv_debug/) if you are unfamiliar with its usage.

## Set up project

### CMSIS Packs

Open the `CMSIS Pack Installer` and install the necessary `CMSIS Packs` for the `STM32F401` and `Nucleo` boards.

![CMSIS-Pack #center](Images/cmsis-pack.png)

Close the Pack installer and return to the uVision IDE.

### Create project

Go to 'Project' > 'New uVision Project', and create a project.

![New Project #center](Images/NewKeilProject.png)

A window will show up requesting you to select the target device for the project. select `STM32F401RE`, as shown in this image:

![TargetBoard #center](Images/SelectDevice2.png)

### Configure project

Next, you will be required to select software components/packages that you wish to include in your project.

Add `CMSIS` > `Core` and `Device` > `Startup`.

![SoftwareComponents #center](Images/SoftwareComponents.png)

Your project should now look like this:

![ProjectExplorer #center](Images/ProjectExplorer.png)

Next you need to configure some options for the target. Select the `Options for target` icon shown below.

![TargetOptions #center](Images/TargetOptions.png)

Then under the `C/C++` tab set the `Language C` option to `c99` and the `Optimization` level to `-O1`.

![TargetOptions #center](Images/TargetOptions2.png)

Also, under the `Debug` tab, make sure to set the debugger to `ST-Link Debugger`.

![TargetOptions #center](Images/TargetOptions3.png)

You are ready to start writing the program.
