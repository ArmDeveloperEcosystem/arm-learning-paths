---
title: Introduction to Zenoh
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The need for scalable communication in robotics and edge computing

Modern robotics and industrial IoT systems are evolving rapidly, from indoor collaborative arms on assembly lines to fleets of outdoor autonomous delivery robots. 
These applications must operate in real-time, often across multiple compute nodes, over networks that may span factory LANs, 5G cellular links, or even cloud data centers.

Such systems require fast, reliable, and scalable data communication between nodes. 
This includes not just broadcasting sensor updates or actuator commands (pub/sub), but also performing state queries, storing values for later use, and even distributed computation across nodes. 

A modern protocol must be:
* Low-latency: immediate delivery of time-critical messages
* High-throughput: efficient data flow across many devices
* Decentralized: no reliance on central brokers or fixed infrastructure
* Flexible: able to run on lightweight edge devices, across WANs, or inside cloud-native environments

Traditional communication stacks such as Data Distribution Service (DDS) serve as the backbone for middleware like ROS 2. However, DDS struggles in multi-network or wireless environments where multicast is unavailable, or NAT traversal is needed. Zenoh was developed to address these challenges with a unified approach to data movement, storage, and interaction across heterogeneous, distributed systems.

## What is Zenoh? A scalable pub/sub protocol for the industrial edge

[Eclipse Zenoh](https://zenoh.io/) is a modern, open-source, data-centric communication protocol that goes beyond traditional pub/sub. Designed specifically for edge computing, industrial IoT, robotics, and autonomous systems, Zenoh unifies:

- Data in motion through a powerful and efficient pub/sub model
- Data at rest via geo-distributed storage plugins
- Data in use with direct query support
- On-demand computation via queryable nodes that can generate data dynamically

Unlike most traditional stacks, Zenoh is fully decentralized and designed to operate across cloud-to-edge-to-thing topologies, making it ideal for industrial robotics, autonomous systems, and smart environments. 

It supports heterogeneous platforms, is implemented in Rust for performance and safety, and also offers bindings for Python, enabling rapid prototyping.

Zenoh excels in wireless, 5G, and cross-network deployments, which are environments where multicast is unavailable and DDS often struggles. Its routing engine avoids excessive discovery traffic, conserves bandwidth, and supports seamless bridging between legacy ROS 2/DDS apps and modern, optimized Zenoh networks using Zenoh-Bridge-DDS, a bridge between DDS systems and Zenoh networks.

In this Learning Path, you’ll use Zenoh to build and validate a multi-node distributed communication system across multiple Arm-based platforms, gaining hands-on experience with data exchange and coordination between edge devices.

You can substitute Raspberry Pi with any Linux-based Arm device that supports networking, such as a Cortex-A or Neoverse board.

By the end of this Learning Path, you'll be able to:
- Explain the core architecture and data flow principles behind Eclipse Zenoh protocol, including its support for pub/sub, querying, and queryable edge functions
- Build and run distributed Zenoh examples across multiple Arm-based nodes using Raspberry Pi or other Arm Linux devices
- Rebuild and extend a Zenoh queryable node to simulate edge-side logic

