---
title: Install the JDK and build an application
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---


### Platform Overview
Whether you're using an Azure Linux 3.0 Docker container or a VM created from a custom Azure Linux 3.0 image, the deployment and benchmarking steps remain the same.

### Working inside Azure Linux 3.0 Docker container
The Azure Linux Container Host is an operating system image that's optimized for running container workloads on Azure Kubernetes Service (AKS). Microsoft maintains the Azure Linux Container Host and based it on CBL-Mariner, an open-source Linux 
distribution created by Microsoft. 
To know more about Azure Linux 3.0, kindly refer [What is Azure Linux Container Host for AKS](https://learn.microsoft.com/en-us/azure/azure-linux/intro-azure-linux). Azure Linux 3.0 offers support for Aarch64. However, the standalone VM image for Azure Linux 3.0 or CBL Mariner 3.0 is not available for Arm.

Hence, to use the default software stack provided by the Microsoft team, this guide will focus on creating a docker container with Azure Linux 3.0 as a base image and will build 
and run the Java application inside the container, with the default JDK provided by the Microsoft team via Azure Linux 3.0 environment. 

### Create Azure Linux 3.0 Docker Container 
The [Microsoft Artifact Registry](https://mcr.microsoft.com/en-us/artifact/mar/azurelinux/base/core/about) offers updated docker image for the Azure Linux 3.0.  

To create a docker container, install docker, and then follow the below instructions: 

```console
$ sudo docker run -it --rm mcr.microsoft.com/azurelinux/base/core:3.0
``` 

The default container startup command is bash. tdnf and dnf are the default package managers.

### Install Java

This Azure Linux 3.0 image does not include Java, so you need to install it.  

First update tdnf:

```console
$ tdnf update -y 
``` 
Then install java-devel:

```console
$ tdnf install -y java-devel  
```
 
Java-devel installs both the default JRE and JDK provided by Azure Linux 3.0.

Check to ensure that the JRE is properly installed: 

```console
$ java -version 
``` 

**Your output will look like this:** 

```output
openjdk version "11.0.27" 2025-04-15 LTS 
OpenJDK Runtime Environment Microsoft-11371464 (build 11.0.27+6-LTS) 
OpenJDK 64-Bit Server VM Microsoft-11371464 (build 11.0.27+6-LTS, mixed mode, 
sharing) 
```

**Check to ensure that the JDK is properly installed:**

```console
$ javac -version 
```
Your output will look like this:

```output
javac 11.0.27 
```

Set Java Environment Variable for Arm: 

```console 
$ export JAVA_HOME=/usr/lib/jvm/msopenjdk-11 
$ export PATH=$JAVA_HOME/bin:$PATH 
```
 
{{% notice Note %}}
Azure Linux 3.0 offers the default JDK version 11.0.27. It’s important to ensure that your version of OpenJDK for Arm is at least 11.0.9, or above. There is a large performance gap between OpenJDK-11.0.8 and OpenJDK 11.0.9. A patch added in 11.0.9 reduces false-sharing cache contention. 
For more information, you can view this [Arm community blog](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/java-performance-on-neoverse-n1). 

The [Arm Ecosystem Dashboard](https://developer.arm.com/ecosystem-dashboard/) also recommends Java/OpenJDK version 11.0.9 as minimum recommended on the Arm platforms.
{{% /notice %}}

### Deploy a Java application with Tomcat-like operation 
Apache Tomcat is a Java-based web application server (technically, a Servlet container) that executes Java web applications. It's widely used to host Java servlets, JSP (JavaServer Pages), 
and RESTful APIs written in Java. 
The below Java class simulates the generation of a basic HTTP response and measures the time taken to construct it, mimicking a lightweight Tomcat-like operation. It measures how long it 
takes to build the response string, helping evaluate raw Java execution efficiency before deploying heavier frameworks like Tomcat.
Create a file named `HttpSingleRequestTest.java`, and add the below content to it:

```java
public class HttpSingleRequestTest {
    public static void main(String[] args) {
        long startTime = System.nanoTime();
        String response = generateHttpResponse("Tomcat baseline test on Arm64");
        long endTime = System.nanoTime();
        double durationInMicros = (endTime - startTime) / 1_000.0;
        System.out.println("Response Generated:\n" + response);
        System.out.printf("Response generation took %.2f microseconds.%n", durationInMicros);
    }
    private static String generateHttpResponse(String body) {
        return "HTTP/1.1 200 OK\r\n" +
               "Content-Type: text/plain\r\n" +
               "Content-Length: " + body.length() + "\r\n\r\n" +
               body;
    }
}
```
Compile and Run Java program :

```console
$ javac HttpSingleRequestTest.java
$ java -Xms128m -Xmx256m -XX:+UseG1GC HttpSingleRequestTest
```

- -Xms128m  sets the initial heap size for the Java Virtual Machine to 128 MB. 
- -Xmx256m sets the maximum heap size for the JVM to 256 MB. 
- -XX:+UseG1GC enables the G1 Garbage Collector (Garbage First GC), designed for low pause times and better performance in large heaps.

Output of java program on the Arm VM:
```output

$ javac HttpSingleRequestTest.java
$ java -Xms128m -Xmx256m -XX:+UseG1GC HttpSingleRequestTest
Response Generated:
HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 29

Tomcat baseline test on Arm64
Response generation took 22125.79 microseconds.
```
Output summary:

- The program generated a fake HTTP 200 OK response with a custom message.
- It then measured and printed the time taken to generate that response (22125.79 microseconds).
- This serves as a basic baseline performance test of string formatting and memory handling on the JVM running on an Azure Arm64 instance.
