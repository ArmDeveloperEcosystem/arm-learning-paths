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

The original scheduling directive used in our example

```cpp
blur.compute_at(thresholded, x);
```

instructs Halide to compute the blur function at each iteration of the innermost loop (over the horizontal coordinate x) of the thresholded function. However, as the reviewer correctly pointed out, scheduling at the innermost loop (x) in Halide often results in behavior similar to the default inline scheduling. Yet, explicitly using compute_at(thresholded, x) can introduce additional overhead, such as repeatedly accessing the same small memory region unnecessarily. This could cause redundant memory access because Halide might write intermediate results to a temporary buffer within this innermost loop.

To demonstrate more efficient fusion explicitly—while avoiding redundant intermediate storage—consider instead scheduling blur at an outer loop (e.g., the vertical coordinate y). Doing so significantly improves performance by:
* Reducing redundant computations and memory accesses.
* Explicitly fusing operations at a more cache-efficient granularity.

Here’s how you can update your scheduling:
```cpp
Halide::Var x("x"), y("y");

// Existing blur definition.
Halide::Func blur("blur");
Halide::Func thresholded("thresholded");

// Thresholding definition remains unchanged.
thresholded(x, y) = Halide::select(blur(x, y) > 128, 255, 0);

// Improved fusion: compute blur at each iteration of outer loop (y).
blur.compute_at(thresholded, y);

// Optionally, parallelize across the outer loop for improved multicore utilization.
thresholded.parallel(y);
```

In the improved code snippet:
* blur.compute_at(thresholded, y) explicitly instructs Halide to compute blurred rows just before thresholding each row. This means the intermediate blur results are stored temporarily in a small per-row buffer, significantly reducing redundant computations and repeated memory accesses.
* By choosing y (the vertical loop) instead of the innermost loop (x), we explicitly balance between complete inlining (which may recompute identical results many times) and storing intermediate results explicitly in memory. This strikes a more effective trade-off, avoiding redundant computations while maintaining good cache locality.
* The thresholded.parallel(y) directive parallelizes the computation across multiple rows, taking full advantage of multi-core CPUs to further accelerate processing.

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

This explicit loop-fusion example demonstrates additional optimizations achievable with Halide, clearly differentiating between operation fusion (compute_at) and loop fusion (fuse).

## When to use operation fusion
Operation fusion is especially beneficial for pipelines involving multiple sequential element-wise operations. These operations perform independent transformations on individual pixels without requiring neighboring data. Element-wise operations benefit greatly from fusion since they avoid the overhead associated with repeatedly storing and loading intermediate results, significantly reducing memory bandwidth usage.

Ideal use-cases for fusion are 
* Pixel intensity normalization (scaling and shifting)
* Color-space transformations (e.g., RGB to grayscale conversion)
* Simple arithmetic or logical operations applied pixel-by-pixel

Here’s an illustrative example:
```cpp
Halide::Var x("x"), y("y");
Halide::Func scale("scale"), offset("offset"), clamp_result("clamp_result");

// Element-wise transformations
scale(x, y) = input(x, y) * 1.5f;
offset(x, y) = scale(x, y) + 10.0f;
clamp_result(x, y) = Halide::clamp(offset(x, y), 0.0f, 255.0f);

// Apply fusion for maximum efficiency
scale.compute_at(clamp_result, x);
offset.compute_at(clamp_result, x);
```
In this scenario, fusion is highly effective, eliminating unnecessary intermediate storage and significantly improving performance.

However, fusion can introduce redundancy and inefficiencies when dealing with spatial operations such as blurs or convolutions, especially if:
* The intermediate results are used multiple times.
* The spatial filter has a large kernel (e.g., large Gaussian blur).
* There are multiple sequential layers of spatial filters (e.g., multiple convolution layers).

Consider a Gaussian blur with a large kernel (e.g., 15×15):
```cpp
Halide::Func large_blur("large_blur"), threshold("threshold");

// Large Gaussian blur
large_blur(x, y) = Halide::sum(input(x + r.x, y + r.y) * weight(r.x, r.y));

// Thresholding based on blurred result
threshold(x, y) = Halide::select(large_blur(x, y) > 128, 255, 0);
```

Using aggressive fusion here (large_blur.compute_at(threshold, x)) can result in significant computational redundancy, as each blurred value might be recomputed multiple times for overlapping pixels.

Instead, applying tiling or explicitly storing intermediate results can improve efficiency significantly:

```cpp
// Use tiling and intermediate storage to reduce redundant computation
Halide::Var x_outer, y_outer, x_inner, y_inner;
threshold.tile(x, y, x_outer, y_outer, x_inner, y_inner, 64, 64)
         .parallel(y_outer);
         
// Store blurred results per tile for reuse
large_blur.compute_at(threshold, x_outer);
```

Also, operation fusion is less beneficial (or even detrimental) if intermediate results are frequently reused across multiple subsequent stages or if fusing operations complicates parallelism or vectorization opportunities.

Operation fusion generally improves performance by reducing memory usage, eliminating intermediate storage, and enhancing cache locality. However, fusion may be less beneficial (or even detrimental) under certain circumstances:
* Repeated reuse of intermediate results. If the same intermediate computation is heavily reused across multiple subsequent stages, explicitly storing this intermediate result (using compute_root()) can be more efficient than recomputing it multiple times through fusion.
* Reduced parallelism or vectorization opportunities. Aggressive fusion can complicate or even restrict parallelization and vectorization opportunities, potentially hurting performance. In such scenarios, explicitly scheduling computations separately might yield better overall efficiency.

For example, consider a scenario where a computationally expensive intermediate result is reused multiple times:
```cpp
Halide::Var x("x"), y("y");
Halide::Func expensive_intermediate("expensive_intermediate");
Halide::Func stage1("stage1"), stage2("stage2"), final_stage("final_stage");

// Expensive intermediate computation
expensive_intermediate(x, y) = ...; 

// Multiple stages reusing the intermediate
stage1(x, y) = expensive_intermediate(x, y) + 1;
stage2(x, y) = expensive_intermediate(x, y) * 2;

// Final stage using results from previous stages
final_stage(x, y) = stage1(x, y) + stage2(x, y);
```

In this case, explicitly storing the intermediate computation at the root level is beneficial:
```cpp
expensive_intermediate.compute_root();
```

This prevents redundant recomputation, resulting in higher efficiency compared to aggressively fusing these stages. In short, fusion is particularly effective in pipelines where intermediate results are not heavily reused or where recomputation costs are minimal compared to memory overhead. Being aware of these considerations helps achieve optimal scheduling decisions tailored to your specific pipeline.

## Summary
In this lesson, we learned about operation fusion in Halide, a powerful technique to reduce memory bandwidth and improve computational efficiency. We explored why fusion matters, identified scenarios where fusion is most effective, and demonstrated how Halide’s scheduling constructs (compute_at, store_at, fuse) enable you to apply fusion easily and effectively. By fusing the Gaussian blur and thresholding stages, we improved the performance of our real-time image processing pipeline.