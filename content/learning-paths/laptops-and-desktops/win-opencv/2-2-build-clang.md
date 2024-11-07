---
title: Build OpenCV Applications with Clang
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build OpenCV with Clang

### Clone OpenCV repo

Open up a Windows Powershell and checkout the source tree:

```bash
git clone https://github.com/opencv/opencv
cd opencv
git checkout tags/4.10.0
```

{{% notice Note %}}
You might be able to use a later version. These steps have been tested with the version 4.10.0.
{{% /notice %}}

### Build with Clang

Here, you will use CMake from the command line. First, Run the following command to run the pre-build configuration. 

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
- The Visual Studio 2022 MSVC compiler will be used as the compiler.
- The built library is generated as a single file that includes all of OpenCV's functionality.
- Disable unnecessary options, assuming processing on Arm CPU.Unnecessary options have been disabled to execute processing on Arm CPUs.


If the configuration is successful, a message similar to the following should be displayed at the end of the execution:

```
-- General configuration for OpenCV 4.10.0 =====================================
--   Version control:               4.10.0
--
--   Platform:
--     Timestamp:                   2024-11-06T17:47:31Z
--     Host:                        Windows 10.0.22631 ARM64
--     CMake:                       3.28.1
--     CMake generator:             Ninja
--     CMake build tool:            C:/Users/kokmit01/work/venv/Scripts/ninja.exe
--     Configuration:               Release
--
--   CPU/HW features:
--     Baseline:                    NEON
--       requested:                 NEON FP16
--     Dispatched code generation:  NEON_DOTPROD NEON_FP16
--       requested:                 NEON_FP16 NEON_BF16 NEON_DOTPROD
--       NEON_DOTPROD (1 files):    + NEON_DOTPROD
--       NEON_FP16 (2 files):       + NEON_FP16
--
--   C/C++:
--     Built as dynamic libs?:      YES
--     C++ standard:                11
--     C++ Compiler:                C:/Program Files/LLVM/bin/clang++.exe  (ver 18.1.8)
[...]
--     C Compiler:                  C:/Program Files/LLVM/bin/clang.exe
[...]
--   Install to:                    C:/Users/kokmit01/work/opencv/build_clang/install
-- -----------------------------------------------------------------
--
-- Configuring done (384.4s)
-- Generating done (1.9s)
-- Build files have been written to: C:/Users/kokmit01/work/opencv/build_clang
```

Now run the following command to build and install:

```bash
ninja
ninja install
```

{{% notice Note %}}
The build takes approximately 25 mins on Lenovo X13s
{{% /notice %}}

When the build and the install is complete, confirm the shared library have been created:

```bash { output_lines = "2-6,8-16" }
ls ./install/bin
    Directory: C:\Users\kokmit01\work\opencv\build_clang\install\bin
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        07/11/2024     16:11       26391552 opencv_videoio_ffmpeg4100_64.dll
-a----        07/11/2024     21:56       27175936 opencv_world4100.dll
ls ./install/x64/vc17/lib
    Directory: C:\Users\kokmit01\work\opencv\build_clang\install\lib
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        07/11/2024     16:11            434 OpenCVConfig-version.cmake
-a----        07/11/2024     16:11          15260 OpenCVConfig.cmake
-a----        07/11/2024     16:11            972 OpenCVModules-release.cmake
-a----        07/11/2024     16:11           3879 OpenCVModules.cmake
-a----        07/11/2024     21:56        2849862 opencv_world4100.lib
```

## Build OpenCV Applications


Add C:\Users\kokmit01\work\opencv\build\install\bin to PATH environment variable (for access to dll)
put the dll to the directory with exe file if it doesn't work. 

Set include dir/linker path



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
    //cv::imshow("Test Image", image);
    cv::imwrite("test_image.png", image);
    cv::waitKey(0);
    return 0;
}
```



```bash
 clang++ .\test_opencv.cpp -o test_opencv.exe -I.\build_clang\install\include -L.\build_clang\install\lib -lopencv_world4100
```