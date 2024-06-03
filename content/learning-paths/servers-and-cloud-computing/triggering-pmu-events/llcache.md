---
title: LL Cache Events
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## LL Cache Events
The following events highlight Last Level cache effectiveness:

```C
//LL Cache Effectiveness Metrics
PMU_EVENT_LL_CACHE_RD,
PMU_EVENT_LL_CACHE_MISS_RD,
PMU_EVENT_INST_RETIRED,
```

Excess stores to Normal Cacheable memory cause allocations into the LL cache if a writeback is issued to the LL cache or if there is a shared cache line. 

The LL cache is used to describe levels of caches outside of the core. LL caches can be a System Level Cache (SLC) inside an interconnect such as a mesh, caches in a core in another cluster, or in a remote device. 

In the Neoverse N2 reference system, the SLC is the Last Level cache. A cache line is looked up in the SLC if it is not present in the L1 D-cache or L2 cache in a CPU.

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
        *(volatile unsigned int*) (0x40000000  + (i*64)) = 0xDEADBEEF;
        *(volatile unsigned int*) (0x380000000 + (i*64)) = 0xDEADBEEF;
    }
}
```

The resulting event counts for the code are:

```output 
LL_CACHE_RD is 0
LL_CACHE_MISS_RD is 326
INST_RETIRED is 976
```

`LL_CACHE_RD` counts transactions returned from outside of the N2, including the SLC. In this scenario, you are simulating only one N2 core in a standalone system, meaning that there are no levels of cache after the L2. For these reasons, `LL_CACHE_RD` does not count. 

Systems such as the reference design RD-N2 have an SLC inside the CMN-700 interconnect, which acts as the LL_CACHE. 

`LL_CACHE_MISS_RD` is not 0 since it counts read transactions that are returned from outside the N2, excluding the SLC. So it is likely counting bus read transactions from external system memory or a remote device.


