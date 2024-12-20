---
title: Using Arm Performance Library to accalerate your WoA application
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Insturction APL, install ref,

## Check include and lib folder

## Add lib include into VS

## BLAS code explaination, another RotateCube path

## Setup define, rebuild the project (code size check??)

## Execution, check cpu/mem usage


![img1](apl_disable.gif)

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
