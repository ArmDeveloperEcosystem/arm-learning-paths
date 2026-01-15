---
title: "What You Will Build"

weight: 2

layout: "learningpathall"
---

## Overview

Building custom kernels lets you experiment with new features, patches, or flags without waiting for official Linux distro update availability.  Building is only half the battle,  You also need to deploy, run, and and compare results across kernels and benchmarks to understand how the code is impacting your workloads. 

This learning path shows you how to implement this end‑to‑end workflow for building, configuring, and running [*fastpath*](https://fastpath.docs.arm.com/en/latest/index.html) benchmarks on Arm-compatible Linux kernels.

[`Utility scripts`](https://github.com/geremyCohen/arm_kernel_install_guide) are provided which abstract low‑level setup work, allowing you to focus on how the systems work together, rather than how every dependency is installed.

## Sequence of Operations

This sequence diagram depicts the three main machines you'll create and setup in this LP working together:

  <p align="center">
    <img src="/learning-paths/servers-and-cloud-computing/fastpath/images/sequence_diagram_fastpath_dark.png" alt="EC2 setup" style="width:95%;">
  </p>

### Build Host

The kernel build host is responsible for producing kernel artifacts. Using kernel‑guide scripts, it installs the required development environment and calls into [Tuxmake](https://tuxmake.org/) to build kernels in a consistent and repeatable way.

### System Under Test (SUT)

The SUT host is a blank slate where benchmark workloads actually run -- its the system you are testing performance for.

The provided utility scripts make it easy to prepare the SUT by installing prerequisites such as Docker and the *fastpath* system account.

### Fastpath Host

The *fastpath* host brings it all together, acting as the control plane for benchmarking tasks. Provided utility scripts help you copy kernels from the build host to the *fastpath* host, enabling it to execute benchmarks on the SUT, and aggregate benchmark run results.


## Learning Path Structure

Each chapter in this learning path corresponds to a step in the flow above. For each chapter, the same high‑level pattern applies:

- Bring up the required cloud instance 
- Run utility-script setup for that machine
- Use the machine for its intended role

You do not need to understand every tool or dependency used in this LP. The goal is to understand how the pieces fit together and how each machine contributes to the overall benchmarking workflow.

With that background, you're ready to begin setting up the build machine!
