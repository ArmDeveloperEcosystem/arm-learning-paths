---
title: Compatibility with streaming mode
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Function Multi Versioning is compatible with Arm streaming mode as long as the same calling convention is used across all function versions.

Use a text editor to create a file named `streaming.c` with the code below:

```c
__attribute__((target_clones("sve", "simd")))
void ok_arm_streaming(void) __arm_streaming {}

__arm_locally_streaming __attribute__((target_version("sme2")))
void ok_arm_streaming(void) __arm_streaming {}

__attribute__((target_version("default")))
void ok_arm_streaming(void) __arm_streaming {}


__attribute__((target_clones("sve", "simd")))
void ok_arm_streaming_compatible(void) __arm_streaming_compatible {}

__arm_locally_streaming __attribute__((target_version("sme2")))
void ok_arm_streaming_compatible(void) __arm_streaming_compatible {}

__attribute__((target_version("default")))
void ok_arm_streaming_compatible(void) __arm_streaming_compatible {}


__arm_locally_streaming __attribute__((target_clones("sve", "simd")))
void ok_no_streaming(void) {}

__attribute__((target_version("sme2")))
void ok_no_streaming(void) {}

__attribute__((target_version("default")))
void ok_no_streaming(void) {}


__attribute__((target_clones("sve", "simd")))
void bad_mixed_streaming(void) {}

__attribute__((target_version("sme2")))
void bad_mixed_streaming(void) __arm_streaming {} // expected-error: declaration has a different calling convention

__attribute__((target_version("default")))
void bad_mixed_streaming(void) __arm_streaming_compatible {} // expected-error: declaration has a different calling convention

__arm_locally_streaming __attribute__((target_version("dotprod")))
void bad_mixed_streaming(void) __arm_streaming {} // expected-error: declaration has a different calling convention


void n_caller(void) {
  ok_arm_streaming();
  ok_arm_streaming_compatible();
  ok_no_streaming();
  bad_mixed_streaming();
}

void s_caller(void) __arm_streaming {
  ok_arm_streaming();
  ok_arm_streaming_compatible();
  ok_no_streaming();
  bad_mixed_streaming();
}

void sc_caller(void) __arm_streaming_compatible {
  ok_arm_streaming();
  ok_arm_streaming_compatible();
  ok_no_streaming();
  bad_mixed_streaming();
}
```

To compile with Clang, run:

```console
clang --target=aarch64-linux-gnu -march=armv8-a+sme --rtlib=compiler-rt -c streaming.c
```
