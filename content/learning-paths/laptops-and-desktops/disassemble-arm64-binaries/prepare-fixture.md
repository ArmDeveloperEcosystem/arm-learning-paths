---
title: Prepare an arm64 Mach-O fixture
description: Build an arm64 Mach-O fixture and two negative controls on macOS, then confirm their architecture slices before inspecting SME and SME2 instructions.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build the SME2 fixture and comparison binaries

A macOS binary can contain Scalable Matrix Extension (SME) and SME2 instructions. Including supporting source code or enabling compiler options doesn't mean that those instructions are present in the compiled binary.

You'll build a small Mach-O executable and inspect its final machine code for SME and SME2 instructions. You'll identify state-control, matrix, and predicate instructions. You'll correlate each finding with its exact four bytes and decoded mnemonic. You'll also inspect the operands, static program counter (PC), symbol, and surrounding code.

You can use the same inspection method to check for other instruction groups in a compiled binary.

## Create an example binary containing SME2 instructions

You'll begin by creating an example program from source code. This program will contain an SME2 function, a normal C entry point, and a feature-name string.

The example contains SME and SME2 assembly instructions and is compiled for macOS on Apple silicon. You'll compile the code but never run it, so you don't need SME2 hardware on your Mac.

To begin, create a working directory and navigate to it:

```bash
mkdir arm64-extension-inspection
cd arm64-extension-inspection
```

Create `sme2-main.c`:

```bash
cat > sme2-main.c <<'EOF'
#include <stddef.h>

extern void sme2_fixture_kernel(void);

__attribute__((used))
static const char feature_hint[] = "hw.optional.arm.FEAT_SME2";

void (*volatile keep_sme2_kernel)(void) = sme2_fixture_kernel;

int main(void) {
    return keep_sme2_kernel == NULL || feature_hint[0] == '\0';
}
EOF
```

Next, create `sme2-kernel.S`:

```bash
cat > sme2-kernel.S <<'EOF'
.text
.p2align 2
.globl _sme2_fixture_kernel

_sme2_fixture_kernel:
    smstart
    ptrue p0.s
    ptrue pn8.s
    whilelt pn8.s, x0, x0, vlx2
    zero { za }
    fmopa za0.s, p0/m, p0/m, z0.s, z1.s
    smstop
    ret
EOF
```

Build the example program:

```bash
xcrun clang -arch arm64 -O2 -march=armv9-a+sme2 \
  sme2-main.c sme2-kernel.S -o sme2-positive
```
The `-march=armv9-a+sme2` option enables SME2 instructions during compilation. You'll inspect the compiled binary to confirm that they're present.

You now have a compiled example program ready for inspection.

## Create negative controls

The compiled example program serves as your positive control. Create `string-only-control.c` as a negative control with a feature string and a symbol name similar to SME2, but no SME2 instructions:

```bash
cat > string-only-control.c <<'EOF'
__attribute__((used))
static const char feature_hint[] = "hw.optional.arm.FEAT_SME2";

__attribute__((noinline, used))
void sme2_string_only_marker(void) {
    __asm__ volatile("" ::: "memory");
}

int main(void) {
    return feature_hint[0] == '\0';
}
EOF
```

Create another comparison program, `plain-arm64-control.c`, without SME or SME2 code, names, or strings:

```bash
cat > plain-arm64-control.c <<'EOF'
__attribute__((noinline))
int arm64_plain_add(int left, int right) {
    return left + right;
}

int main(void) {
    return arm64_plain_add(1, 2) == 3 ? 0 : 1;
}
EOF
```

Build both controls for the base `arm64` architecture:

```bash
xcrun clang -arch arm64 -O2 string-only-control.c -o string-only-control
xcrun clang -arch arm64 -O2 plain-arm64-control.c -o plain-arm64-control
```

## Confirm the final architecture slice

With your controls built, begin with file-type and architecture-slice checks before inspecting the instructions.

A thin Mach-O file contains one architecture slice. A universal Mach-O file, also called a fat Mach-O file, can contain several slices, including `arm64` and `x86_64`. A universal file can therefore contain both x86 and Arm executable code.

Use `file` and `lipo` to identify the file type and slices.

Inspect the three final linked executables:

```bash
file sme2-positive string-only-control plain-arm64-control
lipo -info sme2-positive
```

The output is similar to:

```output
sme2-positive:       Mach-O 64-bit executable arm64
string-only-control: Mach-O 64-bit executable arm64
plain-arm64-control: Mach-O 64-bit executable arm64
Non-fat file: sme2-positive is architecture: arm64
```

For a universal binary, `lipo -info` might report both `x86_64` and `arm64`. The later `-arch arm64` options select the slice to inspect.

If you inspect a universal binary, ensure that you're working with the `arm64` slice.

The source code that you'll examine to complete this Learning Path produces a thin Mach-O binary.

## What you've accomplished and what's next

You've built an example binary containing SME2 instructions and two comparison binaries without them.

Next, you'll inspect strings and symbols to see why they don't prove instructions are present.
