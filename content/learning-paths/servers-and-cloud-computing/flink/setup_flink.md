---
# User change
title: "Setup and Configure Flink"

weight: 2 # (intro is 1), 2 is first, 3 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---


## Before you begin
Apache Flink requires Java to run. Flink is implemented in Java and runs on the Java Virtual Machine (JVM). It leverages the Java programming language and its runtime environment to execute data processing tasks and manage distributed computations:

### Install a Java Development Kit (JDK) 11 on your system.  
You can download the JDK from the [official Oracle website](https://www.oracle.com/java/technologies/downloads/archive/).  
Or use an open-source distribution like [OpenJDK](https://openjdk.org/install/).
```bash
sudo apt update
sudo apt install -y openjdk-11-jdk
```

Set Java Environment Variable
```bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64
export PATH=$JAVA_HOME/bin:$PATH
```

## Flink Install

You can find all the versions and components on the [official Flink website](https://flink.apache.org/downloads/)

```bash
mkdir ~/flink-benchmark
cd ~/flink-benchmark
sudo wget https://dlcdn.apache.org/flink/flink-1.17.2/flink-1.17.2-bin-scala_2.12.tgz
tar xzvf flink-1.17.2-bin-scala_2.12.tgz
```

### Flink Configuration
Before you configure Flink, you should learn about two important words: JobManager and TaskManager  
1. JobManager: The JobManager is responsible for coordinating and managing the execution of Flink jobs. It receives job submissions, schedules and assigns tasks to TaskManagers, coordinates checkpoints, and monitors job execution. There is typically one active JobManager in a Flink cluster, although there can be multiple standby JobManagers for high availability setups.  
2. TaskManager: The TaskManager is responsible for executing the tasks assigned by the JobManager. Each TaskManager runs one or more task slots, which are units of resource allocation for executing individual tasks. The TaskManager manages the execution of tasks, including data ingestion, transformation, and output. Multiple TaskManagers work together to form the Flink cluster, with each TaskManager capable of running multiple tasks concurrently.
<br>
<br>
###
```bash
sudo echo {JobManager_IP}:8081 > flink-1.17.2/conf/masters   
sudo echo {TaskManager_1_IP} >> flink-1.17.2/conf/workers   
sudo echo {TaskManager_2_IP} >> flink-1.17.2/conf/workers   
sudo echo {TaskManager_3_IP} >> flink-1.17.2/conf/workers   
...
```
Replace `JobManager_IP` in the command above with the IP address of the JobManager in your setup. You can also use the default setting of "localhost:8081".  
Replace `TaskManager_1_IP`, `TaskManager_2_IP` and `TaskManager_3_IP` in the command above with the IP addresses of the TaskManagers in your setup. You can also use localhost in place of the IP addresses.
