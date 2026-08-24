---
title: Use LUTI with SME2
description: Trace packed indices through the SME2 ZT0 table, streaming Z registers, and ZA matrix accumulators.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## SME and SME2 architectural features

SME extends the Armv9-A architecture and accelerates matrix-heavy computations, such as outer products and matrix multiplication.
SME introduces __Streaming SVE mode__ and the __scalable ZA matrix-storage__ array. ZA accumulates matrix outer products and multi-vector dot products.

SME2 builds on SME and adds __multi-vector instructions__ and the fixed __512-bit ZT0 lookup-table register__.

For this learning path, the important points to note is that LUTI uses packed low-bit codes from Z source registers, reads the corresponding look-up table entries from `ZT0`, and writes expanded operands into Z destination registers.
The expanded operands can then be consumed by SME2 matrix instructions such as `SDOT` or `SMOPA`, with results accumulated in `ZA` array.

## ZT0 lookup-table register

SME2 provides a fixed 512-bit architectural register named `ZT0`. It contains 64 bytes, arranged as sixteen 32-bit table entries.

<p align="center">
  <img
    src="../images/luti2.png"
    alt="SME2 ZT0 Lookup-Table Register"
    width="100%"
  />
    <img
    src="../images/luti4.png"
    alt="SME2 ZT0 Lookup-Table Register"
    width="100%"
  />
</p>

<p align="left">
  <em>Figure 3. ZT0 lookup-table organization and use by LUTI2 and LUTI4. ZT0 entries form a single linear table of entries 0–15. LUTI2 selects among entries 0–3 using 2-bit indices, while LUTI4 can select among all entries 0–15 using 4-bit indices. According to the destination element size, LUTI copies the low 8, 16, or 32 bits of the selected 32-bit table entry into the destination Z registers.
</em>
</p>

LUTI instructions use packed low-bit indices from a source Z register (`Zn`) to select the corresponding `ZT0` register entry.

The relevant `ZT0` entries are expanded to chosen output element destination width and written to output Z registers (`Zd`).

LUTI2 and LUTI4 can populate one, two, or four destination Z registers. The number of destination registers and the expanded element width (`.B`, `.H`, or `.S`) determine how many packed source bits fill the destinations.

The element suffix specifies the expanded destination width:
- `.B` produces 8-bit elements.
- `.H` produces 16-bit elements.
- `.S` produces 32-bit elements.

## Streaming mode

ZT0-based SME2 LUTI instructions need both streaming mode and ZA enabled. `SMSTART` enables the required state, and `SMSTOP` disables it.

Streaming mode changes the execution context in three ways:

- Vector and predicate lengths use the *streaming vector length* (SVL), which can differ from the non-streaming vector length
- Streaming instructions, including the multi-register LUTI2, SDOT, and SMOPA forms, become available
- `PSTATE.ZA` controls access to both the ZA matrix-storage array and `ZT0`

Efficient kernels enter streaming mode before repeated loops and exit afterwards. Streaming mode does not automatically stream matrix data from memory. The kernel still loads only the current computation tile.

## Follow the SME2 LUTI data path

A simplified SME2 LUTI sequence is:

```text
SMSTART
* load ZT0 once
* perform LUTI2
SMSTOP
```

A detailed LUTI SME2 flow is:
  1. Enter SME streaming mode with `SMSTART` and load the LUT into the sixteen 32-bit `ZT0` register.
  2. Load LHS activations and packed RHS data for the current computation tile.
  3. Use LUTI2 or LUTI4 to expand the packed RHS indices from `ZT0` into Z registers.
  4. Feed the expanded RHS elements and LHS activations to SME2 instructions, such as `SDOT` or `SMOPA`.
  5. Accumulate partial matrix products in the SME2 `ZA` array.
  6. Convert, clamp, and store the completed output tile as required by the kernel.
  7. Exit SME streaming mode with `SMSTOP`. This disables the ZA and ZT0 state after the kernel completes.

LUTI replaces the explicit unpack/decode portion of the data path. It does not replace the matrix multiply instruction that consumes the expanded values.

### Example: kernel with LUTI2

This example shows how LUTI2 expands packed 2-bit RHS weights. It simplifies register allocation, predication, addressing, and loop control to focus on the LUTI data flow.

{{% notice Note %}} This example uses a 512-bit streaming vector length (SVL). The SVL is a CPU specific property. {{% /notice %}}

__1. Define and pass the LUT__

`ZT0` contains sixteen 32-bit entries. LUTI2 uses entries 0–3; entries 4–15 are unused and contain zero.
```c
static const int32_t lut_i8_i2[16] = {-2, -1, 0, 1,};
```

For a `.B` LUTI result, the low 8 bits of the selected 32-bit entry form the destination element.

__2. Load the LUT into ZT0__

Enter streaming mode, initialize ZA, and load ZT0. The lookup table does not change across the inner matrix loop, so load it once before the loop.

```asm
smstart                   // Enable Streaming SVE mode and ZA/ZT0 state
zero    {za}              // Zero initialize accumulators for this output tile
ldr     zt0, [x_lut]      // load LUT into fixed 512-bit ZT0 table
```

__3. Load LHS and packed RHS__

Load the LHS activations and packed RHS 2-bit indices for the current computation tile, not the entire matrix.

```asm
ld1rqb  {z0.b}, ... , [x_lhs]               // load LHS
ld1b    {z16.b-z19.b}, ... , [x_packed_rhs] // load RHS packed 2-bit indices
```
  - The `z0.b` register receives the LHS activations.
  - The `z16.b`–`z19.b` registers receive the packed RHS 2-bit indices.

`ld1rqb` is the SVE load-and-replicate-quadword operation. For a 512-bit SVL, you can view `z0` as four 128-bit regions. `ld1rqb` replicates the 16-byte LHS block across those regions.

__4. LUTI2 expands the packed indices__
```asm
luti2   { z24.b - z27.b }, zt0, z16[0]     // unpack 2-bit indices
luti2   { z4.b  - z7.b  }, zt0, z17[0]

luti2   { z8.b  - z11.b }, zt0, z18[0]
luti2   { z12.b - z15.b }, zt0, z19[0]
```
Each LUTI2 instruction reads packed 2-bit indices from one source Z register (`z16` to `z19`) and expands them into four `.B` destination registers for a 512-bit SVL.

__5. Feed the expanded vectors directly to SDOT__

The expanded vectors can now feed SME2 matrix instructions such as `SDOT` or `SMOPA`, which accumulate the results in `ZA`.

## What you've learned and what's next

You've learned how LUTI operates within SME2: a micro-kernel loads the lookup table into `ZT0`, uses packed low-bit indices in Z registers to expand the RHS values, and feeds those expanded values into SME2 instructions.

Next, you'll apply these concepts to a complete low-bit matrix multiplication kernel and examine how LUTI can replace explicit unpacking and decoding in the inner computation loop.

## Further reading
- [Arm SME2 Introduction](https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/part4-arm-sme2-introduction)
- [SME2 lookup table Armv9-A Documentation](https://developer.arm.com/documentation/109246/0101/SME-Overview/SME-and-SME2/SME2-lookup-table)
- [Introduction to streaming and non-streaming mode](https://arm-software.github.io/acle/main/acle.html#controlling-the-use-of-streaming-mode)
