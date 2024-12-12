---
title: OpenCV and Compilers for Windows on Arm
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is OpenCV?

Open Source Computer Vision Library (OpenCV) is a popular, Open Source library that developers can use to build computer vision applications. It provides a set of tools and functions that can help you with tasks around images and videos. 

Here are some of the benefits of using OpenCV:

* __Ease of Use__: OpenCV comes with pre-built functions for common tasks like reading, displaying, and processing images and videos. This saves time compared to the requirement to cover absolutely every detail when writing an algorithm.

* __Image Processing__: You can perform operations like changing colors, applying filters, resizing, rotating, and other transformations to images with minimal code.

* __Video Handling__: Developers can use OpenCV to capture, modify, and analyze video frames, making it ideal for creating applications like video surveillance or video editing tools.

* __Computer Vision Algorithms__: OpenCV includes built-in algorithms for complex tasks like object detection (e.g., face and eye recognition), edge detection, and image segmentation.

* __Machine Learning__: It includes modules for training models using basic machine learning algorithms, which can be applied for pattern recognition and data analysis in visual data.

* __Community and Resources__: Being open-source and widely adopted, there is a large community of developers contributing to and supporting OpenCV. This makes it easier to find tutorials, documentation, and answers to questions.


## Which compilers are available for Windows on Arm Development?

MSVC (Microsoft Visual C++) and Clang are options for developers building Windows on Arm applications.

* __MSVC__: A compiler developed by Microsoft that’s part of the Visual Studio IDE. It’s designed specifically for Windows and integrates well with the Windows development ecosystem.

* __Clang__: An open-source compiler that is part of the LLVM project. It’s known for its modern design and cross-platform capabilities. 

MSVC is ideal for Windows-focused projects needing seamless integration with Visual Studio. Clang is ideal for cross-platform projects or when using modern C++ features.

## Before you begin

Any Windows on Arm machine which has the required tools installed can be used for this Learning Path. You will learn how to build OpenCV using both MSVC and Clang. 

Please install the following tools required for both methods.

* [CMake](/install-guides/cmake)

{{% notice Note %}}
The instructions were tested with the version 3.28.1
{{% /notice %}}

* [Git](https://git-scm.com/downloads/win)

{{% notice Note %}}
There is currently no Arm version of Git. Install the 64-bit x86 version.
{{% /notice %}}

Follow the link to install the required tools for a method using MSVC.

* [Visual Studio 2022 or higher](/install-guides/vs-woa). 

{{% notice Note %}}
The instructions were tested with Visual Studio 2022.
{{% /notice %}}

To build using Clang, please install the following.

* [LLVM](/install-guides/llvm-woa/)

{{% notice Note %}}
The instructions were tested with the version 18.1.8.
{{% /notice %}}

* [Ninja]( https://github.com/ninja-build/ninja/releases)

{{% notice Note %}}
The instructions were tested with version 1.11.1
{{% /notice %}}

Make sure LLVM Clang and Ninja are in your search path. If they are not, you can use Windows Control Panel to set the PATH environment variable.

You now have the required development tools installed. Please proceed to the page for the compiler you want to build with.
