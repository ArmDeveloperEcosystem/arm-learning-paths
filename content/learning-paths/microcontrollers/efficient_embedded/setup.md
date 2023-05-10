---
# User change
title: "Setting Up A Project In Keil MDK" 

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

The first thing to do is set up a new project. Simply open Keil and go to 'Project' > 'New uVision Project'.

![New Project](Images/NewKeilProject.png)

Select an appropriate place and name for the project.

A window will show up requesting you to select the target device for the project. select the Nucleo F401RE, as shown in this image:

![TargetBoard](Images/SelectDevice2.png)

Next, you will be required to select software components/packages that you wish to include in your project. Add CMSIS > Core and Device > Startup.

![SoftwareComponents](Images/SoftwareComponents.png)

Your project should now look like this:

![ProjectExplorer](Images/ProjectExplorer.png)

Next you need to configure some options for the target. Select the 'Options for target' icon shown below.

![TargetOptions](Images/TargetOptions.png)

Then under the C/C++ tab set the 'Language C' option to 'c99' and the 'Optimization' level to '-O1'.

![TargetOptions](Images/TargetOptions2.png)

Also, under the 'Debug' tab, make sure to set the debugger to 'ST-Link Debugger'.

![TargetOptions](Images/TargetOptions3.png)

You are ready to start writing the program.