---
# User change
title: "Create RTOS threads"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
We shall now implement the main RTOS thread (`app_main()`), whose role is primarily to start and manage the other threads of the system.

In this example we shall create 3 threads. The number and naming of the threads is arbitrary.

## Create app_main()

Right click on the `Source` folder under the `FVP` target, and `Add a new item`. Select `C file (.c)`, and create the `app_main.c` file with the contents below:

```C
#include "cmsis_os2.h"

void thread1(void *);
void thread2(void *);
void thread3(void *);

void app_main (void *argument) {
	osThreadNew(thread1, NULL, NULL);	// Create thread1
	osThreadNew(thread2, NULL, NULL);	// Create thread2
	osThreadNew(thread3, NULL, NULL);	// Create thread3
}
```
## Create threads

We can now implement the functionality of the threads themselves. Let's start with a simple example... each thread will say hello, and then pause for a period, forever.

Right click on the `Source` folder under the `FVP` target, and `Add a new item`. Select `C file (.c)`, and create the `threads.c` file with contents below:
```C
#include "cmsis_os2.h"
#include <stdio.h>

void __attribute__((noreturn)) thread1(void *argument){
	for(;;){
		printf("hello from thread 1\n");
		osDelay(1000);
	}
}

void __attribute__((noreturn)) thread2(void *argument){
	for(;;){
		printf("hello from thread 2\n");
		osDelay(1000);
	}
}

void __attribute__((noreturn)) thread3(void *argument){
	for(;;){
		printf("hello from thread 3\n");
		osDelay(1000);
	}
}
```
## Build and run the example

Save all files, and click `build` (`F7`) the example.

Click `Debug` (`Ctrl+F5`) to launch the FVP, and put the IDE into debug mode.
* Use the menu (`View` > `Watch Windows` > `RTX RTOS`) to observe the RTOS features.
* Use the menu (`View` > `Serial Windows` > `Debug (printf)`) to observe the printf output.

Click `Run` (`F5`) to start the application.

Observe in the `RTX RTOS` view that the threads have been created. Two other threads, `osRtxIdleThread` and `osRtxTimerThread` will also be created.

However no output is seen in the `printf viewer`. This is because semihosting is not supported by uVision.

[Event Recorder](https://www.keil.com/pack/doc/compiler/EventRecorder/html/index.html) can be used instead for the printf functionality. It is supported for both FVPs and real hardware. In the next section, we will cover how to use the Event Recorder functionality with this example.

## Comments for Arm Development Studio users
* Recommend to create debug configuration after project has been built.
  * Navigate the menu to `File` > `New` > `Model Connection`.
  * Create a Debug connection, and associate it with your project.
  * Select the `MPS2_Cortex-M4` from the selection of FVPs Installed with Arm DS.
  * In the Debug configuration view:
    * Navigate to `Files` tab, and browse for your image.
	* Navigate to `Debugger` tab, and `Debug from symbol (main)`
	* Navigate to `OS Awareness` tab, and select `Keil CMSIS-RTOS RTX` from the pull-down.
  * When debugging, use the `OS Data` pane to observe RTOS information.
* Arm Debugger does support semihosting. You will see the printf() output in `Target Console` pane.
* Arm Debugger does not support Event Recorder Viewer.
