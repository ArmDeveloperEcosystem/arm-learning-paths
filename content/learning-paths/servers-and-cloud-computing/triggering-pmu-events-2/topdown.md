---
title: Topdown Methodology L1 Events
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

{{% notice Note %}}
The white paper [Arm CPU Telemetry Solution Topdown Methodology Specification](https://developer.arm.com/documentation/109542/0100/?lang=en) describes the Topdown Methodology referenced below. 
{{% /notice %}}

```C
//Top Down L1 Metrics
PMU_EVENT_CPU_CYCLES,
PMU_EVENT_STALL_SLOT_BACKEND,
PMU_EVENT_STALL_SLOT_FRONTEND,
PMU_EVENT_STALL_SLOT,
PMU_EVENT_BR_MIS_PRED,
PMU_EVENT_OP_RETIRED,
PMU_EVENT_OP_SPEC,   
```
These PMU events highlight backend inefficiency, frontend inefficiency, bad speculation, and retiring. The following groups are described below:
- Backend inefficiency: execution unit, D-Cache misses, translation delays caused by D-TLB walks
- Frontend inefficiency: branch prediction unit, fetch latency due to I-Cache misses, translation delays caused by I-TLB walks
- Bad speculation: branch mispredictions
- Retiring: underutilization of micro-architectural capabilities 
-- Ex. Using scalar execution instead of vector operations

## Backend
The code below creates pressure on the backend. Excessive stores to Normal Cacheable memory cause D-cache misses by filling up the cache and cause D-TLB walks because new translations are not yet cached in the TLB. 
```C
void stores()
{
    for (volatile unsigned int i = 0; i < 150; i++)
    {
        *(volatile unsigned int*) (0x3C0000000 + (i*64)) = 0xDEADBEEF;
        *(volatile unsigned int*) (0x180000000 + (i*64)) = 0xDEADBEEF;
        *(volatile unsigned int*) (0x200000000 + (i*64)) = 0xDEADBEEF;
        *(volatile unsigned int*) (0x2C0000000 + (i*64)) = 0xDEADBEEF;
        *(volatile unsigned int*) (0x1C0000000 + (i*64)) = 0xDEADBEEF;
        *(volatile unsigned int*) (0x100000000 + (i*64)) = 0xDEADBEEF;
        *(volatile unsigned int*) (0x40000000 + (i*64)) = 0xDEADBEEF;
        *(volatile unsigned int*) (0x380000000 + (i*64)) = 0xDEADBEEF;
    } 
}
```

```output
CPU_CYCLES is 8622
STALL_SLOT_BACKEND is 31753
STALL_SLOT_FRONTEND is 13902
STALL_SLOT is 45655
```

The simulation results show a significantly higher cycle count for the backend compared to the frontend. `STALL_SLOT_BACKEND` counts the number of cycles when no operation is sent for execution on a slot due to the backend. In this case, there may be issue stage fullness or execution stage fullness because of D-cache misses and D-TLB walks. When a cache miss occurs, the CPU must use extra cycles to check the next level cache, going all the way to main memory if needed. Likewise, when a translation is not readily available in the D-TLB, the CPU must perform a translation table walk to retrieve the translation, causing latency.

## Frontend
The following code is intended to create frontend inefficiency using branches, causing stress on the branch prediction unit. 
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

    // GCD
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

```output
CPU_CYCLES is 414
STALL_SLOT_BACKEND is 396
STALL_SLOT_FRONTEND is 1829
STALL_SLOT is 2225
```

Now, the simulation results show a higher cycle count for the frontend. `STALL_SLOT_FRONTEND` counts the number of cycles when no operation is sent for execution on a slot due to the frontend. Since the branch predictor is also in the frontend, the excessive branching creates latency.

## Bad Speculation
The following GCD code can be used for bad speculation as well. More branching will result in branch mispredictions. 
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

    // GCD
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

```output
CPU_CYCLES is 414
STALL_SLOT is 2225
BR_MIS_PRED is 20
```
 
The simulation results show 20 branch mispredictions, counted by `BR_MIS_PRED`. `BR_MIS_PRED` counts speculatively executed branches that were either mispredicted or were not predicted.

## Retiring
We can also create code to measure the retiring of a CPU:
```C
    .global scalar
    .type scalar, "function"
    .cfi_startproc
    .global scalar
scalar:
    MOV X1, #0x1100
    MOV X2, #0x0000
    ADD X0, X1, X2
    RET
    .cfi_endproc
```

```output
CPU_CYCLES is 51
STALL_SLOT is 295
OP_RETIRED is 8
OP_SPEC is 11
```
 
The results above show how many operations were retired using scalar addition. Retiring can reveal if a CPU is utilizing its full capabilities. `OP_RETIRED` counts the number of operations executed, whereas `OP_SPEC` counts the number of speculative operations executed. `OP_RETIRED` is lower than `OP_SPEC` because some speculatively executed operations may have been abandoned due to a branch mispredict.


