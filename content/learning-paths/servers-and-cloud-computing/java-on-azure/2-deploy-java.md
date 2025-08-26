---
title: Install Java on Microsoft Azure Virtual Machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---



## Java Installation on Azure Linux 3.0
Install Java on Azure Linux 3.0 by updating the system and installing `java-devel`, which includes both JRE and JDK. Verify the installation using `java -version` and `javac -version`, then set the `JAVA_HOME` environment variable for Arm-based systems.


### Install Java

This Azure Linux 3.0 image does not include Java, so you need to install it.  

First update tdnf:

```console
tdnf update -y 
``` 
Then install java-devel:

```console
tdnf install -y java-devel  
```
 
Java-devel installs both the default JRE and JDK provided by Azure Linux 3.0.

Check to ensure that the JRE is properly installed: 

```console
java -version 
``` 

You should see an output similar to: 

```output
openjdk version "11.0.27" 2025-04-15 LTS 
OpenJDK Runtime Environment Microsoft-11371464 (build 11.0.27+6-LTS) 
OpenJDK 64-Bit Server VM Microsoft-11371464 (build 11.0.27+6-LTS, mixed mode, 
sharing) 
```

Check to ensure that the JDK is properly installed:

```console
javac -version 
```
You should see an output similar to:

```output
javac 11.0.27 
```

Set Java Environment Variable for Arm: 

```console 
export JAVA_HOME=/usr/lib/jvm/msopenjdk-11 
export PATH=$JAVA_HOME/bin:$PATH 
```
 
{{% notice Note %}}
Azure Linux 3.0 offers the default JDK version 11.0.27. It’s important to ensure that your version of OpenJDK for Arm is at least 11.0.9, or above. There is a large performance gap between OpenJDK-11.0.8 and OpenJDK 11.0.9. A patch added in 11.0.9 reduces false-sharing cache contention. 
For more information, you can view this [Arm community blog](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/java-performance-on-neoverse-n1). 

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) also recommends Java/OpenJDK version 11.0.9 as minimum recommended on the Arm platforms.
{{% /notice %}}

Java installation is complete. You can now proceed with the baseline testing.
