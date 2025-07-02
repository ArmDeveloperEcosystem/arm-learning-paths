---
title: Streaming mode
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In real-world large-scale software, a program moves back and forth from
streaming mode, and some streaming mode routines call other streaming mode
routines, which means that some state needs to be saved and restored. This
includes the ZA storage. This is defined in the ACLE and supported by the
compiler: the programmer *just* has to annotate the functions with some keywords
and let the compiler automatically perform the low-level tasks of managing the
streaming mode. This frees the developer from a tedious and error-prone task.
See [Introduction to streaming and non-streaming
mode](https://arm-software.github.io/acle/main/acle.html#controlling-the-use-of-streaming-mode)
for further information. The rest of this section references information from
the ACLE.

## About streaming mode

The AArch64 architecture defines a concept called *streaming mode*, controlled
by a processor state bit called `PSTATE.SM`. At any given point in time, the
processor is either in streaming mode (`PSTATE.SM==1`) or in non-streaming mode
(`PSTATE.SM==0`). There is an instruction called `SMSTART` to enter streaming mode
and an instruction called `SMSTOP` to return to non-streaming mode.

Streaming mode has three main effects on C and C++ code:

- It can change the length of SVE vectors and predicates: the length of an SVE
  vector in streaming mode is called the “streaming vector length” (SVL), which
  might be different from the normal non-streaming vector length. See
  [Effect of streaming mode on VL](https://arm-software.github.io/acle/main/acle.html#effect-of-streaming-mode-on-vl)
  for more details.
- Some instructions can only be executed in streaming mode, which means that
  their associated ACLE intrinsics can only be used in streaming mode. These
  intrinsics are called “streaming intrinsics”.
- Some other instructions can only be executed in non-streaming mode, which
  means that their associated ACLE intrinsics can only be used in non-streaming
  mode. These intrinsics are called “non-streaming intrinsics”.

The C and C++ standards define the behavior of programs in terms of an *abstract
machine*. As an extension, the ACLE specification applies the distinction
between streaming mode and non-streaming mode to this abstract machine: at any
given point in time, the abstract machine is either in streaming mode or in
non-streaming mode.

This distinction between processor mode and abstract machine mode is mostly just
a specification detail. However, the usual “as if” rule applies: the
processor's actual mode at runtime can be different from the abstract machine's
mode, provided that this does not alter the behavior of the program. One
practical consequence of this is that C and C++ code does not specify the exact
placement of `SMSTART` and `SMSTOP` instructions; the source code simply places
limits on where such instructions go. For example, when stepping through a
program in a debugger, the processor mode might sometimes be different from the
one implied by the source code.

ACLE provides attributes that specify whether the abstract machine executes statements:

- In non-streaming mode, in which case they are called *non-streaming statements*.
- In streaming mode, in which case they are called *streaming statements*.
- In either mode, in which case they are called *streaming-compatible statements*.

SME provides an area of storage called ZA, of size `SVL.B` x `SVL.B` bytes. It
also provides a processor state bit called `PSTATE.ZA` to control whether ZA
is enabled.

In C and C++ code, access to ZA is controlled at function granularity: a
function either uses ZA or it does not. Another way to say this is that a
function either “has ZA state” or it does not.

If a function does have ZA state, the function can either share that ZA state
with the function's caller or create new ZA state “from scratch”. In the latter
case, it is the compiler's responsibility to free up ZA so that the function can
use it; see the description of the lazy saving scheme in
[AAPCS64](https://arm-software.github.io/acle/main/acle.html#AAPCS64) for details
about how the compiler does this.
