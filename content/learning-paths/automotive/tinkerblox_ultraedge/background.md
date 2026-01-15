---
title: UltraEdge HPC-I execution fabric for AI & mixed workloads

weight: 2

layout: "learningpathall"
---

{{% notice Note %}}
REMOVE ME:  Need to review content for Intro/background...
{{% /notice %}}

### Overview

UltraEdge was built with the vision of orchestrating the edge-native
execution fabric for high-performance compute infrastructure

-   UltraEdge is a ‘built-for-edge’ adaptive **AI & Mixed Workloads**
    execution stack built on the ethos of high performance, high
    fungibility & ultra-low footprint
-   Developed through strategic alliances with world-renowned technology
    powerhouses
-   Clear dual focus on Mixed workloads and new-age AI workloads
-   Full stack enablement through MicroStack & NeuroStack systems
-   Curated for AI@Edge with preferred edge deployment approach by Edge
    AI Foundation
-   Managed cluster” orchestration through integration with Kube-stack
    and/or Slurm
-   Observability for control plane, diagnostics & telemetry
-   Demonstrable value to customer through lower TCO of CPU-GPU clusters

### UltraEdge High-Level Architecture

{{% notice Note %}}
REMOVE ME:  It would be good to put a high-level picture of the architecture here. Then text below can detail the high points. 
{{% /notice %}}

**UltraEdge ‘Core’ Layer **  
Handles compute infrastructure management including service
orchestration, lifecycle management, rule engine orchestration, and
data-flow management .

**UltraEdge ‘Boost’ Layer **  
Implements performance-critical routines and FFI (Foreign Function
Interface) calls; Contains dynamic connectors, and southbound protocol
adapters

**UltraEdge ‘Prime’ Layer **  
Contains business logic, trigger & activation sequences, and AI & mixed
workload orchestration .

**UltraEdge Edge-Cloud ‘Connect’ Layer **  
Supports data streaming to databases (InfluxDB, SQLite) and provides
diagnostic/logging outputs . **UltraEdge Dock** Supports workload orchestration 
management through kube-stack or slurm.
