---
title: Introduction Zenoh
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The Need for Scalable Communication in Robotics and Edge Computing

Modern robotics and industrial IoT (IIoT) systems are evolving rapidly—from indoor collaborative arms on assembly lines to fleets of outdoor autonomous delivery robots. 
These applications must operate in real-time, often across multiple compute nodes, over networks that may span factory LANs, 5G cellular links, or even cloud data centers.

Such systems require fast, reliable, and scalable data communication between nodes. 
This includes not just broadcasting sensor updates or actuator commands (i.e., pub/sub), but also performing state queries, storing values for later use, and even distributed computation across nodes. A modern protocol must be:
* Low-latency: Immediate delivery of time-critical messages.
* High-throughput: Efficient data flow across many devices.
* Decentralized: No reliance on central brokers or fixed infrastructure.
* Flexible: Able to run on lightweight edge devices, across WANs, or inside cloud-native environments.

Traditional communication stacks such as DDS ([Data Distribution Service](https://en.wikipedia.org/wiki/Data_Distribution_Service)) serve as the backbone for middleware like ROS 2. However, DDS struggles in multi-network or wireless environments where multicast is unavailable, or NAT traversal is needed.
These constraints can severely impact deployment and performance at the edge.


## Zenoh: An Open-Source Pub/Sub Protocol for the Industrial Edge

[Eclipse Zenoh](https://zenoh.io/) is a modern, [open-source](https://github.com/eclipse-zenoh/zenoh) data-centric communication protocol that goes beyond traditional pub/sub. Designed specifically for edge computing, IIoT, robotics, and autonomous systems, Zenoh unifies:

* Data in motion through a powerful and efficient pub/sub model.
* Data at rest via geo-distributed storage plugins.
* Data in use with direct query support.
* On-demand computation via queryable nodes that can generate data dynamically.

Unlike most traditional stacks, Zenoh is fully decentralized and designed to operate across cloud-to-edge-to-thing topologies, making it ideal for industrial robotics, autonomous systems, and smart environments. 
It supports heterogeneous platforms, is implemented in Rust for performance and safety, and also offers bindings for Python, enabling rapid prototyping.

Zenoh is particularly effective in wireless, 5G, or cross-network deployments where multicast and DDS fall short. 
Its routing engine avoids excessive discovery traffic, conserves bandwidth, and supports seamless bridging between legacy ROS 2/DDS apps and modern, optimized Zenoh networks using zenoh-bridge-dds.

In this learning path, you’ll use Zenoh to build and validate a multi-node distributed communication system across multiple Arm-based platforms, gaining hands-on experience with data exchange and coordination between edge devices.

To make the upcoming demo more intuitive and easy to follow, we’ll demonstrate the setup using two physical Cortex-A Linux devices. 

I’ll be using Raspberry Pi boards in this learning path, but you’re free to substitute them with any Cortex-A devices that support network connectivity with Linux-based OS installed, depending on your development setup.

In real-world ROS 2 deployment scenarios, developers typically conduct validation and performance testing across systems with more than two nodes.
To simulate such environments, using [Arm virtual hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware) is also a common and efficient approach.

This will help you quickly validate your architecture choices and communication patterns when designing distributed applications.

* Raspberry Pi,
* Linux-based Cortex-A, or
* Arm Virtual Hardware (AVH).

After this learning path, you will:
* Understand the core architecture and data flow principles behind Eclipse Zenoh, including its support for pub/sub, querying, and queryable edge functions.
* Build and run distributed Zenoh examples across multiple Arm-based nodes—using Raspberry Pi or AVH to simulate scalable deployment environments.
* Rebuild and extend the Zenoh queryable example to simulate edge-side logic.

By the end of this learning path, you’ll have deployed a fully functional, scalable, and latency-aware Zenoh system.

You can also check [here](https://zenoh.io/docs/getting-started/first-app) to find some simple examples.
