---
title: Basic GC Tuning Options
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Update the JDK version 

If you are on an older version of JDK, a sensible first step is to use one of the latest long-term-support (LTS) releases of JDK. This is because the GC versions included with recent JDKs offer improvements on previous releases. For example, the G1GC included with JDK 11 offers improvements in the pause time compared to JDK 8. 

As shown earlier, you can use the `java --version` command to check the version currently in use:

```output
$ java --version
openjdk 21.0.4 2024-07-16 LTS
OpenJDK Runtime Environment Corretto-21.0.4.7.1 (build 21.0.4+7-LTS)
OpenJDK 64-Bit Server VM Corretto-21.0.4.7.1 (build 21.0.4+7-LTS, mixed mode, sharing)
```


### Use an alternative GC

In this section, you will use the `HeapUsageExample.java` file you created earlier. 

The Garbage-First Garbage Collector (G1GC) is designed to handle large heaps and aims to provide low pause times by dividing the heap into regions and performing incremental garbage collection. This makes it suitable for applications with high allocation rates and large memory footprints.

You can run the following command to generate the GC logs using a different GC and compare the two. 

To make this comparison, change the Garbage Collector from `Serial` to `G1GC` using the `-XX:+UseG1GC` option:

```bash
java -Xms512m -Xmx1024m -XX:+UseG1GC -Xlog:gc:file=gc.log:tags,uptime,time,level:filecount=10,filesize=16m HeapUsageExample.java
```
From the created log file `gc.log`, you can see that at a similar time after startup (~0.75s), the Pause Young time reduced from ~3.6ms to ~1.9ms. Further, the time between GC pauses has improved from ~46ms to every ~98ms.

```output
[2024-11-08T16:13:53.088+0000][0.790s][info][gc          ] GC(2) Pause Young (Normal) (G1 Evacuation Pause) 307M->3M(514M) 1.976ms
...
[2024-11-08T16:13:53.186+0000][0.888s][info][gc          ] GC(3) Pause Young (Normal) (G1 Evacuation Pause) 307M->3M(514M) 1.703ms
```
As described in the previous section, the performance improvement from moving to a G1GC depends on the CPU overhead of your system. The performance can vary depending on the cloud instance size and available CPU resources. 

### Add Garbage Collector Targets

You can manually provide targets for specific metrics and the GC will attempt to meet those requirements. For example, if you have a time-sensitive application such as a REST server, you might want to ensure that all customers receive a response within a specific time. You might find that if a client request is sent during Garbage Collection that you need to ensure that the GC pause time is minimized. 

Running the command with the `-XX:MaxGCPauseMillis=<N>` sets a target max GC pause time:

```bash
java -Xms512m -Xmx1024m -XX:+UseG1GC -XX:MaxGCPauseMillis=1 -Xlog:gc:file=gc.log:tags,uptime,time,level:filecount=10,filesize=16m HeapUsageExample.java
```

Looking at the output below, you can see that at the same initial state after ~0.7s the pause time has reduced. However, you can also see the initial size of the Young space has gone from 307MiB above to 124MiB. The GC decided to reduce the size of the Young space to reduce the pause time at the expense of more frequent pauses. 

```output
[2024-11-08T16:27:37.061+0000][0.765s][info][gc] GC(18) Pause Young (Normal) (G1 Evacuation Pause) 124M->3M(514M) 0.489ms
[2024-11-08T16:27:37.149+0000][0.853s][info][gc] GC(19) Pause Young (Normal) (G1 Evacuation Pause) 193M->3M(514M) 0.482ms
```

Here are some additional target options that you can consider to tune performance:

-   -XX:InitiatingHeapOccupancyPercent: 

This defines the old generation occupancy threshold to trigger a concurrent GC cycle. Adjusting this is beneficial if your application experiences long GC pauses due to high old generation occupancy. For example, lowering this threshold can help start GC cycles earlier, reducing the likelihood of long pauses during peak memory usage.

-   -XX:ParallelGCThreads

This specifies the number of threads for parallel GC operations. Increasing this value is beneficial for applications running on multi-core processors, as it allows GC tasks to be processed faster. For instance, a high-throughput server application might benefit from more parallel GC threads to minimize pause times and improve overall performance.

-   -XX:G1HeapRegionSize

This determines the size of G1 regions, which must be a power of 2 between 1 MB and 32 MB. Adjusting this can be useful for applications with specific memory usage patterns. For example, setting a larger region size can reduce the number of regions and associated overhead for applications with large heaps, while smaller regions might be better for applications with more granular memory allocation patterns.

See [Garbage First Garbage Collector Tuning](https://www.oracle.com/technical-resources/articles/java/g1gc.html) for more information of G1GC tuning. 

