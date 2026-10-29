---
title: Prepare an arm64 Mach-O fixture
description: Build an arm64 Mach-O fixture and two negative controls on macOS, then confirm their architecture slices before inspecting extension instructions.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Verify extension-specific code in a final binary

An arm64 binary can contain code for optional Arm architecture extensions such as Scalable Matrix Extension 2 (SME2), Scalable Vector Extension 2 (SVE2), Dot Product, or cryptographic instructions. Specific code or libraries, such as Kleidi for SME2, can implement their associated functionality. Importing the supporting source code doesn't prove that the extension logic is present in the compiled binary.

You build a small Mach-O executable and inspect its final machine code, using SME2 as the example extension. You identify state-control, matrix, and predicate instructions, then correlate each finding with its exact four bytes and decoded mnemonic. You also inspect the operands, static program counter (PC), symbol, and surrounding code.

You can use the same evidence model to inspect other Arm architecture extensions in a final binary.

## Create a traceable SME2 fixture

You will begin by creating an SME2-based executable from source code. This fixture will contain an SME2 function, a normal C entry point, and a feature-name string. You will compile the code but never run it, so the Mac you develop this on doesn't need SME2 hardware. 

The code you write is Arm-specific and won't work on x86-based systems.

To begin, create a working directory and move into it:

```bash
mkdir arm64-extension-inspection
cd arm64-extension-inspection
```

Run the following command to create `sme2-main.c`:

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

Next, run the following command to create `sme2-kernel.S`:

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

Build the final SME2-Mach-O executable. The `-march=armv9-a+sme2` option makes the compile-time intent explicit, but you will verify the linked output rather than treating this flag as proof.

```bash
xcrun clang -arch arm64 -O2 -march=armv9-a+sme2 \
  sme2-main.c sme2-kernel.S -o sme2-positive
```

You now have a compiled fixture ready for inspection.

## Create negative controls

The compiled fixture serves as your positive control. Create `string-only-control.c` as a negative control with a feature string and SME2-like symbol name, but no SME2 instructions:

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

Run the following command to create another true-negative fixture, `plain-arm64-control.c` without extension-specific source, names, or strings:

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

Build both controls for the base arm64 architecture:

```bash
xcrun clang -arch arm64 -O2 string-only-control.c -o string-only-control
xcrun clang -arch arm64 -O2 plain-arm64-control.c -o plain-arm64-control
```

## Confirm the final architecture slice

With your controls built, begin with file-type and architecture-slice checks before moving to instruction inspection.

A *thin* Mach-O file contains one architecture slice. A universal, or *fat* Mach-O file can contain several slices, such as arm64 and x86_64. This allows x86 and Arm executable code to coexist in the same file.

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

For a universal (fat) binary, `lipo -info` might report both `x86_64` and `arm64`. The later `-arch arm64` options select the slice to inspect.

A binary you inspect outside this Learning Path might be a fat binary. If it is, you'd need to be sure you are working with the Mach-O slice.

The source code in this Learning Path produces a thin Mach-O binary.

## What you've accomplished and what's next

You built one true positive fixture and two true negative fixtures. Next, you will use strings and symbols to collect attribution hints while keeping them separate from instruction proof.
