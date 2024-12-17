---
title: Build a simple math application and profiling the performance
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Import an sample project from GitHub..

trace code... [x86 w/o apl]

```c
#include <jni.h>
#include "streamline_annotate.h"

JNIEXPORT void JNICALL Java_AnnotateStreamline_AnnotateSetup(JNIEnv* env, jobject obj) {
    gator_annotate_setup();
}

JNIEXPORT jlong JNICALL Java_AnnotateStreamline_GetTime(JNIEnv* env, jobject obj) {
    return gator_get_time();
}
```


## Build and Test


## Profiling


### Quick conclusion



```cmake
# Sets the minimum CMake version required for this project.
cmake_minimum_required(VERSION 3.22.1)

# Declare the project name. 
project("StreamlineAnnotationJNI")

# Create and name the library
add_library(${CMAKE_PROJECT_NAME} SHARED
    annotate_jni_wrapper.c
    streamline_annotate.c)

# Specifies libraries CMake should link to your target library. 
# Adding in the Android system log library pulls in the NDK path.
find_library( # Sets the path to the NDK library.
        log-lib
        log )

target_link_libraries( # Specifies the target library.
        ${CMAKE_PROJECT_NAME}
        ${log-lib} )
```

## Build and Test


## Profiling


### Quick conclusion
