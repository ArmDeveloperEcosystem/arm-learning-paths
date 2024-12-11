---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Automatic Memory Management

Garbage Collection (GC) is the term used in programming to describe automatic memory management, primarily deployed within managed langauages such as Java. 

In a programming language such as C, developers need to explicitly free variables once they are no longer required. Automatic memory management means that this is not necessary which removes the potential for human error.

Generally, the Garbage Collector must perform three main tasks:

* Find the objects to free.
* Free the memory.
* Compact the heap.

Java Virtual Machine distributions typically come with several Garbage Collectors, which has the disadvantage that subsequently Java has less control of memory growth which can cause knock-on effects such as page faults. In addition, the automatic process of finding variables with memory can be freed creates CPU overhead, such as during the GC mark-swap algorithm. The execution of a Java application might pause during this process, and so being able to control the length and frequency of these pauses can greatly improve performance.

### Garbage Collection Generations 

Most GCs further separate the heap of the memory into generations: 

* The young generation holds data that is used for a short period.
* The old generation holds longer-lived data. 

This takes advantage of the fact that most data is short-lived so it is faster to process just the young generation during GC, resulting in shorted pause times. 

A full GC refers to going through the entire heap, leading to the so called 'stop-the-world pauses' that impact the performance of your application. 

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
