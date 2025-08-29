---
title: Set up Tomcat
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Overview 

There are numerous client-server and network-based workloads, with Tomcat being a typical example of such applications. Tomcat provides services via HTTP/HTTPS network requests.

In this section, you will set up a benchmark environment using `Apache Tomcat` and `wrk2` to simulate an HTTP load and evaluate performance on an Arm-based bare metal instance. This Learning Path was tested on an AWS `c8g.metal-48xl` instance.

## Set up the Tomcat benchmark server
[Apache Tomcat](https://tomcat.apache.org/) is an open-source Java Servlet container that runs Java web applications, handles HTTP requests, and serves dynamic content. It supports technologies such as Servlet, JSP, and WebSocket.

## Install the Java Development Kit (JDK)

Install OpenJDK 21 on your Arm-based Ubuntu 24.04 bare-metal instance: 

```bash
sudo apt update
sudo apt install -y openjdk-21-jdk
```

## Install Tomcat 

Download and extract Tomcat:

```bash
wget -c https://dlcdn.apache.org/tomcat/tomcat-11/v11.0.10/bin/apache-tomcat-11.0.10.tar.gz
tar xzf apache-tomcat-11.0.10.tar.gz
```
Alternatively, you can build Tomcat [from source](https://github.com/apache/tomcat).

## Enable access to Tomcat examples

To access the built-in examples from your local network or external IP, use a text editor to modify the `context.xml` file by updating the `RemoteAddrValve` configuration to allow all IP addresses.

The file is at:
```bash
~/apache-tomcat-11.0.10/webapps/examples/META-INF/context.xml
```

Replace the existing allow value as shown:
```xml
<Valve className="org.apache.catalina.valves.RemoteAddrValve" allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1" />
```

With:
```xml
<Valve className="org.apache.catalina.valves.RemoteAddrValve" allow=".*" />
```
Save the changes to your file.

## Start the Tomcat server
{{% notice Note %}}
To achieve maximum performance of Tomcat, the maximum number of file descriptors that a single process can open simultaneously should be sufficiently large.
{{% /notice %}}

Start the server:

```bash
ulimit -n 65535 && ~/apache-tomcat-11.0.10/bin/startup.sh
```

You should see output like:

```output
Using CATALINA_BASE:   /home/ubuntu/apache-tomcat-11.0.10
Using CATALINA_HOME:   /home/ubuntu/apache-tomcat-11.0.10
Using CATALINA_TMPDIR: /home/ubuntu/apache-tomcat-11.0.10/temp
Using JRE_HOME:        /usr
Using CLASSPATH:       /home/ubuntu/apache-tomcat-11.0.10/bin/bootstrap.jar:/home/ubuntu/apache-tomcat-11.0.10/bin/tomcat-juli.jar
Using CATALINA_OPTS:
Tomcat started.
```

## Confirm server access

In your browser, open: `http://${tomcat_ip}:8080/examples`.

You should see the Tomcat welcome page and examples, as shown below:

![Screenshot of the Tomcat homepage showing version and welcome panel alt-text#center](./_images/lp-tomcat-homepage.png "Apache Tomcat homepage")

![Screenshot of the Tomcat examples page showing servlet and JSP demo links alt-text#center](./_images/lp-tomcat-examples.png "Apache Tomcat examples")

{{% notice Note %}}Make sure port 8080 is open in the security group of the IP address for your Arm-based Linux machine.{{% /notice%}}

## Set up the benchmarking client using wrk2
[Wrk2](https://github.com/giltene/wrk2) is a high-performance HTTP benchmarking tool specialized in generating constant throughput loads and measuring latency percentiles for web services. `wrk2` is an enhanced version of `wrk` that provides accurate latency statistics under controlled request rates, ideal for performance testing of HTTP servers.

{{% notice Note %}}
Currently `wrk2` is only supported on x86 machines. Run the benchmark client steps below on a bare metal `x86_64` server running Ubuntu 24.04
{{% /notice %}}

## Install dependencies 

Install the required packages:

```bash
sudo apt-get update
sudo apt-get install -y build-essential libssl-dev git zlib1g-dev
```

## Clone and build wrk2

Clone the repository and compile the tool:

```bash
sudo git clone https://github.com/giltene/wrk2.git
cd wrk2
sudo make
```

Move the binary to a directory in your system’s PATH:
 
```bash
sudo cp wrk /usr/local/bin
```

## Run the benchmark
{{% notice Note %}}
To achieve maximum performance of wrk2, the maximum number of file descriptors that a single process can open simultaneously should be sufficiently large.
{{% /notice %}}

Use the following command to benchmark the HelloWorld servlet running on Tomcat:

```bash
ulimit -n 65535 && wrk -c32 -t16 -R50000 -d60 http://${tomcat_ip}:8080/examples/servlets/servlet/HelloWorldExample
```
You should see output similar to:

```console
Running 1m test @ http://172.31.46.193:8080/examples/servlets/servlet/HelloWorldExample
  16 threads and 32 connections
  Thread calibration: mean lat.: 3.381ms, rate sampling interval: 10ms
  Thread calibration: mean lat.: 3.626ms, rate sampling interval: 10ms
  Thread calibration: mean lat.: 3.020ms, rate sampling interval: 10ms
  Thread calibration: mean lat.: 3.578ms, rate sampling interval: 10ms
  Thread calibration: mean lat.: 3.166ms, rate sampling interval: 10ms
  Thread calibration: mean lat.: 3.275ms, rate sampling interval: 10ms
  Thread calibration: mean lat.: 3.454ms, rate sampling interval: 10ms
  Thread calibration: mean lat.: 3.655ms, rate sampling interval: 10ms
  Thread calibration: mean lat.: 3.334ms, rate sampling interval: 10ms
  Thread calibration: mean lat.: 3.089ms, rate sampling interval: 10ms
  Thread calibration: mean lat.: 3.365ms, rate sampling interval: 10ms
  Thread calibration: mean lat.: 3.382ms, rate sampling interval: 10ms
  Thread calibration: mean lat.: 3.342ms, rate sampling interval: 10ms
  Thread calibration: mean lat.: 3.349ms, rate sampling interval: 10ms
  Thread calibration: mean lat.: 3.023ms, rate sampling interval: 10ms
  Thread calibration: mean lat.: 3.275ms, rate sampling interval: 10ms
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.02ms  398.88us   4.24ms   66.77%
    Req/Sec     3.30k   210.16     4.44k    70.04%
  2999776 requests in 1.00m, 1.56GB read
Requests/sec:  49996.87
Transfer/sec:     26.57MB
```
