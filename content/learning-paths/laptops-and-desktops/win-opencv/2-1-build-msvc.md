---
title: Build OpenCV Applications with MSVC
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build OpenCV with MSVC

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

### Build with MSVC

Here, you will use CMake from the command line. First, Run the following command to run the pre-build configuration. 

```bash
mkdir build_msvc
cd build_msvc

cmake `
-S .. `
-B . `
-G "Visual Studio 17 2022" `
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
--     CMake generator:             Visual Studio 17 2022
--     CMake build tool:            C:/Program Files/Microsoft Visual Studio/2022/Professional/MSBuild/Current/Bin/arm64/MSBuild.exe
--     MSVC:                        1941
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
--     C++ Compiler:                C:/Program Files/Microsoft Visual Studio/2022/Professional/VC/Tools/MSVC/14.41.34120/bin/Hostarm64/arm64/cl.exe  (ver 19.41.34123.0)
[...]
--     C Compiler:                  C:/Program Files/Microsoft Visual Studio/2022/Professional/VC/Tools/MSVC/14.41.34120/bin/Hostarm64/arm64/cl.exe
[...]
--   Install to:                    C:/Users/kokmit01/work/opencv/build_msvc/install
-- -----------------------------------------------------------------
--
-- Configuring done (93.6s)
-- Generating done (2.8s)
-- Build files have been written to: C:/Users/kokmit01/work/opencv/build_msvc
```

Now run the following command to build and install:

```bash
cmake --build . --config Release
cmake --build . --target INSTALL --config Release
```

{{% notice Note %}}
The build takes approximately 20 mins on Lenovo X13s
{{% /notice %}}

When the build and the install is complete, confirm the shared library have been created:

```bash { output_lines = "2-12,14-22" }
ls ./install/x64/vc17/bin
    Directory: C:\Users\kokmit01\work\opencv\build_msvc\install\x64\vc17\bin
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        07/11/2024     21:56          43008 opencv_annotation.exe
-a----        07/11/2024     21:56         143872 opencv_interactive-calibration.exe
-a----        07/11/2024     21:56          41984 opencv_model_diagnostics.exe
-a----        07/11/2024     22:03          36864 opencv_version.exe
-a----        07/11/2024     22:03          35328 opencv_version_win32.exe
-a----        07/11/2024     16:11       26391552 opencv_videoio_ffmpeg4100_64.dll
-a----        07/11/2024     22:03          56320 opencv_visualisation.exe
-a----        07/11/2024     21:56       27175936 opencv_world4100.dll
ls ./install/x64/vc17/lib
    Directory: C:\Users\kokmit01\work\opencv\build_msvc\install\x64\vc17\lib
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        07/11/2024     16:11            434 OpenCVConfig-version.cmake
-a----        07/11/2024     16:11          15260 OpenCVConfig.cmake
-a----        07/11/2024     16:11            972 OpenCVModules-release.cmake
-a----        07/11/2024     16:11           3879 OpenCVModules.cmake
-a----        07/11/2024     21:56        2849862 opencv_world4100.lib
```

{{% notice Note %}}
The directory name in the middle is "x64," but there is no need to worry as the generated libraries and executable files will definitely run as ARM64.
{{% /notice %}}

```bash { output_lines = "2" }
./install/x64/vc17/bin/pencv_version.exe
4.10.0
```

## Build OpenCV Applications


Add C:\Users\kokmit01\work\opencv\build\install\x64\vc17\bin to PATH environment variable (for access to dll)
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
    cv::imwrite("test_image.png", image);
    cv::waitKey(0);
    return 0;
}
```