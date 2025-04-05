---
# User change
title: "Introduction, Background, and Installation"

weight: 2

layout: "learningpathall"
---

## Introduction
Halide is a powerful, open-source programming language specifically designed to simplify and optimize high-performance image and signal processing pipelines. Initially developed by researchers at MIT and Adobe in 2012, Halide addresses a critical challenge in computational imaging: efficiently mapping image-processing algorithms onto diverse hardware architectures without extensive manual tuning. It accomplishes this by clearly separating the description of an algorithm (defining what computations are performed) from its schedule (detailing how and where those computations execute). This design enables rapid experimentation and effective optimization for various processing platforms, including CPUs, GPUs, and mobile hardware.

A key advantage of Halide lies in its innovative programming model. By clearly distinguishing between algorithmic logic and scheduling decisions—such as parallelism, vectorization, memory management, and hardware-specific optimizations—developers can first focus on ensuring the correctness of their algorithms. Performance tuning can then be handled independently, significantly accelerating development cycles. This approach often yields performance that matches or even surpasses manually optimized code. As a result, Halide has seen widespread adoption across industry and academia, powering image processing systems at technology giants such as Google, Adobe, and Facebook, and enabling advanced computational photography features used by millions daily.

In this learning path, you will explore Halide’s foundational concepts, set up your development environment, and create your first functional Halide application. By the conclusion, you will understand what makes Halide uniquely suited to efficient image processing and be ready to build your own optimized pipelines.

## Key Concepts in Halide
### Separation of Algorithm and Schedule
At the core of Halide’s design philosophy is the principle of clearly separating algorithms from schedules. Traditional image-processing programming tightly couples algorithmic logic with execution strategy, complicating optimization and portability. In contrast, Halide explicitly distinguishes these two components:
* Algorithm. Defines what computations are performed—for example, image filters, pixel transformations, or other mathematical operations on image data.
* Schedule. Specifies how and where these computations are executed, addressing critical details such as parallel execution, memory usage, caching strategies, and hardware-specific optimizations.

This separation allows developers to rapidly experiment and optimize their code for different hardware architectures or performance requirements without altering the core algorithmic logic.

### Functions, Vars, and Pipelines
Halide introduces several essential concepts to simplify image-processing pipelines:
* Functions (Func). Represent discrete computational steps or operations applied across pixels in an image. By defining computations declaratively, functions simplify the description of complex image-processing algorithms.
* Variables (Var). Symbolize spatial coordinates or dimensions of the data (e.g., horizontal position x, vertical position y, and channel c). Vars serve as symbolic indices to define how computations apply across image data.
* Pipelines. Comprise interconnected Halide functions that collectively form a complete image-processing workflow. Pipelines clearly define data dependencies, facilitating structured and modular image-processing tasks.

### Scheduling Strategies (Parallelism, Vectorization, Tiling)
Halide offers several powerful scheduling strategies designed for maximum performance:
* Parallelism. Executes computations concurrently across multiple CPU cores, significantly reducing execution time for large datasets.
* Vectorization. Enables simultaneous processing of multiple data elements using SIMD (Single Instruction, Multiple Data) instructions available on CPUs and GPUs, greatly enhancing performance.
* Tiling. Divides computations into smaller blocks (tiles) optimized for cache efficiency, thus improving memory locality and reducing overhead due to memory transfers.

By combining these scheduling techniques, developers can achieve optimal performance tailored specifically to their target hardware architecture.

## System Requirements and Environment Setup
To start developing with Halide, your system must meet several requirements and dependencies.

### Installation Options
Halide can be set up using one of two main approaches:
* Installing pre-built binaries - pre-built binaries are convenient, quick to install, and suitable for beginners or standard platforms (Windows, Linux, macOS).
* Building from source - building Halide from source offers greater flexibility, allowing optimization for your specific hardware or operating system configuration.

Here, we’ll use pre-built binaries:
1. Visit the official Halide releases [page](https://github.com/halide/Halide/releases). As of this writing, the latest Halide version is v19.0.0.
2. Download and unzip the binaries to a convenient location (e.g., /usr/local/halide on Linux/macOS or C:\halide on Windows).
3. Optionally set environment variables to simplify further usage:
```console
export HALIDE_DIR=/path/to/halide
export PATH=$HALIDE_DIR/bin:$PATH
```

Halide depends on the following key software packages:
1. LLVM (required for efficient compilation and optimization): 
* Linux (Ubuntu):
```console
sudo apt-get install llvm-15-dev libclang-15-dev clang-15
```
* macOS (Homebrew):
```console
brew install llvm
```
2. OpenCV (for image handling in later lessons):
* Linux (Ubuntu):
```console
sudo apt-get install libopencv-dev pkg-config
```
* macOS (Homebrew)::
```console
brew install opencv pkg-config
```

## Your First Halide Program
Now you’re ready to build your first Halide-based application. Save the following as hello-world.cpp:
```cpp
#include "Halide.h"
#include <opencv2/opencv.hpp>
#include <iostream>

using namespace Halide;
using namespace cv;

int main() {
    // Static path for the input image.
    std::string imagePath = "img.png";

    // Load the input image using OpenCV (BGR by default).
    Mat input = imread(imagePath, IMREAD_COLOR);
    if (input.empty()) {
        std::cerr << "Error: Unable to load image from " << imagePath << std::endl;
        return -1;
    }
        
    // Convert from BGR to RGB (Halide expects RGB order).
    cvtColor(input, input, COLOR_BGR2RGB);

    // Wrap the OpenCV Mat data in a Halide::Buffer.
    // Dimensions: (width, height, channels)
    Buffer<uint8_t> inputBuffer(input.data, input.cols, input.rows, input.channels());

    // Create an ImageParam for symbolic indexing.
    ImageParam inputImage(UInt(8), 3);
    inputImage.set(inputBuffer);

    // Define a Halide pipeline that inverts the image.
    Var x("x"), y("y"), c("c");
    Func invert("invert");
    invert(x, y, c) = 255 - inputImage(x, y, c);

    // Schedule the pipeline so that the channel dimension is the innermost loop,
    // ensuring that the output is interleaved.
    invert.reorder(c, x, y);

    // Realize the output buffer with the same dimensions as the input.
    Buffer<uint8_t> outputBuffer = invert.realize({input.cols, input.rows, input.channels()});

    // Wrap the Halide output buffer directly into an OpenCV Mat header.
    // This does not copy data; it creates a header that refers to the same memory.
    Mat output(input.rows, input.cols, CV_8UC3, outputBuffer.data());

    // Convert RGB back to BGR for proper display in OpenCV.
    cvtColor(output, output, COLOR_RGB2BGR);

    // Display the input and processed image.
    imshow("Original Image", input);
    imshow("Inverted Image", output);
    waitKey(0); // Wait for a key press before closing the window.

    return 0;
}
```

This program demonstrates how to combine Halide’s image processing capabilities with OpenCV’s image I/O and display functionality. It begins by loading an image from disk using OpenCV, specifically reading from a static file named img.png (here we use a Cameraman image). Since OpenCV loads images in BGR format by default, the code immediately converts the image to RGB format so that it is compatible with Halide’s expectations.

Once the image is loaded and converted, the program wraps the raw image data into a Halide buffer, which captures the image’s dimensions (width, height, and the number of color channels). An ImageParam is then created, allowing the Halide pipeline to use symbolic indexing with variables. The core of the pipeline is defined by a function called invert, which computes a new pixel value by subtracting the original value from 255. This operation effectively inverts the image’s colors. The scheduling directive invert.reorder(c, x, y) ensures that the output buffer is stored in an interleaved manner—making it compatible with the memory layout expected by OpenCV.

After the pipeline processes the image, the output is realized into another Halide buffer. Instead of copying pixel data back and forth, the program directly wraps this buffer into an OpenCV Mat header. This efficient step avoids unnecessary data duplication. Finally, because OpenCV displays images in BGR format, the code converts the processed image back from RGB to BGR. The program then displays both the original and the inverted images in separate windows, waiting for a key press before exiting. This workflow showcases a streamlined integration between Halide for high-performance image processing and OpenCV for handling input and output operations.

## Compilation Instructions
Compile the program as follows (replace /path/to/halide accordingly):
```console
g++ -std=c++17 hello-world.cpp -o hello-world \
    -I/path/to/halide/include -L/path/to/halide/lib -lHalide \
    $(pkg-config --cflags --libs opencv4) -lpthread -ldl \
    -Wl,-rpath,/path/to/halide/lib
```

Run the executable:
```console
./hello-world
```

You will see two windows displaying the original and inverted images:
![img1](Figures/01.png)
![img2](Figures/02.png)

## Summary
In this lesson, you’ve learned Halide’s foundational concepts, explored the benefits of separating algorithms and schedules, set up your development environment, and created your first functional Halide application integrated with OpenCV. 

