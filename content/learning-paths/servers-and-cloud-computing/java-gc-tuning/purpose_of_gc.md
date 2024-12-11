---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Automatic Memory Management

Garbage Collection (GC) is the term used in programming to describe the concept and process of automatic memory management, primarily deployed within managed languages such as Java. 

In a programming language such as C, developers need to explicitly free variables once they are no longer required. Automatic memory management removes the requirement for this procedure, meaning that there is less potential for human error.

The Garbage Collector must perform three main tasks:

* Find the objects to free.
* Free the memory.
* Compact the heap.

Java Virtual Machine distributions typically come with several Garbage Collectors, which can have the disadvantage that Java has less control of memory growth. This can subsequently cause knock-on effects such as page faults. In addition, the automatic process of finding variables with memory that can be freed creates CPU overhead, occurring during times such as the GC mark-swap algorithm. The execution of a Java application might pause during this process, and so being able to control the length and frequency of these pauses is key to optimizing performance.

### Garbage Collection Generations 

Most Garbage Collectors separate the heap of the memory into generations: 

* The young generation holds data that is used for a short period.
* The old generation holds longer-lived data. 

By doing this there are shorter pause times, as most data is short-lived and is faster to process.

A full Garbage Collections means going through the entire heap, leading to 'stop-the-world' pauses that impact the performance of an application. 


