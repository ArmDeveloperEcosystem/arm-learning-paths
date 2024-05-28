---
title: Topdown Methodology L1 Events
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---


{{% notice Note %}}
To run the code in this Learning Path and collect the output, your software or debug environment needs a way to print a message to a console. The code used here was run on an Arm internal simulation environment, but you can run it on any simulation environment with printf() support, or on hardware with printf() support. 

This code was run in a bare-metal environment in EL3 with minimal software overhead. If you are running this code on an operating system, such as Linux, you may see slight variations in the PMU event counts due to the overhead of the OS.
{{% /notice %}}

The first step in topdown performance analysis is to investigate the CPU pipeline efficiency and look at the distribution of how CPU cycles are spent. 

The results from the first phase guide where to look next to find areas for performance improvement.

{{% notice Note %}}
The white paper [Arm CPU Telemetry Solution Topdown Methodology Specification](https://developer.arm.com/documentation/109542/0100/?lang=en) describes the Topdown Methodology referenced below. 
{{% /notice %}}

The first-level metrics to look at are:

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

These PMU events highlight backend inefficiency, frontend inefficiency, bad speculation, and instruction retiring. 

The following groups are described below:

- Backend inefficiency: execution unit, D-Cache misses, and translation delays caused by D-TLB walks.
- Frontend inefficiency: branch prediction unit, fetch latency due to I-Cache misses, and translation delays caused by I-TLB walks.
- Bad speculation: branch mispredictions.
- Retiring: under-utilization of micro-architectural capabilities such as scalar execution instead of vector operations.

## Backend inefficiency

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

The resulting event counts for the code are:

```output
CPU_CYCLES is 8622
STALL_SLOT_BACKEND is 31753
STALL_SLOT_FRONTEND is 13902
STALL_SLOT is 45655
```

The results show a significantly higher cycle count for the backend compared to the frontend. `STALL_SLOT_BACKEND` counts the number of cycles when no operation is sent for execution on a slot due to the backend. In this case, there may be issue stage fullness or execution stage fullness because of D-cache misses and D-TLB walks. When a cache miss occurs, the CPU must use extra cycles to check the next level cache, going all the way to main memory if needed. Likewise, when a translation is not readily available in the D-TLB, the CPU must perform a translation table walk to retrieve the translation, causing latency.

## Frontend inefficiency

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

The resulting event counts for the code are:

```output
CPU_CYCLES is 414
STALL_SLOT_BACKEND is 396
STALL_SLOT_FRONTEND is 1829
STALL_SLOT is 2225
```

Now the results show a higher cycle count for the frontend. `STALL_SLOT_FRONTEND` counts the number of cycles when no operation is sent for execution on a slot due to the frontend. Since the branch predictor is also in the frontend, the excessive branching creates latency.

## Bad Speculation

The following greatest common divisor (GCD) code can be used for bad speculation as well. More branching results in higher branch mispredictions. 

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

The resulting event counts for the code are:

```output
CPU_CYCLES is 414
STALL_SLOT is 2225
BR_MIS_PRED is 20
```
 
The results show 20 branch mispredictions, counted by `BR_MIS_PRED`. `BR_MIS_PRED` counts speculatively executed branches that were either mispredicted or were not predicted.

## Retiring

The code below can be used to measure the retiring of a CPU:

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

The resulting event counts for the code are:

```output
CPU_CYCLES is 51
STALL_SLOT is 295
OP_RETIRED is 8
OP_SPEC is 11
```
 
The results show how many operations were retired using scalar addition. Retiring can reveal if a CPU is utilizing its full capabilities. `OP_RETIRED` counts the number of operations executed, whereas `OP_SPEC` counts the number of speculative operations executed. `OP_RETIRED` is lower than `OP_SPEC` because some speculatively executed operations may have been abandoned due to a branch mispredict.

