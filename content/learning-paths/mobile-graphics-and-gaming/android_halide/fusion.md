---
# User change
title: "Demonstrating Operation Fusion"

weight: 4

layout: "learningpathall"
---

## Objective
In this section, you’ll learn about operation fusion, a powerful performance optimization technique offered by Halide. We’ll explore how combining multiple processing stages into a single fused operation reduces memory usage, decreases scheduling overhead, and significantly enhances performance. You’ll see when and why to apply operation fusion, analyze the performance of a baseline pipeline, identify bottlenecks, and then leverage Halide’s scheduling constructs like compute_at, store_at, and fuse to optimize and accelerate your image-processing applications.

## What is operation fusion?
Operation fusion (also known as operator fusion or kernel fusion) is a technique used in high-performance computing, especially in image and signal processing pipelines, where multiple computational steps (operations) are combined into a single processing stage. Instead of computing and storing intermediate results separately, fused operations perform calculations in one continuous pass, reducing redundant memory operations and improving efficiency.

## How fusion reduces memory bandwidth and scheduling overhead
Every individual stage in a processing pipeline typically reads input data, computes intermediate results, writes these results back to memory, and then the next stage again reads this intermediate data. This repeated read-write cycle introduces significant overhead, particularly in memory-intensive applications like image processing. Operation fusion dramatically reduces this overhead by:
1. Reducing memory accesses. Intermediate results stay in CPU registers or caches rather than being repeatedly written to and read from main memory.
2. Improving cache utilization. Data is accessed in a contiguous manner, improving CPU cache efficiency.
3. Reducing scheduling overhead. By executing multiple operations in a single pass, scheduling complexity and overhead are minimized.

## When to use operation fusion
Operation fusion is most beneficial in scenarios that involve multiple sequential operations or transformations performed on large datasets, particularly when these intermediate results are large or costly to recompute. Typical situations include:
* Image filtering pipelines (blur, sharpen, threshold sequences)
* Color transformations followed by thresholding or other pixel-wise operations
* Complex signal processing operations involving repeated data transformations

Operation fusion is less beneficial (or even detrimental) if intermediate results are frequently reused across multiple subsequent stages or if fusing operations complicates parallelism or vectorization opportunities.

## Typical scenarios and performance-critical pipelines
Some performance-critical pipelines where fusion is especially beneficial include:
* Real-time video processing (e.g., streaming transformations)
* Computational photography applications (HDR blending, tone mapping)
* Computer vision tasks (feature extraction followed by thresholding)

## Baseline pipeline analysis
To demonstrate the benefit of operation fusion, we’ll revisit the Gaussian blur and threshold pipeline from the previous lesson and then apply fusion.

### Review of the non-fused pipeline
Recall the pipeline we created previously:
1. Gaussian Blur. Smoothes the image using a convolution kernel.
2. Thresholding. Converts the blurred image to a binary image based on pixel intensities.

In the non-fused version, these stages are separately realized, meaning intermediate blurred results are computed and stored in memory before thresholding.

```cpp
Halide::Func blur("blur");
// blur definition here
Halide::Buffer<uint8_t> blurBuffer = blur.realize({ width, height });

Halide::Func thresholded("thresholded");
thresholded(x, y) = Halide::cast<uint8_t>(Halide::select(blurBuffer(x, y) > 128, 255, 0));

Halide::Buffer<uint8_t> outputBuffer = thresholded.realize({ width, height });
```

### Performance profiling to identify bottlenecks
The primary bottleneck in the non-fused pipeline is memory access:
1. Intermediate results (blurBuffer) are written to and read from memory.
2. This results in additional latency, reduced cache efficiency, and unnecessary memory bandwidth usage.

Profiling this pipeline with tools like Halide’s built-in profiler typically shows memory bandwidth as a major limiting factor. 
For details on how to enable and interpret Halide’s profiler, please refer to the official [Halide profiling tutorial](https://halide-lang.org/tutorials/tutorial_lesson_21_auto_scheduler_generate.html#profiling).

## Applying operation fusion in Halide
To apply operation fusion, Halide provides powerful scheduling constructs that allow you to precisely control when and where operations are computed and stored.

### Scheduling techniques
The three primary Halide scheduling methods to enable fusion are:
1. compute_at - compute the values of one Func at the iteration point of another.
2. store_at - store intermediate results at a particular loop iteration or stage to minimize memory footprint.
3. fuse - merge loop variables of two dimensions into one, improving loop efficiency.

### Using constructs like compute_at, store_at, and fuse
Let’s fuse the blur and thresholding stages using compute_at to ensure both operations execute together, eliminating intermediate storage. To do so, create a new file camera-capture-fusion.cpp, and modify it as follows:

```cpp
#include "Halide.h"
#include <opencv2/opencv.hpp>
#include <iostream>
#include <exception>

using namespace cv;
using namespace std;

// This function clamps the coordinate (coord) within [0, maxCoord - 1].
static inline Halide::Expr clampCoord(Halide::Expr coord, int maxCoord) {
    return Halide::clamp(coord, 0, maxCoord - 1);
}

int main() {
    // Open the default camera with OpenCV.
    VideoCapture cap(0);
    if (!cap.isOpened()) {
        cerr << "Error: Unable to open camera." << endl;
        return -1;
    }

    while (true) {
        // Capture a frame from the camera.
        Mat frame;
        cap >> frame;
        if (frame.empty()) {
            cerr << "Error: Received empty frame." << endl;
            break;
        }

        // Convert the frame to grayscale.
        Mat gray;
        cvtColor(frame, gray, COLOR_BGR2GRAY);

        // Ensure the grayscale image is continuous in memory.
        if (!gray.isContinuous()) {
            gray = gray.clone();
        }

        int width  = gray.cols;
        int height = gray.rows;

        // Create a simple 2D Halide buffer from the grayscale Mat.
        Halide::Buffer<uint8_t> inputBuffer(gray.data, width, height);

        // Create a Halide ImageParam for a 2D UInt(8) image.
        Halide::ImageParam input(Halide::UInt(8), 2, "input");
        input.set(inputBuffer);

        // Define variables for x (width) and y (height).
        Halide::Var x("x"), y("y");

        // Define a function that applies a 3x3 Gaussian blur.
        Halide::Func blur("blur");
        Halide::RDom r(0, 3, 0, 3);

        // Kernel layout: [1 2 1; 2 4 2; 1 2 1], sum = 16.
        Halide::Expr weight = Halide::select(
            (r.x == 1 && r.y == 1), 4,
            (r.x == 1 || r.y == 1), 2,
            1
        );

        Halide::Expr offsetX = x + (r.x - 1);
        Halide::Expr offsetY = y + (r.y - 1);

        // Manually clamp offsets to avoid out-of-bounds.
        Halide::Expr clampedX = clampCoord(offsetX, width);
        Halide::Expr clampedY = clampCoord(offsetY, height);

        // Accumulate weighted sum in 32-bit int before normalization.
        Halide::Expr val = Halide::cast<int>(input(clampedX, clampedY)) * weight;

        blur(x, y) = Halide::cast<uint8_t>(Halide::sum(val) / 16);

        // Add a thresholding stage on top of the blurred result.
        // If blur(x,y) > 128 => 255, else 0
        Halide::Func thresholded("thresholded");
        thresholded(x, y) = Halide::cast<uint8_t>(
            Halide::select(blur(x, y) > 128, 255, 0)
        );

        // Apply fusion scheduling
        blur.compute_at(thresholded, x);
        thresholded.parallel(y);        

        // Realize the thresholded function. Wrap in try-catch for error reporting.
        Halide::Buffer<uint8_t> outputBuffer;
        try {
            outputBuffer = thresholded.realize({ width, height });
        } catch (const std::exception &e) {
            cerr << "Halide pipeline error: " << e.what() << endl;
            break;
        }

        // Wrap the Halide output in an OpenCV Mat and display.
        Mat blurredThresholded(height, width, CV_8UC1, outputBuffer.data());

        imshow("Processed image", blurredThresholded);

        // Exit the loop if a key is pressed.
        if (waitKey(30) >= 0) {
            break;
        }
    }

    cap.release();
    destroyAllWindows();
    return 0;
}
```

We modified the code to use blur.compute_at(thresholded, x). This scheduling instructs Halide to compute the blur function at each iteration of the thresholded function’s inner loop (x). Thus, the blurred value is computed immediately before thresholding, eliminating any intermediate buffer storage.

Calling realize() twice separately—first for the intermediate (blur) stage and again for the final (thresholded) stage—would indeed create a less efficient implementation. Such an approach explicitly stores and retrieves intermediate results, unnecessarily increasing memory usage. To clearly illustrate this inefficient baseline in Halide examples, developers typically apply the compute_root() directive to intermediate functions, explicitly storing intermediate results into memory. By contrast, using compute_at() ensures intermediate stages are computed directly at their point of use, fusing them into a single stage and effectively eliminating redundant memory accesses.

The directive thresholded.parallel(y) further enhances efficiency by parallelizing the outer loop across multiple CPU cores, thus accelerating execution.

The presented code demonstrates operation fusion, combining computational stages via compute_at. Halide also offers a separate optimization technique called loop fusion (via the fuse scheduling directive), which specifically merges two loop indices into a single loop variable. While the use of compute_at sufficiently addresses memory and computational efficiency concerns, explicit loop fusion can be used for additional optimization, especially to enhance cache locality or simplify parallelization.

Below is a snippet explicitly demonstrating how the fuse directive can be applied in the context of the existing pipeline:

```cpp
// Existing definitions
Halide::Var x("x"), y("y");

// Gaussian blur definition remains as before.
Halide::Func blur("blur");
Halide::RDom r(0, 3, 0, 3);
Halide::Expr weight = Halide::select(
    (r.x == 1 && r.y == 1), 4,
    (r.x == 1 || r.y == 1), 2,
    1
);

Halide::Expr offsetX = clampCoord(x + (r.x - 1), width);
Halide::Expr offsetY = clampCoord(y + (r.y - 1), height);
Halide::Expr val = Halide::cast<int32_t>(input(offsetX, offsetY)) * weight;
blur(x, y) = Halide::cast<uint8_t>(Halide::sum(val) / 16);

// Thresholding definition
Halide::Func thresholded("thresholded");
thresholded(x, y) = Halide::select(blur(x, y) > 128, 255, 0);

// ---- Explicit use of loop fusion (fuse) ----
Halide::Var xy("xy");  // New fused loop variable.

// Fuse x and y dimensions into one linearized dimension (xy).
thresholded.fuse(x, y, xy);

// Parallelize the fused loop for improved performance.
thresholded.parallel(xy);

// Compute blur within thresholded, ensuring operation fusion.
blur.compute_at(thresholded, xy);
```

This explicit loop-fusion example demonstrates additional optimizations achievable with Halide, clearly differentiating between operation fusion (compute_at) and loop fusion (fuse)

## Summary
In this lesson, we learned about operation fusion in Halide, a powerful technique to reduce memory bandwidth and improve computational efficiency. We explored why fusion matters, identified scenarios where fusion is most effective, and demonstrated how Halide’s scheduling constructs (compute_at, store_at, fuse) enable you to apply fusion easily and effectively. By fusing the Gaussian blur and thresholding stages, we improved the performance of our real-time image processing pipeline.