---
title: Deploying LTO
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deploying LTO

### A Simple Use Case
Using link-time optimization with GCC can be as simple as passing the `-flto` flag during compilation and linking.

For a traditional, stepwise build of an executable, you would compile each translation unit with LTO enabled:
```bash
gcc -c -O2 -flto component-1.c
gcc -c -O2 -flto component-2.c
gcc -o myprog -flto -O2 component-1.o component-2.o
```
In this case, each object file contains LTO information, and the final link step performs whole-program optimization before generating machine code.

For small programs, this can be simplified into a single command:
```bash
gcc -o myprog -flto -O2 component-1.c component-2.c
```
Both approaches produce an executable that benefits from link-time optimization across all translation units.

### Modifying LTO behaviour
#### Flexible object files

When compiling with `-flto`, GCC normally emits **slim LTO objects**. These object files contain only GCC’s internal intermediate representation and no conventional machine code. As a result, they can only be linked by an LTO-capable linker invocation.
In some cases—such as when building libraries intended for broader reuse, it may be desirable to retain conventional object code alongside the LTO data. This can be achieved using the `-ffat-lto-objects` flag, for example:
```bash
gcc -c -O2 -flto -ffat-lto-objects component-1.c
```
With this option enabled, GCC emits both:
  * The intermediate representation used for LTO, and
  * The non-LTO object code that would normally be produced
    
Such fat LTO objects provide greater compatibility at the cost of increased object file size.

#### Parallelization
Link-time optimization can be computationally expensive, especially for larger programs. GCC supports parallelizing LTO to reduce build times.

This behavior is controlled through the `-flto` flag:

  * -flto=auto enables automatic parallelization based on available system resources
  * -flto=<n> explicitly specifies the number of parallel LTO jobs to run
    
For example:  
```bash
gcc -O2 -flto=4 -o myprog component-1.c component-2.c
```
When parallelization is enabled, GCC partitions the program into multiple units of roughly equal size. The compiler attempts to minimize cross-partition references, which could otherwise reduce the effectiveness of certain whole-program optimizations.

#### Caching
During code development, it is possible to cache the outputs of translational units inside LTO, thus significantly shortening edit-compile cycles. This can be achieved using the `-flto-incremental=<path>` flag.
