---
title: Overview
weight: 2

# FIXED, DO NOT MODIFY
layout: learningpathall
---

{{< notice Note >}}
This section introduces the key concepts that form the foundation of this Learning Path. Review it before starting this Learning Path.
{{< /notice >}}

# Edge AI

Edge AI refers to artificial intelligence models that run directly on edge devices, processing data locally rather than relying on cloud computing. These models are optimized for real-time decision-making on resource-constrained devices such as microcontrollers, embedded systems, and IoT sensors.

TinyML (Tiny Machine Learning) is a subset of Edge AI that focuses on deploying machine learning models on ultra-low-power microcontrollers. These devices typically have less than 1 MB of flash memory and a few hundred kilobytes of RAM, and they are designed to run for extended periods on minimal power, which is often for years on a single coin-cell battery.

Despite these constraints, TinyML enables on-device inference, allowing edge devices to make intelligent decisions in real time without sending data to the cloud. This makes smart functionality possible in low-cost, battery-powered devices used in applications such as environmental monitoring, wearables, smart homes, and industrial sensors.

## Key characteristics of Edge AI and TinyML

Key features of Edge AI and TinyML include:

- **Low power consumption**: designed to run on batteries or harvested energy for months or years  
- **Small model size**: models are optimized (for example, quantized or pruned) to fit into a few kilobytes or megabytes  
- **Limited compute and memory**: typically operate with under 1 MB of RAM and very limited storage  
- **Real-time inference**: immediate local decision-making (for example, wake-word detection)  
- **Low latency**: no reliance on cloud; inference is performed on-device  
- **Applications**: often used in audio classification, gesture detection, and anomaly detection  

Example devices include Arduino Nano 33 BLE Sense, STM32 MCUs, Raspberry Pi Pico, and Arduino Nano RP2040 Connect.

## Run AI models on resource-constrained devices

Running AI on edge devices presents challenges. These devices often lack high-performance CPUs or GPUs, making compute power and memory usage key concerns. Since many edge devices run on batteries, energy efficiency is also critical.

To overcome these constraints, models are optimized using techniques such as *quantization*, *pruning*, and *knowledge distillation*. These methods reduce model size and resource requirements while maintaining acceptable accuracy.

## Edge AI workflow

[1] Data collection  
→ Sensors capture data (such as audio, motion, and vision)  

[2] Model training  
→ Use cloud or local compute for training  

[3] Model optimization  
→ Apply quantization, pruning, or distillation  

[4] Deployment  
→ Flash model onto Arm-based edge device  

[5] On-device inference  
→ Device makes real-time predictions locally

## Applications of Edge AI

Edge AI is used in a wide range of real-world applications:

- **Smart homes**: voice assistants process wake words locally; security systems detect motion and identify anomalies  
- **Wearables**: smartwatches detect heart rate irregularities; fitness trackers analyze motion patterns  
- **Industrial systems**: predictive maintenance uses vibration and temperature data; safety sensors shut down equipment automatically  
- **Agriculture**: AI-powered sensors optimize irrigation and fertilizer use  
- **Autonomous systems**: onboard AI enables real-time navigation and obstacle avoidance


## The BLERP framework

To recall the benefits of Edge AI, the **BLERP** mnemonic highlights five critical aspects:

| Area       | Description                                                                                                                                                           |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **B – Bandwidth**   | Reduces the need to send large amounts of data to the cloud, which is especially useful for video or sensor streams.                                         |
| **L – Latency**     | Enables real-time decision-making by processing data locally, with no round trips to the cloud. Crucial for self-driving cars, health monitors, and offline use.   |
| **E – Economics**   | Running models on-device reduces long-term costs related to cloud compute, data transfer, and power usage.                                                   |
| **R – Reliability** | Devices remain functional even when disconnected from the internet which is important for mission-critical or remote deployments.                                     |
| **P – Privacy**     | Data stays on-device, reducing risk and helping meet regulatory requirements like GDPR or HIPAA.                                                             |

## Why learn Edge AI?

Edge AI is revolutionizing industries by making smart, local decision-making possible at the device level:

- **Healthcare**: enables remote diagnostics and patient monitoring  
- **Agriculture**: improves yield through intelligent irrigation and pest control  
- **Manufacturing**: reduces downtime through predictive maintenance and quality inspection


By bringing intelligence to the edge, developers can create responsive, efficient, and secure systems that operate independently of constant internet access.

## Next steps

To build effective TinyML and Edge AI solutions, you’ll need both high-quality data and the right combination of software and hardware. In this Learning Path, you’ll train a model to recognize specific voice commands and use those commands to control LEDs on the Arduino Nano RP2040 Connect.

In the next steps, you’ll walk through each part of the process in detail.
