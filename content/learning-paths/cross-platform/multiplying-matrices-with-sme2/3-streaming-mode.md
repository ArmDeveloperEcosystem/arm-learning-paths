---
title: Streaming mode and ZA State in SME
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understanding streaming mode

In large-scale software, programs often switch between streaming and non-streaming mode. Some streaming-mode functions may call others, requiring portions of processor state, such as the ZA storage, to be saved and restored. This behavior is defined in the Arm C Language Extensions (ACLE) and is supported by the compiler.

To use streaming mode, you simply annotate the relevant functions with the appropriate keywords. The compiler handles the low-level mechanics of streaming mode management, removing the need for error-prone, manual work.

{{% notice Note %}}
For more information, see the [Introduction to streaming and non-streaming mode](https://arm-software.github.io/acle/main/acle.html#controlling-the-use-of-streaming-mode). The rest of this section references content from the ACLE specification.
{{% /notice %}}

## Streaming mode behavior and compiler handling

* The AArch64 architecture defines a concept called *streaming mode*, controlled
by a processor state bit `PSTATE.SM`. 

* At any given point in time, the processor is either in streaming mode (`PSTATE.SM==1`) or in non-streaming mode (`PSTATE.SM==0`). 

* To enter streaming mode, there is the instruction `SMSTART`, and to return to non-streaming mode, the instruction is `SMSTOP`.

* Streaming mode affects C and C++ code in the following ways:

  - It can change the length of SVE vectors and predicates. The length of an SVE vector in streaming mode is called the *Streaming Vector Length* (SVL), which might differ from the non-streaming vector length. See [Effect of streaming mode on VL](https://arm-software.github.io/acle/main/acle.html#effect-of-streaming-mode-on-vl) for further information.
  - Some instructions, and their associated ACLE intrinsics, can only be executed in streaming mode.These intrinsics are called *streaming intrinsics*.
  - Other instructions are restricted to non-streaming mode, and their instrinsics are called *non-streaming intrinsics*.

The ACLE specification extends the C and C++ abstract machine model to include streaming mode. At any given time, the abstract machine is either in streaming or non-streaming mode.

This distinction between abstract machine mode and processor mode is mostly a specification detail. At runtime, the processor’s mode may differ from the abstract machine’s mode - as long as the observable program behavior remains consistent (as per the "as-if" rule).

One
practical consequence of this is that C and C++ code does not specify the exact
placement of `SMSTART` and `SMSTOP` instructions; the source code simply places
limits on where such instructions go. For example, when stepping through a
program in a debugger, the processor mode might sometimes be different from the
one implied by the source code.

ACLE provides attributes that specify whether the abstract machine executes statements:

- In non-streaming mode, in which case they are called *non-streaming statements*.
- In streaming mode, in which case they are called *streaming statements*.
- In either mode, in which case they are called *streaming-compatible statements*.

## Working with ZA state

SME also introduces a matrix storage area called ZA, sized `SVL.B` × `SVL.B` bytes. It
also provides a processor state bit called `PSTATE.ZA` to control whether ZA
is enabled.

In C and C++, ZA usage is specified at the function level: a function either uses ZA or it doesn't. That is, a function either has ZA state or it does not.

If a function does have ZA state, the function can either share that ZA state
with the function's caller or create new ZA state. In the latter
case, it is the compiler's responsibility to free up ZA so that the function can
use it - see the description of the lazy saving scheme in
[AAPCS64](https://arm-software.github.io/acle/main/acle.html#AAPCS64) for details
about how the compiler does this.
 