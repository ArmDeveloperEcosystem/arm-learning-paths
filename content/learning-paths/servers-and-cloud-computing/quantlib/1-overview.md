---
title: Understand the QuantLib benchmark workflow on Azure Cobalt
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is QuantLib?

QuantLib is an open-source C++ library for quantitative finance. It provides tools for pricing, modeling, trading, and risk management, and is widely used as both a development library and a representative financial computing workload.

Because QuantLib is a substantial C++ codebase with realistic compute behavior, it is also useful as a benchmark when evaluating cloud systems and processor architectures.

In this Learning Path, you will build QuantLib from source and run its benchmark executable on an Arm-based Azure Cobalt virtual machine.

## Why use Azure Cobalt?

Azure Cobalt provides Arm64 virtual machines for cloud-native development and performance evaluation. Running QuantLib on Azure Cobalt gives you a practical way to measure how a real C++ finance workload behaves on Arm-based cloud infrastructure.

The workflow in this Learning Path uses:

- Ubuntu Server 22.04 LTS
- an Arm64 Azure Cobalt virtual machine
- a source build of QuantLib
- QuantLib's benchmark executable for repeatable performance testing

## What you'll do

This Learning Path follows a simple workflow:

1. Create and connect to an Arm64 Azure Cobalt virtual machine
2. Install the tools needed to build QuantLib
3. Download and compile QuantLib from source
4. Run benchmark workloads with different problem sizes and thread counts
5. Compare and record results

{{% notice Note %}}
This Learning Path focuses on building and benchmarking QuantLib on Azure Cobalt. It is not a general introduction to quantitative finance or QuantLib development.
{{% /notice %}}

## Benchmarking goals

When benchmarking a workload such as QuantLib, the goal is not just to obtain one runtime number. You want a repeatable process that lets you compare runs across system sizes, thread counts, software versions, and compiler settings.

For that reason, this Learning Path emphasizes:

- using a known VM configuration
- keeping the software environment consistent
- changing one benchmark variable at a time
- recording commands and results so runs can be reproduced later

## What you've learned and what's next

In this section, you've seen why QuantLib is a useful benchmark workload and how Azure Cobalt provides an Arm64 environment for evaluating it.

In the next section, you'll create an Azure Cobalt virtual machine, connect to it over SSH, and build QuantLib from source.