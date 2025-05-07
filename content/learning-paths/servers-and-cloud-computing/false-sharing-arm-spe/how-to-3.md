---
title: False Sharing Example
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Installing GoogleBenchmark from Source

We will use the Google benchmark framework to create a simple test structure. Since, as of writing, a binary is not available from the AL package manager, we build it from source. Follow the [official repositories instructions](https://github.com/google/benchmark) for more details. 

```bash
# Check out the library.
git clone https://github.com/google/benchmark.git
cd benchmark
cmake -E make_directory "build"
cmake -E chdir "build" cmake -DBENCHMARK_DOWNLOAD_DEPENDENCIES=on -DCMAKE_BUILD_TYPE=Release ../
cmake -DBENCHMARK_DOWNLOAD_DEPENDENCIES=on -DCMAKE_BUILD_TYPE=Release -S . -B "build"
cmake --build "build" --config Release -- -j$(nproc)
```

### Example

