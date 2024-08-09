---
title: Motivation
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is hybrid-runtime?
Hybrid-runtime enables the deployment of software onto other processors, such as Cortex-M or Cortex-R-based CPUs. The deployment is made possible by using cloud-native technologies in the system, with Linux running on the Cortex-A application cores.

## Example use cases

Here are some examples where this functionality can be useful:

- System-wide firmware updates made easy, secure and controllable at scale. The hybrid runtime makes it possible to update what's running on the Cortex-M on-demand, for example, to address bugs, security vulnerabilities, performance, or to update functionality.
- Partitioning applications over multiple IPs. It enables applications to be divided into different services, where each service runs on a different core, depending on its requirements. In a scenario where you want to preserve energy, one part can run on a Cortex-M while the main CPU is asleep. Then, once an event is detected, Cortex-A is woken up and can start running its part of the application. The parts can then be deployed and managed in a uniform way.
- Taking full advantage of the system's capabilities. This is useful in a system with boards that are idle for a majority of the time. By making it easy to access them, you can leverage existing cores on every edge node.

More details on the runtime can be found on the [hybrid-runtime GitHub page](https://github.com/smarter-project/hybrid-runtime.git).

