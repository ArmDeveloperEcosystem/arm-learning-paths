---
# User change
title: Example project for Context-switching operation

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
As a part of [Armv8-M Memory Model and MPU User Guide](https://developer.arm.com/documentation/107565/latest/) , there are a set of open-source example projects are accompanied with the user guide. The source code for the example project is available in GitHub repository [here](https://github.com/ARM-software/m-profile-user-guide-examples/tree/main/Memory_model/rtos_context_switch). 

The goal of this example is to show a simple and easy to understand the real-time kernel context switching operations, using MPU regions concept available in Cortex-M processors. This goal is accomplished by having two threads, A and B, that switches alternatively between them and a Systick Interrupt Service Routine(ISR) that acts as a kernel code.
This example project is developed, built, and run using:
  - Arm Development Studio 2022.1
  - Arm Compiler for Embedded 6.18
  - Fast Models Fixed Virtual Platforms (FVP) 11.18
  - CMSIS 5.8.0 (available in GitHub repository)

## Scope

This is an example that shows how to create a very simple RTOS (Real Time Operating System) capable of dealing with context switching and thread isolation. For simplicity, only two threads, thread A and thread B, are created.

Basic context switching and thread isolation requirements considered for this example are listed below:
  - Two isolated threads called as thread A and thread B will be created
  - Both thread A and thread B will be executed in unprivileged mode.
  - Each thread has its own dedicated process stack.
  - The MPU regions are set up in such a way that the data and code corresponding to Thread A is not accessible to Thread B and vice versa.
  - A System Tick Timer (SysTick) generates regular SysTick exception as an interruption to switch between threads.
  - The SysTick handler acts as a real-time kernel code and is responsible for context switching. The Systick handler is also responsible for MPU reprogramming that is needed for thread isolation.
  - The MPU regions for SysTick handler is set up in such a way that it neither of the threads can access the memory used by kernel code (i.e.) SysTick handler.
More details about the algorithm and structure used in this example can be found in Chapter: Use-Case-Examples of [Armv8-M Memory Model and MPU User Guide](https://developer.arm.com/documentation/107565/latest/).

## Building the example project

This example is built with Arm Compiler for Embedded 6 using the supplied Eclipse project.
To import this project, follow the guidelines in the section "Import an existing Eclipse project" in the Arm Development Studio Getting Started Guide.
To build the projects within the Arm DS IDE:
1.	In the Project Explorer view, select the project you want to build.
2.	Select Project - Build Project.

## Running the example project

The executable is intended for running on an Armv8-M FVP model supplied with Arm Development Studio. A ready-made launch configuration rtos_context_switch.launch is provided.
1.	Select Run - Debug Configurations....
2.	Select rtos_context_switch from the list of Generic Arm C/C++ Application configurations.
3.	Click on Debug to start debugging. The executable image will be downloaded to the target and the program counter set to main.
4.	Run the executable (press F8). Text output appears in the Target Console view.

## Output in Target Console

This is part of the output in the Target Console view shown when running this example:

```
Pentagonal number: 2262 
Pentagonal number: 2380 
Pentagonal number: 2501 
...
Fibonacci number: 0 
Fibonacci number: 1 
Fibonacci number: 2 
Fibonacci number: 3 
```
