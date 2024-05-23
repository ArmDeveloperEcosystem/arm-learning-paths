---
title: L1 Data Cache Events
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## L1 Data Cache Events

Use these PMU events to measure the effectiveness of the L1 Data Cache: 

```C
    //L1 D-Cache Effectiveness Metrics
    PMU_EVENT_L1D_CACHE_REFILL,
    PMU_EVENT_L1D_CACHE,
    PMU_EVENT_INST_RETIRED,
```

To trigger these events, run code that issues stores to Normal Cacheable memory such as:

```C
void stores()
{
    for (volatile unsigned int i = 0; i < 10; i++) 
    {
        *(volatile unsigned int*) (0x3C0000000 + (i*64)) = 0xDEADBEEF; 
    } 
}
```

The resulting event counts are:

```output
L1D_CACHE_REFILL is 11
L1D_CACHE is 65
INST_RETIRED is 100
```

These stores trigger 65 accesses into the L1 D-cache, counted by `L1D_CACHE`. 

Event `L1D_CACHE_REFILL` counts 11 refills in the L1 D-cache as these stores were not previously there in the cache, so the CPU allocates these cache lines for future access. 

### L1 Data Cache Read Access

This section describes what happens in the L1 D-cache during a read, which can be triggered by this code:    

```C
void read_access()
{
    for (volatile unsigned int i = 0; i < 30; i++)
    {
        char *value = (char *)0x3C0000000 + (i*64);
    }
}
```

Events that always occur are: 
`L1D_CACHE`, `L1D_CACHE_RD`, `MEM_ACCESS`, `MEM_ACCESS_RD`.

```output
L1D_CACHE is 135
L1D_CACHE_RD is 93
MEM_ACCESS is 135
MEM_ACCESS_RD is 93
```

`MEM_ACCESS` counts memory accesses issued by the Load Store Unit (LSU) inside your core, which is equal to `L1D_CACHE` in this instance. `MEM_ACCESS_RD` counts the number of memory accesses issued by the LSU due to load operations, which is equal to `L1D_CACHE_RD` in this instance. `L1D_CACHE_RD` counts L1 D-cache accesses caused by a load operation.

Additional events that occur with an L1 cache miss:

* `L1D_CACHE_REFILL`, 
* `L1D_CACHE_REFILL_RD`, 
* `L2 cache read access events`.

If the cache line refill is from an outside cluster: `L1D_CACHE_REFILL_OUTER`, and the events above.

If the L1 D-cache was full and the evicted line was dirty: 

* `L1D_CACHE_WB`
* `L1D_CACHE_WB_VICTIM`
*...and the events above. 

Note: `L1D_CACHE_REFILL_OUTER` is only counted when cache line allocations into the L1 D-cache are obtained from outside of the cluster. 

```output
L1D_CACHE_REFILL is 1
L1D_CACHE_REFILL_RD is 1
L1D_CACHE_REFILL_OUTER is 1
L1D_CACHE_WB is 0
L1D_CACHE_WB_VICTIM is 0
```

The same code produces the above results, showing the L1 D-cache is refilled once from a read, and from outside of the cluster. This refill did not cause a dirty cache line eviction, counted by `L1D_CACHE_WB_VICTIM`. `L1D_CACHE_WB` counts any cache line evictions of dirty data, whereas `L1D_CACHE_WB_VICTM` counts any cache line evictions of dirty data due to a new cache line allocation.


### L1 Data cache write access 

This section describes what happens in the L1 D-cache during a read, which can be triggered by using store instructions to Normal Cacheable memory.  

```C  
void write_access()
{
    for (volatile unsigned int i = 0; i < 30; i++)
    {
        *(volatile unsigned int*) (0x3C0000000 + (i*64)) = 0xDEADBEEF;
    }
}
```

Events that always occur:

* `L1D_CACHE`
* `L1D_CACHE_WR`
* `MEM_ACCESS`
* `MEM_ACCESS_WR`

```output
L1D_CACHE is 164
L1D_CACHE_WR is 71
MEM_ACCESS is 164
MEM_ACCESS_WR is 71
```

`MEM_ACCESS` counts memory accesses issued by the Load Store Unit, which is equal to `L1D_CACHE` in this instance. `MEM_ACCESS_WR` counts the number of memory accesses issued by the LSU due to store operations, which is equal to `L1D_CACHE_WR` in this instance. `L1D_CACHE_WR` counts L1 D-cache accesses caused by store operations.

Additional events that occur with an L1 Cache miss:

* `L1D_CACHE_REFILL`
* `L1D_CACHE_REFILL_WR` 
* `L2 cache read access events`

If the cache line refill is from an outside cluster: `L1D_CACHE_REFILL_OUTER`, and the events above.

If the L1 D-cache was full and the evicted line was dirty: 

* `L1D_CACHE_WB`
* `L1D_CACHE_WB_VICTIM`
* ..and the events above. 

Note: `L1D_CACHE_REFILL_OUTER` is only counted when cache line allocations into the L1 D-cache are obtained from outside of the cluster. 

```output
L1D_CACHE_REFILL is 30
L1D_CACHE_REFILL_WR is 29
L1D_CAHE_REFILL_OUTER is 4
L1D_CACHE_WB is 0
L1D_CACHE_WB_VICTIM is 0
```

Add a few more stores to Normal Cacheable memory to trigger `L1D_CACHE_WB`:

```C
void write_access()
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
L1D_CACHE_REFILL is 235
L1D_CACHE_REFILL_WR is 234
L1D_CAHE_REFILL_OUTER is 41
L1D_CACHE_WB is 118
L1D_CACHE_WB_VICTIM is 118
```

`L1D_CACHE_WB` counts both victim cache line evictions and cache writebacks from snoops or software-based Cache Maintenance Operations (CMOs).  

`L1D_CACHE_WB_VICTIM` is a subset of `L1D_CACHE_WB`, only counting writebacks that are a result of a cache line allocation. As they are equal, all writebacks were caused by a cache line allocation.
