---
# User change
title: "Initialize the Operating System"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
[Keil RTX5](https://www2.keil.com/mdk5/cmsis/rtx) is a feature-rich real-time operating system (RTOS). CMSIS and the [CMSIS-RTOS2](https://arm-software.github.io/CMSIS_5/RTOS2/html/index.html) API makes it easy to work with.

When setting up the project's Run-Time Environment, ensure you add the appropriate system initialization code (`C Startup`).

Once this is done, the `RTX5` initialization code is typically the same. It involves setting up the `SysTick` timer with the [SystemCoreClockUpdate()](https://www.keil.com/pack/doc/CMSIS/Core/html/group__system__init__gr.html#gae0c36a9591fe6e9c45ecb21a794f0f0f) function, then initializing and starting the RTOS.

## Create `main()`

Return to the `CMSIS` view.

Within the `Source Files` group, a `main.c` is automatically created. Click on the file to open it in the text editor.

Delete any auto-generated code and replace it with the following:

```C
#include "RTE_Components.h"
#include  CMSIS_device_header
#include "cmsis_os2.h"

void app_main(void *);

int __attribute__((noreturn)) main (void) {
    SystemCoreClockUpdate();                    // initialize clocks etc

	osKernelInitialize();                       // initialize RTOS

	osThreadNew(app_main, NULL, NULL);          // Create application main thread

	if (osKernelGetState() == osKernelReady)    // If all OK...
		osKernelStart();                        // Start thread execution

	while(1);                                   // If you get to here, something has gone wrong!
}
```

## Understanding the Code

The function [osKernelStart()](https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__KernelCtrl.html#ga9ae2cc00f0d89d7b6a307bba942b5221) is designed to never return.

If your code reaches the infinite `while()` loop, something has gone wrong - most likely with the platform initialization code.

All threads should follow a prototype like this:
```C
void thread(void *);
```
The argument for this function is provided as the second parameter of the [osThreadNew()](https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__ThreadMgmt.html#ga48d68b8666d99d28fa646ee1d2182b8f) function. Use `NULL` if no argument to pass.

In the example above, `app_main` is used as the main application thread, but this naming is arbitrary. From here, you will spawn all other threads in the RTOS.

{{% notice %}} Tip: Naming the main application thread is flexible. Choose a name that clearly reflects its function. {{% /notice %}}
