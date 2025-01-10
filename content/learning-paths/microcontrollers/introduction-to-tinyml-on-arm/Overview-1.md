---
title: Introduction to TinyML
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This Learning Path is about TinyML. It serves as a starting point for learning how cutting-edge AI technologies may be put on even the smallest of devices, making Edge AI more accessible and efficient. You will learn how to setup on your host machine and target device to facilitate compilation and ensure smooth integration across all devices.

In this section, you get an overview of the domain with real-life use-cases and available devices.

## Overview
TinyML represents a significant shift in machine learning deployment. Unlike traditional machine learning, which typically depends on cloud-based servers or high-powered hardware, TinyML is tailored to function on devices with limited resources, constrained memory, low power, and less processing capabilities. TinyML has gained popularity because it enables AI applications to operate in real-time, directly on the device, with minimal latency, enhanced privacy, and the ability to work offline. This shift opens up new possibilities for creating smarter and more efficient embedded systems.

### Benefits and applications

The advantages of TinyML match up well with the Arm architecture, which is widely used in IoT, mobile devices, and edge AI deployments.

Here are some key benefits of TinyML on Arm:


- **Power Efficiency**: TinyML models are designed to be extremely power-efficient, making them ideal for battery-operated devices like sensors, wearables, and drones.

- **Low Latency**: Because the AI processing happens on-device, there's no need to send data to the cloud, reducing latency and enabling real-time decision-making.

- **Data Privacy**: With on-device computation, sensitive data remains local, providing enhanced privacy and security. This is particularly crucial in healthcare and personal devices.

- **Cost-Effective**: Arm devices, which are cost-effective and scalable, can now handle sophisticated machine learning tasks, reducing the need for expensive hardware or cloud services.

- **Scalability**: With billions of Arm devices in the market, TinyML is well-suited for scaling across industries, enabling widespread adoption of AI at the edge.

TinyML is being deployed across multiple industries, enhancing everyday experiences and enabling groundbreaking solutions. The table below contains a few examples of TinyML applications.

| Area                  |  Device, Arm IP           | Description                                                                                             |
| ------                | -------                   | ------------                                                                                            |
| Healthcare            | Fitbit Charge 5, Cortex-M | Monitor vital signs such as heart rate, detect arrhythmias, and provide real-time feedback.             |
| Agriculture           | OpenAg, Cortex-M          | Monitor soil moisture and optimize water usage.                                                         |
| Home automation       | Arlo, Cortex-A            | Detect objects and people, trigger alerts or actions while saving bandwidth and improving privacy.      |
| Industrial IoT        | Siemens, Cortex-A         | Analyze vibration patterns in machinery to predict when maintenance is needed and prevent breakdowns.   |
| Wildlife conservation | Conservation X, Cortex-M  | Identify animal movements or detect poachers in remote areas without relying on external power sources. |

### Examples of Arm-based devices

There are many Arm-based off-the-shelf devices you can use for TinyML projects. Some of them are listed below, but the list is not exhaustive.

#### Raspberry Pi 4 and 5

Raspberry Pi single-board computers are excellent for prototyping TinyML projects. They are commonly used for prototyping machine learning projects at the edge, such as in object detection and voice recognition for home automation.

#### NXP i.MX RT microcontrollers

NXP i.MX RT microcontrollers are low-power microcontrollers that can handle complex TinyML tasks while maintaining energy efficiency, making them ideal for applications like wearable healthcare devices and environmental sensors.

#### STM32 microcontrollers

STM32 microcontrollers are used in industrial IoT applications for predictive maintenance. These microcontrollers are energy-efficient and capable of running TinyML models for real-time anomaly detection in factory machinery.

#### Arduino Nano 33 BLE Sense

The Arduino Nano, equipped with a suite of sensors, supports TinyML and is ideal for small-scale IoT applications, such as detecting environmental changes and movement patterns.

#### Edge Impulse

In addition to hardware, there are software platforms that can help you build TinyML applications.

Edge Impulse platform offers a suite of tools for developers to build and deploy TinyML applications on Arm-based devices. It supports devices like Raspberry Pi, Arduino, and STMicroelectronics boards.

Now that you have an overview of the subject, move on to the next section where you will set up an environment on your host machine.