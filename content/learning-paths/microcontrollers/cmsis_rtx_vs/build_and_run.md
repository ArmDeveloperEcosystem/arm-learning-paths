---
# User change
title: "Build and run the application"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
You are now ready to build and run the application.

## Build

In the CMSIS Extension view,  save all files, and click the hammer icon to build the example.

## Debug

Click the `Debug` icon, or enter the `Run and Debug` extension view.

Select the debug connection previously configured to launch the FVP.

Use the controls to step through the code.

Once the OS is initialized, the output from the threads is displayed in the `Debug Console`.

```
[model] hello from thread 1
[model] hello from thread 2
[model] hello from thread 3
[model] hello from thread 1
[model] hello from thread 2
...
```
Click `Stop` (`Ctrl`+`F5`) to terminate the debug session.

{{% notice  Note%}}
For a more feature rich debug environment, it is recommended to use `Arm Keil μVision IDE`.

See [Build an RTX5 RTOS application with Keil μVision](/learning-paths/microcontrollers/cmsis_rtx/).
{{% /notice %}}
