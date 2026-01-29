---
title: UltraEdge HPC-I execution fabric for AI & mixed workloads

weight: 2

layout: "learningpathall"
---

### Introduction

UltraEdge is an edge-native, high-performance execution fabric designed to run AI and mixed workloads without the overhead of traditional container platforms. While technologies like Docker and Kubernetes were created for general-purpose cloud environments, they introduce latency, resource bloat, and non-deterministic behavior that are poorly suited for edge deployments.

UltraEdge takes a fundamentally different approach. It replaces heavyweight container runtimes with a lean, deterministic execution stack purpose-built for performance-oriented compute. This enables millisecond-level startup times, predictable performance, and a dramatically smaller resource footprint—allowing workloads to start faster, run closer to the hardware, and make full use of available CPU and GPU resources.

At the core of UltraEdge are two specialized execution systems:

· **MicroStack**, optimized for enterprise and mixed workloads

· **NeuroStack**, purpose-built for AI inference and accelerated compute

Together, these systems deliver up to **30× faster startup times** and **3.8× smaller package sizes** compared to conventional container-based approaches. By removing unnecessary abstraction layers, UltraEdge ensures compute cycles are spent on execution—not on managing the runtime itself.

This learning path introduces the architecture, principles, and components that make UltraEdge a high-performance execution fabric for modern edge infrastructure. 

### Ultraedge Overview

UltraEdge was built with the vision of **orchestrating the edge-native execution fabric for high-performance compute infrastructure**

Key design principles and capabilities include:

· **Built-for-edge execution stack** 

A lightweight, adaptive platform for **AI and mixed workloads** optimized for low latency, high determinism, and minimal footprint.

· **Dual workload focus** 

Native support for both traditional enterprise workloads and next-generation AI workloads, without compromising performance.

· **Full-stack enablement** 

Delivered through the **MicroStack** and **NeuroStack** execution systems, each optimized for its workload domain.

· **High fungibility and efficiency**

Maximizes utilization of CPU and GPU resources while reducing operational and infrastructure overhead.

· **Ecosystem-aligned development**

Developed through strategic alliances with leading technology partners and curated for **AI@Edge**, including alignment with Edge AI Foundation deployment approaches.

· **Cluster-aware orchestration**

Integrates with Kubernetes-based stacks and Slurm for managed cluster orchestration.

· **Built-in observability**

Provides control-plane visibility, diagnostics, and telemetry for operational insight.

· **Lower total cost of ownership (TCO)**

Demonstrable reduction in CPU/GPU cluster costs through faster startup, higher utilization, and reduced runtime overhead. 

### UltraEdge High-Level Architecture

UltraEdge is composed of layered systems, each responsible for a distinct aspect of execution and orchestration:

![High-level Architecture diagram](https://raw.githubusercontent.com/Tinkerbloxsupport/arm-learning-path-support/main/static/images/High-level%20architecture%20diagram.png)

---

#### 1. UltraEdge Core Layer
*Manages the foundational execution fabric, including:*
* Compute infrastructure management
* Service orchestration and lifecycle management
* Rule-engine orchestration
* Data-flow management across workloads

#### 2. UltraEdge Boost Layer
*Provides performance-critical acceleration, including:*
* Low-level optimized routines
* FFI (Foreign Function Interface) integrations
* Dynamic connectors and southbound protocol adapters

#### 3. UltraEdge Prime Layer
*Implements workload intelligence and orchestration logic, including:*
* Business logic execution
* Trigger and activation sequences
* AI and mixed workload coordination

#### 4. UltraEdge Dock
*Provides workload and cluster orchestration through:*
* Kubernetes-based stacks
* Slurm-based scheduling environments

#### 5. UltraEdge Edge-Cloud Connect Layer
*Enables data movement and observability, including:*
* Data streaming to databases (e.g., InfluxDB, SQLite)
* Diagnostics, logging, and telemetry outputs

