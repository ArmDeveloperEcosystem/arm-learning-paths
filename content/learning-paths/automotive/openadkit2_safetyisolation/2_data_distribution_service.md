---
title: How to use Data Distribution Service (DDS)
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction to DDS
Data Distribution Service (DDS) is a real-time, high-performance middleware designed for distributed systems.
It is particularly valuable in automotive software development, including applications such as autonomous driving (AD) and advanced driver assistance systems (ADAS). 

DDS uses a decentralized architecture that supports scalable, low-latency, and reliable data exchange, which is ideal for managing high-frequency sensor streams.

In modern vehicles, multiple sensors such as LiDAR, radar, and cameras must continuously communicate with compute modules. 

DDS ensures these components share data seamlessly and in real time, both within the vehicle and across infrastructure such as V2X systems, including traffic lights and road sensors.

{{% notice Tip %}}
To get started with open-source DDS on Arm platforms, see the [Installation Guide for CycloneDDS](/install-guides/cyclonedds).
{{% /notice %}}


## Why automotive software needs DDS

Next-generation automotive software architectures, such as SOAFEE, depend on deterministic, distributed communication. Traditional client-server models introduce latency and create single points of failure. In contrast, DDS uses a publish-subscribe model that enables direct, peer-to-peer communication across system components.

For example, a LiDAR sensor broadcasting obstacle data can simultaneously deliver updates to perception, SLAM, and motion planning modules. This approach avoids redundant network traffic and does not require central coordination.

Additionally, DDS provides a flexible Quality of Service (QoS) configuration, allowing engineers to fine-tune communication parameters based on system requirements. Low-latency modes are ideal for real-time decision-making in vehicle control, while high-reliability configurations ensure data integrity in safety-critical applications such as V2X communication.

These capabilities make DDS an essential backbone for autonomous vehicle stacks, where real-time sensor fusion and control coordination are critical for safety and performance.

## DDS architecture and operation

DDS uses a data-centric publish-subscribe (DCPS) model, allowing producers and consumers of data to communicate without direct dependencies. This modular approach enhances system flexibility and maintainability, making it well suited for complex automotive environments.

DDS organizes communication within domains, which act as isolated scopes. Inside each domain, the following elements are used:
- Topics represent named data streams, such as /vehicle/speed or /perception/objects.
- DataWriters (publishers) send data to topics.
- DataReaders (subscribers) receive data from topics.

This structure enables concurrent, decoupled communication between multiple modules without hardcoding communication links.

Each domain contains multiple topics, representing specific data types such as vehicle speed, obstacle detection, or sensor fusion results. Publishers use DataWriters to send data to these topics, while subscribers use DataReaders to receive the data. This architecture supports concurrent data processing, ensuring that multiple modules can work with the same data stream simultaneously.

For example, in an autonomous vehicle, LiDAR, radar, and cameras continuously generate large amounts of sensor data. The perception module subscribes to these sensor topics, processes the data, and then publishes detected objects and road conditions to other components like path planning and motion control. Since DDS automatically handles participant discovery and message distribution, engineers do not need to manually configure communication paths, reducing development complexity.

## Real-world use in autonomous driving

DDS is widely used in autonomous driving systems, where real-time data exchange is crucial. A typical use case involves high-frequency sensor data transmission and decision-making coordination between vehicle subsystems.

For instance, a LiDAR sensor generates millions of data points per second, which need to be shared with multiple modules. DDS allows this data to be published once and received by multiple subscribers, including perception, localization, and mapping components. After processing, the detected objects and road features are forwarded to the path planning module, which calculates the vehicle's next movement. Finally, control commands are sent to the vehicle actuators, ensuring precise execution.

This real-time data flow must occur within milliseconds to enable safe autonomous driving. DDS ensures minimal transmission delay, enabling rapid response to dynamic road conditions. In emergency scenarios, such as detecting a pedestrian or sudden braking by a nearby vehicle, DDS facilitates instant data propagation, allowing the system to take immediate corrective action.

For example, Autoware, an open-source autonomous driving software stack, uses DDS to handle high-throughput communication across its modules. 

The Perception stack publishes detected objects from LiDAR and camera sensors to a shared topic, which is then consumed by the Planning module in real-time. Using DDS allows each subsystem to scale independently while preserving low-latency and deterministic communication.

## Publish-subscribe model and data transmission

Let’s explore how DDS’s publish-subscribe model fundamentally differs from traditional communication methods in terms of scalability, latency, and reliability.

Traditional client-server communication requires a centralized server to manage data exchange. This architecture introduces several drawbacks, including increased latency and network congestion, which can be problematic in real-time automotive applications.

DDS adopts a publish-subscribe model, enabling direct communication between system components. Instead of relying on a central entity to relay messages, DDS allows each participant to subscribe to relevant topics and receive updates as soon as new data becomes available. This approach reduces dependency on centralized infrastructure and improves overall system performance.

For example, in an automotive perception system, LiDAR, radar, and cameras continuously publish sensor data. Multiple subscribers, including object detection, lane recognition, and obstacle avoidance modules, can access this data simultaneously without additional network overhead. DDS automatically manages message distribution, ensuring efficient resource utilization.

DDS supports multiple transport mechanisms to optimize communication efficiency:
* Shared memory transport is ideal for ultra-low-latency communication within an ECU, minimizing processing overhead.
* UDP or TCP/IP is used for inter-device communication, such as V2X applications where vehicles exchange safety-critical messages.
* Automatic participant discovery eliminates the need for manual configuration, allowing DDS nodes to detect and establish connections dynamically.

## Compare DDS with traditional communication models

The following table highlights how DDS improves upon traditional client-server communication patterns in the context of real-time automotive applications:

| Feature              | Traditional client-server architecture      | DDS publish-subscribe model       |
|----------------------|--------------------------------------------|---------------------------        |
| Data Transmission    | Relies on a central server                 | Direct peer-to-peer communication |
| Latency              | Higher latency                             | Low latency                       |
| Scalability          | Limited by server capacity                 | Suitable for large-scale systems  |
| Reliability          | Server failure affects the whole system    | No single point of failure        |
| Use Cases            | Small-scale applications                   | V2X, autonomous driving           |

These features make DDS a highly adaptable solution for automotive software engineers seeking to develop scalable, real-time communication frameworks.

DDS is a critical building block in distributed automotive systems. By enabling scalable, low-latency communication and fault tolerance, it powers real-time coordination in modern architectures like ROS 2, SOAFEE, and Autoware.

Its data-centric publish-subscribe architecture removes the limitations of traditional client-server models and forms the backbone of modern automotive software frameworks like ROS 2 and SOAFEE.



