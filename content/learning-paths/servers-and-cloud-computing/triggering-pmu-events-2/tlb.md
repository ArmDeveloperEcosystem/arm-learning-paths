---
title: TLB Events
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### ITLB Events

You can use the events described below to demonstrate ITLB effectiveness:

```C
//ITLB Effectiveness Metrics
PMU_EVENT_L1I_TLB,
PMU_EVENT_L1I_TLB_REFILL,
PMU_EVENT_L2D_TLB,
PMU_EVENT_L2D_TLB_REFILL,
PMU_EVENT_ITLB_WALK,
PMU_EVENT_INST_RETIRED,
```

To trigger an ITLB walk, there must be a miss in the ITLB. The following self-modifying code places a new instruction into memory that has not been accessed before:

```C
    .global itlb_test
    .type itlb_test, "function"
    .cfi_startproc
    .global itlb_test
itlb_test:
    LDR x0, =ret_opcode
    LDR w1, [x0]
    LDR x2, =0xc0000000
    STR x1, [x2]
    DC CVAU, x2
    DSB SY
    IC IVAU, x2
    DSB SY
    ISB

    BR x2
ret_opcode:
    RET
    .cfi_endproc
```

The resulting event counts for the code are:

```output
L1I_TLB is 57
L1I_TLB_REFILL is 1
L2D_TLB is 2
L2D_TLB_REFILL is 1
ITLB_WALK is 0
INST_RETIRED is 15
```
 
In this case, there are 57 accesses into the ITLB, but only one refill into both the L1 I-TLB and the L2 D-TLB. So, only one translation was not cached in the L1 I-TLB. `ITLB_WALK` does not count in this scenario, because for it to count, a miss in the L1 I-TLB and L2 TLB must be driven at the same time. Through branch prediction or speculation, the data might already exist in the L2 TLB.

To trigger an L2_TLB miss, the following assembly function clears the TLB to remove any branch prediction or speculation:

```C
    .global clear_tlb
    .type clear_tlb, "function"
    .cfi_startproc
    .global clear_tlb
clear_tlb:
    TLBI ALLE3
    DSB SY
    ISB
    .cfi_endproc
```

`TLBI ALLE3` clears the entire ITLB, for only EL3 translations, and removes any *predicted* translations to force a miss. Then, new memory will be accessed. 

```output
L1I_TLB is 73
L1I_TLB_REFILL is 3 
L2D_TLB is 6
L2D_TLB_REFILL is 4
ITLB_WALK is 3
INST_RETIRED is 17
```

## Instruction side TLB access

This section describes what happens in the ITLB during a TLB access, which can be triggered using store instructions.  

```C  
void stores()
{
    for (volatile unsigned int i = 0; i < 30; i++)
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

Events that always occur:

`L1I_TLB`

```output
L1I_TLB is 227
L1I_TLB_REFILL is 0
L2D_TLB is 9
L2D_TLB_REFILL is 9
ITLB_WALK is 0
```
 
No ITLB walks are triggered since there might be speculation or branch prediction happening in the ITLB. Similarly, there are no L1 I-TLB refills, since there are no misses that result in allocations. 

Additional events that occur with an L1 I-TLB miss:
`L2D_TLB` and `L1I_TLB_REFILL`.

Additional events that occur with an L2 TLB miss:
`ITLB_WALK` and `L2D_TLB_REFILL`.

To trigger TLB Refills and an ITLB walk, clear the TLB with the following code:

```C
    .global clear_tlb
    .type clear_tlb, "function"
    .cfi_startproc
    .global clear_tlb
clear_tlb:
    TLBI ALLE3
    DSB SY
    ISB
    .cfi_endproc
```

The resulting event counts for the code are:

```output
L1I_TLB is 73
L1I_TLB_REFILL is 3
L2D_TLB is 6
L2D_TLB_REFILL is 4
ITLB_WALK is 3
```

After clearing the ITLB, you can force new memory accesses translations, resulting in ITLB walks and L1 I-TLB refills. Note that `ITLB_WALK` does not count walks triggered by TLB maintenance operations. Instead, these walks might be the result of the barrier instructions. 

### D-TLB Events

The following PMU events provide metrics on D-TLB effectiveness:

```C
//DTLB Effectiveness Metrics
PMU_EVENT_L1D_TLB,
PMU_EVENT_L1D_TLB_REFILL,
PMU_EVENT_L2D_TLB,
PMU_EVENT_L2D_TLB_REFILL,
PMU_EVENT_INST_RETIRED,
PMU_EVENT_DTLB_WALK,
```

A lot of stores cause D-TLB accesses, refills, and walks.

```C
void stores()
{
    for (volatile unsigned int i = 0; i < 30; i++)
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

Since these 8 stores access new memory translations, there are 8 counts of `L1D_TLB_REFILL`, `L2D_TLB_REFILL`, and `DTLB_WALK`.

```output
L1D_TLB is 731
L1D_TLB_REFILL is 8 
L2D_TLB is 8
L2D_TLB_REFILL is 8
DTLB_WALK is 8
INST_RETIRED is 976
```

## Data side TLB access for a load instruction

This section describes what happens in the D-TLB during a load instruction. The following code reads from many different addresses, which forces a D-TLB access.    

```C
void loads()
{
    for (volatile unsigned int i = 0; i < 30; i++)
    {
        char *value = (char *)0x3C0000000 + (i*64);
        char *value1 = (char *)0x200000000 + (i*64);
        char *value2 = (char *)0x1C0000000 + (i*64);
        char *value3 = (char *)0x180000000 + (i*64);
        char *value4 = (char *)0x380000000 + (i*64);
        char *value5 = (char *)0x40000000 + (i*64);
        char *value6 = (char *)0x2C0000000 + (i*64);
    } 
} 
```

Events that always occur during a D-TLB access are:
`LD_SPEC`, `MEM_ACCESS`, `MEM_ACCESS_RD`, `L1D_TLB`, and `L1D_TLB_RD`.

```output
LD_SPEC is 363
MEM_ACCESS is 317
MEM_ACCESS_RD is 278
L1D_TLB is 317
L1D_TLB_REFILL is 278 
```

`MEM_ACCESS` counts memory accesses issued by the Load Store Unit, both load and store operations. `MEM_ACCESS_RD` is a subset of `MEM_ACCESS`, only counting load operations that result in memory accesses. In this case, `MEM_ACCESS` is equal to `L1D_TLB` because each memory access has an associated D-TLB lookup. Similarly, each `MEM_ACCESS_RD` has an associated D-TLB lookup.

Additional events that occur with a L1 D-TLB miss are:
`L2D_TLB`, `L2D_TLB_RD`, `L1D_TLB_REFILL`, and `L1D_TLB_REFILL_RD`.

```output
L2D_TLB is 0
L2D_TLB_RD is 0
L1D_TLB_REFILL is 0
L1D_TLB_REFILL_RD is 0
```

There might be some branch prediction or speculation occurring in the TLB, resulting in no misses. The code below clears the TLB to force a miss.

```C 
    .global clear_tlb
    .type clear_tlb, "function"
    .cfi_startproc
    .global clear_tlb
clear_tlb:
    TLBI ALLE3
    DSB SY
    ISB
    .cfi_endproc
```

Calling this function before the loads produces these results:

```output
L2D_TLB is 7
L2D_TLB_RD is 5
L1D_TLB_REFILL is 3
L1D_TLB_REFILL_RD is 1
```

Now there are refills in the L1 D-TLB caused by the TLB miss. There are also D-side TLB accesses caused by a memory read operation, counted by `L2D_TLB_RD`. `L2_TLB_REFILL_RD` counts any allocation into the L2 TLB caused by an I-side or D-side memory read operation. 

Additional events that occur with a L2 TLB miss are:
`DTLB WALK`, `L2D_TLB_REFILL`, and `L2D_TLB_REFILL_RD`.

```output
DTLB_ALK is 2
L2D_TLB_REFILL is 5
L2D_TLB_REFILL_RD is 3
```

Since the TLB has been cleared, `DTLB_WALK` and `L2_TLB_REFILL` are triggered to get the translations from main memory and refill it into the L2 D-TLB.

## Data side TLB access for a store instruction

This section describes what happens in the D-TLB during a store instruction. The following code writes to many different Normal Cacheable memory addresses, which forces a D-TLB access.  

```C 
void stores()
{
    for (volatile unsigned int i = 0; i < 30; i++)
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

Events that always occur:
`ST_SPEC`, `MEM_ACCESS`, `MEM_ACCESS_WR`, `L1D_TLB`, and `L1D_TLB_WR`.

```output
ST_SPEC is 468
MEM_ACCESS is 702
MEM_ACCESS_WR is 301
L1D_TLB is 702
L1D_TLB_WR is 301
```

`MEM_ACCESS` counts memory accesses that the Load Store Unit issues, both load and store operations. `MEM_ACCESS_WR` is a subset of `MEM_ACCESS`, only counting store operations that result in memory accesses. In this case, `MEM_ACCESS` is equal to `L1D_TLB` because each memory access has an associated D-TLB lookup. Similarly, each `MEM_ACCESS_RD` has an associated D-TLB lookup.

Additional events that occur with a L1 D-TLB miss:
`L2D_TLB`, `L2D_TLB_WR`, `L1D_TLB_REFILL`, and `L1D_TLB_REFILL_WR`.

```output
L2D_TLB is 9
L2D_TLB_WR is 
L1D_TLB_REFILL is 9
L1D_TLB_REFILL_WR is 9
```

Additional events that occur with an L2 TLB miss:
`DTLB_WALK`, `L2D_TLB_REFILL`, and `L2D_TLB_REFILL_WR`.

```output
DTLB_WALK is 9
L2D_TLB_REFILL is 9
L2D_TLB_REFILL_WR is 9
```
These results show that each TLB access is caused by a write operation and missed in each TLB level, causing a D-TLB walk. Each TLB miss also causes a refill into the L1 D-TLB first, and then secondly, a refill into the L2 D-TLB.
