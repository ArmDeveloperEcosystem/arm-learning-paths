---
title: Tuning the GC
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Use an alternative GC

In this section we will use the `HeapUsageExample.java` file we created earlier. 

The G1 GC (Garbage-First Garbage Collector) is designed to handle large heaps and aims to provide low pause times by dividing the heap into regions and performing incremental garbage collection. This makes it suitable for applications with high allocation rates and large memory footprints.

We can run the following command to generate the GC logs using a different GC and compare. We have simply changed the GC from `Serial` to `G1GC` using the `-XX:+UseG1GC` option. 

```bash
java -Xms512m -Xmx1024m -XX:+UseG1GC -Xlog:gc:file=gc.log:tags,uptime,time,level:filecount=10,filesize=16m HeapUsageExample.java
```
From the created log file `gc.log.*`, we can observe that at a very similar time after start up (~0.75s), the Pause Young time has reduced from ~3.6ms to ~1.9ms. Further, the time between GC pauses has imprved from ~46ms to every ~98ms.

```output
[2024-11-08T16:13:53.088+0000][0.790s][info][gc          ] GC(2) Pause Young (Normal) (G1 Evacuation Pause) 307M->3M(514M) 1.976ms
...
[2024-11-08T16:13:53.186+0000][0.888s][info][gc          ] GC(3) Pause Young (Normal) (G1 Evacuation Pause) 307M->3M(514M) 1.703ms
```
The output on your machine will vary. 

### Add GC Targets

You can manually provide targets for specific metrics and the GC will attempt to meet those requirements. For example, if you have a time-sensitive application such as a rest server, you may want to ensure that all customers receive a response within a specific time. You may find that if a client request is sent during GC you need to ensure that the GC pause time is minimised. 

Running the command with the `-XX:MaxGCPauseMillis=<N>` sets a target max GC pause time. 

```bash
java -Xms512m -Xmx1024m -XX:+UseG1GC -XX:MaxGCPauseMillis=1 -Xlog:gc:file=gc.log:tags,uptime,time,level:filecount=10,filesize=16m HeapUsageExample.java
```

Looking at the output below, we can see that at the same initial state after ~0.7s the pause time has been reduced. However, we can also see the initial size of the Young space has gone from 307MiB above to 124MiB. The GC decided to reduce the size of he Young space to reduce the pause time at the expense of more frequent pauses. 

```output
[2024-11-08T16:27:37.061+0000][0.765s][info][gc] GC(18) Pause Young (Normal) (G1 Evacuation Pause) 124M->3M(514M) 0.489ms
[2024-11-08T16:27:37.149+0000][0.853s][info][gc] GC(19) Pause Young (Normal) (G1 Evacuation Pause) 193M->3M(514M) 0.482ms
```

There are several other target options that you can try:
- `-XX:InitiatingHeapOccupancyPercent`: Sets the threshold for the old generation occupancy to start a concurrent GC cycle.
- `-XX:ParallelGCThreads`: Sets the number of threads used for parallel GC operations.
- `-XX:G1HeapRegionSize`: Sets the size of the G1 regions. The value must be a power of 2 between 1 MB and 32 MB.



#### Is your GC NUMA aware?

Non-uniform memory architecture occurs when the memory performance varies depending on which core the application is running on and where the data is in memory. This is a common occurence if you are using a system with multiple sockets. If your system has multiple sockets you need to ensure the GC is aware of this to optimise memory access patterns. The command line option below can be used to enable NUMA-aware GC.

```bash
+XX:+UseNUMA
```
#### Is the GC Heap Size Appropriate?

If the size of the heap is too small, excessive time will be spent in GC compared to the application logic. However disproportionately large heaps will result in longer GC pauses as there is more memory to parse. It is recommended the max heap size is not greater that the physical memory on your system, if multiple JVMs are running the sum of their heaps must not exceed the total physical memory (the `free -h` command can be used to find the phyisical memory). This is to avoid the high latency accesses to access memory on disk from swapping during a full GC sweep.

The `-Xmx <N>` and `-Xms <N>` options can be used to specify the maximum and minimum memory sizes respectively.

Unfortunately there is no hard rule on which values to set. However a rule of thumb is to aim for 30% occupation of the heap after a full GC. This requires running the application until a steady state has been reached.

The heap size is dynamically resized as the application runs. If you know exactly the heap size, setting the minimum and maximum values will slightly improve the performance since resizing will never take place.

#### Is the GC generation sizes appropriate?

Most GCs further separate the heap into generations. The young generation holds data that is used for a short period and the old generation for long-lived data. This takes advantage of the fact that most data is short lived so it's faster to process just the young generation during GC, resulting in shorted pause times. A full GC refers to going through the entire heap, leading to the so called 'stop-the-world pauses'. 

In most cases, we recommend only hand tuning the generation sizes if you are an advanced java user. 

The following command-line flag adjust the ratio of young to old generations from the default value of 2 for all GC algorithms:

```bash
-XX:NewRatio= <N>
```

Additionally, the initial size and maximum size of the young generation can be modified with the `-XX:NewSize` and `-XX:MaxNewSize` respectively. 

#### Which adaptive heap sizing strategy is being used?

The JVM attempts to find an optimal sizing solution within the bounds of the policies and parameters through adaptive sizing, varying the generation and heap sizes dynamically during execution. This is on the assumption that historic GC cycles will be similar to future GC cycles. This is generally true. 

To observe how the JVM is resizing an application, set the `-XX:+PrintAdaptiveSizePolicy` to print the information on generation resizing in the GC log. 

In the specific case where you have existing knowledge of the heap requirements, for example a small, short-lived java utility, disabling adaptive sizing using the `-XX:UseAdaptiveSizePolicy` flag can avoid the small overhead and time taken to resize. This can potentially improve the performance in specific cases. 