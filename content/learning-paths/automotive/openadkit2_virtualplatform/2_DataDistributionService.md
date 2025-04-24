---
title: How to use Data Distribution Service (DDS)
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Introduction to DDS
Data Distribution Service (DDS) is a real-time, high-performance middleware designed for distributed systems, particularly in automotive software development for autonomous driving and advanced driver assistance systems (ADAS). Its decentralized architecture provides scalable, low-latency, and reliable data exchange, making it an essential component in managing high-frequency sensor data.

In modern vehicles, multiple sensors, such as LiDAR, radar, and cameras, must communicate efficiently with computing modules and decision-making units. DDS enables seamless data transmission within the vehicle, ensuring that perception, localization, and control systems receive the necessary data with minimal delay. Additionally, it plays a crucial role in vehicle-to-infrastructure (V2X) communication, allowing vehicles to exchange information with traffic signals, road sensors, and other connected systems to enhance situational awareness and safety.


### Why Automotive Software Needs DDS
Modern automotive software architectures, such as SOAFEE, require deterministic data communication to ensure real-time coordination between sensors, ECUs, and computing modules. Traditional client-server communication models often introduce latency and bottlenecks, whereas DDS provides a direct, decentralized solution that enhances reliability and scalability.

A key advantage of DDS is its ability to enable direct data exchange between system components without relying on a central server. This reduces the risk of a single point of failure and minimizes delays, which is crucial for autonomous driving applications where milliseconds can make a difference. For example, a LiDAR sensor publishing obstacle detection data can simultaneously send information to multiple subscribers, including perception, SLAM (Simultaneous Localization and Mapping), and motion planning modules. This parallel data distribution ensures all relevant subsystems have the latest environmental data without requiring multiple separate transmissions.

Additionally, DDS provides a flexible Quality of Service (QoS) configuration, allowing engineers to fine-tune communication parameters based on system requirements. Low-latency modes are ideal for real-time decision-making in vehicle control, while high-reliability configurations ensure data integrity in safety-critical applications like V2X communication.


### Architecture and Operation
DDS is based on a data-centric publish-subscribe (DCPS) model, allowing producers and consumers of data to communicate without direct dependencies. This modular approach enhances system flexibility and maintainability, making it well-suited for complex automotive environments.

In DDS, all participants operate within a **domain**, which provides logical isolation between different applications. Each domain contains multiple **topics**, representing specific data types such as vehicle speed, obstacle detection, or sensor fusion results. **Publishers** use **DataWriters** to send data to these topics, while **subscribers** use **DataReaders** to receive the data. This architecture supports concurrent data processing, ensuring that multiple modules can work with the same data stream simultaneously.

For example, in an autonomous vehicle, LiDAR, radar, and cameras continuously generate large amounts of sensor data. The perception module subscribes to these sensor topics, processes the data, and then publishes detected objects and road conditions to other components like path planning and motion control. Since DDS automatically handles participant discovery and message distribution, engineers do not need to manually configure communication paths, reducing development complexity.


### Applications in Autonomous Driving
DDS is widely used in autonomous driving systems, where real-time data exchange is crucial. A typical use case involves high-frequency sensor data transmission and decision-making coordination between vehicle subsystems.

For instance, a LiDAR sensor generates millions of data points per second, which need to be shared with multiple modules. DDS allows this data to be published once and received by multiple subscribers, including perception, localization, and mapping components. After processing, the detected objects and road features are forwarded to the path planning module, which calculates the vehicle's next movement. Finally, control commands are sent to the vehicle actuators, ensuring precise execution.

This real-time data flow must occur within milliseconds to enable safe autonomous driving. DDS ensures minimal transmission delay, enabling rapid response to dynamic road conditions. In emergency scenarios, such as detecting a pedestrian or sudden braking by a nearby vehicle, DDS facilitates instant data propagation, allowing the system to take immediate corrective action.

For example: [Autoware](https://www.autoware.org/)—an open-source autonomous driving software stack—uses DDS to handle high-throughput communication across its modules. For example, the **Perception** stack publishes detected objects from LiDAR and camera sensors to a shared topic, which is then consumed by the **Planning** module in real-time. Using DDS allows each subsystem to scale independently while preserving low-latency and deterministic communication.

### Publish-Subscribe Model and Data Transmission
Traditional client-server communication requires a centralized server to manage data exchange. This architecture introduces several drawbacks, including increased latency and network congestion, which can be problematic in real-time automotive applications.

DDS adopts a publish-subscribe model, enabling direct communication between system components. Instead of relying on a central entity to relay messages, DDS allows each participant to subscribe to relevant topics and receive updates as soon as new data becomes available. This approach reduces dependency on centralized infrastructure and improves overall system performance.

For example, in an automotive perception system, LiDAR, radar, and cameras continuously publish sensor data. Multiple subscribers, including object detection, lane recognition, and obstacle avoidance modules, can access this data simultaneously without additional network overhead. DDS automatically manages message distribution, ensuring efficient resource utilization.

DDS supports multiple transport mechanisms to optimize communication efficiency:
- **Shared memory transport**: Ideal for ultra-low-latency communication within an ECU, minimizing processing overhead.
- **UDP or TCP/IP**: Used for inter-device communication, such as V2X applications where vehicles exchange safety-critical messages.
- **Automatic participant discovery**: Eliminates the need for manual configuration, allowing DDS nodes to detect and establish connections dynamically.

#### Comparison of DDS and Traditional Communication Methods

| **Feature**          | **Traditional Client-Server Architecture** | **DDS Publish-Subscribe Model** |
|----------------------|--------------------------------|---------------------------|
| **Data Transmission** | Relies on a central server    | Direct peer-to-peer communication |
| **Latency**          | Higher latency                 | Low latency               |
| **Scalability**      | Limited by server capacity     | Suitable for large-scale systems |
| **Reliability**      | Server failure affects the whole system | No single point of failure |
| **Use Cases**       | Small-scale applications       | V2X, autonomous driving   |

These features make DDS a highly adaptable solution for automotive software engineers seeking to develop scalable, real-time communication frameworks.

Here is an [installation guide](https://learn.arm.com/install-guides/cyclonedds) on how to install open-source DDS on an Arm platform.

