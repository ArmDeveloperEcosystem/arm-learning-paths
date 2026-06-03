---
title: Choose an AWS Graviton instance
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## What is Garbage Collection? (GC)
Memory management is a critical aspects of application performance, and Garbage Collection (GC) plays a central role in automating that process. GC continuously identifies and removes objects that are no longer needed, freeing memory for re-use for other purposes..

While this automation improves productivity and application safety, inefficient garbage collection can lead to increased CPU usage, longer response times, and unexpected application pauses. 

Tracking GC metrics provides a window into an application's memory health, helping engineers optimize performance, and ensuring the system can scale efficiently under load.

## Measuring default Go GC behavior on Arm servers

Go is one such language which implements GC.  As Go applications can spend meaningful time allocating memory and running garbage collection, it is important to understand how the Go runtime behaves under default settings. 

In this Learning Path, you'll run Go benchmarks on an AWS Graviton instance. The goal is to build a clean baseline, measuring operation time, allocation rate, GC frequency, and GC pause cost.

## Selecting an instance for Go GC measurements

An AWS Graviton `m8g.xlarge` instance has enough CPU and memory to make Go runtime behavior visible, while keeping costs minimal. It's a good starting point as it provides four vCPUs and 16 GiB of memory on AWS Graviton4. If you choose to run this Learning Path on a different instance, make sure it has at least 4 vCPUs and 16 GiB of memory to ensure the benchmark runs smoothly and provides meaningful GC metrics.

Avoid burstable `t4g` instances as CPU credits can affect benchmark repeatability and make GC measurements harder to explain.

{{% notice Note %}}
You can use larger instances, such as `m8g.2xlarge`, when you want more CPU width or more memory headroom. Start with `m8g.xlarge` so the first benchmark run is easy to reproduce and inexpensive.
{{% /notice %}}


## Checking instance availability

Use the AWS CLI to check whether `m8g.xlarge` is available in your selected Region.

Replace `us-east-1` with the Region you want to use.

```console
aws ec2 describe-instance-type-offerings \
    --region us-east-1 \
    --location-type availability-zone \
    --filters Name=instance-type,Values=m8g.xlarge \
    --query 'InstanceTypeOfferings[].Location' \
    --output table
```

If the command returns one or more Availability Zones, you can use `m8g.xlarge` in that Region.  If you are unable to find `m8g.xlarge` in your Region, you can try a different Region, or fallback to an 'm7g.xlarge' instance, which is based on the previous generation AWS Graviton3:

```console
aws ec2 describe-instance-type-offerings \
    --region us-east-1 \
    --location-type availability-zone \
    --filters Name=instance-type,Values=m7g.xlarge \
    --query 'InstanceTypeOfferings[].Location' \
    --output table
```

Once you have chosen an instance type, provision it to run Ubuntu 24.04 LTS Arm64.  Once the instance is running, and you are ssh'd into it, you can proceed to the next step.
