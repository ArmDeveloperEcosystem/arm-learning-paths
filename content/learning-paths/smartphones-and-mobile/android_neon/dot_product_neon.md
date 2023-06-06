---
# User change
title: "Implement dot product of two vectors"

weight: 3

layout: "learningpathall"
---

In this section you will implement the dot product of two vectors using C++. Starting from Armv8.4a architecture, the dot product is part of the instruction set. 

You will first implement the dot product of two vectors without using Neon intrinsics. Open `app/src/main/cpp/native-lib.cpp` from the Project pane and replace the contents of this file with the code below:
```console
#include <jni.h>
#include <string>
#include <arm_neon.h>
#include <chrono>

using namespace std;

short* generateRamp(short startValue, short len) {
    short* ramp = new short[len];

    for(short i = 0; i < len; i++) {
        ramp[i] = startValue + i;
    }

    return ramp;
}

double µsElapsedTime(chrono::system_clock::time_point start) {
    auto end = chrono::system_clock::now();

    return chrono::duration_cast<chrono::microseconds>(end - start).count();
}

chrono::system_clock::time_point now() {
    return chrono::system_clock::now();
}

int dotProduct(short* vector1, short* vector2, short len) {
    int result = 0;

    for(short i = 0; i < len; i++) {
        result += vector1[i] * vector2[i];
    }

    return result;
}
```

With this code, you have now implemented two helper methods `generateRamp` and `µsElapsedTime`.
`generateRamp` generates the ramp, which is the vector of 16-bit integers. The `µsElapsedTime` method is used to measure the code execution time. 

In the `dotProduct` method you calculate the dot product of two equal length vectors by multiplying the vectors element by element and then accumulating the resulting products. This implementation of dot product does not use Neon intrinsics.




