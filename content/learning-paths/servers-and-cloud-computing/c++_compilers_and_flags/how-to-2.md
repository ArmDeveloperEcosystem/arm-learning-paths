---
title: Setup Your Environment
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

If you are new to cloud computing, please refer to our learning path on [Getting started with Servers and Cloud Computing](https://learn.arm.com/learning-paths/servers-and-cloud-computing/intro/).

## Connect to an AWS Arm-based Instance

In this example we will be building and running our C++ application on an AWS Graviton 2 instance running Ubuntu 24.04 LTS. Once connected run the following commands to confirm the operating system and archiecture version. 

```bash
cat /etc/*lsb*
```

You will see an output such as the following:

```output
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=24.04
DISTRIB_CODENAME=noble
DISTRIB_DESCRIPTION="Ubuntu 24.04.1 LTS"
```

Next, we will confirm we are using a 64-bit Arm-based system using the following command

```bash
uname -m
```

You will see the following output.

```output
aarch64
```

## Enable Environment modules



## Understand the Neoverse version and supported CPU extensions

To understand which version of the Arm Neoverse architecture the instance of your choice uses you can use various resource, such as the [Arm partner webpage](https://www.arm.com/partners/aws).

To find this, when connected to a specific AWS instance, such as `t4g.2xlarge`, run the `lscpu command and we can observe the underlying Neoverse Architecture as per the information below. 

```output
lscpu | grep -i model
Model name:                           Neoverse-N1
Model:                                1
```