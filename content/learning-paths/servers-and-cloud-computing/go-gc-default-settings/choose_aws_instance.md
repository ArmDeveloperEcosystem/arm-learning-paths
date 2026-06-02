---
title: Choose an AWS Graviton instance
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Select an instance for Go GC measurements

Use an AWS Graviton instance that has enough CPU and memory to make Go runtime behavior visible, while keeping the Learning Path inexpensive to run.

For the first prototype, use `m8g.xlarge`.

`m8g.xlarge` is a good starting point because it provides four vCPUs and 16 GiB of memory on AWS Graviton4. Four vCPUs are enough to observe default Go CPU parallelism and GC worker behavior without requiring a large benchmark host. The 16 GiB memory size is enough for allocation-heavy benchmarks without immediately making the lab memory-bound.

Avoid burstable `t4g` instances for this Learning Path. CPU credits can affect benchmark repeatability and make GC measurements harder to explain.

If `m8g.xlarge` is not available in your AWS Region or Availability Zone, use `m7g.xlarge` as the fallback. It has the same vCPU and memory shape on an earlier Graviton generation, so the commands and benchmark workflow remain the same.

## Recommended prototype machine

Use this instance shape for the first version of the Learning Path:

| Purpose | Instance type | Processor | vCPUs | Memory |
| --- | --- | --- | ---: | ---: |
| Default prototype | `m8g.xlarge` | AWS Graviton4 | 4 | 16 GiB |
| Fallback | `m7g.xlarge` | AWS Graviton3 | 4 | 16 GiB |

{{% notice Note %}}
You can use larger instances, such as `m8g.2xlarge`, when you want more CPU width or more memory headroom. Start with `m8g.xlarge` so the first benchmark run is easy to reproduce and inexpensive.
{{% /notice %}}

The commands in this Learning Path were validated on an `m8g.xlarge` instance running Ubuntu 24.04 LTS Arm64 and Go 1.26.3.

## Check instance availability

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

If the command returns one or more Availability Zones, you can use `m8g.xlarge` in that Region.

Run the same command for `m7g.xlarge` if `m8g.xlarge` is not available:

```console
aws ec2 describe-instance-type-offerings \
    --region us-east-1 \
    --location-type availability-zone \
    --filters Name=instance-type,Values=m7g.xlarge \
    --query 'InstanceTypeOfferings[].Location' \
    --output table
```

You have now selected a repeatable AWS Graviton test machine. You will confirm the default Go runtime environment before running the benchmark.
