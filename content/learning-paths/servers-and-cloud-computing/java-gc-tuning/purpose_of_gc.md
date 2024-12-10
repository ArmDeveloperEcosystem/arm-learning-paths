---
title: The Purpose of Garbage Collector
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Purpose and Setup

Garbage Collection (GC) is the term for automatic memory management, primarily used within managed langauages such as Java. 

Automatic memory management means that developers do not need to explicitly free variables once they are no longer required, such as in the C programming language. 

Java Virtual Machine distributions typically come with several Garbage Collectors. The disadvantage is this is that Java has less control of memory growth which can cause knock-on effects such as page faults. In addition, the automatic process of finding variables whose memory can be freed occurs CPU overhead that may run intermittently such as in the GC mark-swap algorithm. The execution of your Java application might pause during this time, controlling the length and frequency of these pauses can greatly improve performance.

Broadly speaking, the Garbage Collector must perform three main tasks:

* Find the objects to free.
* Free the memory.
* Compact the heap. 

Most GCs further separate the heap into generations: 

* The young generation holds data that is used for a short period.
* The old generation holds longer-lived data. 

This takes advantage of the fact that most data is short-lived so it is faster to process just the young generation during GC, resulting in shorted pause times. A full GC refers to going through the entire heap, leading to the so called 'stop-the-world pauses' that impact the performance of your application. 

### Check the JDK version 

Different versions of the Java Development Kit (JDK) ship with different Garbage Collectors. 

First, check the version of Java installed on your system by running the following command: 

```bash
java --version
```

The output should look similar to:

```output
openjdk 21.0.4 2024-07-16 LTS
OpenJDK Runtime Environment Corretto-21.0.4.7.1 (build 21.0.4+7-LTS)
OpenJDK 64-Bit Server VM Corretto-21.0.4.7.1 (build 21.0.4+7-LTS, mixed mode, sharing)
```

If the `java` command is not recognised, please follow the [Arm Java install guide](/install-guides/java/) to install Java on your system. 

### Check which GCs are available

To find out the range of standard GCs that are available for you to use, run the following command which will print the information:

```bash
java -XX:+PrintFlagsFinal -version | egrep 'Use\w+GC'
```

The output below shows that five GCs are available to use. The middle column shows the default value. Here you can see that the `G1GC` GC is enabled. 

```output
     bool UseAdaptiveSizeDecayMajorGCCost          = true                                      {product} {default}
     bool UseAdaptiveSizePolicyWithSystemGC        = false                                     {product} {default}
     bool UseDynamicNumberOfGCThreads              = true                                      {product} {default}
     bool UseG1GC                                  = true                                      {product} {ergonomic}
     bool UseMaximumCompactionOnSystemGC           = true                                      {product} {default}
     bool UseParallelGC                            = false                                     {product} {default}
     bool UseSerialGC                              = false                                     {product} {default}
     bool UseShenandoahGC                          = false                                     {product} {default}
     bool UseZGC                                   = false                                     {product} {default}

```

In the next section, you will learn about the different types of GCs.
