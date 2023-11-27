---
title: Build Executable
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build Executable

BOLT works by rearranging both functions and code within functions to move hot code closer together and reduce memory overhead.

To do this the binary needs atleast an unstripped symbol table and prefers being linked with relocations which can be enabled with the linker flag `--emit-relocs`. This flag should be used to get maximum performance gains.

BOLT is also incompatiable with the GCC flag `-freorder-blocks-and-partition` which is enabled by default in GCC version 8. This can be avoided by adding the flag `-fno-reorder-blocks-and-partition`.

The executable will be used when collecting profile information and passed into BOLT to optimise it.

GCC

```bash
gcc <args> -Wl,--emit-relocs -fno-reorder-blocks-and-partition
```

Clang

```bash
clang <args> -Wl,--emit-relocs
```
