---
# User change
title: "Building a Simple Camera Image Processing Workflow"

weight: 3

layout: "learningpathall"
---

## Objective
In this section, we will build a real-time camera processing pipeline using Halide. First, we capture video frames from a webcam using OpenCV, then implement a Gaussian blur to smooth the captured images, followed by thresholding to create a clear binary output highlighting prominent image features. After establishing this pipeline, we will optimize performance further by applying Halide’s tiling strategy, a technique that enhances cache efficiency and execution speed, particularly beneficial for high-resolution or real-time applications.

## Gaussian blur and thresholding
Create a new camera-capture.cpp file and modify it as follows:
```cpp
#include "Halide.h"
#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>      // For std::string
#include <cstdint>     // For uint8_t, etc.
#include <exception>   // For std::exception

using namespace cv;
using namespace std;

// Clamp coordinate within [0, maxCoord - 1].
static inline Halide::Expr clampCoord(Halide::Expr coord, int maxCoord) {
    return Halide::clamp(coord, 0, maxCoord - 1);
}

int main() {
    // Open the default camera.
    VideoCapture cap(0);
    if (!cap.isOpened()) {
        cerr << "Error: Unable to open camera." << endl;
        return -1;
    }

    while (true) {
        // Capture frame.
        Mat frame;
        cap >> frame;
        if (frame.empty()) {
            cerr << "Error: Received empty frame." << endl;
            break;
        }

        // Convert to grayscale.
        Mat gray;
        cvtColor(frame, gray, COLOR_BGR2GRAY);
        if (!gray.isContinuous()) {
            gray = gray.clone();
        }

        int width  = gray.cols;
        int height = gray.rows;

        // Wrap grayscale image into Halide buffer.
        Halide::Buffer<uint8_t> inputBuffer(gray.data, width, height);

        // Define ImageParam (symbolic representation of input image).
        Halide::ImageParam input(Halide::UInt(8), 2, "input");
        input.set(inputBuffer);
        
        // Define variables representing image spatial coordinates.
        // "x" for horizontal dimension (width), "y" for vertical dimension (height).
        // In Halide, it’s a common convention to use short variable names such as x and y to represent image coordinates clearly and concisely. This follows a well-established mathematical and programming convention:
	    // x typically refers to the horizontal spatial dimension (width).
	    // y typically refers to the vertical spatial dimension (height).
        Halide::Var x("x"), y("y");

        // Kernel layout: [1 2 1; 2 4 2; 1 2 1], sum = 16.
        int kernel_vals[3][3] = {
            {1, 2, 1},
            {2, 4, 2},
            {1, 2, 1}
        };
        Halide::Buffer<int> kernelBuf(&kernel_vals[0][0], 3, 3);

        Halide::RDom r(0, 3, 0, 3);
        Halide::Func blur("blur");
        Halide::Expr val = Halide::cast<int32_t>(
            input(clampCoord(x + r.x - 1, width),
                clampCoord(y + r.y - 1, height))
        ) * kernelBuf(r.x, r.y);

        blur(x, y) = Halide::cast<uint8_t>(Halide::sum(val) / 16);

        // Thresholding stage.
        Halide::Func thresholded("thresholded");
        thresholded(x, y) = Halide::cast<uint8_t>(
            Halide::select(blur(x, y) > 128, 255, 0)
        );

        // Realize pipeline.
        Halide::Buffer<uint8_t> outputBuffer;
        try {
            outputBuffer = thresholded.realize({ width, height });
        } catch (const std::exception &e) {
            cerr << "Halide pipeline error: " << e.what() << endl;
            break;
        }

        // Wrap output in OpenCV Mat and display.
        Mat blurredThresholded(height, width, CV_8UC1, outputBuffer.data());
        imshow("Processed Image", blurredThresholded);

        // Wait for 30 ms (~33 FPS). Exit if any key is pressed.
        if (waitKey(30) >= 0) {
            break;
        }
    }

    cap.release();
    destroyAllWindows();
    return 0;
}
```

This code demonstrates a real-time image processing pipeline using Halide and OpenCV. Initially, the default camera is accessed, continuously capturing color video frames. Each captured frame is immediately converted into a grayscale image via OpenCV for simplicity.

Next, the grayscale image is wrapped into a Halide buffer for processing. We define symbolic variables x and y, representing horizontal (width) and vertical (height) image coordinates, respectively.

The pipeline applies a Gaussian blur using a 3×3 kernel explicitly defined in a Halide buffer:

```cpp
int kernel_vals[3][3] = {
    {1, 2, 1},
    {2, 4, 2},
    {1, 2, 1}
};
Halide::Buffer<int> kernelBuf(&kernel_vals[0][0], 3, 3);
```

Reason for choosing this kernel:
* It provides effective smoothing by considering the immediate neighbors of each pixel, making it computationally lightweight yet visually effective.
* The weights approximate a Gaussian distribution, helping to maintain image details while reducing noise and small variations.

The Gaussian blur calculation utilizes a Halide reduction domain (RDom), iterating over the 3×3 neighborhood around each pixel.To handle boundary pixels safely, pixel coordinates are manually clamped within valid bounds:

```cpp
Halide::Expr val = Halide::cast<int32_t>(
    input(clampCoord(x + r.x - 1, width),
          clampCoord(y + r.y - 1, height))
) * kernelBuf(r.x, r.y);

blur(x, y) = Halide::cast<uint8_t>(Halide::sum(val) / 16);
```


Here’s the Halide expression using the reduction domain (RDom):
```cpp
Halide::RDom r(0, 3, 0, 3);

// Gaussian blur kernel weights: center pixel has weight 4,
// edge neighbors (up, down, left, right) have weight 2,
// and diagonal neighbors have weight 1.
Halide::Expr weight = Halide::select(
    (r.x == 1 && r.y == 1), 4,             // center pixel
    (r.x == 1 || r.y == 1), 2,             // direct neighbors (edges)
    1                                      // diagonal neighbors (corners)
);
```

After blurring, the pipeline applies a thresholding operation, converting the blurred image into a binary image: pixels above the intensity of 128 become white (255), while others become black (0).

The final result is realized by Halide and directly wrapped into an OpenCV matrix (Mat) without extra memory copies. This processed image is displayed in real-time.

The main loop continues processing and displaying images until any key is pressed, providing an interactive demonstration of Halide’s performance and seamless integration with OpenCV for real-time applications.

After the Gaussian blur stage, a thresholding operation is applied. This step converts the blurred grayscale image into a binary image, assigning a value of 255 to pixels with intensity greater than 128 and 0 otherwise, thus highlighting prominent features against the background.

Finally, the processed image is returned from Halide to an OpenCV matrix and displayed in real-time. The loop continues until a key is pressed, providing a smooth, interactive demonstration of Halide’s ability to accelerate and streamline real-time image processing tasks.

In the above example we used manually clamped coordiantes. An alternative and often recommended approach is to leverage Halide’s built-in function, BoundaryConditions::repeat_edge. Halide internally optimizes loops based on the specified boundary conditions, effectively partitioning loops to separately handle edge pixels, improving vectorization, parallelization, and overall efficiency.

The alternative implementation could look like this:

```cpp
// Use Halide's built-in boundary handling instead of manual clamping.
Halide::Func inputClamped = Halide::BoundaryConditions::repeat_edge(input);

// Offsets around the current pixel.
Halide::Expr offsetX = x + (r.x - 1);
Halide::Expr offsetY = y + (r.y - 1);

// Directly use clamped function to safely access pixel values.
Halide::Expr val = Halide::cast<int32_t>(inputClamped(offsetX, offsetY)) * weight;
```

Here, we used a fixed array for the kernel. Alternatively, you can define the 3×3 Gaussian blur kernel using the Halide select expression, clearly assigning weights based on pixel positions:
```cpp
// Define a reduction domain to iterate over a 3×3 neighborhood
Halide::RDom r(0, 3, 0, 3);

// Explicitly assign Gaussian kernel weights based on pixel position:
// - 4 for the center pixel (r.x == 1 && r.y == 1)
// - 2 for direct horizontal and vertical neighbors (either r.x or r.y is 1 but not both)
// - 1 for corner (diagonal) neighbors
Halide::Expr weight = Halide::select(
    (r.x == 1 && r.y == 1), 4,              // center pixel
    (r.x == 1 || r.y == 1), 2,              // direct horizontal or vertical neighbors
    1                                      // diagonal (corner) neighbors
);

// Apply the kernel weights to the neighborhood pixels
Halide::Expr val = Halide::cast<int32_t>(
    input(clampCoord(x + r.x - 1, width),
          clampCoord(y + r.y - 1, height))
) * weight;

// Compute blurred pixel value
blur(x, y) = Halide::cast<uint8_t>(Halide::sum(val) / 16);
```

This expression explicitly assigns:
* Weight = 4 for the center pixel (r.x=1, r.y=1)
* Weight = 2 for direct horizontal and vertical neighbors (r.x=1 or r.y=1 but not both)
* Weight = 1 for corner pixels (diagonal neighbors)

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
In this section, we will explore two complementary scheduling optimizations provided by Halide: Parallelization and Tiling. Both techniques help enhance performance but achieve it through different mechanisms—parallelization leverages multiple CPU cores, whereas tiling improves cache efficiency by optimizing data locality.

Below, we’ll demonstrate each technique separately for clarity and to emphasize their distinct benefits.

### Parallelization
Parallelization is a scheduling optimization that allows computations to execute simultaneously across multiple CPU cores. By distributing the computational workload across available processing units, Halide effectively reduces the overall execution time, especially beneficial for real-time or computationally intensive image processing tasks.

Let’s first apply parallelization to our existing Gaussian blur and thresholding pipeline:

```cpp
// Thresholded function (as previously defined)
Halide::Func thresholded("thresholded");
thresholded(x, y) = Halide::select(blur(x, y) > 128, 255, 0);

// Parallelize the processing across multiple CPU cores
thresholded.parallel(y);
```

Here, the parallel(y) directive instructs Halide to parallelize execution along the vertical dimension (y). This distributes computations along available cores on multicore CPUs. 

### Tiling
Tiling is a scheduling technique that divides computations into smaller, cache-friendly blocks or tiles. This approach significantly enhances data locality, reduces memory bandwidth usage, and leverages CPU caches more efficiently. While tiling can also use parallel execution, its primary advantage comes from optimizing intermediate data storage.

We’ll demonstrate tiling in two scenarios:
1. Tiling for cache efficiency (with explicit intermediate storage)
2. Tiling for parallelization (without explicit intermediate storage)

### Tiling for enhanced cache efficiency (explicit intermediate storage)
When intermediate results between computation stages are temporarily stored, tiling achieves maximum performance gains. Smaller intermediate tiles comfortably fit within CPU caches, greatly improving data locality and minimizing redundant memory access.

Here’s how to explicitly tile the Gaussian blur computation to store intermediate results in tiles:

```cpp
// Define variables
Halide::Var x("x"), y("y"), x_outer, y_outer, x_inner, y_inner;

// Define functions
Halide::Func blur("blur"), thresholded("thresholded");

// Thresholded function definition
thresholded(x, y) = Halide::select(blur(x, y) > 128, 255, 0);

// Apply tiling to divide computation into 64×64 tiles
thresholded.tile(x, y, x_outer, y_outer, x_inner, y_inner, 64, 64)
           .parallel(y_outer);

// Compute blur within each tile explicitly to enhance cache efficiency
blur.compute_at(thresholded, x_outer);
```

In this scheduling:
* tile(...) divides the image into smaller blocks (tiles), optimizing cache locality.
* blur.compute_at(thresholded, x_outer) instructs Halide to explicitly store intermediate blur results per tile, effectively utilizing the CPU’s cache.

This approach reduces memory bandwidth demands, as each tile’s intermediate results remain in cache, greatly accelerating the pipeline for large or complex operations.

Recompile your application as before, then run:
```console
./camera-capture
```

### Tiling for parallelization (without explicit intermediate storage)
In contrast, tiling can also facilitate parallel execution without explicitly storing intermediate results. This approach mainly leverages tiling to simplify workload partitioning across CPU cores.

Here’s a simple parallel tiling approach for our pipeline:

```cpp
// Define variables
Halide::Var x("x"), y("y"), x_outer, y_outer, x_inner, y_inner;

// Thresholded function definition
Halide::Func thresholded("thresholded");
thresholded(x, y) = Halide::select(blur(x, y) > 128, 255, 0);

// Apply simple tiling schedule to divide workload and parallelize execution
thresholded.tile(x, y, x_outer, y_outer, x_inner, y_inner, 64, 64)
           .parallel(y_outer);
```

Here, the tiling directive primarily divides the workload into manageable segments for parallel execution. While this also improves cache locality indirectly, the absence of explicit intermediate storage means the primary gain is parallel execution rather than direct cache efficiency.

### Tiling vs. parallelization
* Parallelization directly speeds up computations by distributing workload across CPU cores.
* Tiling for cache efficiency explicitly stores intermediate results within tiles to maximize cache utilization, greatly reducing memory bandwidth requirements.
* Tiling for parallelization divides workload into smaller segments, primarily to simplify parallel execution rather than optimize cache usage directly.

## Summary
In this section, we built a complete real-time image processing pipeline using Halide and OpenCV. Initially, we captured live video frames and applied Gaussian blur and thresholding to highlight image features clearly. By incorporating Halide’s tiling optimization, we also improved performance by enhancing cache efficiency and parallelizing computation. Through these steps, we demonstrated Halide’s capability to provide both concise, clear code and high performance, making it an ideal framework for demanding real-time image processing tasks.

