---
# User change
title: "Initialize the operating system"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
[Keil RTX5](https://www2.keil.com/mdk5/cmsis/rtx) is quite a feature rich real-time operating system (RTOS). CMSIS and the [CMSIS-RTOS2](https://arm-software.github.io/CMSIS_5/RTOS2/html/index.html) API makes it very easy to work with.

When setting up the project Run-time environment, the appropriate system initialization code (`C Startup`) was added.

From there, the `RTX5` initialization code is always essentially the same, setting up the `SysTick` timer with the [SystemCoreClockUpdate()](https://www.keil.com/pack/doc/CMSIS/Core/html/group__system__init__gr.html#gae0c36a9591fe6e9c45ecb21a794f0f0f) function, then initializing and starting the RTOS.

## Create main()

Right click on the `Source` folder under the `FVP` target, and `Add new item`.

Select `C file (.c)`, and create the `main.c`file with the contents below:

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
{{% notice  Arm Development Studio%}}
Right-click on the project, and select `New` > `Source File` from the pop-up menu.
{{% /notice %}}


## Understanding the code

The function [osKernelStart()](https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__KernelCtrl.html#ga9ae2cc00f0d89d7b6a307bba942b5221) should never return.

If your code gets to the infinite `while()` loop, something has gone wrong - most likely with the platform initialization code.

All threads use a prototype of the form:
```C
void thread(void *);
```
where the argument is passed as the second parameter of the [osThreadNew()](https://arm-software.github.io/CMSIS_6/latest/RTOS2/group__CMSIS__RTOS__ThreadMgmt.html#ga48d68b8666d99d28fa646ee1d2182b8f) function. Use `NULL` if no argument to pass.

In the above, `app_main` is used as the main application thread, but this naming is arbitrary. From here, you shall spawn all other threads of the RTOS.
