---
title: Build a simple math application and profiling the performance
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Clone Example from GitHub

We use a Windows application that renders a rotating 3D cube to perform the calculations on different programming options.

First, clone this Windows application repository from GitHub:

```cmd
git clone https://github.com/odincodeshen/SpinTheCubeInGDI.git
```

{{% notice Note %}}
To facilitate explaining the topic, this repository is forked from the original author [here](https://github.com/marcpems/SpinTheCubeInGDI) with some modifications to aid in the following explanations.
{{% /notice %}}

## Quick Introduction

Click the SpinTheCubeInGDI.sln to open the project.
This source code implements a Windows application that renders a spinning 3D cube.

Four of key components are:
 - Shape Generation: Generates the vertices for a sphere using a golden ratio-based algorithm.
 - Rotation Calculation: 
   The application uses a rotation matrix to rotate the 3D shape around the X, Y, and Z axes. The rotation angle is incremented over time, creating the animation. This code apply two options to calculate:
    - Multithreading: The application utilizes multithreading to improve performance by distributing the rotation calculations across multiple threads.
    - Arm Performance Libraries: Used for optimized calculations. (Explained in the next session)
 - Drawing: The application draws the transformed vertices of the shapes on the screen, using Windows API.
 - Performance Measurement: The code measures and displays the number of transforms per second.


## Calculation Option#1 -- Multithreading

In this learning path, our focus is on the impact of different Calculation option on performance.
The multithreading implement on the project involved two of functions:
 - CalcThreadProc():
    
    This function is the entry point for each calculation thread.  Each calculation thread waits on its semaphore in semaphoreList.
   
    When a thread receives a signal, it calls `applyRotation()` to transform its assigned vertices. The updated vertices are stored in the drawSphereVertecies vector
   
    ```c++
    DWORD WINAPI CalcThreadProc(LPVOID data)
    {
        // need to know where to start and where to end
        int threadNum = LOWORD(data);
        int threadCount = HIWORD(data);
        int pointStride = spherePoints / threadCount;

        while (!closeThreads)
        {
            // wait on a semaphore
            WaitForSingleObject(semaphoreList[threadNum], INFINITE);

            EnterCriticalSection(&cubeDraw[threadNum]);
            // run the calculations for the set of points - need to be global
            applyRotation(UseCube ? cubeVertices : sphereVertices, rotationInX, threadNum * pointStride, pointStride);
            LeaveCriticalSection(&cubeDraw[threadNum]);

            // set a semaphore to say we are done
            ReleaseSemaphore(doneList[threadNum], 1, NULL);
        }

        return 0;
    }
    ```
 
 - applyRotation():
    This function applies the rotation matrix to a subset of the shape's vertices.

    ```c++
    void applyRotation(std::vector<double>& shape, const std::vector<double>& rotMatrix, int startPoint, int stride)
    {
        double refx, refy, refz;

        // Start looking at the reference verticies 
        auto point = shape.begin();
        point += startPoint * 3;

        // Start the output transformed verticies 
        auto outpoint = drawSphereVertecies.begin();
        outpoint += startPoint * 3;

        int counter = 0;
        while (point != shape.end() && counter < stride)
        {
            counter++;

            // take the next three values for a 3d point
            refx = *point; point++;
            refy = *point; point++;
            refz = *point; point++;

            *outpoint = scale * rotMatrix[0] * refx + 
                        scale * rotMatrix[3] * refy + 
                        scale * rotMatrix[6] * refz; outpoint++;

            *outpoint = scale * rotMatrix[1] * refx + 
                        scale * rotMatrix[4] * refy + 
                        scale * rotMatrix[7] * refz; outpoint++;

            *outpoint = scale * rotMatrix[2] * refx + 
                        scale * rotMatrix[5] * refy + 
                        scale * rotMatrix[8] * refz; outpoint++;
        }
    }
    ```


## Build and Test

After gaining a general understanding of the project, you can compile it. 
Build the project, and once successful, run `SpinTheCubeInGDI.exe`.

You'll see a simulated 3D sphere continuously rotating. The number in the upper-left corner represents the number of frames per second (FPS). A higher number indicates better performance, and vice versa.

 ![gif1](./figures/multithreading.gif)

On my test machine, the performance generally falls between 3 and 6 FPS, which is unstable.

{{% notice Note %}}
Performance may vary depending on the hardware and the system load at the time of testing.
{{% /notice %}}


You can also use the [profiling tools](https://learn.microsoft.com/en-us/visualstudio/profiling/profiling-feature-tour?view=vs-2022) to observe the dynamic CPU and memory usage while the program is running.
 ![img8](./figures/mt_cpumem_usage1.png)


