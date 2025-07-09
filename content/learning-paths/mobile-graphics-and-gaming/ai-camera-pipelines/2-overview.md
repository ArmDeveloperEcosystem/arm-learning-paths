---

title: Overview
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall

---

## KleidiAI

[KleidiAI](https://gitlab.arm.com/kleidi/kleidiai) is an open-source library that provides optimized, performance-critical routines - also known as micro-kernels - for artificial intelligence (AI) workloads on Arm CPUs.

These routines are tuned to take full advantage of specific Arm hardware architectures to maximize performance. The [KleidiAI](https://gitlab.arm.com/kleidi/kleidiai) library is designed for easy integration into C or C++ machine learning (ML) and AI frameworks. 

Several popular AI frameworks already take advantage of [KleidiAI](https://gitlab.arm.com/kleidi/kleidiai) to improve performance on Arm platforms.

## KleidiCV

[KleidiCV](https://gitlab.arm.com/kleidi/kleidicv) is an open-source library that provides high-performance image processing functions for AArch64. 

It is designed to be lightweight and simple to integrate into a wide variety of projects. Some computer vision frameworks, such as OpenCV, leverage [KleidiCV](https://gitlab.arm.com/kleidi/kleidicv) to accelerate image processing on Arm devices.

## AI camera pipelines

This Learning Path provides two example applications that combine AI and computer vision (CV) techniques:
- Background Blur.
- Low-Light Enhancement.

Both applications:
- Use input and output images that are stored in `ppm` (Portable Pixmap format), with three RGB channels (Red, Green, and Blue). Each channel supports 256 intensity levels (0-255) commonly referred to as `RGB8`.
- Convert the images to the `YUV420` color space for processing.
- Apply the relevant effect (background blur or low-light enhancement).
- Convert the processed images back to `RGB8` and save them as `ppm` files.

### Background Blur

The background blur pipeline is implemented as follows:

![example image alt-text#center](blur_pipeline.png "Background Blur Pipeline Diagram")

### Low Light Enhancement

The low-light enhancement pipeline is adapted from the LiveHDR+ method originally proposed by Google Research in 2017:

![example image alt-text#center](lle_pipeline.png "Low-Light Enhancement Pipeline Diagram")

The Low-Resolution Coefficient Prediction Network (implemented with LiteRT) performs computations such as:
- Strided convolutions.
- Local feature extraction using convolutional layers.
- Global feature extraction using convolutional and fully connected layers.
- Add, convolve, and reshape operations.