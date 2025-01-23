---
# User change
title: "Build and run the application"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
You are now ready to build and run your application.

## Build

In the CMSIS Extension view,  save all your files. Then, click the hammer icon to build the example.

## Debug

To start debugging, click the `Debug` icon, or enter the `Run and Debug` extension view.

Choose the debug connection you configured earlier to launch the FVP (Fixed Virtual Platform).

Use the debugging controls to step through your code.

Once the OS is initialized, you will see the output from the threads displayed in the `Debug Console`.

```
[model] hello from thread 1
[model] hello from thread 2
[model] hello from thread 3
[model] hello from thread 1
[model] hello from thread 2
...
```
To end the debug session, click `Stop` or press `Ctrl`+`F5`.

{{% notice  Note%}}
For a more feature-rich debugging environment, consider using the `Arm Keil μVision IDE`.

For more details, see [Build an RTX5 RTOS application with Keil μVision](/learning-paths/embedded-and-microcontrollers/cmsis_rtx/).
{{% /notice %}}
