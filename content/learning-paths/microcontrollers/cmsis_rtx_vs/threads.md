---
# User change
title: "Create RTOS Threads"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
In this step, you will implement the main RTOS thread (`app_main`), which is primarily responsible for starting and managing the other threads in the system.

You will create three threads. The number and naming of the threads are flexible, so feel free to adjust as needed.

## Create `app_main`

Click on the `+` icon within the `Source Files` Group, and add a new file `app_main.c`. Populate with the below.

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
## Create Threads

Now you can implement the functionality of the threads themselves. Start with a simple example. Each thread will say hello, and then pause for a period, forever.

Click on the `+` icon within the `Source Files` Group, and add a new file `threads.c`. Populate with the contents below.

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
