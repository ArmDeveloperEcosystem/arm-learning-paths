---
# User change
title: "Building a Simple Camera Image Processing Workflow"

weight: 3

layout: "learningpathall"
---

## Objective
In this section, we’ll build a real-time camera processing pipeline using Halide. We’ll start by capturing video frames from a webcam using OpenCV, then implement a Gaussian blur to smooth the captured images, followed by thresholding to create a clear binary output highlighting the most prominent image features. After establishing this pipeline, we’ll explore how to optimize performance further by applying Halide’s tiling strategy, a technique for enhancing cache efficiency and execution speed, particularly beneficial for high-resolution or real-time applications

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
        
        // Define variables representing image spatial coordinates.
        // "x" for horizontal dimension (width), "y" for vertical dimension (height).
        // In Halide, it’s a common convention to use short variable names such as x and y to represent image coordinates clearly and concisely. This follows a well-established mathematical and programming convention:
	    // x typically refers to the horizontal spatial dimension (width).
	    // y typically refers to the vertical spatial dimension (height).
        Halide::Var x("x"), y("y");

        // Define a function that applies a 3x3 Gaussian blur.
        Halide::Func blur("blur");

        // Define a reduction domain (RDom) that iterates over a 3x3 region.
        // This is used to apply a convolution (Gaussian blur) operation in Halide.
        Halide::RDom r(0, 3, 0, 3);

        // Kernel layout: [1 2 1; 2 4 2; 1 2 1], sum = 16.
        Halide::Expr weight = Halide::select(
            (r.x == 1 && r.y == 1), 4,
            (r.x == 1 || r.y == 1), 2,
            1
        );

        // Calculate the neighboring pixel's horizontal offset relative to the current pixel.
        // r.x iterates over the kernel width (0, 1, 2), so subtracting 1 centers the kernel.
        Halide::Expr offsetX = x + (r.x - 1);
        Halide::Expr offsetY = y + (r.y - 1);

        // Manually clamp offsets to avoid out-of-bounds.
        Halide::Expr clampedX = clampCoord(offsetX, width);
        Halide::Expr clampedY = clampCoord(offsetY, height);

        // Accumulate weighted sum in 32-bit int before normalization.
        // Accumulate weighted sum explicitly using a 32-bit integer type (int32_t) for consistent precision and overflow behavior.
        Halide::Expr val = Halide::cast<int32_t>(input(clampedX, clampedY)) * weight;

        // Compute the Gaussian blur value by summing the weighted neighborhood values (stored as int32_t)
        // and dividing by the kernel's total weight (16) to normalize. Cast the result back to uint8_t (8-bit unsigned integer)
        // suitable for grayscale pixel intensity representation.
        blur(x, y) = Halide::cast<uint8_t>(Halide::sum(val) / 16);

        // Add a thresholding stage on top of the blurred result.
        // If blur(x,y) > 128 => 255, else 0
        Halide::Func thresholded("thresholded");
        thresholded(x, y) = Halide::cast<uint8_t>(
            Halide::select(blur(x, y) > 128, 255, 0)
        );

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
        // Wait up to 30 milliseconds for a key press.
        // If a key is pressed during this interval, exit the loop and terminate the application.
        // A value of 30 sets the approximate frame delay, roughly corresponding to ~33 frames per second.
        if (waitKey(30) >= 0) {
            break;
        }
    }

    cap.release();
    destroyAllWindows();
    return 0;
}
```

This code demonstrates a simple real-time image processing pipeline using Halide and OpenCV. Initially, it opens the computer’s default camera to continuously capture video frames. Each captured frame, originally in color, is converted into a single-channel grayscale image using OpenCV. Although grayscale conversion is handled here via OpenCV for simplicity, performing it within Halide could further enhance performance through operation fusion and reduced memory overhead.

The grayscale image data is then passed to Halide via a buffer to perform computations. Within Halide, the program implements a Gaussian blur using a 3x3 convolution kernel with weights specifically chosen to smooth the image (weights: [1 2 1; 2 4 2; 1 2 1]). To safely handle pixels near image borders, the coordinates are manually clamped, ensuring all pixel accesses remain valid within the image dimensions.

The kernel chosen here is a 3×3 Gaussian blur kernel, a commonly used convolutional kernel designed to smooth images by reducing high-frequency noise and detail, while preserving edges and larger image structures. A Gaussian blur kernel assigns higher weights to the center pixels and lower weights to surrounding pixels, closely approximating a Gaussian distribution (bell-shaped curve).

Specifically, the chosen kernel is:

(1/16) × | 1  2  1 |

         | 2  4  2 |         

         | 1  2  1 |

Reason for choosing this kernel:
* It provides effective smoothing by considering the immediate neighbors of each pixel, making it computationally lightweight yet visually effective.
* The weights approximate a Gaussian distribution, helping to maintain image details while reducing noise and small variations.

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

This expression explicitly assigns:
* Weight = 4 for the center pixel (r.x=1, r.y=1)
* Weight = 2 for direct horizontal and vertical neighbors (r.x=1 or r.y=1 but not both)
* Weight = 1 for corner pixels (diagonal neighbors)

After the Gaussian blur stage, a thresholding operation is applied. This step converts the blurred grayscale image into a binary image, assigning a value of 255 to pixels with intensity greater than 128 and 0 otherwise, thus highlighting prominent features against the background.

Finally, the processed image is returned from Halide to an OpenCV matrix and displayed in real-time. The loop continues until a key is pressed, providing a smooth, interactive demonstration of Halide’s ability to accelerate and streamline real-time image processing tasks.

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

## Tiling
Tiling is a powerful scheduling optimization provided by Halide, allowing image computations to be executed efficiently by dividing the workload into smaller, cache-friendly blocks called tiles. By processing these smaller regions individually, we significantly improve data locality, reduce memory bandwidth usage, and better leverage CPU caches, ultimately boosting performance for real-time applications.

We can easily extend our Gaussian blur and thresholding pipeline to leverage Halide’s built-in tiling capabilities. Let’s apply a simple tiling schedule to our existing pipeline. Replace the code segment immediately after defining the thresholded function with the following:

```cpp
// Apply a simple tiling schedule
Halide::Var x_outer, y_outer, x_inner, y_inner;
thresholded.tile(x, y, x_outer, y_outer, x_inner, y_inner, 64, 64)
           .parallel(y_outer);
```

The .tile(x, y, x_outer, y_outer, x_inner, y_inner, 64, 64) statement divides the image into 64×64 pixel tiles, significantly improving cache locality. While the parallel(y_outer) executes each horizontal row of tiles in parallel across available CPU cores, boosting execution speed.

Recompile your application as before, then run:
```console
./camera-capture
```

## Summary
In this section, we built a complete real-time image processing pipeline using Halide and OpenCV. Initially, we captured live video frames and applied Gaussian blur and thresholding to highlight image features clearly. By incorporating Halide’s tiling optimization, we also improved performance by enhancing cache efficiency and parallelizing computation. Through these steps, we demonstrated Halide’s capability to provide both concise, clear code and high performance, making it an ideal framework for demanding real-time image processing tasks.

