---
title: Further information on implementation 
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

To select the most appropriate version of a function, each call to a versioned function is routed through an indirect function resolver which is pointed by the called symbol (ifunc). 

The compiler generates a resolver based on the function versions declared in the translation unit. A typical resolver implementation uses a runtime library to detect the presence of the architectural features on which the function versions depend and returns a pointer to the correct version. 

The resolution of the called symbol is delayed until runtime, when the dynamic loader runs the resolver and updates the procedure linkage table (PLT) with a pointer to the chosen implementation. The resolver function is run only once and its returned value remains unchanged for the lifetime of the process. 

Relocations handle references to the called symbol, which return the cached PLT entry.

#### Differences between GCC 14 and LLVM 19 implementations

- The attribute `target_version` in GCC is only supported for C++, not for C.
- The set of features as indicated by the [mapping table](https://arm-software.github.io/acle/main/acle.html#mapping) differs in support between the two compilers.
- GCC can statically resolve calls to versioned functions, whereas LLVM cannot.

#### Resolver emission with LLVM

When using the LLVM compiler, the resolver is emitted in the translation unit (TU) which contains the definition of the default version. To correctly generate a resolver the compiler must be aware of all the versions of a function. Therefore, the user must declare every function version in the TU where the default version resides. 

Here is an example:

Assume `file1.c` contains the code:

```c
int func1(void);
int func2(void) { return func1(); }
```

Assume `file2.c` contains:

```c
__attribute__((target_version("sve")))
int func1(void) { return 1; }

__attribute__((target_version("default")))
int func1(void) { return 0; }
```

The compilation of `file1.c` yields normal code generation since no version of `func1` other than the default is declared. 

When compiling `file2.c` a resolver is emitted for `func1` due to the presence of its default definition. GCC does not currently support multiversioning for this example as it only generates a resolver when a function is called.

#### Static resolution with GCC

The GCC compiler optimizes calls to versioned functions when they can be statically resolved. 

Such calls would otherwise be routed through the resolver, but instead they become direct which allows them to be inlined. 

This might be possible whenever a function is compiled with a sufficiently high set of architecture features (so including `target`/`target_version`/`target_clones` attributes, and command line options). 

LLVM is not yet able to perform this optimization.
