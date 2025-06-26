---
# User change
title: "Background and Installation"

weight: 2

layout: "learningpathall"
---

## Introduction
Halide is a powerful, open-source programming language specifically designed to simplify and optimize high-performance image and signal processing pipelines. Initially developed by researchers at MIT and Adobe in 2012, Halide addresses a critical challenge in computational imaging: efficiently mapping image-processing algorithms onto diverse hardware architectures without extensive manual tuning. It accomplishes this by clearly separating the description of an algorithm (specifying the mathematical or logical transformations applied to images or signals) from its schedule (detailing how and where those computations execute). This design enables rapid experimentation and effective optimization for various processing platforms, including CPUs, GPUs, and mobile hardware.

A key advantage of Halide lies in its innovative programming model. By clearly distinguishing between algorithmic logic and scheduling decisions—such as parallelism, vectorization, memory management, and hardware-specific optimizations—developers can first focus on ensuring the correctness of their algorithms. Performance tuning can then be handled independently, significantly accelerating development cycles. This approach often yields performance that matches or even surpasses manually optimized code. As a result, Halide has seen widespread adoption across industry and academia, powering image processing systems at technology giants such as Google, Adobe, and Facebook, and enabling advanced computational photography features used by millions daily.

In this learning path, you will explore Halide’s foundational concepts, set up your development environment, and create your first functional Halide application. By the end, you will understand what makes Halide uniquely suited to efficient image processing and be ready to build your own optimized pipelines.

The example code for this Learning Path is available in the following repositories: [here](https://github.com/dawidborycki/Arm.Halide.Hello-World.git) and [here](https://github.com/dawidborycki/Arm.Halide.AndroidDemo.git)

## Key concepts in Halide
### Separation of algorithm and schedule
At the core of Halide’s design philosophy is the principle of clearly separating algorithms from schedules. Traditional image-processing programming tightly couples algorithmic logic with execution strategy, complicating optimization and portability. In contrast, Halide explicitly distinguishes these two components:
* Algorithm. Defines what computations are performed—for example, image filters, pixel transformations, or other mathematical operations on image data.
* Schedule. Specifies how and where these computations are executed, addressing critical details such as parallel execution, memory usage, caching strategies, and hardware-specific optimizations.

This separation allows developers to rapidly experiment and optimize their code for different hardware architectures or performance requirements without altering the core algorithmic logic.

### Functions, vars, and pipelines
Halide introduces several essential concepts to simplify image-processing pipelines:
* Functions (Func). Represent discrete computational steps or operations applied across pixels in an image. By defining computations declaratively, functions simplify the description of complex image-processing algorithms.
* Variables (Var). Symbolize spatial coordinates or dimensions of the data (e.g., horizontal position x, vertical position y, and channel c). Vars serve as symbolic indices to define how computations apply across image data.
* Pipelines. Comprise interconnected Halide functions that collectively form a complete image-processing workflow. Pipelines clearly define data dependencies, facilitating structured and modular image-processing tasks.

Beyond manual scheduling strategies, Halide also provides an Autoscheduler, a powerful tool that automatically generates optimized schedules tailored to specific hardware architectures, further simplifying performance optimization.

### Scheduling strategies (parallelism, vectorization, tiling)
Halide offers several powerful scheduling strategies designed for maximum performance:
* Parallelism. Executes computations concurrently across multiple CPU cores, significantly reducing execution time for large datasets.
* Vectorization. Enables simultaneous processing of multiple data elements using SIMD (Single Instruction, Multiple Data) instructions available on CPUs and GPUs, greatly enhancing performance.
* Tiling. Divides computations into smaller blocks (tiles) optimized for cache efficiency, thus improving memory locality and reducing overhead due to memory transfers.

By combining these scheduling techniques, developers can achieve optimal performance tailored specifically to their target hardware architecture.

## System requirements and environment setup
To start developing with Halide, your system must meet several requirements and dependencies.

### Installation options
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
sudo apt-get install llvm-19-dev libclang-19-dev clang-19
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
* macOS (Homebrew):
```console
brew install opencv pkg-config
```

Halide examples were tested with OpenCV 4.11.0

## Your first Halide program
Now you’re ready to build your first Halide-based application. Save the following as hello-world.cpp:
```cpp
#include "Halide.h"
#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>
#include <cstdint>

using namespace Halide;
using namespace cv;

int main() {
    // Static path for the input image.
    std::string imagePath = "img.png";

    // Load the input image using OpenCV (BGR by default).
    Mat input = imread(imagePath, IMREAD_COLOR);
    // Alternative: Halide has a built-in IO function to directly load images as Halide::Buffer.
    // Example: Halide::Buffer<uint8_t> inputBuffer = Halide::Tools::load_image(imagePath);
    if (input.empty()) {
        std::cerr << "Error: Unable to load image from " << imagePath << std::endl;
        return -1;
    }
            
    // Convert RGB back to BGR for correct color display in OpenCV (optional but recommended for OpenCV visualization).
    cvtColor(input, input, COLOR_BGR2RGB);

    // Wrap the OpenCV Mat data in a Halide::Buffer.
    Buffer<uint8_t> inputBuffer(input.data, input.cols, input.rows, input.channels());

    // Example Halide pipeline definition directly using inputBuffer
    // Define Halide pipeline variables:
    // x, y - spatial coordinates (width, height)
    // c    - channel coordinate (R, G, B)
    Var x("x"), y("y"), c("c");
    Func inverted("inverted");
    inverted(x, y, c) = 255 - inputBuffer(x, y, c);

    // Schedule the pipeline so that the channel dimension is the innermost loop,
    // ensuring that the output is interleaved.
    invert.reorder(c, x, y);

    // Realize the output buffer with the same dimensions as the input.
    Buffer<uint8_t> outputBuffer = invert.realize({input.cols, input.rows, input.channels()});

    // Wrap the Halide output buffer directly into an OpenCV Mat header.
    // CV_8UC3 indicates an 8-bit unsigned integer image (CV_8U) with 3 color channels (C3), typically representing RGB or BGR images.
    // This does not copy data; it creates a header that refers to the same memory.
    Mat output(input.rows, input.cols, CV_8UC3, outputBuffer.data());

    // Convert from BGR to RGB for consistency (optional, but recommended if your pipeline expects RGB).
    cvtColor(output, output, COLOR_RGB2BGR);

    // Display the input and processed image.
    imshow("Original Image", input);
    imshow("Inverted Image", output);

    // Wait indefinitely until a key is pressed.
    waitKey(0); // Wait for a key press before closing the window.

    return 0;
}
```

This program demonstrates how to combine Halide’s image processing capabilities with OpenCV’s image I/O and display functionality. It begins by loading an image from disk using OpenCV, specifically reading from a static file named img.png (here we use a Cameraman image). Since OpenCV loads images in BGR format by default, the code immediately converts the image to RGB format so that it is compatible with Halide’s expectations.

Once the image is loaded and converted, the program wraps the raw image data into a Halide buffer, capturing the image’s dimensions (width, height, and color channels). Next, the Halide pipeline is defined through a function named invert, which specifies the computations to perform on each pixel—in this case, subtracting the original pixel value from 255 to invert the colors. The pipeline definition alone does not perform any actual computation; it only describes what computations should occur and how to schedule them.

The actual computation occurs when the pipeline is executed with the call to invert.realize(...). This is the step that processes the input image according to the defined pipeline and produces an output Halide buffer. The scheduling directive (invert.reorder(c, x, y)) ensures that pixel data is computed in an interleaved manner (channel-by-channel per pixel), aligning the resulting data with OpenCV’s expected memory layout for images.

Finally, the processed Halide output buffer is efficiently wrapped in an OpenCV Mat header without copying pixel data. For proper display in OpenCV, which uses BGR channel ordering by default, the code converts the processed image back from RGB to BGR. The program then displays the original and inverted images in separate windows, waiting for a key press before exiting. This approach demonstrates a streamlined integration between Halide for high-performance image processing and OpenCV for convenient input and output operations.

By default, Halide orders loops based on the order of the variables declared. In this case, the original ordering would be (x, y, c). This default ordering means that Halide processes images channel-by-channel (all reds, then all greens, then all blues), which is called planar layout.

However, most common image-processing libraries (such as OpenCV) expect image data in an interleaved layout (RGBRGBRGB...). To match this memory layout, it’s beneficial to reorder loops such that the color channel loop (c) becomes the innermost loop.

Specifically, calling:
```cpp
invert.reorder(c, x, y);
```

changes the loop nesting to process each pixel’s channels together (R, G, B for the first pixel, then R, G, B for the second pixel, and so on), resulting in:
* Better memory locality and cache performance when interfacing with interleaved libraries like OpenCV.
* Reduced overhead for subsequent image-handling operations (display, saving, or further processing).

## Compilation instructions
Compile the program as follows (replace /path/to/halide accordingly):
```console
export DYLD_LIBRARY_PATH=/path/to/halide/lib/libHalide.19.dylib
g++ -std=c++17 hello-world.cpp -o hello-world \
    -I/path/to/halide/include -L/path/to/halide/lib -lHalide \
    $(pkg-config --cflags --libs opencv4) -lpthread -ldl \
    -Wl,-rpath,/path/to/halide/lib
```

Note that, on Linux, you would set LD_LIBRARY_PATH instead:
```console
export LD_LIBRARY_PATH=/path/to/halide/lib/
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

