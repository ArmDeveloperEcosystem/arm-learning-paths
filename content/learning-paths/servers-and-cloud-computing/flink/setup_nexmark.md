---
# User change
title: "Setup and Config Nexmark"

weight: 3 # (intro is 1), 2 is first, 3 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Overview
[Nexmark](https://github.com/nexmark/nexmark) is a benchmark suite for queries over continuous data streams. This project is inspired by the [NEXMark research paper](https://web.archive.org/web/20100620010601/http://datalab.cs.pdx.edu/niagaraST/NEXMark/) and [Apache Beam Nexmark](https://beam.apache.org/documentation/sdks/java/testing/nexmark/).

## Requirements
The Nexmark benchmark framework runs Flink queries on [standalone cluster](https://nightlies.apache.org/flink/flink-docs-release-1.13/docs/deployment/resource-providers/standalone/overview/), see the Flink documentation for more detailed requirements and how to setup it.


### Software Requirements:
- JDK 1.8.x or higher (Nexmark scripts uses some tools of JDK)
- ssh (sshd must be running to use the Flink and Nexmark scripts that manage remote components)
- Install Maven:
  ```console
  sudo apt install maven
  ```

### Environment Variables:
The following environment variable should be set on every node for the Flink and Nexmark scripts.
- JAVA_HOME: point to the directory of your JDK installation.
- FLINK_HOME: point to the directory of your Flink installation.
  
```console
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64
export FLINK_HOME=~/flink-benchmark/flink-1.17.2
```
### Minimum requirements:
- 3 worker node
- Each machine has 8 cores and 32 GB RAM
- 800 GB SSD local disk

## Nexmark Install and Config

- Step-1: Git clone the latest nexmark and build it on your master node.

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

- Step-2: Copy the jars under nexmark/lib to flink/lib which contains the Nexmark source generator.
  
```console
cp ~/flink-benchmark/nexmark-flink/lib/*.jar ~/flink-benchmark/flink-1.17.2/lib
```

- Step-3: Configure Flink:
    - Edit flink-1.17.2/conf/workers of the master node and enter the IP address of each worker node. It is recommend to set 8 entries. Follow the example shown below to set the entries.
 
  ```console
  sudo echo {JobManager_IP}:8081 > ~/flink-benchmark/flink-1.17.2/conf/masters    
  sudo echo {TaskManager_1_IP} >> ~/flink-benchmark/flink-1.17.2/conf/workers   
  sudo echo {TaskManager_2_IP} >> ~/flink-benchmark/flink-1.17.2/conf/workers    
  sudo echo {TaskManager_3_IP} >> ~/flink-benchmark/flink-1.17.2/conf/workers   
  ```
    - Replace flink-1.17.2/conf/sql-client-defaults.yaml with nexmark-flink/conf/sql-client-defaults.yaml
    ```console
    cp ~/flink-benchmark/nexmark-flink/conf/sql-client-defaults.yaml ~/flink-benchmark/flink-1.17.2/conf
    ```
    - Open the file `nexmark-flink/conf/flink-conf.yaml` in an editor of your choice and update the following configurations:
        - Set jobmanager.rpc.address to you master IP address
        - Set state.checkpoints.dir to your local file path (recommend to use SSD), e.g. file:///home/username/checkpoint.
        - Set state.backend.rocksdb.localdir to your local file path (recommend to use SSD), e.g. /home/username/rocksdb.
    
      ```console
      #Set jobmanager.rpc.address: {JobManager_IP}
      #Set state.checkpoints.dir: file:///home/username/checkpoint
      #Set state.backend.rocksdb.localdir: /home/username/rocksdb
      #Set env.java.opts: [add -XX:+IgnoreUnrecognizedVMOptions]
      ```
      - Copy this file to flink-1.17.2/conf/flink-conf.yaml
      ```console
      cp ~/flink-benchmark/nexmark-flink/conf/flink-conf.yaml ~/flink-benchmark/flink-1.17.2/conf
      ```

- Step-4: Configure Nexmark benchmark.  
  - Edit nexmark-flink/conf/nexmark.yaml and set nexmark.metric.reporter.host to your master IP address.
```console
#set nexmark.metric.reporter.host: {JobManager_IP}
```

- Step-5: Copy flink and nexmark to your worker nodes using scp.
```console
scp -r ~/flink-benchmark root@{TaskManager_IP}:~/
```

- Step-6: Start Flink Cluster by running flink/bin/start-cluster.sh on the master node.
```console
bash ~/flink-benchmark/flink-1.17.2/bin/start-cluster.sh
```

- Step-7: Setup the benchmark cluster by running nexmark/bin/setup_cluster.sh on the master node.
```console
bash ~/flink-benchmark/nexmark-flink/bin/setup_cluster.sh
```

