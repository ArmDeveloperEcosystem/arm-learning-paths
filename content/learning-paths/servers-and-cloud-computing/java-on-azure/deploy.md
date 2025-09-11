---
title: Install Java
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---



## Java Installation on Azure Ubuntu Pro virtual machine
Install Java on Ubuntu Pro virtual machine by updating the system and installing `default-jdk`, which includes both JRE and JDK. Verify the installation using `java -version` and `javac -version`, then set the `JAVA_HOME` environment variable for Arm-based systems.


### Install Java

```console
sudo apt update
sudo apt install -y default-jdk
```
 
`default-jdk` installs both the default JRE and JDK provided by Azure Ubuntu Pro machine.

Check to ensure that the JRE is properly installed: 

```console
java -version 
``` 

You should see an output similar to: 

```output
openjdk version "21.0.8" 2025-07-15
OpenJDK Runtime Environment (build 21.0.8+9-Ubuntu-0ubuntu124.04.1)
OpenJDK 64-Bit Server VM (build 21.0.8+9-Ubuntu-0ubuntu124.04.1, mixed mode, sharing)
```

Check to ensure that the JDK is properly installed:

```console
javac -version 
```
You should see an output similar to:

```output
javac 21.0.8
```

Set Java Environment Variable for Arm: 

```console 
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-arm64
export PATH=$JAVA_HOME/bin:$PATH
source ~/.bashrc 
```
 
{{% notice Note %}}
Ubuntu Pro 24.04 LTS offers the default JDK version 21.0.8. It’s important to ensure that your version of OpenJDK for Arm is at least 11.0.9, or above. There is a large performance gap between OpenJDK-11.0.8 and OpenJDK 11.0.9. A patch added in 11.0.9 reduces false-sharing cache contention. 
For more information, you can view this [Arm community blog](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/java-performance-on-neoverse-n1). 

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) also recommends Java/OpenJDK version 11.0.9 as minimum recommended on the Arm platforms.
{{% /notice %}}

Java installation is complete. You can now proceed with the baseline testing.
