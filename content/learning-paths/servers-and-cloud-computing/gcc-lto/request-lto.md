---
title: Deploying LTO
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deploy LTO

### A simple use case

Enable link-time optimization with GCC by passing the `-flto` flag during both compilation and linking.

For a traditional, stepwise build of an executable, compile each translation unit with LTO enabled:
```bash
gcc -c -O2 -flto component-1.c
gcc -c -O2 -flto component-2.c
gcc -o myprog -flto -O2 component-1.o component-2.o
```
Each object file contains LTO information embedded in special sections. The final link step performs whole-program optimization before generating machine code.

For small programs, you can simplify this into a single command:
```bash
gcc -o myprog -flto -O2 component-1.c component-2.c
```
Both approaches produce an executable that benefits from link-time optimization across all translation units. The `-O2` optimization level is recommended as a baseline, though you can also use `-O3` for more aggressive optimizations.

### Modify LTO behavior

#### Flexible object files

When compiling with `-flto`, GCC normally emits **slim LTO objects**. These object files contain only GCC's internal intermediate representation (GIMPLE bytecode) and no conventional machine code. As a result, they can only be linked by an LTO-capable linker invocation.

For libraries intended for broader reuse—or when you need compatibility with non-LTO builds—you can retain conventional object code alongside the LTO data using the `-ffat-lto-objects` flag:

```bash
gcc -c -O2 -flto -ffat-lto-objects component-1.c
```

With this option enabled, GCC emits both:

- The intermediate representation used for LTO
- The non-LTO object code that would normally be produced
    
Fat LTO objects provide greater compatibility at the cost of increased object file size (typically 1.5-2x larger). Use this option when building static or shared libraries that might be linked without LTO.

#### Parallelization
Link-time optimization can be computationally expensive, especially for larger programs. GCC supports parallelizing LTO to reduce build times by distributing the optimization work across multiple CPU cores.

Control this behavior through the `-flto` flag:

- `-flto=auto` enables automatic parallelization based on available system resources
- `-flto=<n>` explicitly specifies the number of parallel LTO jobs to run
    
For example:  
```bash
gcc -O2 -flto=4 -o myprog component-1.c component-2.c
```
When parallelization is enabled, GCC partitions the program into multiple units of roughly equal size. The compiler attempts to minimize cross-partition references, which could otherwise reduce the effectiveness of certain whole-program optimizations. For best results, set the parallelization level to match the number of available CPU cores.

#### Caching
During iterative development, repeatedly recompiling with LTO can increase build times. GCC provides support for caching intermediate LTO results to speed up incremental builds by reusing previously computed optimization information.

Enable this using the `-flto-incremental=<path>` option:

```bash
gcc -O2 -flto -flto-incremental=lto-cache -c component-1.c
```

When enabled, GCC stores intermediate optimization results in the specified directory. Subsequent builds reuse previous work where possible, significantly reducing edit–compile cycle times. The cache directory grows over time, so you may need to clean it periodically during development.

## What you've accomplished and what's next

You've learned how to enable LTO with the `-flto` flag for both simple and complex build scenarios. You can now configure LTO behavior using fat objects for compatibility, parallelize LTO jobs to speed up builds, and cache intermediate results during development.

Next, you'll see concrete performance and code size results from enabling LTO on industry-standard benchmarks.
