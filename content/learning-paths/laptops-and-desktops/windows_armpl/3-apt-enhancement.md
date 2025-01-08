---
title: Using Arm Performance Libraries to accalerate your WoA application
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduce Arm Performance Libraries
In the previous session, we gained some understanding of the performance of the first calculation option. 
Now, we will try Arm Performance Libraries and explore the differences in performance.

[Arm Performance Libraries](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Libraries) provides optimized standard core math libraries for numerical applications on 64-bit Arm-based processors. The libraries are built with OpenMP across many BLAS, LAPACK, FFT, and sparse routines in order to maximize your performance in multi-processor environments.

Follow this [learning path](https://learn.arm.com/install-guides/armpl/) to install Arm Performance Libraries on Windows 11. 
You can also reference this [document](https://developer.arm.com/documentation/109361/latest/) about Arm Performance Libraries on Windows.

After successful installation, you'll find five directories in the installation folder. The `include` and `lib` are the directories contain include header files and library files, respectively. Please take note of these two directories, as we'll need them for Visual Studio setup later.


 ![img9](./figures/apl_directory.png)

## Include Arm Performance Libraries into Visual Studio

To utilize the provided performance optimizations on Arm Performance Libraries, you need to manually add the paths into Visual Studio.

You need to configure two places in your Visual Studio projects:
 - #### External Include Directories:

    1. In the Solution Explorer, right-click on your project and select "Properties". 
    2. In the left pane of the Property Pages, expand "Configuration Properties". Select "VC++ Directories"
    3. In the right pane, find the "Additional Include Directories" setting.
    4. Click on the dropdown menu. Select "<Edit...>"
    5. In the dialog that opens, click the "New Line" icon to add Arm Performance Libraries `include` path.
    ![img10](./figures/ext_include.png)
 
 - #### Additional Library Directories:

    1. In the Solution Explorer, right-click on your project and select "Properties". 
    2. In the left pane of the Property Pages, expand "Configuration Properties". Select "Linker"
    3. In the right pane, find the "Additional Library Directories" setting.
    4. Click on the dropdown menu. Select "<Edit...>"
    5. In the dialog that opens, click the "New Line" icon to add Arm Performance Libraries `library` path.
    ![img10](./figures/linker_lib.png)


{{% notice Note %}}

Visual Studio allows users to set the above two paths for each individual configuration. To apply the settings to all configurations in your project, select "All Configurations" in the "Configuration" dropdown menu.
{{% /notice %}}



 ## Calculation Option#2 -- Arm Performance Libraries

You are now ready to use Arm Performance Libraries in your project.
Open the souece code file `SpinTheCubeInGDI.cpp` and search for the `_USE_ARMPL_DEFINES` definition.
Removing the comment will enable the Arm Performance Libraries feature.

When variable useAPL is True, the application will call `applyRotationBLAS()` instead of multithreading code to apply the rotation matrix to the 3D vertices.

```c++
void RotateCube(int numCores)
{
    rotationAngle += 0.00001;
    if (rotationAngle > 2 * M_PI)
    {
        rotationAngle -= 2 * M_PI;
    }

    // rotate around Z and Y
    rotationInX[0] = cos(rotationAngle) * cos(rotationAngle);
    rotationInX[1] = -sin(rotationAngle);
    rotationInX[2] = cos(rotationAngle) * sin(rotationAngle);
    rotationInX[3] = sin(rotationAngle) * cos(rotationAngle);
    rotationInX[4] = cos(rotationAngle);
    rotationInX[5] = sin(rotationAngle) * sin(rotationAngle);
    rotationInX[6] = -sin(rotationAngle);
    rotationInX[7] = 0;
    rotationInX[8] = cos(rotationAngle);

    if (useAPL)
    {
        applyRotationBLAS(UseCube ? cubeVertices : sphereVertices, rotationInX);
    }
    else
    {
        for (int x = 0; x < numCores; x++)
        {
            ReleaseSemaphore(semaphoreList[x], 1, NULL);
        }
        WaitForMultipleObjects(numCores, doneList.data(), TRUE, INFINITE);
    }

    Calculations++;
}
```

`applyRotationBLAS()` adopts BLAS matrix multiplier instead of multithreading for calculate implementation.

Basic Linear Algebra Subprograms (BLAS) are a set of well defined basic linear algebra operations in Arm Performance Libraries, check [cblas_dgemm](https://developer.arm.com/documentation/101004/2410/BLAS-Basic-Linear-Algebra-Subprograms/CBLAS-functions/cblas-dgemm?lang=en) to learn more about the function.

```c++
void applyRotationBLAS(std::vector<double>& shape, const std::vector<double>& rotMatrix)
{
    EnterCriticalSection(&cubeDraw[0]);
#if defined(_M_ARM64) && defined(_USE_ARMPL_DEFINES)
    // Call the BLAS matrix mult for doubles. 
    // Multiplies each of the 3d points in shape 
    // list with rotation matrix, and applies scale
    cblas_dgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans, (int)shape.size() / 3, 3, 3, scale, shape.data(), 3, rotMatrix.data(), 3, 0.0, drawSphereVertecies.data(), 3);
#endif
    LeaveCriticalSection(&cubeDraw[0]);
}
```

## Build and Test

Rebuild the code and run `SpinTheCubeInGDI.exe` again, You'll see the Frame Rate has increased. 
On my machine, the performance stably remains between 11 and 12.

![gif2](./figures/apl_enable.gif)

Re-running profiling tools, you can see that the CPU usage has decreased significantly. There is no difference in memory usage.
 ![img11](./figures/apl_on_cpu_mem_usage.png)

## Conclusion:

This example demonstrates that Arm Performance Libraries on Windows can improve performance for specific workloads.


