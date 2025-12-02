---
title: Example 3 - inline assembly at runtime
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This example manipulates strings using SVE2 instructions and inline assembly. 

Moreover, the compiler generates an optimized version of memcpy using FEAT_MOPS.

More details on the SkipWord implementation can be found in [SVE Programming Examples](https://developer.arm.com/documentation/dai0548/latest).

Use a text editor to create a file named `skip-word.c` with the code below:

```c
#include <stdio.h>
#include <string.h>

__attribute__((target_clones("default", "mops")))
char *CopyWord(char *dst, const char *src) {
  size_t n = strlen(src);
  memcpy(dst, src, n + 1);
  return dst + n;
}

__attribute__((target_version("sve2")))
const char *SkipWord(const char *p, const char *end) {
  printf("Running the sve2 SkipWord\n");
  __asm volatile (
    "mov w2, #0xd090000\n\t"
    "add w2, w2, #0xa20\n\t"
    "mov z1.s, w2\n\t"
    "whilelt p0.b, %0, %1\n"
    "1:\n\t"
    "ld1b z0.b, p0/z, [%0]\n\t"
    "match p1.b, p0/z, z0.b, z1.b\n\t"
    "b.any 2f\n\t"
    "incb %0\n\t"
    "whilelt p0.b, %0, %1\n\t"
    "b.first 1b\n\t"
    "mov %0, %1\n\t"
    "b 3f\n"
    "2:\n\t"
    "brkb p2.b, p0/z, p1.b\n\t"
    "incp %0, p2.b\n"
    "3:\n\t"
    : "+r" (p)
    : "r" (end)
    : "w2", "p0", "p1", "p2", "z0", "z1");
    return p;
}

__attribute__((target_version("default")))
const char *SkipWord(const char *p, const char *end) {
  printf("Running the default SkipWord\n");
  while (p != end && *p != ' ' && *p != '\n' && *p != '\r' && *p != '\t')
    p++;
  return p;
}

int main(int argc, char **argv) {
  if (argc != 3)
    return -1;
  char buffer[256];
  char *end = CopyWord(buffer, argv[1]);
  end = CopyWord(end, argv[2]);
  printf("%s\n", buffer);
  printf("%s\n", SkipWord(buffer, buffer + strlen(buffer)));
  return 0;
}
```

You can compile and run the above example on hardware that has both SVE2 and Armv8 instructions (no SVE2):

To compile with Clang, use:

```console
clang --target=aarch64-linux-gnu -march=armv8-a -O3 skip-word.c --rtlib=compiler-rt
```

To compile with GCC, run:

```console
g++ -march=armv8-a -O3 skip-word.c
```

To run the application:

```console
./a.out "test 2" " strings"
```

The output is:

```output
test 2 strings
Running the sve2 SkipWord
2 strings
```

The SVE2 version is selected as it has higher priority than the default, as indicated by the [mapping table](https://arm-software.github.io/acle/main/acle.html#mapping).
