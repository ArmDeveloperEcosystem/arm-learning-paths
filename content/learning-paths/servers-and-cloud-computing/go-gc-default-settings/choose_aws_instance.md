---
title: Choose an AWS Graviton-based instance to measure Go garbage collection metrics
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Measure default Go garbage collection behavior on Arm servers

Memory management is a critical aspect of application performance, and garbage collection (GC) plays a central role in automating that process. GC continuously identifies and removes objects that are no longer needed, freeing memory for reuse.

While this automation improves productivity and application safety, inefficient garbage collection can lead to increased CPU usage, longer response times, and unexpected application pauses. 

Tracking GC metrics provides a window into an application's memory health that you can use to optimize performance and ensure the system can scale efficiently under load.

As Go applications can spend meaningful time allocating memory and running garbage collection, it's important to understand how the Go runtime behaves under default settings. 

In this Learning Path, you'll run Go benchmarks on an Amazon EC2 instance powered by AWS Graviton. The goal is to build a clean baseline measuring operation time, allocation rate, GC frequency, and GC pause cost.

### Select an instance for Go garbage collection measurements

An `m8g.xlarge` instance powered by AWS Graviton has enough CPU and memory to make Go runtime behavior visible, while keeping costs minimal. It's a good starting point as it provides four vCPUs and 16 GiB of memory on AWS Graviton4. If you choose to run this Learning Path on a different instance, make sure it has at least 4 vCPUs and 16 GiB of memory to ensure the benchmark runs smoothly and provides meaningful GC metrics.

Avoid burstable `t4g` instances as CPU credits can affect benchmark repeatability and make GC measurements harder to explain.

{{% notice Note %}}
You can use larger instances, such as `m8g.2xlarge`, when you want more CPU width or more memory headroom. Start with `m8g.xlarge` so the first benchmark run is easy to reproduce and inexpensive.
{{% /notice %}}


#### Check instance availability

Use the AWS CLI to check whether `m8g.xlarge` is available in your selected AWS Region, replacing `us-east-1` with the Region you want to use:

```console
aws ec2 describe-instance-type-offerings \
    --region us-east-1 \
    --location-type availability-zone \
    --filters Name=instance-type,Values=m8g.xlarge \
    --query 'InstanceTypeOfferings[].Location' \
    --output table
```

If the command returns one or more Availability Zones, you can use `m8g.xlarge` in that Region. 

If `m8g.xlarge` is not available in your Region, try a different Region, or fall back to an `m7g.xlarge` instance, which is based on the previous generation AWS Graviton3:

```console
aws ec2 describe-instance-type-offerings \
    --region us-east-1 \
    --location-type availability-zone \
    --filters Name=instance-type,Values=m7g.xlarge \
    --query 'InstanceTypeOfferings[].Location' \
    --output table
```

#### Launch an instance

After selecting an instance type, launch it with the Ubuntu 24.04 LTS (arm64) AMI. You can do this using the [Amazon EC2 console](https://console.aws.amazon.com/ec2/) or the AWS CLI. When configuring the instance:

- Select your chosen instance type (`m8g.xlarge` or `m7g.xlarge`)
- Choose the Ubuntu 24.04 LTS arm64 AMI for your Region
- Configure a security group that allows inbound SSH (port 22) from your IP address
- Associate an existing key pair or create a new one for SSH access

After the instance reaches the running state, connect to it over SSH:

```bash
ssh -i /path/to/your-key.pem ubuntu@<instance-public-ip>
```
## What you've accomplished and what's next

You've now deployed an Arm-based Linux Amazon EC2 instance powered by AWS Graviton. 

In the next section, you'll install Go and Benchstat on the instance so that you can run garbage collection benchmarks.
