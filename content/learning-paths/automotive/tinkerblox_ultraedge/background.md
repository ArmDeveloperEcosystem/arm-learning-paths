---
title: Understand UltraEdge HPC-I architecture for edge AI and mixed workloads

weight: 2

layout: "learningpathall"
---

## Introduction
UltraEdge is an edge-native, high-performance execution fabric designed to run AI and mixed workloads without the overhead of traditional container platforms. While technologies like Docker and Kubernetes were created for general-purpose cloud environments, they introduce latency, resource bloat, and non-deterministic behavior that are poorly suited for edge deployments.

UltraEdge takes a fundamentally different approach. It replaces heavyweight container runtimes with a lean, deterministic execution stack purpose-built for performance-oriented compute. This enables millisecond-level startup times, predictable performance, and a dramatically smaller resource footprint - allowing workloads to start faster, run closer to the hardware, and make full use of available CPU and GPU resources.

At the core of UltraEdge are two specialized execution systems: 

· MicroStack, optimized for enterprise and mixed workloads

· NeuroStack, purpose-built for AI inference and accelerated compute

Together, these systems deliver up to 30x faster startup times and 3.8x smaller package sizes compared to conventional container-based approaches. By removing unnecessary abstraction layers, UltraEdge ensures compute cycles are spent on execution - not on managing the runtime itself.

This Learning Path introduces the architecture, principles, and components that make UltraEdge a high-performance execution fabric for modern edge infrastructure.

## UltraEdge overview

UltraEdge orchestrates an edge-native execution fabric for high-performance compute infrastructure. Key design principles and capabilities include:

**Built-for-edge execution stack**

A lightweight, adaptive platform for AI and mixed workloads optimized for low latency, high determinism, and minimal footprint.

**Dual workload focus**

Native support for both traditional enterprise workloads and next-generation AI workloads, without compromising performance.

**Full-stack enablement**

Delivered through MicroStack and NeuroStack execution systems, each optimized for its workload domain.



## Understand UltraEdge architecture for edge AI and mixed workloads

UltraEdge is an edge-native, high-performance execution fabric for AI and mixed workloads on Arm platforms. Unlike traditional container platforms such as Docker and Kubernetes, UltraEdge minimizes latency, resource overhead, and non-deterministic behavior, making it ideal for edge deployments where performance and efficiency are critical.

## Explore UltraEdge execution fabric

UltraEdge replaces heavyweight container runtimes with a lean, deterministic execution stack. This enables millisecond-level startup times, predictable performance, and a smaller resource footprint. You can start workloads faster, run closer to the hardware, and maximize CPU and GPU utilization.

UltraEdge includes two specialized execution systems:
- **MicroStack**: Optimized for enterprise and mixed workloads
- **NeuroStack**: Purpose-built for AI inference and accelerated compute

These systems deliver up to 30x faster startup times and 3.8x smaller package sizes compared to conventional container-based approaches. By removing unnecessary abstraction layers, UltraEdge ensures compute cycles are spent on execution, not on managing the runtime.

## Review UltraEdge features and design principles

UltraEdge orchestrates edge-native execution for high-performance compute infrastructure. Its design principles include:

- built-for-edge execution stack: lightweight, adaptive platform for AI and mixed workloads, optimized for low latency and high determinism
- dual workload focus: native support for both enterprise and next-generation AI workloads
- full-stack enablement: delivered through MicroStack and NeuroStack, each optimized for its domain
- high efficiency: maximizes CPU and GPU utilization, reduces operational overhead
- ecosystem alignment: developed with technology partners and aligned with Edge AI Foundation deployment approaches
- cluster-aware orchestration: integrates with Kubernetes and Slurm for managed cluster orchestration
- built-in observability: provides diagnostics, telemetry, and control-plane visibility
- lower total cost of ownership (TCO): reduces CPU/GPU cluster costs through faster startup, higher utilization, and less runtime overhead


## UltraEdge architecture layers

UltraEdge is composed of layered systems, each responsible for a distinct aspect of execution and orchestration:

![UltraEdge high-level architecture diagram showing layered execution systems for edge AI and mixed workloads alt-txt#center](https://raw.githubusercontent.com/Tinkerbloxsupport/arm-learning-path-support/main/static/images/High-level%20architecture%20diagram.png "UltraEdge high-level architecture")

UltraEdge organizes functionality into five specialized layers. Each layer is responsible for a specific aspect of workload execution and orchestration:

- **Core layer**: manages compute infrastructure, service orchestration, rule engines, and data flow across workloads.
- **Boost layer**: accelerates workloads with optimized routines, FFI (Foreign Function Interface) integrations, and dynamic connectors.
- **Prime layer**: coordinates workload intelligence, business logic, triggers, and AI/mixed workload orchestration.
- **Dock layer**: orchestrates workloads and clusters using Kubernetes-based stacks and Slurm-based scheduling.
- **Edge-cloud connect layer**: enables data streaming to databases (such as InfluxDB, SQLite), diagnostics, logging, and telemetry outputs.

## What you've accomplished and what's next

In this section, you:
- Learned the motivation and architecture behind UltraEdge
- Reviewed the layered execution systems and their roles in edge AI and mixed workloads

Next, you'll move on to hands-on installation and configuration of UltraEdge on your target Arm platform.

