---
# User change
title: "Building a Simple Camera Image Processing Workflow"

weight: 3

layout: "learningpathall"
---

## Objective
In this section, you will build a real-time camera processing pipeline using Halide. First, you capture video frames from a webcam using OpenCV, then implement a Gaussian (binomial) blur to smooth the captured images, followed by thresholding to create a clear binary output highlighting prominent image features. After establishing this pipeline, you will measure performance and then explore Halide's  scheduling options—parallelization and tiling—to understand when they help and when they don’t.

## Gaussian blur and thresholding
Create a new `camera-capture.cpp` file and modify it as follows:
```cpp
#include "Halide.h"
#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>
#include <cstdint>
#include <exception>

using namespace Halide;
using namespace cv;
using namespace std;

int main() {
    // Open the default camera.
    VideoCapture cap(0);
    if (!cap.isOpened()) {
        cerr << "Error: Unable to open camera.\n";
        return -1;
    }

    // Grab one frame to determine dimensions and channels
    Mat frame;
    cap >> frame;
    if (frame.empty()) {
        cerr << "Error: empty first frame.\n";
        return -1;
    }

    // Ensure BGR 3-channel layout
    if (frame.channels() == 4)
        cvtColor(frame, frame, COLOR_BGRA2BGR);
    else if (frame.channels() == 1)
        cvtColor(frame, frame, COLOR_GRAY2BGR);
    if (!frame.isContinuous())
        frame = frame.clone();

    const int width  = frame.cols;
    const int height = frame.rows;
    const int ch     = frame.channels();

    // Input
    ImageParam input(UInt(8), 3, "input");
    input.dim(0).set_stride(ch);  // interleaved: x stride = channels
    input.dim(2).set_stride(1);
    input.dim(2).set_bounds(0, 3);

    // Clamp borders 
    Func inputClamped = BoundaryConditions::repeat_edge(input);

    // Grayscale conversion (Rec.601 weights)
    Var x("x"), y("y");
    Func gray("gray");
    gray(x, y) = cast<uint8_t>(0.114f * inputClamped(x, y, 0) +
                               0.587f * inputClamped(x, y, 1) +
                               0.299f * inputClamped(x, y, 2));

    // 3×3 binomial blur 
    Func blur("blur");
    const uint16_t k[3][3] = {{1,2,1},{2,4,2},{1,2,1}};
    Expr sum = cast<uint16_t>(0);
    for (int j = 0; j < 3; ++j)
        for (int i = 0; i < 3; ++i)
            sum += cast<uint16_t>(gray(x + i - 1, y + j - 1)) * k[j][i];
    blur(x, y) = cast<uint8_t>(sum / 16);

    // Threshold fused with blur 
    Func output("output");
    Expr T = cast<uint8_t>(128);
    output(x, y) = select(blur(x, y) > T, cast<uint8_t>(255), cast<uint8_t>(0));
    
    // Allocate output buffer once
    Buffer<uint8_t> outBuf(width, height);

    // JIT compile once outside the loop
    Pipeline pipe(output);
    pipe.compile_jit();

    namedWindow("Processing Workflow", WINDOW_NORMAL);

    while (true) {
        cap >> frame;
        if (frame.empty()) break;
        if (frame.channels() == 4)
            cvtColor(frame, frame, COLOR_BGRA2BGR);
        else if (frame.channels() == 1)
            cvtColor(frame, frame, COLOR_GRAY2BGR);
        if (!frame.isContinuous())
            frame = frame.clone();

        // Use Halide::Buffer::make_interleaved directly
        Buffer<uint8_t> inputBuf =
            Buffer<uint8_t>::make_interleaved(frame.data, frame.cols, frame.rows, frame.channels());

        input.set(inputBuf);

        try {
            pipe.realize(outBuf);
        } catch (const Halide::RuntimeError& e) {
            cerr << "Halide runtime error: " << e.what() << "\n";
            break;
        } catch (const std::exception& e) {
            cerr << "std::exception: " << e.what() << "\n";
            break;
        }

        // Display
        Mat view(height, width, CV_8UC1, outBuf.data());
        imshow("Processing Workflow", view);
        if (waitKey(1) >= 0) break;
    }

    destroyAllWindows();
    return 0;
}
```

The camera delivers interleaved BGR frames. Inside Halide, we convert to grayscale (Rec.601), apply a 3×3 binomial blur (sum/16 with 16-bit accumulation), then threshold to produce a binary image. We compile once (outside the capture loop) and realize per frame for real-time processing.

A 3×3 filter needs neighbors (x±1, y±1). At the image edges, some taps would fall outside the valid region. Rather than scattering manual clamps across expressions, we wrap the input once:

```cpp
// Wrap the input so out-of-bounds reads replicate the nearest edge pixel.
Func inputClamped = BoundaryConditions::repeat_edge(input);
```

Any out-of-bounds access replicates the nearest edge pixel. This makes the boundary policy obvious, keeps expressions clean, and ensures all downstream stages behave consistently at the edges.

Grayscale conversion happens inside Halide using Rec.601 weights. We read B, G, R from the interleaved input and compute luminance:

```cpp
// Grayscale (Rec.601)
Var x("x"), y("y");
Func gray("gray");
gray(x, y) = cast<uint8_t>(0.114f * inputClamped(x, y, 0) +    // B
                           0.587f * inputClamped(x, y, 1) +    // G
                           0.299f * inputClamped(x, y, 2));    // R
```

Next, the pipeline applies a Gaussian-approximate (binomial) blur using a fixed 3×3 kernel. For this learning path, we implement it with small loops and 16-bit accumulation for safety:

```cpp
Func blur("blur");
const uint16_t k[3][3] = {{1,2,1},{2,4,2},{1,2,1}};  // sum = 16
Expr sum = cast<uint16_t>(0);
for (int j = 0; j < 3; ++j)
    for (int i = 0; i < 3; ++i)
        sum += cast<uint16_t>(gray(x + i - 1, y + j - 1)) * k[j][i];
blur(x, y) = cast<uint8_t>(sum / 16);
```

Why this kernel?
* It provides effective smoothing while remaining computationally lightweight.
* The weights approximate a Gaussian distribution, which reduces noise but preserves edges better than a box filter.
* This is mathematically a binomial filter, a standard and efficient approximation of Gaussian blurring.

After the blur, the pipeline applies thresholding to produce a binary image. We explicitly cast constants to uint8_t to remove ambiguity and avoid redundant widen/narrow operations in generated code:

```cpp
Func output("output");
    Expr T = cast<uint8_t>(128);
    output(x, y) = select(blur(x, y) > T, cast<uint8_t>(255), cast<uint8_t>(0));
```

This simple but effective step emphasizes strong edges and regions of high contrast, often used as a building block in segmentation and feature extraction pipelines

Finally, the result is realized by Halide and displayed via OpenCV. The pipeline is built once (outside the capture loop) and then realized each frame:
```cpp
// Build the pipeline once (outside the capture loop)
Buffer<uint8_t> outBuf(width, height);
Pipeline pipe(output);
pipe.compile_jit();

// Per frame
pipe.realize(outBuf);
Mat view(height, width, CV_8UC1, outBuf.data());
imshow("Processing Workflow", view);
```

The main loop continues capturing frames, running the Halide pipeline, and displaying the processed output in real time until a key is pressed. This illustrates how Halide integrates cleanly with OpenCV to build efficient, interactive image-processing applications.

## Compilation instructions
Compile the program as follows (replace /path/to/halide accordingly):
```console
g++ -std=c++17 camera-capture.cpp -o camera-capture \
    -I/path/to/halide/include -L/path/to/halide/lib -lHalide \
    $(pkg-config --cflags --libs opencv4) -lpthread -ldl \
    -Wl,-rpath,/path/to/halide/lib
```

Run the executable:
```console
./camera-capture
```

The output should look as in the figure below:
![img3](Figures/03.png)

## Parallelization and Tiling
In this section, you will explore two complementary scheduling optimizations provided by Halide: Parallelization and Tiling. Both techniques help enhance performance but achieve it through different mechanisms—parallelization leverages multiple CPU cores, whereas tiling improves cache efficiency by optimizing data locality.

Now you will learn how to use each technique separately for clarity and to emphasize their distinct benefits. 

Let’s first lock in a measurable baseline before we start changing the schedule. You will create a second file, `camera-capture-perf-measurement.cpp`, that runs the same grayscale → blur → threshold pipeline but prints per-frame timing, FPS, and MPix/s around the Halide realize() call. This lets you quantify each optimization you will add next (parallelization, tiling, caching).

Create `camera-capture-perf-measurement.cpp` with the following code:
```cpp
#include "Halide.h"
#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>
#include <cstdint>
#include <exception>
#include <chrono>
#include <iomanip>

using namespace Halide;
using namespace cv;
using namespace std;

int main() {
    // Open the default camera.
    VideoCapture cap(0);
    if (!cap.isOpened()) {
        cerr << "Error: Unable to open camera.\n";
        return -1;
    }

    // Grab one frame to determine dimensions and channels
    Mat frame;
    cap >> frame;
    if (frame.empty()) {
        cerr << "Error: empty first frame.\n";
        return -1;
    }

    // Ensure BGR 3-channel layout
    if (frame.channels() == 4)      cvtColor(frame, frame, COLOR_BGRA2BGR);
    else if (frame.channels() == 1) cvtColor(frame, frame, COLOR_GRAY2BGR);
    if (!frame.isContinuous())      frame = frame.clone();

    const int width  = frame.cols;
    const int height = frame.rows;
    const int ch     = frame.channels();   

    // Build the pipeline once (outside the capture loop)
    ImageParam input(UInt(8), 3, "input");
    input.dim(0).set_stride(ch);  // interleaved: x stride = channels
    input.dim(2).set_stride(1);
    input.dim(2).set_bounds(0, 3);

    // Clamp borders
    Func inputClamped = BoundaryConditions::repeat_edge(input);

    // Grayscale conversion (Rec.601 weights)
    Var x("x"), y("y");
    Func gray("gray");
    gray(x, y) = cast<uint8_t>(0.114f * inputClamped(x, y, 0) +
                               0.587f * inputClamped(x, y, 1) +
                               0.299f * inputClamped(x, y, 2));

    // 3×3 binomial blur
    Func blur("blur");
    const uint16_t k[3][3] = {{1,2,1},{2,4,2},{1,2,1}};
    Expr sum = cast<uint16_t>(0);
    for (int j = 0; j < 3; ++j)
        for (int i = 0; i < 3; ++i)
            sum += cast<uint16_t>(gray(x + i - 1, y + j - 1)) * k[j][i];
    blur(x, y) = cast<uint8_t>(sum / 16);

    // Threshold (binary)
    Func output("output");
    Expr T = cast<uint8_t>(128);
    output(x, y) = select(blur(x, y) > T, cast<uint8_t>(255), cast<uint8_t>(0));

    // Baseline schedule: materialize gray; fuse blur+threshold into output
    gray.compute_root();

    // Allocate output buffer once & JIT once
    Buffer<uint8_t> outBuf(width, height);
    Pipeline pipe(output);
    pipe.compile_jit();

    namedWindow("Processing Workflow", WINDOW_NORMAL);

    bool warmed_up = false;
    for (;;) {
        cap >> frame;
        if (frame.empty()) break;
        if (frame.channels() == 4)      cvtColor(frame, frame, COLOR_BGRA2BGR);
        else if (frame.channels() == 1) cvtColor(frame, frame, COLOR_GRAY2BGR);
        if (!frame.isContinuous())      frame = frame.clone();

        // Use Halide::Buffer::make_interleaved directly
        Buffer<uint8_t> inputBuf =
            Buffer<uint8_t>::make_interleaved(frame.data, frame.cols, frame.rows, frame.channels());
        input.set(inputBuf);

        // Performance timing strictly around realize()
        auto t0 = chrono::high_resolution_clock::now();
        pipe.realize(outBuf);
        auto t1 = chrono::high_resolution_clock::now();

        double ms = chrono::duration<double, milli>(t1 - t0).count();
        double fps = ms > 0.0 ? 1000.0 / ms : 0.0;
        double mpixps = ms > 0.0 ? (double(width) * double(height)) / (ms * 1000.0) : 0.0;

        cout << fixed << setprecision(2)
             << (warmed_up ? "" : "[warm-up] ")
             << "realize: " << ms << " ms  |  "
             << fps << " FPS  |  "
             << mpixps << " MPix/s\r" << flush;
        warmed_up = true;

        // Display
        Mat view(height, width, CV_8UC1, outBuf.data());
        imshow("Processing Workflow", view);
        if (waitKey(1) >= 0) break;
    }

    cout << "\n";
    destroyAllWindows();
    return 0;
}
```
 
* The console prints ms, FPS, and MPix/s per frame, measured strictly around realize() (camera capture and UI are excluded).
* The first frame is labeled [warm-up] because it includes Halide's JIT compilation. You can ignore it when comparing schedules.
* MPix/s = (width*height)/seconds is a good resolution-agnostic metric to compare schedule variants.

Build and run the application. Here is the sample output:

```console
% ./camera-capture-perf-measurement 
realize: 4.84 ms  |  206.53 FPS  |  428.25 MPix/s
```

This gives an FPS of 206.53, and average throughput of 428.25 MPix/s. Now you can start measuring potential improvements from scheduling.

### Parallelization
Parallelization lets Halide run independent pieces of work at the same time on multiple CPU cores. In image pipelines, rows (or row tiles) are naturally parallel once producer data is available. By distributing work across cores, we reduce wall-clock time—crucial for real-time video.

With the baseline measured, apply a minimal schedule that parallelizes the blur reduction across rows while keeping the final stage explicit at root. This avoids tricky interactions between a parallel consumer and an unscheduled reduction.

Add these lines after defining output(x, y) (and before any realize()):
```cpp
blur.compute_root().parallel(y);   // parallelize reduction across scanlines
output.compute_root();             // cheap pixel-wise stage at root
```

This does two important things:
* compute_root() on blur moves the reduction to the top level, so it isn’t nested under a parallel loop that might complicate reduction ordering.
* parallel(y) parallelizes over the pure loop variable y (rows), not the reduction domain r, which is the safe/idiomatic way to parallelize reductions in Halide.

Now rebuild and run the application again. The results should look like:
```output
% ./camera-capture-perf-measurement
realize: 3.80 ms  |  263.07 FPS  |  545.49 MPix/s
```

That’s ≈20% faster than baseline.

### Tiling
Tiling is a scheduling technique that divides computations into smaller, cache-friendly blocks or tiles. This approach significantly enhances data locality, reduces memory bandwidth usage, and leverages CPU caches more efficiently. While tiling can also use parallel execution, its primary advantage comes from optimizing intermediate data storage.

Tiling splits the image into cache-friendly blocks (tiles). Two wins:
* Partitioning: tiles are easy to parallelize across cores.
* Locality: when you cache intermediates per tile, you avoid refetching/recomputing data and hit L1/L2 more often.

Now lets look at both flavors.

### Tiling with explicit intermediate storage (best for cache efficiency)
Here you will cache gray once per tile so the 3×3 blur can reuse it instead of recomputing RGB -> gray up to 9× per output pixel.

Before using this, remove any earlier compute_root().parallel(y) schedule for blur.

```cpp
// After defining: input, gray, blur, thresholded
Halide::Var xo("xo"), yo("yo"), xi("xi"), yi("yi");

// Tile & parallelize the consumer; vectorize inner x on planar output.
output
    .tile(x, y, xo, yo, xi, yi, 128, 64)
    .vectorize(xi, 16)
    .parallel(yo);

// Compute blur inside each tile and vectorize its inner x.
blur
    .compute_at(output, xo)
    .vectorize(x, 16);

// Cache RGB→gray per tile (reads interleaved input → keep unvectorized).
gray
    .compute_at(output, xo)
    .store_at(output, xo);
```

In this scheduling:
* tile(...) splits the image into cache-friendly blocks and makes it easy to parallelize across tiles.
* blur.compute_at(thresholded, xo) localizes the blur computation to each tile (it doesn’t force storing blur; it just computes it where it’s needed, keeping the working set small).
* gray.compute_at(...).store_at(...) materializes a tile-local planar buffer for the grayscale intermediate so blur can reuse it within the tile.
* Vectorization is applied only to planar stages (blur, thresholded), gray stays unvectorized because it reads interleaved input (x-stride = channels).

Recompile your application as before, then run. What we observed on our machine:
```output
realize: 2.36 ms  |  423.10 FPS  |  877.34 MPix/s
```

This was the fastest variant here—caching a planar grayscale per tile enabled efficient reuse and vectorized blur reads.

### Tiling for parallelization (without explicit intermediate storage)
Tiling can also be used just to partition work across cores, without caching intermediates. This keeps the schedule simple: you split the output into tiles, parallelize across tiles, and vectorize along unit-stride x. Producers are computed inside each tile to keep the working set small, but don’t materialize extra tile-local buffers:
```cpp
// Tiling (partitioning only)
Halide::Var xo("xo"), yo("yo"), xi("xi"), yi("yi");

output
    .tile(x, y, xo, yo, xi, yi, 128, 64)  // try 128x64; tune per CPU
    .vectorize(xi, 16)                    // safe: planar, unit-stride along x
    .parallel(yo);                        // run tiles across cores

blur
    .compute_at(output, xo)               // keep work tile-local
    .vectorize(x, 16);                    // vectorize planar blur
```

What this does
* tile(...) splits the image into cache-friendly blocks and makes parallelization straightforward.
* parallel(yo) distributes tiles across CPU cores.
* compute_at(thresholded, xo) evaluates blur per tile (better locality) without forcing extra storage.
* Vectorization is applied to planar stages (blur, thresholded).

Recompile your application as before, then run. On our test machine, we got 5.56 ms (179.91 FPS, 373.07 MPix/s). This is slower than both the baseline and the parallelization-only schedule. The main reasons:
* Recomputation of gray: with a 3×3 blur, each output reuses up to 9 neighbors; leaving gray inlined means RGB→gray is recomputed for each tap.
* Interleaved input: gray reads BGR interleaved data (x-stride = channels), limiting unit-stride vectorization efficiency upstream.
* Overhead vs. work: a 3×3 blur has low arithmetic intensity; extra tile/task overhead isn’t amortized.

Tiling without caching intermediates mainly helps partition work, but for tiny kernels on CPU (and interleaved sources) it often underperforms. The earlier “quick win” (blur.compute_root().parallel(y)) remains the better choice here.

### Tiling vs. parallelization
* Parallelization spreads independent work across CPU cores. For this pipeline, the safest/most effective quick win was:
```cpp
blur.compute_root().parallel(y);
thresholded.compute_root();
```
* Tiling for cache efficiency helps when an expensive intermediate is reused many times per output (e.g., larger kernels, separable/multi-stage pipelines, multiple consumers) and when producers read planar data. Caching gray per tile with a tiny 3×3 kernel over an interleaved source added overhead and ran slower.
* Tiling for parallelization (partitioning only) simplifies work distribution and enables vectorization of planar stages, but with low arithmetic intensity (3×3) and an interleaved source it underperformed here.

When to choose what:
* Start with parallelizing the main reduction at root.
* Add tiling + caching only if: kernel ≥ 5×5, separable/multi-pass blur, or the intermediate is reused by multiple consumers—and preferably after converting sources to planar (or precomputing a planar gray).
* Keep stages that read interleaved inputs unvectorized; vectorize only planar consumers.

## Summary
In this section, you built a real-time Halide+OpenCV pipeline—grayscale, a 3×3 binomial blur, then thresholding—and instrumented it to measure throughput. The baseline landed at 4.84 ms (206.53 FPS, 428.25 MPix/s). A small, safe schedule tweak that parallelizes the blur reduction across rows improved performance to 3.80 ms (263.07 FPS, 545.49 MPix/s)—about +20%. A tiling schedule used only for partitioning was slower at 5.56 ms (179.91 FPS, 373.07 MPix/s). In contrast, tiling with a cached per-tile grayscale (so the blur reuses a planar intermediate) was the fastest at 2.36 ms (423.10 FPS, 877.34 MPix/s).

The pattern is clear. On CPU, with a small kernel and an interleaved camera source, the most reliable first step is to parallelize the main reduction across rows. Tiling pays off when you also cache a reused intermediate (e.g., a planar grayscale) so downstream stages get unit-stride, vectorizable access and better locality. Keep stages that read interleaved inputs unvectorized; vectorize planar consumers. From there, tune tile sizes and thread count for your target. Boundary conditions are handled once with repeat_edge, keeping edge behavior consistent and scheduling clean.

