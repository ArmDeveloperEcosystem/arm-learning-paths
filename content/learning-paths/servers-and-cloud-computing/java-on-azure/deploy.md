---
title: Install Java
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Java on Azure Ubuntu Pro 24.04 LTS (Arm64)

In this section, you will install Java on your Arm-based Ubuntu Pro virtual machine. The goal is to ensure you have both the Java Runtime Environment (JRE) for running Java applications and the Java Development Kit (JDK) for compiling code and running benchmarks.


## Install OpenJDK (JRE + JDK)

Use the Ubuntu package manager. The `default-jdk` package installs both the runtime and the compiler.

```console
sudo apt update
sudo apt install -y default-jdk
```

## Verify your installation

Confirm the architecture and the installed Java versions:

```console
uname -m
java -version
javac -version
```

You see the version information printed: 

```output
aarch64
openjdk version "21.0.8" 2025-07-15
OpenJDK Runtime Environment (build 21.0.8+9-Ubuntu-0ubuntu124.04.1)
OpenJDK 64-Bit Server VM (build 21.0.8+9-Ubuntu-0ubuntu124.04.1, mixed mode, sharing)
```

Check to ensure that the JDK is properly installed:

```console
which java
which javac
```
The output should look similar to:

```output
/usr/bin/java
/usr/bin/javac
```

Set the Java Environment Variables to point to the root directory of your JDK installation.

Use a text editor to edit the file `$HOME/.bashrc` and add the 2 environment variables.

```console 
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-arm64
export PATH=$JAVA_HOME/bin:$PATH
```
Source the updated `$HOME/.bashrc` file.

```console
source ~/.bashrc 
```

Confirm the new settings.

```console
echo $JAVA_HOME
which java
which javac
```

The output is:

```output
/usr/lib/jvm/java-21-openjdk-arm64
/usr/lib/jvm/java-21-openjdk-arm64/bin/java
/usr/lib/jvm/java-21-openjdk-arm64/bin/javac
```

{{% notice Note %}}
Ubuntu Pro 24.04 LTS provides OpenJDK 21 by default. Ensure your OpenJDK for Arm64 is **11.0.9 or newer** if you must run Java 11; releases before 11.0.9 can suffer performance issues due to false‑sharing cache contention. See the Arm community blog: [Java performance on Neoverse N1](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/java-performance-on-neoverse-n1). You can also consult the [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) for package guidance on Arm Neoverse Linux systems.
{{% /notice %}}

