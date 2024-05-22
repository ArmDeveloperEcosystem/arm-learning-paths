---
title: L2 Unified Cache Events
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## L2 Unified Cache Events

The following PMU events can be used to highlight effectiveness of the L2 cache: 

```C
        // L2 Cache Effectiveness Metrics
        PMU_EVENT_L2D_CACHE_REFILL,
        PMU_EVENT_L2D_CACHE,
        PMU_EVENT_L2D_CACHE_WR,
        PMU_EVENT_L2D_CACHE_RD,
        PMU_EVENT_L1D_CACHE_WR,
        PMU_EVENT_INST_RETIRED,
```

To trigger these events, the L1 D-cache must be full. To acheieve this, you can run code to issue many stores to Normal Cacheable memory.

```C
void stores()
{
    for (volatile unsigned int i = 0; i < 30; i++)
    {
        *(volatile unsigned int*) (0x3C0000000 + (i*64)) = 0xDEADBEEF;
    }
}
```

The resulting event counts for the code are:

```output
L2D_CACHE is 32
L2D_CACHE_REFILL is 5
L2D_CACHE_WR is 0
L2D_CACHE_RD is 32
L1D_CACHE_WR is 70
INST_RETIRED is 280
```

The stores created 32 L2 D-cache accesses and 5 refills. `L2D_CACHE_WR` is 0 because no memory write operation was looked up in the L2 cache, counting any writebacks from the L1 data cache that allocate into the L2 cache. However, you can see L2 cache accesses due to reads, in `L2D_CACHE_RD`. This event counts whether there is a hit or a miss in the L2 cache. As a result, all of the data written was stored in the L1 D-cache and the L2 D-cache refills were triggered by read operations only.

Writing to more addresses will trigger L2 cache accesses due to write operations:

```C
void stores()
{
    for (volatile unsigned int i = 0; i < 30; i++)
    {
        *(volatile unsigned int*) (0x3C0000000 + (i*64)) = 0xDEADBEEF;
        *(volatile unsigned int*) (0x180000000 + (i*64)) = 0xDEADBEEF;
        *(volatile unsigned int*) (0x200000000 + (i*64)) = 0xDEADBEEF;
    } 
}
```

The resulting event counts for the code are:

```output
L2D_CACHE is 95
L2D_CACHE_REFILL is 14
L2D_CACHE_WR is 1
L2D_CACHE_RD is 94
L1D_CACHE_WR is 142
INST_RETIRED is 491
```

There is 1 L2 D-cache access due to a write operation, counted by `L2D_CACHE_WR`. To trigger even more, there must be more stores issued to Normal Cacheable memory.

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

The resulting event counts for the code are:

```output
L2D_CACHE is 350
L2D_CACHE_REFILL is 38
L2D_CACHE_WR is 111
L2D_CACHE_RD is 239
L1D_CACHE_WR is 301
INST_RETIRED is 976
```

Now there are 111 L2 D-cache accesses due to write operations. 

## L2 Cache Read Access

This code highlights what occurs during an L2 cache read access, caused by a series of loads.

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

Events that will always occur during an L2 read access are:
`L2D_CACHE`, `L2D_CACHE_RD` 

```output
L2D_CACHE is 1
L2D_CACHE_RD is 1
```

Additional events that occur when there is an L2 cache miss are:
`L2D_CACHE_REFILL`, `L2D_CACHE_REFILL_RD`, `BUS_ACCESS`, and `BUS_ACCESS_RD`

The resulting event counts for the code are:

```
L2D_CACHE_REFILL is 1
L2D_CACHE_REFILL_RD
BUS_ACCESS is 2
BUS_ACCESS_RD is 2
```

`BUS_ACCESS` counts any memory accesses issued by the LSU from the CPU to the DSU. Since the DSU is always implemented with the direct connect configuration for Neoverse cores and has no L3 cache, the transaction will go to the system interconnect, counting D-side and I-side accesses. In the RD-N2 system, the Coherent Mesh Network (CMN) is the system interconnect. `BUS_ACCESS_RD` will work similarly and counts the memory read transactions issued by the LSU from the CPU to the system interconnect.  Since there was a miss in the `L2D_CACHE`, an access to the system interconnect must be made to check for the missed data. The missed data was found outside of the L2 cache, resulting in a `L2D_CACHE_REFILL`. 

Additional events that occur if the cache line was fetched outside of the CMN mesh:
`REMOTE_ACCESS`

Otherwise, if the cache line was not fetched outside of the mesh, `REMOTE_ACCESS` will not count.

```output
REMOTE_ACCESS is 0
L2D_CACHE_REFILL is 1
L2D_CACHE_REFILL_RD is 1
L2D_CACHE_WB is 0
```

`REMOTE_ACCESS` is 0 because you are not simulating a multi-socket system, so another socket is never accessed. 

Additional events that occur if the L2 cache is full: 
`L2D_CACHE_WB` and `L2D_CACHE_WB_VICTIM`

Reads don’t typically cause writebacks. You can use a store instruction to trigger the above events plus a writeback:

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

The resulting event counts for the code are:

```output
REMOTE_ACCESS is 0
L2D_CACHE_REFILL is 74
L2D_CACHE_REFILL_RD is 74
L2D_CACHE_WB is 63
L2D_CACHE_WB_VICTIM is 63
```

Due to the stores, there are 63 cache line writebacks, meaning any data that is written from the L2 cache to outside the CPU. All of these writebacks were caused by a new allocation into the L2 cache, counted by `L2D_CACHE_WB_VICTIM`, forcing an eviction chosen by the victim counter.


## L2 Cache Write Access

This code highlights what occurs during an L2 cache write access. In order to trigger this, a series of stores to Normal Cacheable memory to fill up the L1 D-cache will cause an overflow into the L2 cache. 

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

Events that will always occur during an L2 cache write access are:
`L2D_CACHE` and `L2D_CACHE_WR`

```output
L2D_CACHE is 366
L2D_CACHE_WR is 116
```

Additional events that occur when there is an L2 cache miss are:
`L2D_CACHE_REFILL`, `L2D_CACHE_REFILL_WR`, `BUS_ACCESS` and `BUS_ACCESS_WR`

```output
L2D_CACHE_REFILL is 49
L2D_CACHE_REFILL_WR is 49
BUS_ACCESS is 704
BUS_ACCESS_WR is 24
```

`BUS_ACCESS` counts any memory accesses issued by the LSU from the CPU to the DSU. Since the DSU is always implemented with the direct connect configuration for Neoverse cores and has no L3 cache, the transaction will go to the system interconnect, counting D-side and I-side accesses. `BUS_ACCESS_WR` will work similarly and counts the memory write transactions issued by the LSU from the CPU to the system interconnect. Since there was a miss in the `L2D_CACHE`, an access to the system interconnect must be made to check for the missed data.  


Events that occur if the cache line was fetched outside of the CMN mesh:
`REMOTE_ACCESS`,  and the events listed above.

Otherwise, if the cache line was not fetched outside of the mesh, `REMOTE_ACCESS` will not count but `L2D_CACHE_REFILL` and `L2D_CACHE_REFILL_RD` will – as seen below:

```output
REMOTE_ACCESS is 0
L2D_CACHE_REFILL is 49
L2D_CACHE_REFILL_WR is 49
```

`REMOTE_ACCESS` is 0 because you are not simulating a multi socket system so another socket is never accessed. However, the missed data was found outside of the L2 cache, resulting in a `L2D_CACHE_REFILL`.

Events that occur if the L2 cache is full: 
`L2D_CACHE_WB`, `L2D_CACHE_WB_VICTIM`, and the events listed above (`REMOTE_ACCESS` may not count).

```output
L2D_CACHE_WB is 14
L2D_CACHE_WB_VICTIM is 14
```
There are 14 cache line writebacks, meaning any data that is written from the L2 cache to outside the CPU. All of these writebacks were caused by a new allocation into the L2 cache, forcing an eviction chosen by the victim counter.



