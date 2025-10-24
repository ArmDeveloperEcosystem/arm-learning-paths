---
title: Further information on implementation 
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

To select the most appropriate version of a function, each call to a versioned function is routed through an indirect function resolver which is pointed by the called symbol (ifunc). 

The compiler generates a resolver based on the function versions declared in the translation unit. A typical resolver implementation uses a runtime library to detect the presence of the architectural features on which the function versions depend and returns a pointer to the correct version. Features implied by the command line are not exempt from runtime detection.

The resolution of the called symbol is delayed until runtime, when the dynamic loader runs the resolver and updates the procedure linkage table (PLT) with a pointer to the chosen implementation. The resolver function is run only once and its returned value remains unchanged for the lifetime of the process. 

Relocations handle references to the called symbol, which return the cached PLT entry.

#### Feature detection at runtime

Some architectural features depend on others as indicated by the [dependencies table](https://arm-software.github.io/acle/main/acle.html#dependencies). Those are detected transitively and they are not exempt from runtime detection if implied by the command line. For example `rcpc3` depends on `rcpc2` which depends on `rcpc`. All three are detected in the following example.

Use a text editor to create a file named `rcpc.c` with the code below:

```c
__attribute__((target_clones("rcpc3", "default"))) int f(void) { return 0; }
```

{{% notice Note %}}
The depended-on features (rcpc2, rcpc) *need not* be specified in the attribute, but they *may* well be (there is no functional difference):
```c
__attribute__((target_clones("rcpc3+rcpc2+rcpc", "default")))
```
{{% /notice %}}

To compile with Clang, run:

```console
clang --target=aarch64-linux-gnu -march=armv8-a+rcpc -O3 --rtlib=compiler-rt -S -o - rcpc.c
```

Here is the generated resolver function containing the runtime detection of features:

```output
       .section        .text.f.resolver,"axG",@progbits,f.resolver,comdat
       .weak   f.resolver
       .p2align        2
       .type   f.resolver,@function
f.resolver:
       str     x30, [sp, #-16]!
       bl      __init_cpu_features_resolver
       adrp    x8, __aarch64_cpu_features
       mov     x9, #12582912
       adrp    x10, f.default
       add     x10, x10, :lo12:f.default
       ldr     x8, [x8, :lo12:__aarch64_cpu_features]
       movk    x9, #1024, lsl #48
       bics    xzr, x9, x8
       adrp    x8, f._Mrcpc3
       add     x8, x8, :lo12:f._Mrcpc3
       csel    x0, x8, x10, eq
       ldr     x30, [sp], #16
       ret
```
{{% notice Note %}}
The immediate value `#12582912` in this assembly is used to construct a bitmask for materializing the runtime detection of `rcpc3`.
{{% /notice %}}

#### Differences between GCC 16 and LLVM 20 implementations

- The set of features as indicated by the [mapping table](https://arm-software.github.io/acle/main/acle.html#mapping) differs in support between the two compilers.

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

#### Static resolution of calls

Normally the called symbol is resolved at runtime (dynamically), however it may be possible to determine which function version to call at compile time (statically).

This may be possible when the caller function is compiled with a sufficiently high set of architecture features (explicitly by using the `target` attribute as an optimization hint, or the multiversioning attributes `target_version`/`target_clones`, and implicitly via command line options). Refer to the example in the next section for details. 

The compiler optimizes calls to versioned functions which can be statically resolved into direct calls. As a result the versioned function may be inlined into the call site.
