---
title: Changes from released compilers
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

#### ACLE specification changes

- The set of supported features has changed as indicated by the [ACLE Q3 change log](https://arm-software.github.io/acle/main/acle.html#changes-between-acle-q2-2024-and-acle-q3-2024) and the [ACLE Q4 change log](https://arm-software.github.io/acle/main/acle.html#changes-between-acle-q3-2024-and-acle-q4-2024).
- The runtime detection of features has changed. Dependent-on features get detected as indicated by the [dependencies table](https://arm-software.github.io/acle/main/acle.html#dependencies).
- The most appropriate version of a function is determined as indicated by the new [selection rules](https://arm-software.github.io/acle/main/acle.html#selection). Previously, the most specific version (the one with most features) was favored over any other version.
- A new predefined macro `__FUNCTION_MULTI_VERSIONING_SUPPORT_LEVEL` has been added to indicate which ACLE version is implemented by the compiler.

#### Semantic changes between LLVM 19 and LLVM 20

With LLVM 19 at least one more version other than the default is needed to trigger function multiversioning. 

With LLVM 20 a header file declaration:

```c
__attribute__((target_version("default"))) void f(void);
```

guarantees that there will be a mangled version `f.default`. Conversely, LLVM 19 would generate an unmangled symbol here since function multiversioning does not trigger when compiling this code in the absence of other versions.

#### Static resolution in LLVM 20

LLVM can optimize calls to versioned functions when they can be statically resolved. For example:

```c
__attribute__((target_version("mops"))) int f(void);
__attribute__((target_version("sve2"))) int f(void);
__attribute__((target_version("sve"))) int f(void);
__attribute__((target_version("default"))) int f(void) { return 0; }

__attribute__((target_version("mops+sve2"))) int caller(void) {
  return f(); // f._Mmops is called directly
}
__attribute__((target_version("mops"))) int caller(void) {
  return f(); // f._Mmops is called directly
}
__attribute__((target_version("sve"))) int caller(void) {
  return f(); // cannot be optimized since SVE2 may be available on target
}
__attribute__((target_version("default"))) int caller(void) {
  return f(); // f.default is called directly
}
```
