---
# User change
title: "Setup and Config Nexmark"

weight: 3 # (intro is 1), 2 is first, 3 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Overview
Nexmark is a benchmark suite specifically designed for evaluating and comparing the performance of streaming data processing systems, particularly those used in the context of online auction scenarios. It provides a set of representative queries and data generators that simulate real-world auction events.  

## Requirements
- [Flink Standalone Cluster](https://nightlies.apache.org/flink/flink-docs-release-1.13/docs/deployment/resource-providers/standalone/overview/)
- JDK 1.8.x or higher (Nexmark scripts uses some tools of JDK)
- ssh (sshd must be running to use the Flink and Nexmark scripts that manage remote components)
- Install Maven:
  ```console
  sudo apt install maven
  ```
- Environment Variables:  
  (The following environment variable should be set on every node for the Flink and Nexmark scripts)
  ```console
  # JAVA_HOME: points to the directory of your JDK installation.
  export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64
  # FLINK_HOME: points to the directory of your Flink installation.
  export FLINK_HOME=~/flink-benchmark/flink-1.17.2
  ```
- Minimum requirements:
  - 3 worker nodes
  - 8 cores and 32 GB RAM on each machine
  - 800 GB SSD local disk

## Nexmark Install and Config

- Git clone the latest nexmark and build it on your ___master___ node:

  ```console
  cd ~/flink-benchmark
  git clone https://github.com/nexmark/nexmark.git
  mv nexmark nexmark-src
  cd nexmark-src/nexmark-flink
  ./build.sh
  mv nexmark-flink.tgz ~/flink-benchmark
  cd ~/flink-benchmark
  tar xzf nexmark-flink.tgz
  ```

- Copy the jars under nexmark/lib to flink/lib which contains the Nexmark source generator:
  
  ```console
  cp ~/flink-benchmark/nexmark-flink/lib/*.jar ~/flink-benchmark/flink-1.17.2/lib
  ```

- Nexmark and Flink Config:  

  - Edit and replace the file `nexmark-flink/conf/flink-conf.yaml`
    ```console
    #Set jobmanager.rpc.address: {JobManager_IP}
    #Set state.checkpoints.dir: file:///home/username/checkpoint (SSD Recommended)
    #Set state.backend.rocksdb.localdir: /home/username/rocksdb (SSD Recommended)
    #Set env.java.opts: [add -XX:+IgnoreUnrecognizedVMOptions]
    #Copy this file to [flink-1.17.2/conf/flink-conf.yaml]
    cp ~/flink-benchmark/nexmark-flink/conf/flink-conf.yaml ~/flink-benchmark/flink-1.17.2/conf
    ```

  - Replace `flink-1.17.2/conf/sql-client-defaults.yaml` with `nexmark-flink/conf/sql-client-defaults.yaml`
    ```console
    cp ~/flink-benchmark/nexmark-flink/conf/sql-client-defaults.yaml ~/flink-benchmark/flink-1.17.2/conf
    ```

  - Edit nexmark-flink/conf/nexmark.yaml and set `nexmark.metric.reporter.host`.
    ```console
    #set nexmark.metric.reporter.host: {JobManager_IP}
    ```

## Scp Flink and Nexmark to your worker nodes:
  ```console
  scp -r ~/flink-benchmark user@{TaskManager_IP}:~/
  ```
