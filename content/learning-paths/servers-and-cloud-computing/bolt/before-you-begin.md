---
title: Before You Begin
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before You Begin

These are 4 steps that will be described in more detail in the following sections. 

1. Build executable
2. Profile executable
3. Convert performance profile into BOLT file format
4. Optimise executable

This is a guide for how to optimise an Arm executable but only 1 of the steps needs to be run on the AArch64 machine. Profiling the executable needs to be run on this AArch64 machine. The other steps can be run on a 2nd machine which is mostly useful if the Arm system you are profiling would take a long time or does not have enough resource, e.g. hard drive space, to compile the BOLT tool, compile the executable or run BOLT.

If you are going to use a 2nd machine to run the more resource intensive steps these are some extra information you might need.

- If you are not compiling your executable on AArch64 you will need to cross compile and then copy the executable to the Arm machine for profiling. See this guide on [Cross Compiling](/install-guides/gcc/cross/).
- Once you have profiled the executable copy the `perf.data` back to the 2nd machine to complete the next steps.
- BOLT should be build for the native architecture of the second machine. It will still be able to optimise an AArch64 executable the same if the native architecture is not AArch64.
- The optimised executable will be AArch64 and will need to be copied back the machine that did the profiling to test it.
