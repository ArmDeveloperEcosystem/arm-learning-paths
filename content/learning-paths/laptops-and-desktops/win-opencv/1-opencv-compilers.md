---
title: OpenCV and Compilers for Windows on Arm
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## OpenCV
OpenCV (Open Source Computer Vision Library) is a popular, open-source library that developers use to build computer vision applications. It provides a set of tools and functions that help you handle tasks related to images and videos without needing to write everything from scratch. 

Here’s what developers should know:

* __Ease of Use__: OpenCV comes with pre-built functions for common tasks like reading, displaying, and processing images and videos. This saves time compared to writing algorithms from the ground up.

* __Image Processing__: You can perform operations like changing colors, applying filters, resizing, rotating, and other transformations to images with minimal code.

* __Video Handling__: Developers can use OpenCV to capture, modify, and analyze video frames, making it ideal for creating applications like video surveillance or video editing tools.

* __Computer Vision Algorithms__: OpenCV includes built-in algorithms for complex tasks like object detection (e.g., face and eye recognition), edge detection, and image segmentation.

* __Machine Learning__: It includes modules for training models using basic machine learning algorithms, which can be applied for pattern recognition and data analysis in visual data.

* __Community and Resources__: Being open-source and widely adopted, there is a large community of developers contributing to and supporting OpenCV. This makes it easier to find tutorials, documentation, and answers to questions.


## Compilers for Windows on Arm Development

When building applications for Windows on Arm, both MSVC (Microsoft Visual C++) and Clang are options for developers, each with its own advantages.

* __MSVC__: A compiler developed by Microsoft that’s part of the Visual Studio IDE. It’s designed specifically for Windows and integrates well with the Windows development ecosystem.

* __Clang__: An open-source compiler that is part of the LLVM project. It’s known for its modern design and cross-platform capabilities. 

MSVC is the go-to for Windows-focused projects needing seamless integration with Visual Studio. Clang is ideal for cross-platform projects or when using modern C++ features with flexibility. 

## Before you begin

Any Windows on Arm machine which has the required tools installed can be used for this Learning Path. You will learn the build methods using both MSVC and Clang. 

Please install the following tools required for both methods.

* [CMake](/install-guides/cmake)

{{% notice Note %}}
The instructions were tested with the version 3.28.1
{{% /notice %}}

* [Git](https://git-scm.com/downloads/win)

{{% notice Note %}}
There is currently no Arm version of Git. Install the 64-bit x86 version.
{{% /notice %}}

Follow the link to intall the required tools for a method using MSVC.

* [Visual Studio 2022 or higher](/install-guides/vs-woa). 

{{% notice Note %}}
The instructions were tested with Visual Studio 2022.
{{% /notice %}}

To build using Clang, please install the following.

* [LLVM](install-guides/llvm-woa/)

{{% notice Note %}}
The instructions were tested with the version 18.1.8.
{{% /notice %}}

* [Ninja]( https://github.com/ninja-build/ninja/releases)

{{% notice Note %}}
The instructions were tested with version 1.11.1
{{% /notice %}}

You use the LLVM Clang and the Ninja generator to build. Set PATH to the paths to your LLVM and Ninja install.

You now have the required development tools installed. Please proceed to the page for the compiler you want to build with.
