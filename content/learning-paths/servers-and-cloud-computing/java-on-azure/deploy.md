---
title: Install Java
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---



## Java Installation on Azure Ubuntu Pro virtual machine
In this section, you will install Java on your Arm-based Ubuntu Pro virtual machine. The goal is to ensure you have both the Java Runtime Environment (JRE) for running Java applications and the Java Development Kit (JDK) for compiling code and running benchmarks.


### Install Java

You will install Java using the Ubuntu package manager. `default-jdk` installs both the default JRE and JDK provided by Azure Ubuntu Pro machine.
```console
sudo apt update
sudo apt install -y default-jdk
```
 
Verify your JRE installation: 

```console
java -version 
``` 

You should the JRE version printed: 

```output
openjdk version "21.0.8" 2025-07-15
OpenJDK Runtime Environment (build 21.0.8+9-Ubuntu-0ubuntu124.04.1)
OpenJDK 64-Bit Server VM (build 21.0.8+9-Ubuntu-0ubuntu124.04.1, mixed mode, sharing)
```

Check to ensure that the JDK is properly installed:

```console
javac -version 
```
The output should look similar to:

```output
javac 21.0.8
```

Set the Java Environment Variables to point to the root directory of your JDK installation: 

```console 
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-arm64
export PATH=$JAVA_HOME/bin:$PATH
source ~/.bashrc 
```
 
{{% notice Note %}}
Ubuntu Pro 24.04 LTS offers the default JDK version 21.0.8. It’s important to ensure that your version of OpenJDK for Arm is at least 11.0.9, or above. There is a large performance gap between OpenJDK-11.0.8 and OpenJDK 11.0.9. A patch added in 11.0.9 reduces false-sharing cache contention. 
For more information, you can view this [Arm community blog](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/java-performance-on-neoverse-n1). 

You can also refer to the [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) for software package version recommendations on Arm Neoverse Linux machines.
{{% /notice %}}

Your Java environment has been successfully configured. You may now proceed with baseline testing.
