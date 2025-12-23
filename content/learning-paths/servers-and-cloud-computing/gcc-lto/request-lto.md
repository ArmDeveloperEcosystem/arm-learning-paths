---
title: Deploying LTO
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deploying LTO

### A simple use-case
To rely on GCC's default configuration for link-time optimization, using the feature is as simple as passing gcc the `-flto` flag when invoking it from the command line.

For the step-wise build of an executable, we'd have:
```sh
gcc -c -O2 -flto component-1.c
gcc -c -O2 -flto component-2.c
gcc -o myprog -flto -O2 component-1.o component-2.o
```
This could be simplified to a one-liner, as follows:
```sh
gcc -o myprog -flto -O2 component-1.c component-2.c
```

### Modifying LTO behaviour
#### Flexible object files

By default, requesting `-flto` when compiling individual object files to be  linked later, we are effectively committing to using LTO every time the object is to be linked into an executable. As such the resulting object files contain only GCC's internal intermediate representation of the code. Such objects are referred to as being _slim_.

This constraint can be relaxed and _fat_ LTO-enabled objects generated, as can be achieved using the `-ffat-lto-objects` flag.  Using this flag causes the final object binary contents that would be generated in the absence of LTO to be emitted alongside intermediate bytecode and can be useful for compatibility purposes.

#### Parallelization
Link-time optimization may be sped up by execution in parallel. This behavior can be controlled by augmenting the `-flto` flag with an argument.

While `-flto=auto` can be used for automatic parallelization, `-flto=<nthread>` allows us to manually specify the desired number of parallel jobs.  Requesting parallelization causes the whole program to be split into multiple partitions of similar size, with the compiler trying to minimize the number of references which cross partition boundaries and which would otherwise lead to missed optimizations.

#### Caching
During code development, it is possible to cache the outputs of translational units inside LTO, thus significantly shortening edit-compile cycles. This can be achieved using the `-flto-incremental=<path>` flag.
