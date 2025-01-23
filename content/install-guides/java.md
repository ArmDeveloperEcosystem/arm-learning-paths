---
title: Java
author_primary: Jason Andrews
minutes_to_complete: 15
official_docs: https://docs.oracle.com/en/java/

additional_search_terms:
- linux
- cloud

multi_install: false
multitool_install_part: false

test_images:
- ubuntu:latest
test_maintenance: false

tool_install: true
weight: 1
layout: installtoolsall
---

Java is a high-level, object-oriented programming language first released by Sun Microsystems in 1995.

Its aim is to have as few implementation dependencies as possible, making it a versatile and widely-used language.

## Is Java available for Arm Linux?

Yes, there are numerous ways to install Java on Arm Linux distributions. 

Below are some of the common methods that you can use to install Java. This includes both the Java runtime environment (JRE), which is used to run Java applications, and the Java Development Kit (JDK), which is used to create Java applications.

Pick the one that works best for you.

{{% notice Note %}}
The Java Technology Compatibility Kit (TCK) is a test suite that you can use to verify whether a Java implementation conforms to the Java SE Platform Specification. It is a crucial tool for ensuring that Java applications can run consistently across different platforms and implementations.

Check the [OCTLA Signatories List](https://openjdk.org/groups/conformance/JckAccess/jck-access.html) to see who has been granted access to the TCK.
{{% /notice %}}

## Can I install Java using the Linux package manager?

For distributions using `apt`, including Debian and Ubuntu, you can install Java using this code:

```console
sudo apt update
sudo apt install default-jre -y
sudo apt install default-jdk -y
```

For distributions using `dnf`, including Fedora and Red Hat, you can install Java using this code:

```console
sudo dnf install java-latest-openjdk
```

For distributions using `pacman`, including Arch and Manjaro, you can install Java using this code:

```console
sudo pacman -S jdk-openjdk  
sudo pacman -S jre-openjdk  
```

## Can I install Java using Snap?

For Linux distributions using `snap`, you can install Java using this code:

```console
sudo snap install openjdk
```

## How do I install Amazon Corretto?

Amazon Corretto is a no-cost distribution of the Open Java Development Kit (OpenJDK). It is maintained and supported by Amazon Web Services (AWS).

You can install Corretto using `apt` with the commands:

```console
wget -O - https://apt.corretto.aws/corretto.key | sudo gpg --dearmor -o /usr/share/keyrings/corretto-keyring.gpg && \
echo "deb [signed-by=/usr/share/keyrings/corretto-keyring.gpg] https://apt.corretto.aws stable main" | sudo tee /etc/apt/sources.list.d/corretto.list
sudo apt-get update; sudo apt-get install -y java-21-amazon-corretto-jdk
```

You can find out more about the installation options for Corretto in the [Amazon Corretto 21 Guide for Linux](https://docs.aws.amazon.com/corretto/latest/corretto-21-ug/linux-info.html).

## How do I install the Microsoft Build of OpenJDK?

The Microsoft Build of OpenJDK is a no-cost, open source distribution of OpenJDK. It includes Long-Term Support (LTS) binaries for Java 11 and Java 17 and runs on Arm Linux.

{{% notice Note %}}
The Arm architecture is not available in the repositories for the `apt` package manager. 
{{% /notice %}}

You can download a tar.gz file from [Download the Microsoft Build of OpenJDK](https://learn.microsoft.com/en-gb/java/openjdk/download)

For example:

```console
wget https://aka.ms/download-jdk/microsoft-jdk-21.0.4-linux-aarch64.tar.gz
```

Extract the contents of the file:

```console
tar xvf microsoft-jdk-21.0.4-linux-aarch64.tar.gz
```

Move the contents to a directory of your choice: 

```console
sudo mv  jdk-21.0.4+7/ /usr/local
```

Set up environment variables to locate your installation:

```console
export JAVA_HOME=/usr/local/jdk-21.0.4+7
export PATH=$JAVA_HOME/bin:$PATH
```

Add the environment variables to your `~/.bashrc` file to set them permanently.

For more information about the available versions and supported platforms refer to [About the Microsoft Build of OpenJDK](https://learn.microsoft.com/en-gb/java/openjdk/overview).

## How do I install Eclipse Temurin from the Adoptium Working Group?

The Adoptium Working Group promotes and supports high-quality, TCK-certified runtimes and associated technology for use across the Java ecosystem. 

Eclipse Temurin is the name of the OpenJDK distribution from Adoptium.

To install Temurin on Ubuntu run:

```console
sudo apt install -y wget apt-transport-https gpg
wget -qO - https://packages.adoptium.net/artifactory/api/gpg/key/public | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/adoptium.gpg > /dev/null
echo "deb https://packages.adoptium.net/artifactory/deb $(awk -F= '/^VERSION_CODENAME/{print$2}' /etc/os-release) main" | sudo tee /etc/apt/sources.list.d/adoptium.list
sudo apt update 
sudo apt install temurin-17-jdk -y
```

For more information about the available versions and supported platforms refer to [Temurin documentation](https://adoptium.net/docs/).

## How do I install Java from Oracle?

You can download Java from the [Oracle website](https://www.oracle.com/java/technologies/javase-downloads.html) and install it manually. Look for the files with ARM64 in the description.

Download a [tar.gz](https://download.oracle.com/java/22/latest/jdk-22_linux-aarch64_bin.tar.gz) file from the website. 

Extract the contents of the file:

```console
tar xvf jdk-22_linux-aarch64_bin.tar.gz
```

Move the contents to a directory of your choice: 

```console
sudo mv jdk-22.0.2 /usr/local/
```

Set up environment variables to locate your installation:

```console
export JAVA_HOME=/usr/local/jdk-22.0.2
export PATH=$JAVA_HOME/bin:$PATH
```

Add the environment variables to your `~/.bashrc` file to set them permanently.

## Can I change the default Java version if multiple versions are installed?

Yes, you can change the default version. For systems with `apt` use:

```console
sudo update-alternatives --config java
```

You will be given the option to select a new version. The options are dependent on the software currently installed on your computer. 

```output
There are 3 choices for the alternative java (providing /usr/bin/java).

  Selection    Path                                           Priority   Status
------------------------------------------------------------
* 0            /usr/lib/jvm/java-21-amazon-corretto/bin/java   12100004  auto mode
  1            /usr/lib/jvm/java-17-openjdk-arm64/bin/java     1711      manual mode
  2            /usr/lib/jvm/java-21-amazon-corretto/bin/java   12100004  manual mode
  3            /usr/lib/jvm/java-21-openjdk-arm64/bin/java     2111      manual mode

Press <enter> to keep the current choice[*], or type selection number:
```

In this example, if you select option 1, Java 17 becomes the default. 

## How do I print the Java version?

Print the version of the Java runtime, by running:

```console
java -version
```

The output will be similar to:

```output
openjdk version "21.0.4" 2024-07-16
OpenJDK Runtime Environment (build 21.0.4+7-Ubuntu-1ubuntu224.04)
OpenJDK 64-Bit Server VM (build 21.0.4+7-Ubuntu-1ubuntu224.04, mixed mode, sharing)
```

Print the version of the Java compiler:

```console
javac -version
```

The output will be similar to:

```output
javac 21.0.4
```

## Which version of Java should I use for Arm Linux systems?

For performance and security, it’s important to ensure that your version of Java is at least 11.0.12. Earlier versions lack significant performance improvements. Java performance has steadily increased over time and newer versions provide improved performance.

## Which flags are available for tuning the JVM?

The Java Virtual Machine (JVM) includes a number of flags which are available to tune performance and aid in debugging. Some of the flags are general-purpose and some are Arm architecture-specific. 

To print the final values of the flags after the JVM has been initialized, run:

```console
java -XX:+PrintFlagsFinal -version
```

Generally the biggest performance improvements from JVM flags can be obtained from heap and garbage collection (GC) tuning, as long as you understand your workload well.

Default initial heap size is 1/64th of RAM and default maximum heap size is 1/4th of RAM. If you know your memory requirements, you should set both of these flags to the same value (e.g. `-Xms12g` and `-Xmx12g` for an application that uses at most 12 GB). Setting both flags to the same value will prevent the JVM from having to periodically allocate additional memory. Additionally, for cloud workloads max heap size is often set to 75%-85% of RAM, much higher than the default setting.

If you are deploying in a cloud scenario where you might be deploying the same stack to systems that have varying amounts of RAM, you might want to use `-XX:MaxRAMPercentage` instead of `-Xmx`, so you can specify a percentage of max RAM rather than a fixed max heap size. This setting can also be helpful in containerized workloads.

Garbage collector choice will depend on the workload pattern for which you're optimizing.

* If your workload is a straightforward serial single-core load with no multithreading, the `UseSerialGC` flag should be set to true.
* For multi-core small heap batch jobs (<4GB), the `UseParallelGC` flag should be set to true.
* The G1 garbage collector (`UseG1GC` flag) is better for medium to large heaps (>4GB). This is the most commonly used GC for large parallel workloads, and is the default for high-core environments. If you want to optimize throughput, use this one.
* The ZGC (`UseZGC` flag) has low pause times, which can drastically improve tail latencies. If you want to prioritize response time at a small cost to throughput, use ZGC.
* The Shenandoah GC (`UseShenandoahGC` flag) is still fairly niche. It has ultra low pause times and concurrent evacuation, making it ideal for low-latency applications, at the cost of increased CPU use.

## Are there other tools commonly used in Java projects?

There are a number of Java-related tools you might like to install.

### Apache Maven

Apache Maven is a powerful build automation tool primarily used for Java projects. 

It simplifies the build process by providing a uniform build system, with dependency and project management capabilities.

You can install it from the `apt` package manager:

```console
sudo apt-get install -y maven
```

Print the version:

```console
mvn -v
```

The output is similar to:

```output
Apache Maven 3.8.7
Maven home: /usr/share/maven
Java version: 22.0.2, vendor: Oracle Corporation, runtime: /usr/local/jdk-22.0.2
Default locale: en, platform encoding: UTF-8
OS name: "linux", version: "6.8.0-41-generic", arch: "aarch64", family: "unix"
```

### Gradle

Gradle is another build automation tool that is widely used for Java projects. 

It is designed to be highly customizable and flexible, making it suitable for a wide range of projects. 

You can install it from the `apt` package manager:

```console
sudo apt install gradle -y
```

You can also install specific versions by downloading and extracting a zip file:

```console
wget https://services.gradle.org/distributions/gradle-8.10-bin.zip -O gradle-8.10-bin.zip
unzip gradle-8.10-bin.zip
sudo mv gradle-8.10 /opt/gradle
sudo ln -s /opt/gradle/bin/gradle /usr/local/bin/gradle
```

Print the version:

```console
gradle -v
```

The output is similar to:

```output
Welcome to Gradle 8.10!

Here are the highlights of this release:
 - Support for Java 23.
 - Faster configuration cache.
 - Improved configuration cache reports.

For further information, see https://docs.gradle.org/8.10/release-notes.html.


------------------------------------------------------------
Gradle 8.10
------------------------------------------------------------

Build time:    2024-08-14 11:07:45 UTC
Revision:      fef2edbed8af1022cefaf44d4c0514c5f89d7b78

Kotlin:        1.9.24
Groovy:        3.0.22
Ant:           Apache Ant(TM) version 1.10.14 compiled on August 16 2023
Launcher JVM:  22.0.2 (Oracle Corporation 22.0.2+9-70)
Daemon JVM:    /usr/local/jdk-22.0.2 (no JDK specified, using current Java home)
OS:            Linux 6.8.0-41-generic aarch64
```

### Apache Ant

Apache Ant is a Java-based build tool used to automate the build process for Java projects. It is similar to Make but is designed specifically for Java projects. 

Ant uses XML to describe the build process and dependencies.

You can install it from the `apt` package manager:

```console
sudo apt install ant -y
```

You can also install specific versions by downloading and extracting a zip file:

```console
wget https://downloads.apache.org/ant/binaries/apache-ant-1.10.13-bin.zip -O apache-ant-1.10.13-bin.zip
unzip apache-ant-1.10.13-bin.zip
sudo mv apache-ant-1.10.13 /opt/ant
sudo ln -s /opt/ant/bin/ant /usr/local/bin/ant
```

Print the version:

```console
ant -version
```

The output is similar to:

```output
Apache Ant(TM) version 1.10.13 compiled on January 4 2023
```

### Apache JMeter

JMeter is an open-source tool designed for performance and load testing Java applications. 

You can install it using:

```console
wget https://downloads.apache.org/jmeter/binaries/apache-jmeter-5.6.3.tgz
tar xzf apache-jmeter-5.6.3.tgz
sudo mv apache-jmeter-5.6.3 /opt/jmeter
sudo ln -s /opt/jmeter/bin/jmeter /usr/local/bin/jmeter
```

Print the version:

```console
jmeter --version
```

The output is similar to:

```output
Aug 27, 2024 9:01:58 PM java.util.prefs.FileSystemPreferences$1 run
INFO: Created user preferences directory.
    _    ____   _    ____ _   _ _____       _ __  __ _____ _____ _____ ____
   / \  |  _ \ / \  / ___| | | | ____|     | |  \/  | ____|_   _| ____|  _ \
  / _ \ | |_) / _ \| |   | |_| |  _|    _  | | |\/| |  _|   | | |  _| | |_) |
 / ___ \|  __/ ___ \ |___|  _  | |___  | |_| | |  | | |___  | | | |___|  _ <
/_/   \_\_| /_/   \_\____|_| |_|_____|  \___/|_|  |_|_____| |_| |_____|_| \_\ 5.6.3

Copyright (c) 1999-2024 The Apache Software Foundation
```

You are ready to use Java on your Arm Linux system. 
