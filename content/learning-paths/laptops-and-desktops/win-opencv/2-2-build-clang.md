---
title: Build OpenCV Applications with Clang
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How do I build OpenCV with Clang?

Follow the steps below to build OpenCV and a test application using the library with the Clang compiler.

### Clone the OpenCV repository

Open up a Windows PowerShell and checkout the source tree:

```bash
git clone https://github.com/opencv/opencv
cd opencv
git checkout tags/4.10.0
```

{{% notice Note %}}
You might be able to use a later version, but these steps have been tested with the version 4.10.0.
{{% /notice %}}

### Pre-build configuration

You can use CMake from the command line. 

First, run the following command to run the pre-build configuration. 

```bash
mkdir build_clang
cd build_clang

cmake `
-S .. `
-B . `
-G "Ninja" `
-DCMAKE_C_COMPILER=clang `
-DCMAKE_CXX_COMPILER=clang++ `
-DCMAKE_BUILD_TYPE=Release `
-DBUILD_opencv_world=ON `
-DWITH_ITT=OFF `
-DWITH_OPENCL=OFF `
-DWITH_OPENCLAMDBLAS=OFF `
-DWITH_OPENCLAMDFFT=OFF `
-DWITH_OPENCL_D3D11_NV=OFF `
-DWITH_DIRECTML=OFF `
-DWITH_DIRECTX=OFF `
-DWITH_ADE=OFF `
-DWITH_CAROTENE=OFF
```

The given options specify the following:
- The source code is located one level above the current directory.
- The build will be performed in the current directory.
- The Clang compiler will be used as the compiler.
- The compiled library is generated as a single file that includes all of OpenCV's functionality.
- Unnecessary options have been disabled, assuming processing on Arm CPUs.

&nbsp;

If the configuration is successful, a message similar to the following should be displayed at the end of the execution:

```
-- General configuration for OpenCV 4.10.0 =====================================
--   Version control:               4.10.0
--
--   Platform:
--     Timestamp:                   2024-11-08T09:23:57Z
--     Host:                        Windows 10.0.22631 ARM64
--     CMake:                       3.28.1
--     CMake generator:             Ninja
--     CMake build tool:            C:/Users/username/work/venv/Scripts/ninja.exe
--     Configuration:               Release
--
--   CPU/HW features:
--     Baseline:                    NEON
--       requested:                 NEON FP16
--     Dispatched code generation:  NEON_DOTPROD NEON_FP16 NEON_BF16
--       requested:                 NEON_FP16 NEON_BF16 NEON_DOTPROD
--       NEON_DOTPROD (1 files):    + NEON_DOTPROD
--       NEON_FP16 (2 files):       + NEON_FP16
--       NEON_BF16 (0 files):       + NEON_BF16
--
--   C/C++:
--     Built as dynamic libs?:      YES
--     C++ standard:                11
--     C++ Compiler:                C:/Program Files/LLVM/bin/clang++.exe  (ver 18.1.8)
[...]
--     C Compiler:                  C:/Program Files/LLVM/bin/clang.exe
[...]
--   Install to:                    C:/Users/username/work/opencv/build_clang/install
-- -----------------------------------------------------------------
--
-- Configuring done (244.5s)
-- Generating done (1.4s)
-- Build files have been written to: C:/Users/username/work/opencv/build_clang
```

### Build and install

Run the following commands to build and install OpenCV:

```bash
ninja
ninja install
```

{{% notice Note %}}
The build takes approximately 25 mins on a Lenovo X13s
{{% /notice %}}

&nbsp;

When the build and the install steps are complete, confirm the shared library has been created by inspecting the results in the `install/bin` directory:

```bash { output_lines = "2-11" }
ls ./install/bin
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        08/11/2024     09:51          40448 opencv_annotation.exe
-a----        08/11/2024     09:51         126464 opencv_interactive-calibration.exe
-a----        08/11/2024     09:51          40448 opencv_model_diagnostics.exe
-a----        08/11/2024     09:51          38400 opencv_version.exe
-a----        08/11/2024     09:51          35840 opencv_version_win32.exe
-a----        08/11/2024     09:23       26391552 opencv_videoio_ffmpeg4100_64.dll
-a----        08/11/2024     09:51          51712 opencv_visualisation.exe
-a----        08/11/2024     09:50       20207104 opencv_world4100.dll
```

Also inspect the  `install/lib` directory:

```bash { output_lines = "2-9" }
ls ./install/lib
    Directory: C:\Users\username\work\opencv\build_clang\install\lib
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        08/11/2024     09:23            434 OpenCVConfig-version.cmake
-a----        08/11/2024     09:23          15254 OpenCVConfig.cmake
-a----        08/11/2024     09:23            936 OpenCVModules-release.cmake
-a----        08/11/2024     09:23           3749 OpenCVModules.cmake
-a----        08/11/2024     09:50        2862548 opencv_world4100.lib
```

&nbsp;

The library used in your application is `opencv_world<version>.lib/dll`. 

Once the library files are correctly generated, run the following command to ensure there are no errors.

```bash { output_lines = "2" }
./install/bin/opencv_version.exe
4.10.0
```

&nbsp;

## Build OpenCV Applications

Once the OpenCV library has been successfully created, you can create a simple application and try using it.

### Prepare an application program

First, use a text editor to save the following C++ program as `test_opencv.cpp` in the `build_clang` directory.

```cpp
#include <opencv2/opencv.hpp>
#include <iostream>
int main() {
    cv::Mat image = cv::Mat::zeros(100, 100, CV_8UC3);
    if (image.empty()) {
        std::cout << "Failed to create an image!" << std::endl;
        return -1;
    }
    cv::circle(image, cv::Point(50, 50), 30, cv::Scalar(255, 0, 0), -1);
    cv::imwrite("test_image.png", image);
    cv::waitKey(0);
    return 0;
}
```

This program is a simple example that uses OpenCV to create a 100x100 black image, draw a blue circle on it, and save it as a file.

### Compile the program

Compile the code using the command below: 

```bash
clang++ .\test_opencv.cpp -o test_opencv.exe -I.\install\include -L.\install\lib -lopencv_world4100
```

The given options specify the following:
* __`-o`__: Specifies the name of the generated executable file.
* __`-I`__: Indicates the directory where the OpenCV header files to be included are located.
* __`-L`__: Specifies the directory where the libraries for linking are located.
* __`-l`__: Specifies the name of the library to link. When linking `opencv_world4100.lib`, omit the `.lib` extension and specify it as `-lopencv_world4100`.

### Run the program

To run the executable, you need to ensure that the directory containing the dynamic libraries (DLLs) is added to the `PATH` environment variable, or place the DLLs in the same location as the executable. 

{{% notice Note %}}
The command below adds the DLL directory to the beginning of the `PATH` environment variable. Since this is a temporary setting, the `PATH` will revert to its original state when the PowerShell session is closed. To set it permanently, you need to use the Windows system settings or the `[Environment]::SetEnvironmentVariable()` method.

```bash
$env:PATH = "./install/bin;" + $env:PATH
```
{{% /notice %}}

Run the test program:

```bash
.\test_opencv.exe
```

When you execute the command, it will finish quickly, and `test_image.png` is generated. If you do not have the DLL directory in your search path, the program appears to run, but no `test_image.png` is generated. 

Open the image file, it should look like the example shown below.

![test_image pic](test_image.png "test_image.png")

Congratulations! You are now ready to create your own OpenCV applications using Clang.
