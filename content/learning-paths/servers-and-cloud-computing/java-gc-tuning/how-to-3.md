---
title: Tuning the GC
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Is your GC NUMA aware?

Non-uniform memory architecture occurs when the memory performance varies depending on which core the application is running on and where the data is in memory. This is a common occurence if you are using a system with multiple sockets. If your system has multiple sockets you need to ensure the GC is aware of this to optimise memory access patterns. The command line option below can be used to enable NUMA-aware GC.

```bash
+XX:+UseNUMA
```
### Is the GC Heap Size Appropriate?

If the size of the heap is too small, excessive time will be spent in GC compared to the application logic. However disproportionately large heaps will result in longer GC pauses as there is more memory to parse. It is recommended the max heap size is not greater that the physical memory on your system, if multiple JVMs are running the sum of their heaps must not exceed the total physical memory (the `free -h` command can be used to find the phyisical memory). This is to avoid the high latency accesses to access memory on disk from swapping during a full GC sweep. Please see the memory analysis section for more information.

The `-Xmx <N>` and `-Xms <N>` options can be used to specify the maximum and minimum memory sizes respectively.

Unfortunately there is no hard rule on which values to set. However a rule of thumb is to aim for 30% occupation of the heap after a full GC. This requires running the application until a steady state has been reached.

The heap size is dynamically resized as the application runs. If you know exactly the heap size, setting the minimum and maximum values will slightly improve the performance since resizing will never take place.