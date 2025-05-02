---
# User change
title: "Overview"

weight: 2

layout: "learningpathall"
---

## What is OpenCV in Computer Vision?
Open Source Computer Vision Library (OpenCV) is a framework for real-time computer vision, that you can use across different platforms, including mobile devices. Modern smartphones equipped with advanced cameras and powerful processors can efficiently handle complex computer vision tasks, and OpenCV is a go-to choice for developers. Its cross-platform compatibility allows the creation of versatile applications that work across multiple devices without extensive code modifications.

## What does OpenCV offer Android Developers?
For Android developers, OpenCV offers an SDK designed for integration with Android Studio, the primary development environment. The SDK simplifies the process of adding OpenCV libraries, managing dependencies, and configuring projects, enabling developers to easily incorporate vision capabilities into their applications.

## How does OpenCV Integrate with Android and Kotlin?
OpenCV integrates with Android development, leveraging Kotlin's concise syntax and Java's interoperability, to simplify implementation. You can use OpenCV's diverse set of functionalities, such as image and video capture, filtering, transformations, feature detection, object recognition, and machine learning integration, to build efficient and maintainable applications.

## How is Performance Optimized with HAL?
OpenCV is optimized for performance, utilizing native C++ code for efficient processing. This ensures optimized real-time performance, particularly on mobile devices where computational resources might be limited. 

A critical component in enabling these optimizations is the Hardware Acceleration Layer (HAL). HAL serves as an abstraction layer that enables hardware-specific acceleration by utilizing device-specific optimizations. This significantly boosts the performance of OpenCV functions on supported hardware, which reduces processing time and power consumption. HAL makes OpenCV adaptable to modern multi-core processors and GPU architectures, which are essential for computationally-intensive tasks, such as object detection and image recognition.

## What is KleidiCV?
KleidiCV is an Arm Kleidi Library, a suite of highly performant open-source Arm routines that leverages OpenCV's HAL for hardware acceleration. KleidiCV focuses on optimizing various OpenCV functions specifically for Arm processors, ensuring faster execution and lower power consumption. 

This integration is particularly beneficial for mobile and embedded systems where performance efficiency is critical. By utilizing HAL, KleidiCV allows developers to harness the full potential of Arm hardware, making it an ideal solution for applications requiring high-performance computer vision on Arm-based devices.

## A Performant Solution
By combining OpenCV's feature set, the hardware optimization from HAL, and specialized enhancements such as Arm's KleidiCV, developers can build efficient, high-performing computer vision solutions tailored for modern mobile and embedded systems.

In this Learning Path, you will learn how you can use KleidiCV-accelerated OpenCV in an Android application.

You can find all the code used in this Learning Path in a [GitHub repository](https://github.com/dawidborycki/Arm64.KleidiCV.Demo.git).
