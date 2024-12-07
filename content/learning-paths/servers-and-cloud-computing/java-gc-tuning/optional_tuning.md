---
title: Intermediate GC Tuning Options
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Optional Tuning Parameters

If you have an intermediate understanding of Java performance, you can experiment with the additional tuning options in this section to see how it impacts your applications performance. This is a non-exhaustive list. Please see the 'Next Steps' tab for further reading. 

### Which adaptive heap sizing strategy is being used?

The JVM attempts to find an optimal sizing solution within the bounds of the policies and parameters through adaptive sizing, varying the generation and heap sizes dynamically during execution. This is on the assumption that historic GC cycles will be similar to future GC cycles. This is generally true. 

However, in specific cases where you have existing knowledge of the heap requirements, for example a small, short-lived java utility, disabling adaptive sizing using the flag shown below can avoid the small overhead and time taken to resize. Note the `-` before the `UseAdaptiveSizePolicy` disables this feature.  

```bash
-XX:-UseAdaptiveSizePolicy
```

In JDK8, to observe how the JVM is resizing an application, set the `-XX:+PrintAdaptiveSizePolicy` to print the information on generation resizing in the GC log. 

### Is your GC NUMA aware?

Non-uniform memory architecture(NUMA) occurs when the memory performance varies depending on which core the application is running on and where the data is in memory. This is a common occurence if you are using a system with multiple sockets. If your system has multiple sockets you need to ensure the GC is aware of this to optimise memory access patterns. The `numactl` command line tool can be used to check if your system is of non-uniform memory architecture. 

You can install `numactl` with your distribution's package manager, For example on Ubuntu, you can run `sudo apt-get install numactl`.

The command line option below can be used to enable NUMA-aware GC:

```bash
+XX:+UseNUMA
```


### Is the GC Heap Size Appropriate?

If the size of the heap is too small, excessive time will be spent in GC compared to the application logic. However disproportionately large heaps will result in longer GC pauses as there is more memory to parse. The `-Xmx <N>` and `-Xms <N>` options can be used to specify the maximum and minimum memory sizes respectively. If you know the heap size required based on data, setting the minimum and maximum values will slightly improve the performance since resizing will never take place.

It is recommended the max heap size is not greater that the physical memory on your system. If multiple JVMs are running the sum of their heaps must not exceed the total physical memory (the `free -h` command can be used to find the phyisical memory). This is to avoid the high latency accesses to access memory on disk from swapping during a full GC sweep.

Unfortunately there is no hard rule on which values to set. However a rule of thumb is to aim for 30% occupancy of the heap after a full GC. This requires running the application until a steady state has been reached.

### Are the GC generation sizes appropriate?

Going a step further, garbage collectors (GCs) divide the heap into generations: young, survivor, and old. The young generation holds short-lived data, while the old generation holds long-lived data. This separation allows GCs to process the young generation more quickly, reducing pause times. It is recommended to hand tune the generation sizes if you are an advanced java user. As an example use case, in a Java application where startup performance is critical, tuning the young generation size can help. By increasing the young generation size, you can reduce the frequency of minor GCs during startup, leading to faster application initialization.

Use the following command-line flag adjust the ratio of young to old generations from the default value of 2 for all GC algorithms:

```bash
-XX:NewRatio= <N>
```

Additionally, the initial size and maximum size of the young generation can be modified with `-XX:NewSize` and `-XX:MaxNewSize` respectively. For more information, you can refer to the [factors affecting garbage collection performance](https://docs.oracle.com/en/java/javase/11/gctuning/factors-affecting-garbage-collection-performance.html#GUID-4ADBEDE9-5D52-4FBF-ADB2-431C3EB089C5)

