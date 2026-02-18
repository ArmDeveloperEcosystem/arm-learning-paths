---
title: "Overview of the Fastpath benchmarking workflow"

weight: 2

layout: "learningpathall"
---

## Overview

Building custom Linux kernels lets you experiment with new features, patches, or flags without waiting for official Linux distro update availability. Building the kernel is only half the battle. You also need to deploy, run, and compare results across kernels and benchmarks to understand how the code impacts your workloads.

This Learning Path shows you how to implement this end-to-end workflow for building, configuring, and running benchmarks using [Fastpath](https://fastpath.docs.arm.com/en/latest/index.html) on Arm Linux systems.

[Utility scripts](https://github.com/geremyCohen/arm_kernel_install_guide) are provided which abstract low‑level setup work, allowing you to focus on how the systems work together, rather than how every dependency is installed.

If you want to learn more about building Linux kernels for Arm systems, see the [Build the Linux kernel](/learning-paths/servers-and-cloud-computing/kernel-build/) Learning Path.

## Sequence of operations

The following diagram shows how the three machines you'll create work together:

![Sequence diagram showing the interaction between the Build Host, Fastpath Host, and System Under Test (SUT) during the kernel benchmarking workflow. The Build Host compiles kernels using tuxmake, the Fastpath Host orchestrates benchmarking tasks and aggregates results, and the SUT runs benchmark workloads. Arrows indicate kernel artifacts flowing from Build Host to Fastpath Host, and benchmark commands flowing from Fastpath Host to SUT, with results returning to Fastpath Host.alt-txt#center](images/sequence_diagram_fastpath_dark.png "Fastpath benchmarking workflow: three-machine architecture diagram")

### Kernel build host

The kernel build host is responsible for producing kernel artifacts. Using build scripts, it installs the required development environment and calls [tuxmake](https://tuxmake.org/) to build kernels in a consistent and repeatable way.

### System Under Test (SUT)

The SUT host is a clean system where benchmark workloads run. It's the system you're doing performance testing on. 

The provided utility scripts make it easy to prepare the SUT by installing prerequisites such as Docker and the Fastpath system account.

### Fastpath host

The Fastpath host acts as the control plane for benchmarking tasks. Provided utility scripts help you copy kernels from the build host to the Fastpath host, enabling it to execute benchmarks on the SUT and aggregate benchmark run results.

## Workflow steps

Each section in this Learning Path corresponds to a step in the flow above. For each section, the same high-level pattern applies:

- Create the required cloud instance
- Run utility script setup for that machine
- Use the machine for its intended purpose

The goal is to understand how the pieces fit together and how each machine contributes to the overall benchmarking workflow. You'll work through the setup systematically, with each step building on the previous one.

You're ready to begin setting up the build machine.
