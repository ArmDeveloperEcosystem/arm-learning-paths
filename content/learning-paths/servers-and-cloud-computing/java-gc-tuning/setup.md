---
title: Setup
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
### Check the JDK version 

Different versions of the Java Development Kit (JDK) ship with different Garbage Collectors. 

To check the version of Java installed on your system, run the following command: 

```bash
java --version
```

The output should look similar to:

```output
openjdk 21.0.4 2024-07-16 LTS
OpenJDK Runtime Environment Corretto-21.0.4.7.1 (build 21.0.4+7-LTS)
OpenJDK 64-Bit Server VM Corretto-21.0.4.7.1 (build 21.0.4+7-LTS, mixed mode, sharing)
```

If the `java` command is not recognized, you can follow the [Arm Java install guide](/install-guides/java/) to install Java on your system. 

### Identify available Garbage Collectors

To find out the range of standard Garbage Collectors that are available for you to use, run the following command which prints the information:

```bash
java -XX:+PrintFlagsFinal -version | egrep 'Use\w+GC'
```

The example output below shows that five GCs are available to use. The middle column shows the default value. Here you can see that the `G1GC` GC is enabled: 

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
