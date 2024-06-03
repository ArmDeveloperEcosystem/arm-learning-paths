---
title: L1 Instruction Cache Events
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## L1 Instruction Cache Events

You can use the PMU events below to measure L1 Instruction Cache effectiveness:

```C
//L1 I-cache Effectiveness Metrics
PMU_EVENT_L1I_CACHE_REFILL,
PMU_EVENT_L1I_CACHE,
PMU_EVENT_INST_RETIRED,
PMU_EVENT_INST_SPEC,
```

A series of stores to Normal Cacheable memory leads to allocations into the L1 I-cache. 

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
        *(volatile unsigned int*) (0x80000000 + (i*64)) = 0xDEADBEEF;
        *(volatile unsigned int*) (0x380000000 + (i*64)) = 0xDEADBEEF;
    } 
}
```

These stores trigger 455 accesses in the L1 I-cache, causing 5 refills of cache lines that were not in the cache before. More stores results in fewer refills to the L1 I-cache, but also results in more refills to the L1 D-cache, since the L1 I-cache only stores instructions and can snoop in the L1 D-cache. Similarly, a single instruction fetch to the L1 I-cache can access multiple instructions.

```output
L1I_CACHE is 455
L1I_CACHE_REFILL is 5
INST_RETIRED is 1096
INST_SPEC is 1893
``` 

## Instruction side cache access

Using the above code and results, this section lists the events that occur during an I-side cache access, and an I-side cache miss.

Events that always occur:
`L1I_CACHE`

Additional events that occur when there is an L1 cache miss: 
`L1I_CACHE_REFILL` and L2 cache read access events.
