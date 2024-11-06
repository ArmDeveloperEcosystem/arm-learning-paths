---
title: Purpose of GC
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### The Purpose of GC

Garbage collection (GC) is the term used for automatic memory management primarily within managed langauages such as Java. This means developers do not need to explicitly free variables once they're no longer required, such as in the C programming language. Java Virtual Machine distributions typically come with several GCs. The disadvantage is that Java has less control of memory growth which can cause knock-on effects such as page faults. Further, the automatic process of finding variables whose memory can be freed occurs CPU overhead that may run intermittently such as in the GC mark-swap algorithm. The execution of your Java application may pause during this time, controlling the length and frequency of these pauses can greatly improve performance.

### Check Which JDK version you are running

Difference versions of the Java Development Kit (JDK) will ship with various GCs. First, check the version of Java installed on your system by running the following command. 

```bash
java --version
```

You should see an output like the following.

```output
openjdk 21.0.4 2024-07-16 LTS
OpenJDK Runtime Environment Corretto-21.0.4.7.1 (build 21.0.4+7-LTS)
OpenJDK 64-Bit Server VM Corretto-21.0.4.7.1 (build 21.0.4+7-LTS, mixed mode, sharing)
```

Since we are running this command on an AWS instance, we are using a managed version of OpenJDK 21 from AWS also called Corretto. 

### Checking which GCs are available

Next, we want to understand which standard GCs are available to us. The following command can be used to print the GCs. 

```bash
java -XX:+PrintFlagsFinal -version | egrep 'Use\w+GC'
```

The command looks to parse the full text for the specific GCs using a regular expression. The output below shows that 5 GCs are available to us. The middle column shows the default value. Here we can see that the `G1GC` GC is the default enabled GC. 

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

