---
# User change
title: "Demonstrating Operation Fusion"

weight: 4

layout: "learningpathall"
---

## Objective
In the previous section, we explored parallelization and tiling. Here, we focus specifically on loop fusion using Halide’s fuse directive. Loop fusion merges multiple loop indices into a single loop variable, enhancing cache locality and simplifying parallel execution.

## What is operation fusion?
Operation fusion (also known as operator fusion or kernel fusion) is a technique used in high-performance computing, especially in image and signal processing pipelines, where multiple computational steps (operations) are combined into a single processing stage. Instead of computing and storing intermediate results separately, fused operations perform calculations in one continuous pass, reducing redundant memory operations and improving efficiency.

## How fusion reduces memory bandwidth and scheduling overhead
Loop fusion combines two or more nested loops into a single loop. This technique is distinct from operation fusion (compute_at), which places the computation of one function inside another’s loop nest. While operation fusion reduces intermediate storage, loop fusion simplifies loop structure, improving cache performance and parallel efficiency.

Every individual stage in a processing pipeline typically reads input data, computes intermediate results, writes these results back to memory, and then the next stage again reads this intermediate data. This repeated read-write cycle introduces significant overhead, particularly in memory-intensive applications like image processing. Operation fusion reduces this overhead by:
1. Reducing memory accesses. Intermediate results stay in CPU registers or caches rather than being repeatedly written to and read from main memory.
2. Improving cache utilization. Data is accessed in a contiguous manner, improving CPU cache efficiency.
3. Reducing scheduling overhead. By executing multiple operations in a single pass, scheduling complexity and overhead are minimized.

## Loop fusion in practice
Let’s explicitly apply Halide’s loop fusion to our previously demonstrated Gaussian blur and threshold pipeline. Create a new file camera-capture-fusion.cpp, and paste there the following code:

```cpp
#include "Halide.h"
#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>
#include <cstdint>
#include <exception>

using namespace cv;
using namespace std;

static inline Halide::Expr clampCoord(Halide::Expr coord, int maxCoord) {
    return Halide::clamp(coord, 0, maxCoord - 1);
}

int main() {
    VideoCapture cap(0);
    if (!cap.isOpened()) {
        cerr << "Error: Unable to open camera." << endl;
        return -1;
    }

    while (true) {
        Mat frame;
        cap >> frame;
        if (frame.empty()) {
            cerr << "Error: Received empty frame." << endl;
            break;
        }

        Mat gray;
        cvtColor(frame, gray, COLOR_BGR2GRAY);
        if (!gray.isContinuous()) {
            gray = gray.clone();
        }

        int width  = gray.cols;
        int height = gray.rows;

        Halide::Buffer<uint8_t> inputBuffer(gray.data, width, height);
        Halide::ImageParam input(Halide::UInt(8), 2, "input");
        input.set(inputBuffer);

        int kernel_vals[3][3] = {
            {1, 2, 1},
            {2, 4, 2},
            {1, 2, 1}
        };
        Halide::Buffer<int> kernelBuf(&kernel_vals[0][0], 3, 3);

        Halide::Var x("x"), y("y"), xy("xy");
        Halide::RDom r(0, 3, 0, 3);

        Halide::Func blur("blur");
        Halide::Expr val = Halide::cast<int32_t>(
            input(clampCoord(x + r.x - 1, width),
                  clampCoord(y + r.y - 1, height))
        ) * kernelBuf(r.x, r.y);
        blur(x, y) = Halide::cast<uint8_t>(Halide::sum(val) / 16);

        Halide::Func thresholded("thresholded");
        thresholded(x, y) = Halide::cast<uint8_t>(Halide::select(blur(x, y) > 128, 255, 0));

        // Fuse
        thresholded.fuse(x, y, xy);
        blur.compute_at(thresholded, xy);

        Halide::Buffer<uint8_t> outputBuffer;
        try {
            outputBuffer = thresholded.realize({width, height}); // 2D output as usual
        } catch (const Halide::CompileError &e) {
            cerr << "Halide compile error: " << e.what() << endl;
            break;
        } catch (const std::exception &e) {
            cerr << "Halide pipeline error: " << e.what() << endl;
            break;
        }

        Mat blurredThresholded(height, width, CV_8UC1, outputBuffer.data());
        imshow("Processed Image (Fused)", blurredThresholded);

        if (waitKey(30) >= 0) {
            break;
        }
    }

    cap.release();
    destroyAllWindows();
    return 0;
}
```

The code presented here closely follows the structure from the previous examples, focusing on the Gaussian blur and thresholding pipeline implemented with Halide and OpenCV. In this particular instance, we introduce the explicit use of loop fusion using Halide’s fuse scheduling directive, complemented by operation fusion with compute_at, to showcase how both techniques can synergize to optimize performance further.

In addition to these scheduling optimizations, we’ve also enhanced the exception handling within our pipeline. Specifically, we’ve included a separate catch block to detect and report Halide compilation errors explicitly. This ensures that if there’s a mistake in pipeline definition or scheduling directives that prevent the Halide pipeline from compiling, it is promptly caught and reported with clear feedback, simplifying debugging and improving robustness.

The critical addition to this pipeline is the explicit loop fusion achieved with the following directive:
```cpp
thresholded.fuse(x, y, xy);
```

Here, the two spatial dimensions—horizontal (x) and vertical (y)—are combined into a single, linearized dimension named xy. Loop fusion significantly enhances memory access patterns by promoting data locality. This linearization of loop indices means pixels are accessed sequentially and contiguously, which aligns perfectly with how data is stored in memory. Consequently, cache efficiency is improved, as fewer cache misses occur, resulting in faster data processing. Additionally, fusing loops simplifies the task of parallelizing the computation, as there is now only one unified dimension to distribute across multiple processor cores, making it straightforward and effective.

Alongside loop fusion, we apply operation fusion (compute_at) as previously discussed. This is demonstrated with the line:
```cpp
blur.compute_at(thresholded, xy);
```

Here, the computation of the blurred image (blur) is performed directly within the newly fused loop (xy) of the thresholding operation (thresholded). By placing the blur computation immediately before thresholding, intermediate blurred values do not need to be stored extensively in memory. Instead, they’re calculated as needed and promptly consumed, effectively eliminating redundant intermediate storage and further reducing memory bandwidth requirements.

Combining these two powerful scheduling directives—loop fusion (fuse) and operation fusion (compute_at)—results in a highly optimized pipeline. The main benefits are:
* Enhanced cache locality. Loop fusion ensures contiguous memory access patterns, greatly reducing cache misses.
* Simplified parallelization. With a single fused loop (xy), the computational workload is easier to distribute evenly across CPU cores, maximizing parallel efficiency.
* Reduced loop overhead: Fewer loop iterations and simpler loop structures result in reduced computational overhead, further accelerating real-time processing tasks.

Together, these improvements are crucial for real-time image processing applications where high frame rates and low latency are required.

Though complementary, loop fusion (fuse) and operation fusion (compute_at) target slightly different aspects of pipeline optimization:
* Operation Fusion (compute_at). Focuses primarily on minimizing intermediate memory usage by integrating the computation of dependent operations into the loop structure of their consumers.
* Loop Fusion (fuse). Primarily targets enhancing memory access efficiency and simplifying parallelization by merging loop dimensions.

The explicit combined use of these techniques in the provided final code snippet represents a comprehensive optimization strategy, enabling Halide to deliver maximal real-time performance
Both techniques complement each other. The provided final code snippet demonstrates their combined usage explicitly, maximizing performance.

## When to use operation fusion
Operation fusion is especially beneficial for pipelines involving multiple sequential element-wise operations. These operations perform independent transformations on individual pixels without requiring neighboring data. Element-wise operations benefit greatly from fusion since they avoid the overhead associated with repeatedly storing and loading intermediate results, significantly reducing memory bandwidth usage.

Ideal use-cases for fusion are 
* Pixel intensity normalization (scaling and shifting)
* Color-space transformations (e.g., RGB to grayscale conversion)
* Simple arithmetic or logical operations applied pixel-by-pixel

However, fusion can introduce redundancy and inefficiencies when dealing with spatial operations such as blurs or convolutions, especially if:
* The intermediate results are used multiple times.
* The spatial filter has a large kernel (e.g., large Gaussian blur).
* There are multiple sequential layers of spatial filters (e.g., multiple convolution layers).

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

<!-- ## store_at
In addition to the previously discussed scheduling directives—compute_at (operation fusion) and fuse (loop fusion)—Halide offers another powerful optimization: store_at. While compute_at focuses on deciding where and when intermediate computations occur, store_at explicitly determines where intermediate results are stored in memory.

When using store_at, the computed intermediate results of a Func are explicitly stored at a specified loop level of another function. This is especially beneficial when you need intermediate results multiple times, but want to control their memory footprint precisely.

A directive compute_at decides at what loop nesting level the computation occurs. This typically minimizes intermediate storage by recomputing values as needed. Then, the store_at can be used to decide at what loop nesting level the intermediate results are stored. Useful when repeated computations are expensive, but memory should be tightly controlled.

Typical scenarios for store_at include:
* Expensive intermediate calculations. When intermediate computations are costly, recomputing them every time via compute_at becomes inefficient. Using store_at allows you to compute the results once per specified loop level and reuse them efficiently.
* Controlling memory footprint. Ideal when working with constrained hardware (such as embedded systems or mobile platforms). It explicitly stores data temporarily at chosen granularities, balancing memory usage and performance.

Consider the previous Gaussian blur and thresholding pipeline. Suppose we wish to explicitly store blurred intermediate results per tile to avoid redundant computation, while controlling memory usage tightly:

```cpp
// Variables representing spatial coordinates and tiling structure.
Halide::Var x("x"), y("y"), x_outer, y_outer, x_inner, y_inner;

// Define blur and thresholded functions.
Halide::Func blur("blur"), thresholded("thresholded");

// Gaussian blur computation remains unchanged.
blur(x, y) = Halide::cast<uint8_t>(Halide::sum(val) / 16);

// Thresholding stage.
thresholded(x, y) = Halide::select(blur(x, y) > 128, 255, 0);

// Apply tiling schedule.
thresholded.tile(x, y, x_outer, y_outer, x_inner, y_inner, 64, 64)
           .parallel(y_outer);

// Explicitly store blurred results per tile using store_at.
blur.compute_at(thresholded, x_outer)
    .store_at(thresholded, x_outer);
```

In the above example blur.compute_at(thresholded, x_outer) computes the blurred values within each tile at the outer tile loop. The computation occurs at the tile granularity, reducing redundant computations within each tile. Then, store_at(thresholded, x_outer) explicitly stores the intermediate blurred results once per tile iteration (x_outer). This ensures that the blurred values remain available for reuse within each tile without recomputation, significantly reducing redundant computations.

Benefits of using store_at include:
* Efficient memory usage. Results are stored explicitly at chosen loop granularities, thus balancing recomputation and memory consumption.
* Reduction of redundant computations. Especially beneficial when intermediate computations are resource-intensive.
* Improved cache locality By explicitly controlling storage locations at specific loop iterations, memory accesses become more predictable and efficient.

When to use store_at:
* When intermediate results are used multiple times within a loop iteration and recomputing them each time is computationally expensive.
* When working within tight memory constraints, allowing precise control over intermediate result storage.

While compute_at and fuse directly address computation scheduling and loop structure optimizations, store_at specifically targets memory optimization. Together, these scheduling primitives offer comprehensive control, allowing Halide developers to finely tune their image-processing pipelines for maximum efficiency, balancing computational workload, memory usage, and performance constraints. -->

### Profiling
To profile a pipeline you can use built-in profiler. For details on how to enable and interpret Halide’s profiler, please refer to the official [Halide profiling tutorial](https://halide-lang.org/tutorials/tutorial_lesson_21_auto_scheduler_generate.html#profiling).

## Summary
In this lesson, we learned about operation fusion in Halide, a powerful technique to reduce memory bandwidth and improve computational efficiency. We explored why fusion matters, identified scenarios where fusion is most effective, and demonstrated how Halide’s scheduling constructs (compute_at, store_at, fuse) enable you to apply fusion easily and effectively. By fusing the Gaussian blur and thresholding stages, we improved the performance of our real-time image processing pipeline.