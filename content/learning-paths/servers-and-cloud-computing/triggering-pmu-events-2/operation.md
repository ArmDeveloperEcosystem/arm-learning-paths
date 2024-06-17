---
title: Operation Mix Events
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Operation Mix

The operation mix comprises these groups: 

- SIMD percentage.
- Scalar floating point percentage.
- Integer percentage.
- Branch percentage.
- Load percentage.
- Store percentage.

### SIMD percentage

To trigger `ASE_SPEC` and `ASE_INST_SPEC`,  create a function using NEON instructions:

```C
    .global simd
    .type simd, "function"
    .cfi_startproc
    .global simd
simd:
    LDR X0, =array
    LD2 {v0.4S, v1.4S}, [x0]
    ADD V2.4S, V0.4S, V1.4S
    RET
    .cfi_endproc

.data
array: .word 10, 20, 30, 40, 50, 60
```

The resulting event counts for this code are:

```output
INST_SPEC is 12
ASE_SPEC is 1
ASE_INST_SPEC is 3
```

The results show `ASE_SPEC` is 1 and `ASE_INST_SPEC` is 3. `ASE_INST_SPEC` counts speculatively executed Advanced SIMD operations. Meanwhile, `ASE_SPEC` counts speculatively executed Advanced SIMD operations, excluding load, store, and move micro-operations that move data to or from the SIMD registers. `ASE_INST_SPEC` counts 1 from LD2 and 2 from ADD: adding, then storing. `ASE_SPEC` only counts 1 from the actual NEON add operation.
  
## Scalar floating point percentage

To trigger `VFP_SPEC`, a scalar adding function is made:

```C
    .global scalar_fp
    .type scalar_fp, "function"
    .cfi_startproc
    .global scalar_fp
scalar_fp:
    FMOV D1, #1.5
    FMOV D2, #3.0
    ADD D0, D1, D2
    RET
    .cfi_endproc
```

The resulting event counts for the code are:

```output
INST_SPEC is 11
VFP_SPEC is 2
```

This happens because `VFP_SPEC` does not count instructions that move data to or from floating point registers, it only counts the ADD operation. The results show that `VFP_SPEC` is 2. Although there is one ADD operation, the floating point instruction can be split up into two micro-operations.
 
## Integer and branch percentage

The following code uses a GCD function to trigger `DP_SPEC`, `BR_IMMED_SPEC`, and `BR_INDIRECT_SPEC`.

```C
    .section  GCD,"ax"
    .align 3

    .global gcd
    .type gcd, @function

    .cfi_startproc

gcd:
    CMP W0, W1
    B.EQ exit
    B.LT less
    SUB W0, W0, W1
    B gcd

less:
    SUB W1, W1, W0
    B gcd

exit:
    RET
    .cfi_endproc
```
```C
void branch_test()
{ 
    int ans, e, f;
    e = 50;
    f = 75;
    for (int i = 0; i < 5; i++)
    {
        ans = gcd(e, f);
        e+=5;
        f+=5;
    }
}
```

The resulting event counts for the code are:

```output
INST_SPEC is 326
DP_SPEC is 136
BR_INDIRECT_SPEC is 6
BR_IMMED_SPEC is 113
```

`DP_SPEC` is triggered by speculatively executed logical or arithmetic instructions. `BR_IMMED_SPEC` is triggered by immediate branch instructions, including B <> and B.cond <>. Lastly, `BR_INDIRECT_SPEC` is triggered by any instructions that force a software change of the program counter that are speculatively executed, including RET. 

