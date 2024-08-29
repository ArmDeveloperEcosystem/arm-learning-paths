---
title: Implementation Details
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Implementation details

In order to select the most appropriate version of a function, each call to a versioned function is routed through an indirect function resolver which is pointed by the called symbol (IFUNC). The compiler generates a resolver based on the function versions declared in the translation unit. A typical resolver implementation uses a runtime library to detect the presence of the architectural features on which the function versions depend and returns a pointer to the right version. The resolution of the called symbol is delayed until runtime, when the dynamic loader runs the resolver and updates the procedure linkage table (PLT) with a pointer to the chosen implementation. The resolver function is run only once and its returned value remains unchanged for the lifetime of the process. References to the called symbol are handled by relocations which return the cached PLT entry.

#### Differences between GCC 14 and LLVM 19 implementations

- The attribute `target_version` in GCC is only supported for C++, not for C.
- The set of features as indicated by the table [here](https://arm-software.github.io/acle/main/acle.html#mapping) differs in support between the two compilers.
- GCC can statically resolve calls to versioned functions, whereas LLVM cannot.

#### Resolver emission with LLVM

When using the LLVM compiler the resolver is emitted in the translation unit which contains the definition of the default version. To correctly generate a resolver the compiler must be aware of all the versions of a function. Therefore, the user must declare every function version in the TU where the default version resides. For example:

file1.c
```c
int foo(void);
int bar(void) { return foo(); }
```

file2.c
```c
__attribute__((target_version("sve")))
int foo(void) { return 1; }

__attribute__((target_version("default")))
int foo(void) { return 0; }
```

The compilation of `file1.c` yields normal code generation since no version of `foo` other than the default is declared. When compiling `file2.c` a resolver is emitted for `foo` due to the presence of its default definition. GCC does not currently support Multiversioning for this example since it only generates a resolver when a function is called.

#### Static resolution with GCC

The GCC compiler optimizes calls to versioned functions when they can be statically resolved. Such calls would otherwise be routed through the resolver but instead they become direct which allows them to be inlined. This may be possible whenever a function is compiled with a sufficiently high set of architecture features (so including `target`/`target_version`/`target_clones` attributes, and command line options). LLVM is not yet able to perform this optimization.
