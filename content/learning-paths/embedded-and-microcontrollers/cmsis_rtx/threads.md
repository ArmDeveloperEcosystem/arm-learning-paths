---
# User change
title: "Create RTOS threads"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
Implement the main RTOS thread (`app_main`), whose role is primarily to start and manage the other threads of the system.

In this example you shall create 3 threads. The number and naming of the threads is arbitrary.

## Create app_main

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

You can now implement the functionality of the threads themselves. Start with a simple example... each thread will say hello, and then pause for a period, forever.

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
