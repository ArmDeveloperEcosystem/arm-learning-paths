---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## TinyML


This Learning Path is about TinyML. It is a starting point for learning how innovative AI technologies can be used on even the smallest of devices, making Edge AI more accessible and efficient. You will learn how to set up your host machine and target device to facilitate compilation and ensure smooth integration across devices.

This section provides an overview of the domain with real-life use cases and available devices.

TinyML represents a significant shift in Machine Learning deployment. Unlike traditional Machine Learning, which typically depends on cloud-based servers or high-performance hardware, TinyML is tailored to function on devices with limited resources, constrained memory, low power, and less processing capabilities. 

TinyML has gained popularity because it enables AI applications to operate in real-time, directly on the device, with minimal latency, enhanced privacy, and the ability to work offline. This shift opens up new possibilities for creating smarter and more efficient embedded systems.

### Benefits and applications

The benefits of TinyML align well with the Arm architecture, which is widely used in IoT, mobile devices, and edge AI deployments.

Here are some of the key benefits of TinyML on Arm:


- **Power Efficiency**: TinyML models are designed to be extremely power-efficient, making them ideal for battery-operated devices like sensors, wearables, and drones.

- **Low Latency**: AI processing happens on-device, so there is no need to send data to the cloud, which reduces latency and enables real-time decision-making.

- **Data Privacy**: With on-device computation, sensitive data remains local, providing enhanced privacy and security. This is a priority in healthcare and personal devices.

- **Cost-Effective**: Arm devices, which are cost-effective and scalable, can now handle sophisticated Machine Learning tasks, reducing the need for expensive hardware or cloud services.

- **Scalability**: With billions of Arm devices in the market, TinyML is well-suited for scaling across industries, enabling widespread adoption of AI at the edge.

TinyML is being deployed across multiple industries, enhancing everyday experiences and enabling groundbreaking solutions. The table below contains a few examples of TinyML applications.

| Area                  |  Device, Arm IP             | Description                                                                                                |
| ------                | -------                     | ------------                                                                                               |
| Healthcare            | Fitbit Charge 5, Cortex-M   | To monitor vital signs such as heart rate, detect arrhythmias, and provide real-time feedback.             |
| Agriculture           | OpenAg, Cortex-M            | To monitor soil moisture and optimize water usage.                                                         |
| Home automation       | Arlo, Cortex-A              | To detect objects and people, trigger alerts or actions while saving bandwidth and improving privacy.      |
| Industrial IoT        | Siemens, Cortex-A           | To analyze vibration patterns in machinery to predict when maintenance is needed and prevent breakdowns.   |
| Wildlife conservation | Conservation X, Cortex-M    | To identify animal movements or detect poachers in remote areas without relying on external power sources. |

### Examples of Arm-based devices

There are many Arm-based devices that you can use for TinyML projects. Some of these are listed below, but the list is not exhaustive.

#### Raspberry Pi 4 and 5

Raspberry Pi single-board computers are excellent for prototyping TinyML projects. They are commonly used for prototyping machine learning projects at the edge, such as in object detection and voice recognition for home automation.

#### NXP i.MX RT microcontrollers

NXP i.MX RT microcontrollers are low-power microcontrollers that can handle complex TinyML tasks while maintaining energy efficiency. This makes them ideal for applications like wearable healthcare devices and environmental sensors.

#### STM32 microcontrollers

STM32 microcontrollers are used in industrial IoT applications for predictive maintenance. These microcontrollers are energy-efficient and capable of running TinyML models for real-time anomaly detection in factory machinery.

#### Arduino Nano 33 BLE Sense

The Arduino Nano, equipped with a suite of sensors, supports TinyML and is ideal for small-scale IoT applications, such as detecting environmental changes and movement patterns.

#### Edge Impulse

In addition to hardware, there are software platforms that can help you build TinyML applications.

Edge Impulse offers a suite of tools for developers to build and deploy TinyML applications on Arm-based devices. It supports devices like Raspberry Pi, Arduino, and STMicroelectronics boards.

Now that you have an overview of the subject, you can move on to the next section where you will set up an environment on your host machine.