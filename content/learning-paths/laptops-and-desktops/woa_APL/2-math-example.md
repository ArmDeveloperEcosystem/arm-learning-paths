---
title: Build a simple math application and profiling the performance
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Import an sample project from GitHub..

trace code... [x86 w/o apl]


useAPL = false: Using a Multithreaded Approach with Semaphores
This path focuses on leveraging multiple CPU cores to parallelize the vertex rotation. The code uses semaphores to manage synchronization between worker threads that will perform the work.


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

### Using threading to calcuate 

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

        // do the matrix multiplication and scale
        // [ x, y, z]     [ rotation 0, rotation 1, rotation 2]    [newx, newy, newz]
        //            dot [ rotation 3, rotation 4, rotation 5]  = 
        //                [ rotation 6, rotation 7, rotation 8]     

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


## Profiling


### Quick conclusion



## Build and Test


## Profiling


### Quick conclusion
