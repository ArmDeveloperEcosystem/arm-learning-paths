---
title: Using SIMD Loops
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your development environment

To get started, clone the SIMD Loops project and change to the project directory:

```bash
git clone https://gitlab.arm.com/architecture/simd-loops simd-loops.git
cd simd-loops.git
```

Confirm that you are using an Arm machine:

```bash
uname -m
```

Expected output on Linux:

```output
aarch64
```

On macOS, the expected output is:

```output
arm64
```

## SIMD Loops structure

In the SIMD Loops project, the source code for the loops is organized under the `loops` directory. The complete list of loops is documented in the `loops.inc` file, which includes a brief description and the purpose of each loop. Every loop is associated with a uniquely named source file following the pattern `loop_<NNN>.c`, where `<NNN>` represents the loop number.

A subset of the `loops.inc` file is below:

```output
LOOP(001, "FP32 inner product",                "Use of fp32 MLA instruction", STREAMING_COMPATIBLE)
LOOP(002, "UINT32 inner product",              "Use of u32 MLA instruction", STREAMING_COMPATIBLE)
LOOP(003, "FP64 inner product",                "Use of fp64 MLA instruction", STREAMING_COMPATIBLE)
LOOP(004, "UINT64 inner product",              "Use of u64 MLA instruction", STREAMING_COMPATIBLE)
LOOP(005, "strlen short strings",              "Use of FF and NF loads instructions")
LOOP(006, "strlen long strings",               "Use of FF and NF loads instructions")
LOOP(008, "Precise fp64 add reduction",        "Use of FADDA instructions")
LOOP(009, "Pointer chasing",                   "Use of CTERM and BRK instructions")
LOOP(010, "Conditional reduction (fp)",        "Use of CLAST (SIMD&FP scalar) instructions", STREAMING_COMPATIBLE)
```

A loop is structured as follows:

```c
// Includes and loop_<NNN>_data structure definition

#if defined(HAVE_NATIVE) || defined(HAVE_AUTOVEC)

// C reference or auto-vectorized version
void inner_loop_<NNN>(struct loop_<NNN>_data *data) { ... }

#if defined(HAVE_xxx_INTRINSICS)

// Intrinsics versions: xxx = SME, SVE, or SIMD (NEON)
void inner_loop_<NNN>(struct loop_<NNN>_data *data) { ... }

#elif defined(<ASM_COND>)

// Hand-written inline assembly
// <ASM_COND> = __ARM_FEATURE_SME2p1, __ARM_FEATURE_SME2, __ARM_FEATURE_SVE2p1,
//              __ARM_FEATURE_SVE2, __ARM_FEATURE_SVE, or __ARM_NEON
void inner_loop_<NNN>(struct loop_<NNN>_data *data) { ... }

#else

#error "No implementations available for this target."

#endif

// Main of loop: buffer allocation, loop function call, result checking
```

Each loop is implemented in several SIMD extension variants. Conditional compilation selects one of the implementations for the `inner_loop_<NNN>` function.

The native C implementation is written first, and it can be generated either when building natively with `-DHAVE_NATIVE` or through compiler auto-vectorization with `-DHAVE_AUTOVEC`.

When SIMD ACLE is supported (SME, SVE, or Neon), the code is compiled using high-level intrinsics. If ACLE support isn't available, the build process falls back to handwritten inline assembly targeting one of the available SIMD extensions, such as SME2.1, SME2, SVE2.1, SVE2, and others.

The overall code structure also includes setup and cleanup code in the main function, where memory buffers are allocated, the selected loop kernel is executed, and results are verified for correctness.

At compile time, you can select which loop optimization to compile, whether it's based on SME or SVE intrinsics, or one of the available inline assembly variants.

SIMD Loops requires a C compiler and an objectdump binary. If the toolchain binaries are not available in the PATH, then you can set the following environment variables:

```bash
export C_COMPILER=/path/to/bin/c_compiler
export OBJDUMP=/path/to/bin/objdump
```

Then, run make in the project directory:

```console
make
```

With no target specified, the output shows the list of available targets:

```output
all fmt clean c-scalar scalar autovec-sve autovec-sve2 neon sve sve2 sme2 sme-ssve sve2p1 sme2p1 sve-intrinsics sme-intrinsics
```

To build all loops for all targets, run:

```console
make all
```

To build all loops for a single target, such as Neon, run:

```console
make neon
```

If you are compiling on a Linux machine, you can quickly check which CPU features are available using the following flag. For example, on the Arm AGI CPU:

```bash { command_line="user@localhost | 2-6"}
lscpu | grep Flags
Flags:                                   fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 sm3 sm4 asimddp sha512 sve asimdfhm dit uscat ilrcpc flagm sb paca pacg dcpodp sve2 sveaes svepmull svebitperm svesha3 svesm4 flagm2 frint svei8mm svebf16 i8mm bf16 dgh rng bti ecv afp wfxt ls64
```

There is not an exact match between the Make targets and the reported CPU flags, but you can still quickly determine which features the system lacks—for example, this system does not support SME2.

As a result of the build, two types of binaries are generated.

To select a specific loop, pass parameters to the program. For example, to run loop 1 for 5 iterations using the Neon target:

```console
build/neon/bin/simd_loops -k 1 -n 5
```

The expected output is:

```output
Loop 001 - FP32 inner product
 - Purpose: Use of fp32 MLA instruction
 - Checksum correct.
```

The second type of binary is an individual loop.

To run loop 1 as a standalone binary:

```console
build/neon/standalone/bin/loop_001.elf
```

The expected output is

Example output:

```output
 - Checksum correct.
```

Running on a system without the supported CPU feature will show the following.

```bash
Illegal instruction        (core dumped) <command run>
```
