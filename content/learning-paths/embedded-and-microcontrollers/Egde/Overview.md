---
title:  Overview 
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Edge AI
Edge AI refers to artificial intelligence models that run directly on edge devices, processing data locally rather than relying on cloud computing. These models are optimized for real-time decision-making on resource-constrained devices, such as microcontrollers, embedded systems, and IoT sensors.

**TinyML (Tiny Machine Learning)** is a subset of Edge AI that focuses specifically on deploying machine learning models on ultra-low-power microcontrollers and resource-constrained devices. These microcontrollers typically have limited computational resources — often less than 1 MB of flash memory and only a few hundred kilobytes of RAM — and are designed to run on minimal power, sometimes for years on a single coin-cell battery. Despite these constraints, TinyML enables such devices to perform on-device inference, allowing them to make intelligent decisions in real time without needing to send data to the cloud. This opens the door for smart functionality in low-cost, battery-powered devices used in applications such as environmental monitoring, wearables, smart homes, industrial sensors, and more.

## Key Characteristics of Edge AI and TinyML

Key features of Edge AI and TinyML include;

- **Low Power Consumption**: Designed to run on batteries or harvested energy for months or years.

- **Small Model Size**: Models are optimized (e.g., quantized or pruned) to fit into a few kilobytes or megabytes.

- **Limited Compute & Memory** : Typically operates with <1MB RAM and very limited storage.

- **Real-Time Inference** : Enables immediate local decision-making (e.g., wake-word detection).

- **Low Latency** : No reliance on cloud – inference is performed on-device.

- **Applications** : Often used in audio classification, gesture detection, anomaly detection, etc.

- **Example Devices** : Arduino Nano 33 BLE Sense, STM32 MCUs, Raspberry Pi Pico, Arduino Nano RP2040 Connect, and more.

## Running AI Models on Resource-Constrained Devices

Running AI on edge devices presents several challenges. These devices often lack high-performance CPUs or GPUs, making computational power a limiting factor. Limited RAM and storage require careful memory management, and since many edge devices run on batteries, energy efficiency is a critical concern. To overcome these constraints, models are optimized through techniques such as quantization, pruning, and knowledge distillation, which reduce model size while maintaining accuracy.

## Edge AI Implementation Workflow

The process of implementing Edge AI begins with data collection using sensors, such as cameras, microphones, or motion detectors. This data is then used to train machine learning models on high-performance machines, such as cloud servers or workstations. Once trained, the models undergo optimization to reduce size and computational requirements before being deployed on microcontrollers or Arm-based microprocessors. Finally, inference takes place, where the model processes real-time data directly on the device to make decisions.

## Applications of Edge AI

Edge AI is used in a wide range of applications. In smart homes, voice assistants like Amazon Alexa rely on on-device speech recognition to process wake words. Security systems use AI-driven cameras to detect motion and identify anomalies, while energy management systems optimize power usage by analyzing real-time data from HVAC units.

Wearable devices also benefit from Edge AI. Smartwatches monitor health by detecting heart rate irregularities, and fitness trackers use AI-powered motion analysis to improve exercise tracking.

In industrial settings, predictive maintenance applications rely on IoT sensors to monitor vibrations and temperatures, helping prevent machinery failures. Smart agriculture systems use soil condition sensors to optimize irrigation and fertilization, while autonomous vehicles process sensor data for real-time navigation and obstacle detection.

## Importance of Edge AI

To understand the benefits of **Edge AI**, just **BLERP**, BLERP highlights the critical aspects of deploying machine learning models on edge devices, focusing on **Bandwidth, Latency, Economics, Reliability, and Privacy**. These components are key to understanding the advantages of processing data on-device rather than relying on the cloud. The table below provides an overview of each component and its importance in Edge AI applications "Situnayake, 2023"

| Area     | Description                                                                                                                                                         |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| B – Bandwidth          | Edge AI reduces the amount of data that needs to be sent to the cloud. This is critical when working with high-volume data like video or sensor streams. Processing locally helps avoid congestion and dependency on internet speed. |
| L – Latency            | Edge devices can make real-time decisions faster because they don't rely on cloud round trips. One of the significant benefits of Edge AI is low latency - processing occurs on-device without needing to send data to the cloud. This is crucial for applications requiring real-time decision-making, such as self-driving cars or medical monitoring devices. Additionally, Edge AI allows devices to function in offline environments, making it ideal for remote locations with limited connectivity. |
|  E – Economics          | Running models locally on low-power edge devices is often cheaper in the long run. It reduces cloud compute costs, data transmission costs, and energy consumption. |
|  R – Reliability        | Edge AI systems can continue functioning even with limited or no internet connection. This makes them more robust in remote areas, mission-critical applications, or offline settings. |
| P – Privacy            | Data can be processed locally without being transmitted to external servers, reducing the risk of data breaches and complying with privacy regulations like GDPR or HIPAA. |

## Why Learn Edge AI?

Edge AI is transforming multiple industries. In healthcare, AI-powered medical diagnostics assist in early disease detection, while remote patient monitoring improves access to care. In agriculture, AI-driven sensors optimize soil conditions and pest control, leading to higher yields and resource efficiency. The manufacturing sector benefits from predictive maintenance and quality inspection, reducing downtime and improving productivity.

## Next Steps

To build effective TinyML and Edge AI projects, one needs more than just data—**both software and hardware** play a critical role in the development process. While data forms the foundation for training machine learning models, the **software** enables data processing, model development, and deployment, and the **hardware** provides the physical platform for running these models at the edge.

In this learning path, we will build a model that recognize specific voice commands, which will be used to **control LEDs on the Arduino Nano RP2040 Connect**. In the following steps, both software and hardware components will be discussed in detail.

