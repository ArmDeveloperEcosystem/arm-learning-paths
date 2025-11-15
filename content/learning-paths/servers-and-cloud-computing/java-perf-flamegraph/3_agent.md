---
title: Generate Java flame graphs using a Java agent
weight: 4


### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

You can profile a Java application using `perf` by including a Java agent that enables symbol resolution. This allows `perf` to capture meaningful method names instead of raw memory addresses.

The required library is `libperf-jvmti.so`, a JVM Tool Interface (JVMTI) agent that bridges `perf` and the JVM. It ensures that stack traces collected during profiling can be accurately resolved to Java methods.

In this section, you'll configure Tomcat to use this Java agent and generate a flame graph using the FlameGraph toolkit.

## Locate the Java agent

Locate the `libperf-jvmti.so` library:

```bash
pushd /usr/lib
find . -name libperf-jvmti.so`
```
The output will show the path to the shared object file:

## Modify Tomcat configuration

Open the Tomcat launch script:

```bash
vi apache-tomcat-11.0.9/bin/catalina.sh
```
Add the following line (replace the path if different on your system):

```bash
JAVA_OPTS="$JAVA_OPTS -agentpath:/usr/lib/linux-tools-6.8.0-63/libperf-jvmti.so -XX:+PreserveFramePointer"
```
Now shutdown and restart Tomcat:

```bash
cd apache-tomcat-11.0.9/bin
./shutdown.sh
./startup.sh
```

## Run perf to record profiling data

Run the following command to record a 10-second profile of the Tomcat process:

```bash
sudo perf record -g -k1 -p $(jps | awk /Bootstrap/'{print $1}') -- sleep 10
```
This generates a file named `perf.data`.

If needed, restart `wrk` on your x86 client to generate load during profiling.

## Generate a flame graph

Clone the FlameGraph repository and add it to your PATH:

```bash
git clone https://github.com/brendangregg/FlameGraph.git
export PATH=$PATH:`pwd`/FlameGraph
sudo perf inject -j -i perf.data | perf script | stackcollapse-perf.pl | flamegraph.pl &> profile.svg
```
## View the result

You can now launch `profile.svg` in a browser to analyse the profiling result:

![Flame graph visualization of Java method calls collected using perf and a Java agent on a Tomcat server alt-text#center](_images/lp-flamegraph-agent.webp "Java flame graph built through Java agent and perf")
