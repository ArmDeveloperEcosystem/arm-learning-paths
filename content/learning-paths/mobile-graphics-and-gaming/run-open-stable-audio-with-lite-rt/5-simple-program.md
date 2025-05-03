---
title: Create a simple program
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create and build a simple program

We can now set up a simple program and build it with CMake 

https://git.research.arm.com/gen-ai/sai/audio-stale-open-litert/-/blob/main/runner/

```
 cmake -B build -DTF_LIB_PATH=/home/nindro01/playground/LiteRT/output-base/execroot/litert/bazel-out/k8-opt/bin/tflite -DTF_INCLUDE_PATH=/home/nindro01/playground/LiteRT/third_party/tensorflow/ -DFLATBUFFER_INCLUDE_PATH=/home/nindro01/playground/flatbuffers/include/
 
cmake --build build

./build/audiogen_main 
```



