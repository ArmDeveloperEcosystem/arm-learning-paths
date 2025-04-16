---
title: Essential automotive software technologies
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Before getting into technical details, there are two essential technologies used in automotive software that you need to understand, ROS 2 and Open AD Kit.

## What is Robot Operating System 2 (ROS 2)? 

Robot Operating System 2 (ROS 2) is an open-source robotics middleware designed to provide a flexible, scalable, and real-time capable framework for robot development. It builds upon the foundations of ROS 1, addressing limitations in distributed computing, security, and multi-robot collaboration. ROS 2 is widely used in autonomous systems, industrial automation, and research applications.

Key Features of ROS 2:
- **Cross-Platform Support**: Runs on Linux, Windows, and real-time operating systems (RTOS), ensuring flexibility in deployment.

- **Real-Time Capabilities**: Uses Data Distribution Service (DDS) for efficient inter-process communication, enabling real-time performance.
	
- **Enhanced Security & Reliability**: Provides encrypted communication, deterministic scheduling, and built-in fault tolerance.
	
- **Multi-Robot & Distributed System Support**: Enables large-scale robotic systems and cloud-based robotics applications.
	
- **Modular and Scalable Architecture**: Uses a node-based system where different components operate independently.

Applications of ROS 2:

- ROS 2 is used in autonomous vehicles, robotic arms, drones, and medical robots. It supports simulation tools like Gazebo and integrates with AI frameworks for advanced robotics applications.

- ROS 2's enhanced performance and flexibility make it a crucial enabler for the future of robotics, providing developers with a powerful platform for building intelligent, autonomous systems.

Arm's computing platform fully supports ROS 2 operations. You can use the [ROS install guide](/install-guides/ros2/) to install it on an Arm-based machine.

## Connecting ROS 2 and Automotive Applications

ROS 2 serves as the foundation for many modern automotive software platforms, particularly in autonomous driving applications. Its real-time capabilities, distributed architecture, and robust communication framework make it ideal for processing sensor data, implementing decision-making algorithms, and controlling vehicle systems. This is where Open AD Kit comes into play - it leverages ROS 2's capabilities to create a comprehensive autonomous driving platform that bridges the gap between robotics middleware and automotive-specific requirements. Together, these technologies enable developers to build sophisticated autonomous driving systems with standardized interfaces, scalable architectures, and the flexibility to deploy across various hardware configurations.

## What is Autoware Open AD Kit?

[Open AD Kit](https://autoware.org/open-ad-kit/), the first SOAFEE blueprint, is a collaborative initiative within the [Autoware](https://autoware.org/) and SOAFEE ecosystems. Developed with contributions from Autoware Foundation members and alliance partners, its goal is to enable Autoware as a fully software-defined platform.

The Autoware Foundation hosts Autoware, the world's leading open-source autonomous driving project.

Autoware, built on ROS, features a modular AD stack with well-defined interfaces and APIs for perception, localization, planning, and control. It supports diverse sensors and hardware, enabling adaptability across vehicle types and applications, from research to commercial deployment.

Committed to democratizing AD technology, Autoware fosters collaboration among industry, researchers, and developers. By promoting open standards and innovation, the foundation accelerates autonomous driving adoption while ensuring safety, scalability, and real-world usability, driving the future of autonomous mobility through open-source development and ecosystem synergy.

The Open AD Kit Blueprint has evolved through multiple iterations of containerized Autoware software. It supports both cloud and edge deployments in physical and virtual environments, with OTA updates enabling seamless software upgrades.
The Open AD Kit project continues to be developed by the Open AD Kit working group, and the following are the main goals and principles of the collaborative project:
- Introducing modern cloud-native development and deployment methodologies for the Autoware use
- Introducing mixed-critical orchestration, paving the way for safety and certifiability
- Enabling validation using virtual prototyping platforms to achieve shift-left paradigms
- Providing a consistent production environment to deploy Autoware using hardware abstraction technologies to enable hardware-agnostic solutions

The Open AD Kit Blueprint has been widely adopted by many ecosystem players to develop their own custom-flavored implementations. The blueprint provides a practical and demonstrable example of building SDV applications, particularly in the autonomous driving domain. Additionally, it serves as a model for creating SOAFEE blueprints, fostering a dynamic ecosystem around them.

In the following sections, you will learn how to use the Open AD Kit autonomous driving simulation environment to run SOAFEE within a container and facilitate communication through ROS 2.
