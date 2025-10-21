---
# User change
title: "Demonstrating Operation Fusion"

weight: 4

layout: "learningpathall"
---

## Objective
In the previous section, you explored parallelization and tiling. Here, you will focus on operator fusion (inlining) in Halide i.e., letting producers be computed directly inside their consumers—versus materializing intermediates with compute_root() or compute_at(). You will learn when fusion reduces memory traffic and when materializing saves recomputation (e.g., for large stencils or multi-use intermediates). You will inspect loop nests with print_loop_nest(), switch among schedules (fuse-all, fuse-blur-only, materialize, tile-and-materialize-per-tile) in a live camera pipeline, and measure the impact (ms/FPS/MPix/s).

This section does not cover loop fusion (the fuse directive). You will focus on operator fusion, which is Halide’s default behavior.

## Code
To demonstrate how fusion in Halide works create a new file `camera-capture-fusion.cpp`, and modify it as follows. This code uses a live camera pipeline (BGR → gray → 3×3 blur → threshold), adds a few schedule variants to toggle operator fusion vs. materialization, and print ms / FPS / MPix/s. So you can see the impact immediately.

```cpp
#include "Halide.h"
#include <opencv2/opencv.hpp>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <string>
#include <cstdint>
#include <exception>

using namespace Halide;
using namespace cv;
using namespace std;

enum class Schedule : int {
    Simple = 0,              // materialize gray + blur
    FuseBlurAndThreshold = 1,// materialize gray; fuse blur+threshold
    FuseAll = 2,             // fuse everything (default)
    Tile = 3,                // tile output; materialize gray per tile; blur fused
};

static const char* schedule_name(Schedule s) {
    switch (s) {
        case Schedule::Simple:               return "Simple";
        case Schedule::FuseBlurAndThreshold: return "FuseBlurAndThreshold";
        case Schedule::FuseAll:              return "FuseAll";
        case Schedule::Tile:                 return "Tile";
        default:                             return "Unknown";
    }
}

// Build the BGR->Gray -> 3x3 binomial blur -> threshold pipeline.
// We clamp the *ImageParam* at the borders (Func clamp of ImageParam works in Halide 19).
Pipeline make_pipeline(ImageParam& input, Schedule schedule) {
    Var x("x"), y("y");

    // Assume 3-channel BGR interleaved frames (we convert if needed).
    input.dim(0).set_stride(3);      // x-stride = channels
    input.dim(2).set_stride(1);      // c-stride = 1
    input.dim(2).set_bounds(0, 3);   // three channels

    Func inputClamped = BoundaryConditions::repeat_edge(input);

    // Gray (Rec.601)
    Func gray("gray");
    gray(x, y) = cast<uint8_t>(0.114f * inputClamped(x, y, 0)
                             + 0.587f * inputClamped(x, y, 1)
                             + 0.299f * inputClamped(x, y, 2));

    // 3x3 binomial blur (sum/16)
    Func blur("blur");
    const uint16_t k[3][3] = {{1,2,1},{2,4,2},{1,2,1}};
    Expr blurSum = cast<uint16_t>(0);
    for (int j = 0; j < 3; ++j)
        for (int i = 0; i < 3; ++i)
            blurSum = blurSum + cast<uint16_t>(gray(x + i - 1, y + j - 1)) * k[j][i];
    blur(x, y) = cast<uint8_t>(blurSum / 16);

    // Threshold (binary)
    Func thresholded("thresholded");
    Expr T = cast<uint8_t>(128);
    thresholded(x, y) = select(blur(x, y) > T, cast<uint8_t>(255), cast<uint8_t>(0));

    // Final output
    Func output("output");
    output(x, y) = thresholded(x, y);
    output.compute_root(); // we always realize 'output'

    // Scheduling to demonstrate OPERATOR FUSION vs MATERIALIZATION
    // Default in Halide = fusion/inlining (no schedule on producers).
    Var xo("xo"), yo("yo"), xi("xi"), yi("yi");

    switch (schedule) {
        case Schedule::Simple:
            // Materialize gray and blur (two loop nests); thresholded fuses into output
            gray.compute_root();
            blur.compute_root();
            break;

        case Schedule::FuseBlurAndThreshold:
            // Materialize gray; blur and thresholded remain fused into output
            gray.compute_root();
            break;

        case Schedule::FuseAll:
            // No schedule on producers: gray, blur, thresholded all fuse into output
            break;

        case Schedule::Tile:
            // Tile the output; compute gray per tile; blur stays fused within tile
            output.tile(x, y, xo, yo, xi, yi, 64, 64);
            gray.compute_at(output, xo);
            break;
    }

    // (Optional) Print loop nest once to “x-ray” the schedule
    std::cout << "\n---- Loop structure (" << schedule_name(schedule) << ") ----\n";
    output.print_loop_nest();
    std::cout << "-----------------------------------------------\n";

    return Pipeline(output);
}

int main(int argc, char** argv) {
    // Optional CLI: start with a given schedule number 0..3
    Schedule current = Schedule::FuseAll;
    if (argc >= 2) {
        int s = std::atoi(argv[1]);
        if (s >= 0 && s <= 3) current = static_cast<Schedule>(s);
    }
    std::cout << "Starting with schedule: " << schedule_name(current)
              << " (press 0..3 to switch; q/Esc to quit)\n";

    // Open camera
    VideoCapture cap(0);
    if (!cap.isOpened()) {
        std::cerr << "Error: Unable to open camera.\n";
        return 1;
    }
    cap.set(CAP_PROP_CONVERT_RGB, true); // ask OpenCV for BGR frames

    // Grab one frame to get size/channels
    Mat frame;
    cap >> frame;
    if (frame.empty()) {
        std::cerr << "Error: empty first frame.\n";
        return 1;
    }
    if (frame.channels() == 4) {
        cvtColor(frame, frame, COLOR_BGRA2BGR);
    } else if (frame.channels() == 1) {
        cvtColor(frame, frame, COLOR_GRAY2BGR);
    }
    if (!frame.isContinuous()) frame = frame.clone();

    const int width  = frame.cols;
    const int height = frame.rows;

    // Halide inputs/outputs
    ImageParam input(UInt(8), 3, "input");
    Buffer<uint8_t, 2> outBuf(width, height, "out");

    // Build pipeline for the starting schedule
    Pipeline pipe = make_pipeline(input, current);

    bool warmed_up = false;
    namedWindow("Fusion Demo (live)", WINDOW_NORMAL);

    for (;;) {
        cap >> frame;
        if (frame.empty()) break;
        if (frame.channels() == 4) {
            cvtColor(frame, frame, COLOR_BGRA2BGR);
        } else if (frame.channels() == 1) {
            cvtColor(frame, frame, COLOR_GRAY2BGR);
        }
        if (!frame.isContinuous()) frame = frame.clone();

        // Wrap interleaved frame
        Halide::Buffer<uint8_t> inputBuf = Runtime::Buffer<uint8_t>::make_interleaved(
            frame.data, frame.cols, frame.rows, frame.channels());
        
        input.set(inputBuf);

        // Time the Halide realize() only
        auto t0 = std::chrono::high_resolution_clock::now();
        try {
            pipe.realize(outBuf);
        } catch (const Halide::RuntimeError& e) {
            std::cerr << "Halide runtime error: " << e.what() << "\n";
            break;
        } catch (const std::exception& e) {
            std::cerr << "std::exception: " << e.what() << "\n";
            break;
        }
        auto t1 = std::chrono::high_resolution_clock::now();

        double ms = std::chrono::duration<double, std::milli>(t1 - t0).count();
        double fps = ms > 0.0 ? 1000.0 / ms : 0.0;
        double mpixps = ms > 0.0 ? (double(width) * double(height)) / (ms * 1000.0) : 0.0;

        std::cout << std::fixed << std::setprecision(2)
                  << (warmed_up ? "" : "[warm-up] ")
                  << schedule_name(current) << " | "
                  << ms << " ms  |  "
                  << fps << " FPS  |  "
                  << mpixps << " MPix/s\r" << std::flush;
        warmed_up = true;

        // Show result
        Mat view(height, width, CV_8UC1, outBuf.data());
        imshow("Fusion Demo (live)", view);
        int key = waitKey(1);
        if (key == 27 || key == 'q' || key == 'Q') break;

        // Hotkeys 0..3 to switch schedules live
        if (key >= '0' && key <= '3') {
            Schedule next = static_cast<Schedule>(key - '0');
            if (next != current) {
                std::cout << "\nSwitching to schedule: " << schedule_name(next) << "\n";
                current = next;
                try {
                    pipe = make_pipeline(input, current); // rebuild JIT with new schedule
                } catch (const Halide::CompileError& e) {
                    std::cerr << "Halide compile error: " << e.what() << "\n";
                    break;
                }
                warmed_up = false; // next frame includes JIT, label as warm-up
            }
        }
    }

    std::cout << "\n";
    destroyAllWindows();
    return 0;
}
```

The main part of this program is the `make_pipeline` function. It defines the camera processing pipeline in Halide and applies different scheduling choices depending on which mode we select.

You start by declaring Var x, y as our pixel coordinates. Similarly as before, the camera frames come in as 3-channel interleaved BGR, you will tell Halide how the data is laid out: the stride along x is 3 (one step moves across all three channels), the stride along c (channels) is 1, and the bounds on the channel dimension are 0–2.

Because you don’t want to worry about array bounds when applying filters, you will clamp the input at the borders. In Halide 19, BoundaryConditions::repeat_edge works cleanly when applied to an ImageParam, since it has .dim() information. This way, all downstream stages can assume safe access even at the edges of the image.

```cpp
Pipeline make_pipeline(ImageParam& input, Schedule schedule) {
    Var x("x"), y("y");

    // (a) Interleaved constraints for BGR frames
    input.dim(0).set_stride(3);      // x stride = channels
    input.dim(2).set_stride(1);      // channel stride = 1
    input.dim(2).set_bounds(0, 3);   // channels = 0..2

    // (b) Border handling: clamp the *ImageParam* (works cleanly in Halide 19)
    Func inputClamped = BoundaryConditions::repeat_edge(input);
```

Next comes the gray conversion. As in previous section, you will use Rec.601 weights a 3×3 binomial blur. Instead of using a reduction domain (RDom), you unroll the sum in C++ host code with a pair of loops over the kernel. The kernel values {1, 2, 1; 2, 4, 2; 1, 2, 1} approximate a Gaussian filter. Each pixel of blur is simply the weighted sum of its 3×3 neighborhood, divided by 16.

You will then add a threshold stage. Pixels above 128 become white, and all others black, producing a binary image. Finally, define an output Func that wraps the thresholded result and call compute_root() on it so that it will be realized explicitly when you run the pipeline.

Now comes the interesting part: the scheduling choices. Depending on the Schedule enum passed in, you instruct Halide to either fuse everything (the default), materialize some intermediates, or even tile the output.
  * Simple: Here you will explicitly compute and store both gray and blur across the whole frame with compute_root(). This makes them easy to reuse or parallelize, but requires extra memory traffic.
  * FuseBlurAndThreshold: You compute gray once as a planar buffer, but leave blur and thresholded fused into output. This often works well when the input is interleaved, because subsequent stages read from a planar gray.
  * FuseAll: You will apply no scheduling to producers, so gray, blur, and thresholded are all inlined into output. This minimizes memory usage but can recompute gray many times inside the 3×3 stencil.
  * Tile: You will split the output into 64×64 tiles. Within each tile, we materialize gray (compute_at(output, xo)), so the working set is small and stays in cache. blur remains fused within each tile.

To help you examine what’s happening, print the loop nest Halide generates for each schedule using print_loop_nest(). This will give you a clear view of how fusion or materialization changes the structure of the computation.

```cpp
Var xo("xo"), yo("yo"), xi("xi"), yi("yi");

switch (schedule) {
    case Schedule::Simple:
        // Materialize gray and blur as whole-frame buffers.
        gray.compute_root();
        blur.compute_root();
        break;

    case Schedule::FuseBlurAndThreshold:
        // Materialize only gray; leave blur+threshold fused into output.
        gray.compute_root();
        break;

    case Schedule::FuseAll:
        // No schedules on producers → gray, blur, thresholded all inline into output.
        break;

    case Schedule::Tile:
        // Tile the output; compute gray per tile; blur stays fused inside each tile.
        output.tile(x, y, xo, yo, xi, yi, 64, 64);
        gray.compute_at(output, xo);
        break;
}

// Optional: print loop nest to “x-ray” the shape of the generated loops
std::cout << "\n---- Loop structure (" << schedule_name(schedule) << ") ----\n";
output.print_loop_nest();
std::cout << "-----------------------------------------------\n";

return Pipeline(output);
}
```

All the camera handling is just like before: you open the default webcam with OpenCV, normalize frames to 3-channel BGR if needed, wrap each frame as an interleaved Halide buffer, run the pipeline, and show the result. You will still time only the realize() call and print ms / FPS / MPix/s, with the first frame marked as [warm-up].

The new part is that you can toggle scheduling modes from the keyboard while the application is running:
1. Keys:
* 0 – Simple (materialize gray and blur)
* 1 – FuseBlurAndThreshold (materialize gray; fuse blur+threshold)
* 2 – FuseAll (default fusion: fuse gray+blur+threshold)
* 3 – Tile (tile output; materialize gray per tile; blur fused inside tile)
* q / Esc – quit

Under the hood, pressing 0–3 triggers a rebuild of the Halide pipeline with the chosen schedule:
1. You map the key to a Schedule enum value.
2. You call make_pipeline(input, next) to construct the new scheduled pipeline.
3. You reset the warm-up flag, so the next line of stats is labeled [warm-up] (that frame includes JIT).
4. The main loop keeps grabbing frames; only the Halide schedule changes.

This live switching makes fusion tangible: you can watch the loop nest printout change, see the visualization update, and compare throughput numbers in real time as you move between Simple, FuseBlurAndThreshold, FuseAll, and Tile.

Now, build and run the sample:
```console
g++ -std=c++17 camera-capture-fusion.cpp -o camera-capture-fusion \
  -I/path/to/halide/include -L/path/to/halide/lib -lHalide \
  $(pkg-config --cflags --libs opencv4) -lpthread -ldl \
  -Wl,-rpath,/path/to/halide/lib
./camera-capture-fusion
```

You will see the following output:
```output
% ./camera-capture-fusion
Starting with schedule: FuseAll (press 0..3 to switch; q/Esc to quit)

---- Loop structure (FuseAll) ----
produce output:
  for y:
    for x:
      output(...) = ...
-----------------------------------------------
FuseAll | 18.90 ms  |  52.92 FPS  |  109.74 MPix/s2 MPix/s
Switching to schedule: FuseBlurAndThreshold

---- Loop structure (FuseBlurAndThreshold) ----
produce gray:
  for y:
    for x:
      gray(...) = ...
consume gray:
  produce output:
    for y:
      for x:
        output(...) = ...
-----------------------------------------------
FuseBlurAndThreshold | 4.85 ms  |  206.19 FPS  |  427.55 MPix/s97 MPix/s
Switching to schedule: FuseAll

---- Loop structure (FuseAll) ----
produce output:
  for y:
    for x:
      output(...) = ...
-----------------------------------------------
FuseAll | 18.14 ms  |  55.12 FPS  |  114.30 MPix/s22 MPix/s
Switching to schedule: Tile

---- Loop structure (Tile) ----
produce output:
  for y.yo:
    for x.xo:
      produce gray:
        for y:
          for x:
            gray(...) = ...
      consume gray:
        for y.yi in [0, 63]:
          for x.xi in [0, 63]:
            output(...) = ...
-----------------------------------------------
Tile | 4.98 ms  |  200.73 FPS  |  416.23 MPix/s28 MPix/s
Switching to schedule: Simple

---- Loop structure (Simple) ----
produce gray:
  for y:
    for x:
      gray(...) = ...
consume gray:
  produce blur:
    for y:
      for x:
        blur(...) = ...
  consume blur:
    produce output:
      for y:
        for x:
          output(...) = ...
-----------------------------------------------
Simple | 6.01 ms  |  166.44 FPS  |  345.12 MPix/s15 MPix/s
```

The console output combines two kinds of information:
1. Loop nests – printed by print_loop_nest(). These show how Halide actually arranges the computation for the chosen schedule. They are a great “x-ray” view of fusion and materialization:
* In FuseAll, the loop nest contains only output. That’s because gray, blur, and thresholded are all inlined (fused) into it. Each pixel of output recomputes its 3×3 neighborhood of gray.
* In FuseBlurAndThreshold, there is an extra loop for gray, because we explicitly called gray.compute_root(). The blur and thresholded stages are still fused into output. This reduces recomputation of gray and makes downstream loops simpler to vectorize.
* In Simple, both gray and blur have their own loop nests, and thresholded fuses into output. This introduces two extra buffers, but each stage is computed once and can be parallelized independently.
* In Tile, you see the outer tile loops (y.yo and x.xo) and the inner per-tile loops (y.yi, x.xi). Inside each tile, gray is produced once and then consumed by the fused blur and threshold. This keeps the working set small and cache-friendly.
2. Performance metrics – printed after each realize(). They report:
* ms – the average time to process one frame.
* FPS – frames per second (1000 / ms).
* MPix/s – millions of pixels per second processed.

Comparing the numbers:
* FuseAll runs at ~53 FPS. It has minimal memory traffic but pays for recomputation of gray under the blur.
* FuseBlurAndThreshold jumps to over 200 FPS. By materializing gray, we avoid redundant recomputation and allow blur+threshold to stay fused. This is often the sweet spot for interleaved camera input.
* Simple reaches ~166 FPS. Both gray and blur are materialized, so no recomputation occurs, but memory traffic is higher than in FuseBlurAndThreshold.
* Tile achieves similar speed (~200 FPS). Producing gray per tile balances recomputation and memory traffic by keeping intermediates local to cache.

By toggling schedules live, you can see and measure how operator fusion and materialization change both the loop structure and the throughput:
* Fusion is the default in Halide and eliminates temporary storage, but may cause recomputation for spatial filters.
* Materializing selected stages with compute_root() or compute_at() can reduce recomputation and improve locality. It can also make vectorization and parallelization easier or more effective, but they are not strictly required by materialization and can be applied independently. For best performance, consider these choices together and measure on your target.
* Tile-level materialization (compute_at) provides a hybrid - fusing within tiles while keeping intermediates small and cache-resident.

This demo makes these trade-offs concrete: the loop nest diagrams explain the structure, and the live FPS/MPix/s stats show the real performance impact.

## What “fusion” means in Halide
One of Halide’s defining features is that, by default, it performs operator fusion, also called inlining. This means that if a stage produces some intermediate values, those values aren’t stored in a separate buffer and then re-read later—instead, the stage is computed directly inside the consumer’s loop. In other words, unless you tell Halide otherwise, every producer Func is fused into the next stage that uses it.

Why is this important? Fusion reduces memory traffic, because Halide doesn’t need to write intermediates out to RAM and read them back again. On CPUs, where memory bandwidth is often the bottleneck, this can be a major performance win. Fusion also improves cache locality, since values are computed exactly where they are needed and the working set stays small. The trade-off, however, is that fusion can cause recomputation: if a consumer uses a neighborhood (like a blur that reads 3×3 or 9×9 pixels), the fused producer may be recalculated multiple times for overlapping regions. Whether fusion is faster depends on the balance between compute cost and memory traffic.

Consider the difference in pseudocode:
```cpp
for y:
  for x:
    out(x,y) = threshold( sum_{i,j in 3x3} kernel(i,j) * gray(x+i,y+j) )
    // gray(...) is computed on the fly for each (i,j)
```

Materialized with compute_root():

```cpp
for y: for x: gray(x,y) = ...                // write one planar gray image
for y: for x: out(x,y) = threshold( sum kernel * gray(x+i,y+j) )
```

The fused version eliminates buffer writes but recomputes gray under the blur stencil. The materialized version performs more memory operations but avoids recomputation, and also gives us a clean point to parallelize or vectorize the gray stage.

It’s worth noting that Halide also supports a loop fusion directive (fuse) that merges two loop variables together. That’s a different concept and not our focus here. In this tutorial, we’re talking specifically about operator fusion—the decision of whether to inline or materialize stages.

## How this looks in the live camera demo
Our pipeline is: BGR input → gray → 3×3 blur → thresholded → output. Depending on the schedule, we see different kinds of fusion:
* FuseAll. No schedules on producers. gray, blur, and thresholded are all inlined into output. This minimizes memory traffic but recomputes gray repeatedly inside the 3×3 blur.
* FuseBlurAndThreshold: We add gray.compute_root(), materializing gray once as a planar buffer. This avoids recomputation of gray and makes downstream blur and thresholded vectorize better. blur and thresholded remain fused.
* Simple. Both gray and blur are materialized across the frame. This avoids recomputation entirely but increases memory traffic.
* Tile. We split the output into 64×64 tiles and compute gray per tile (compute_at(output, xo)). This keeps intermediate results local to cache while still fusing blur inside each tile.

By toggling between these modes in the live demo, you can see how the loop nests and throughput numbers change, which makes the abstract idea of fusion much more concrete.

## When to use operator fusion
Fusion is Halide’s default and usually the right place to start. It’s especially effective for:
* Element-wise chains, where each pixel is transformed independently:
examples include intensity scaling or offset, gamma correction, channel mixing, color-space conversions, and logical masking.
* Cheap post-ops after spatial filters:
for instance, there’s no reason to materialize a blurred image just to threshold it. Fuse the threshold directly into the blur’s consumer.

In our code, FuseAll inlines gray, blur, and thresholded into output. FuseBlurAndThreshold materializes only gray, then keeps blur and thresholded fused—a common middle ground that balances memory use and compute reuse.

## When to materialize instead of fuse
Fusion isn’t always best. You’ll want to materialize an intermediate (compute_root() or compute_at()) if:
* The producer would be recomputed many times under a large stencil.
* The producer is read from an interleaved source and it’s easier to vectorize a planar buffer.
* The intermediate is reused by multiple consumers.
* You need a natural stage to apply parallelization or tiling.

### Profiling
The fastest way to check whether fusion helps is to measure it. Our demo prints timing and throughput per frame, but Halide also includes a built-in profiler that reports per-stage runtimes. To learn how to enable and interpret the profiler, see the official [Halide profiling tutorial](https://halide-lang.org/tutorials/tutorial_lesson_21_auto_scheduler_generate.html#profiling).

## Summary
In this section, you have learned about operator fusion in Halide—a powerful technique for reducing memory bandwidth and improving computational efficiency. You explored why fusion matters, looked at scenarios where it is most effective, and saw how Halide’s scheduling constructs such as compute_root() and compute_at() let us control whether stages are fused or materialized. By experimenting with different schedules, including fusing the Gaussian blur and thresholding stages, we observed how fusion can significantly improve the performance of a real-time image processing pipeline
