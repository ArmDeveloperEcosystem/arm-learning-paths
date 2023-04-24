---
# User change
title: "Application setup" 

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Application setup

To build the application on Linux x86_64, clone the repository with:

```bash
git clone https://github.com/m3y54m/sobel-simd-opencv.git
cd sobel-simd-opencv
```

Install the required dependencies:

```bash
sudo apt install -y build-essential g++ libopencv-dev cmake
```

Build the application:
```bash
cmake -S src -B build
cd build/
make
```

Run with:
```bash
./sobel_simd_opencv
```

The output in the terminal should be similar to:
```output
Execution time for non-SIMD Sobel edge detection:
5559.47 us
Execution time for SIMD Sobel edge detection:
2993.71 us
Execution time for OpenCV Sobel edge detection:
5650.26 us
```
In addition, it will open several windows allowing to compare the results between the different versions:

![Sobel filter output#center](output_sobel.jpg)

Here is a summary of our configuration on `x86_64`:

| OS | Compiler | Build tools | External libraries |
| -- | -------- | ----------- | ------------------ |
| Ubuntu 22.04.2 | GCC 11.3.0 | Cmake 3.26.3 | OpenCV 4.5.4 |

