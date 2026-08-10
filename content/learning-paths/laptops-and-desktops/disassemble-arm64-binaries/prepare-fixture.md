---
title: Prepare an arm64 Mach-O fixture
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Verify extension-specific code in a final binary

An arm64 binary can contain code for optional Arm architecture extensions such as Scalable Matrix Extension 2 (SME2), Scalable Vector Extension 2 (SVE2), Dot Product, or cryptographic instructions. The architecture name alone doesn't tell you which extension-specific instructions made it into the final artifact.

In this Learning Path, you build a small Mach-O executable and inspect its final machine code. SME2 provides the worked example because it includes distinctive state-control, matrix, and predicate instructions. You will correlate each finding with its exact four bytes, decoded mnemonic, operands, static program counter (PC), symbol, and surrounding code.

{{% notice Static evidence only %}}
Disassembly proves that instruction bytes are present in executable code. It doesn't prove that the instructions ran, that runtime dispatch selected them, or that they improved performance. Those claims need runtime analysis on a suitable target.
{{% /notice %}}

The same evidence model helps you inspect Arm architecture extension optimizations in release artifacts for Cortex-A and Neoverse systems. The commands in this Learning Path inspect macOS Mach-O files. Neoverse Linux release artifacts are normally Executable and Linkable Format (ELF) files and need the corresponding ELF section-selection and disassembly commands.

## Create a traceable SME2 fixture

Start with source you can trace through the compiler and linker into a final executable. The fixture contains an SME2 function, a normal C entry point that keeps the function in the link, and a feature-name string. You will compile the code but never run it, so the Mac doesn't need SME2 hardware.

Create a working directory and move into it:

```bash
mkdir arm64-extension-inspection
cd arm64-extension-inspection
```

Create `sme2-main.c` with the following content. The volatile function pointer keeps the assembly symbol referenced without calling it.

```c { file_name="sme2-main.c" }
#include <stddef.h>

extern void sme2_fixture_kernel(void);

__attribute__((used))
static const char feature_hint[] = "hw.optional.arm.FEAT_SME2";

void (*volatile keep_sme2_kernel)(void) = sme2_fixture_kernel;

int main(void) {
    return keep_sme2_kernel == NULL || feature_hint[0] == '\0';
}
```

Create `sme2-kernel.S` with the following content. The function contains ordinary SVE predicate setup and strict SME2 predicate forms, so you can see why operands matter during classification.

```asm { file_name="sme2-kernel.S" }
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
```

Build the final Mach-O executable with SME2 enabled in the compiler target. The `-march=armv9-a+sme2` option makes the compile-time intent explicit, but you will verify the linked output rather than treating this flag as proof.

```bash
xcrun clang -arch arm64 -O2 -march=armv9-a+sme2 \
  sme2-main.c sme2-kernel.S -o sme2-positive
```

Don't run `sme2-positive`. Building and disassembling it is safe on an Apple silicon Mac that doesn't implement SME2 because the processor never fetches its instructions.

## Create negative controls

A useful predicate must reject feature-related words stored as data. Create `string-only-control.c` with a feature string and SME2-like symbol name, but no SME2 assembly:

```c { file_name="string-only-control.c" }
__attribute__((used))
static const char feature_hint[] = "hw.optional.arm.FEAT_SME2";

__attribute__((noinline, used))
void sme2_string_only_marker(void) {
    __asm__ volatile("" ::: "memory");
}

int main(void) {
    return feature_hint[0] == '\0';
}
```

Create `plain-arm64-control.c` without extension-specific source, names, or strings:

```c { file_name="plain-arm64-control.c" }
__attribute__((noinline))
int arm64_plain_add(int left, int right) {
    return left + right;
}

int main(void) {
    return arm64_plain_add(1, 2) == 3 ? 0 : 1;
}
```

Build both controls for the base arm64 architecture:

```bash
xcrun clang -arch arm64 -O2 string-only-control.c -o string-only-control
xcrun clang -arch arm64 -O2 plain-arm64-control.c -o plain-arm64-control
```

## Confirm the final architecture slice

A thin Mach-O file contains one architecture slice. A universal Mach-O file can contain several slices, such as arm64 and x86_64. The `file` and `lipo` tools identify those slices, but they don't enumerate optional Arm architecture extensions.

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

For a universal binary, `lipo -info` might report both `x86_64` and `arm64`. The later `-arch arm64` options select the slice to inspect. Neither output would tell you whether SME2 instructions exist.

Always point the workflow at the shipped executable. For a macOS application bundle, that file is normally under `MyApp.app/Contents/MacOS/`. An object file, source file, or build log doesn't establish what survived packaging and linking.

## What you've learned and what's next

You built one positive fixture and two controls as final arm64 Mach-O executables without running them. Next, you will use strings and symbols to collect attribution hints while keeping them separate from instruction proof.
