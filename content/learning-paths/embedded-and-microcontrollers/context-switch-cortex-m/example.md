---
# User change
title: Example Arm DS project for demonstrate context switching operations

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
There are a set of open source example projects that made available alongside the [Armv8-M Memory Model and MPU User Guide](https://developer.arm.com/documentation/107565/latest/). The source code for these example projects is available in the [GitHub repository](https://github.com/ARM-software/m-profile-user-guide-examples/tree/main/Memory_model/rtos_context_switch).

This example demonstrates simple real-time kernel context switching operations between two threads using MPU regions that are available in Arm Cortex-M processors.
You can build and run the example project using the versions of tools and software listed below:
  - [Arm Development Studio 2022.1](/install-guides/armds/)
  - [Arm Compiler for Embedded 6.18](/install-guides/armclang/)
  - [Fast Models Fixed Virtual Platforms (FVP) 11.18](/install-guides/fm_fvp/fvp/)
  - CMSIS 5.8.0

## Overview of the example code

With this example you can create a very simple RTOS (Real Time Operating System) capable of dealing with context switching and thread isolation. For simplicity, only two threads, thread A and thread B, are created.

Basic context switching and thread isolation requirements considered for this example are listed below:
  - Two isolated threads called thread A and thread B are created
  - Both thread A and thread B are executed in unprivileged mode.
  - Each thread has its own dedicated process stack.
  - The MPU regions are set up in a way such that the data and code corresponding to Thread A is not accessible to Thread B and vice versa.
  - A System Tick Timer (SysTick) generates regular SysTick exception as an interruption to switch between threads.
  - The SysTick handler acts as real-time kernel code and is responsible for context switching. The Systick handler is also responsible for MPU reprogramming which is needed for thread isolation.
  - The MPU regions for SysTick handler are set up in a way so that both threads cannot access the memory used by kernel code (i.e.) SysTick handler.
More details about the algorithm and structure used in this example can be found in [Chapter: Use-Case-Examples of Armv8-M Memory Model and MPU User Guide](https://developer.arm.com/documentation/107565/0101/Use-case-examples/rtos-context-switch).

## Build the example project

You can build the example project with Arm Compiler for Embedded version 6.18 using the supplied Eclipse project.
To import this project, follow the guidelines in the section [Import an existing Eclipse project in the Arm Development Studio Getting Started Guide](https://developer.arm.com/documentation/101469/2022-0/Projects-and-examples-in-Arm-Development-Studio/Importing-and-exporting-projects/Import-an-existing-Eclipse-project).

To build the project within the Arm DS IDE:
1.	In the Project Explorer view, select the project you want to build.
2.	Select Project -> Build Project.

## Run the example project

The built executable from previous step can run on an Armv8-M FVP model supplied with Arm Development Studio. A ready to use launch configuration file `rtos_context_switch.launch` is provided with the example project.

Follow the steps below to run the executable using this configuration:
1.	Select Run - Debug Configurations....
2.	Select `rtos_context_switch` from the list of Generic Arm C/C++ Application configurations.
3.	Click on Debug to start debugging. The executable image will be downloaded to the target Armv8-M FVP model and the program counter is set to main.
4.	Run the executable (press F8). Text output appears in the target console view.

## Output in target console

You should see the following output in the target console view when you run this example:

```output
Pentagonal number: 2262 
Pentagonal number: 2380 
Pentagonal number: 2501 
...
Fibonacci number: 0 
Fibonacci number: 1 
Fibonacci number: 2 
Fibonacci number: 3 
```
You have now successfully run a bare-metal context switching application on an Arm Cortex-M target.
