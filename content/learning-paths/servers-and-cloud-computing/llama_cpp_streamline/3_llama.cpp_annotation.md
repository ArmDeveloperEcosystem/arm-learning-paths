---
title: Integrate Streamline Annotations into llama.cpp
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Integrate Streamline Annotations into llama.cpp

To visualize token generation at the Prefill and Decode stages, you can use Streamline's Annotation Marker feature.  

This requires integrating annotation support into the llama.cpp project.  

More information about the Annotation Marker API can be found in the [Streamline User Guide](https://developer.arm.com/documentation/101816/9-7/Annotate-your-code?lang=en).

{{% notice Note %}}
You can either build natively on an Arm platform, or cross-compile on another architecture using an Arm cross-compiler toolchain.
{{% /notice %}}

### Step 1: Build Streamline Annotation library

Install [Arm DS](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio) or [Arm Streamline](https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer) on your development machine first.

Streamline Annotation support code is in the installation directory such as `Arm/Development Studio 2024.1/sw/streamline/gator/annotate`.

For installation guidance, refer to the [Streamline installation guide](/install-guides/streamline/).

Clone the gator repository that matches your Streamline version and build the `Annotation support library`.

The installation step depends on your development machine.

For Arm native build, you can use the following instructions to install the packages.

For other machines, you need to set up the cross compiler environment by installing [Arm GNU toolchain](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads).

You can refer to the [GCC install guide](https://learn.arm.com/install-guides/gcc/cross/) for cross-compiler installation.

{{< tabpane code=true >}}
  {{< tab header="Arm Native Build" language="bash">}}
    apt-get update
    apt-get install ninja-build cmake gcc g++ g++-aarch64-linux-gnu curl zip unzip tar pkg-config git
    cd ~
    git clone https://github.com/ARM-software/gator.git
    cd gator
    ./build-linux.sh
    cd annotate
    make  
  {{< /tab >}}
  {{< tab header="Cross Compiler" language="bash">}}
    apt-get update
    apt-get install ninja-build cmake gcc g++ g++-aarch64-linux-gnu curl zip unzip tar pkg-config git
    cd ~
    git clone https://github.com/ARM-software/gator.git
    cd gator
    make CROSS_COMPILE=/path/to/aarch64_linux_gcc_tool
  {{< /tab >}}
{{< /tabpane >}}

Once complete, the static library `libstreamline_annotate.a` will be generated at `~/gator/annotate/libstreamline_annotate.a` and the header file is at `gator/annotate/streamline_annotate.h`.

### Step 2: Integrate Annotation Marker into llama.cpp

Next, you need to install llama.cpp to run the LLM model.

{{% notice Note %}}
To make the performance profiling content easier to follow, this Learning Path uses a specific release version of llama.cpp to ensure the steps and results remain consistent.
{{% /notice %}}

Before building llama.cpp, create a directory `streamline_annotation` and copy the library `libstreamline_annotate.a` and the header file `streamline_annotate.h` into the new directory. 

```bash
cd ~
wget https://github.com/ggml-org/llama.cpp/archive/refs/tags/b6202.tar.gz 
tar -xvzf b6202.tar.gz
mv llama.cpp-b6202 llama.cpp
cd ./llama.cpp
mkdir streamline_annotation
cp ~/gator/annotate/libstreamline_annotate.a ~/gator/annotate/streamline_annotate.h streamline_annotation
```

To link the `libstreamline_annotate.a` library when building llama-cli, add the following lines at the end of `llama.cpp/tools/main/CMakeLists.txt`.

```makefile
set(STREAMLINE_LIB_PATH "${CMAKE_SOURCE_DIR}/streamline_annotation/libstreamline_annotate.a")
target_include_directories(llama-cli PRIVATE "${CMAKE_SOURCE_DIR}/streamline_annotation")
target_link_libraries(llama-cli PRIVATE "${STREAMLINE_LIB_PATH}")
```

To add Annotation Markers to `llama-cli`, change the `llama-cli` code in `llama.cpp/tools/main/main.cpp` by adding the include file:

```c
#include "streamline_annotate.h" 
```

After the call to `common_init()`, add the setup macro:

```c
    common_init();
    //Add the Annotation setup code
    ANNOTATE_SETUP;
```

Finally, add an annotation marker inside the main loop:

```c
          for (int i = 0; i < (int) embd.size(); i += params.n_batch) {
                int n_eval = (int) embd.size() - i;
                if (n_eval > params.n_batch) {
                    n_eval = params.n_batch;
                }

                LOG_DBG("eval: %s\n", string_from(ctx, embd).c_str());
	
                // Add annotation marker code for Streamline
                {
                  char printf_buf[200];
                  sprintf(printf_buf, "past %d, n_eval %d", n_past,n_eval );
                  ANNOTATE_MARKER_STR(printf_buf);
                }
                // End of annotation marker 

                if (llama_decode(ctx, llama_batch_get_one(&embd[i], n_eval))) {
                    LOG_ERR("%s : failed to eval\n", __func__);
                    return 1;
                }
```

A string is added to the Annotation Marker to record the position of input tokens and number of tokens to be processed.

### Step 3: Build llama-cli

For convenience, llama-cli is statically linked.

Create a new directory `build` under the llama.cpp root directory and change to the new directory: 

```bash
cd ~/llama.cpp
mkdir build && cd build
```

Next, configure the project.

{{< tabpane code=true >}}
  {{< tab header="Arm Native Build" language="bash">}}
    cmake .. \
      -DGGML_NATIVE=ON \
      -DLLAMA_F16C=OFF \
      -DLLAMA_GEMM_ARM=ON \
      -DBUILD_SHARED_LIBS=OFF \
      -DCMAKE_EXE_LINKER_FLAGS="-static -g" \
      -DGGML_OPENMP=OFF \
      -DCMAKE_C_FLAGS="-march=armv8.2-a+dotprod+i8mm -g" \
      -DCMAKE_CXX_FLAGS="-march=armv8.2-a+dotprod+i8mm -g" \
      -DGGML_CPU_KLEIDIAI=ON \
      -DLLAMA_BUILD_TESTS=OFF \
      -DLLAMA_BUILD_EXAMPLES=ON \
      -DLLAMA_CURL=OFF  
  {{< /tab >}}
  {{< tab header="Cross Compiler" language="bash">}}
    cmake .. \
      -DCMAKE_SYSTEM_NAME=Linux \
      -DCMAKE_SYSTEM_PROCESSOR=arm \
      -DCMAKE_C_COMPILER=aarch64-none-linux-gnu-gcc \
      -DCMAKE_CXX_COMPILER=aarch64-none-linux-gnu-g++ \
      -DLLAMA_NATIVE=OFF \
      -DLLAMA_F16C=OFF \
      -DLLAMA_GEMM_ARM=ON \
      -DBUILD_SHARED_LIBS=OFF \
      -DCMAKE_EXE_LINKER_FLAGS="-static -g" \
      -DGGML_OPENMP=OFF \
      -DCMAKE_C_FLAGS="-march=armv8.2-a+dotprod+i8mm -g" \
      -DCMAKE_CXX_FLAGS="-march=armv8.2-a+dotprod+i8mm -g" \
      -DGGML_CPU_KLEIDIAI=ON \
      -DLLAMA_BUILD_TESTS=OFF \
      -DLLAMA_BUILD_EXAMPLES=ON \
      -DLLAMA_CURL=OFF
  {{< /tab >}}
{{< /tabpane >}}


Set `CMAKE_C_COMPILER` and `CMAKE_CXX_COMPILER` to your cross compiler path. Make sure that -march in `CMAKE_C_FLAGS` and `CMAKE_CXX_FLAGS` matches your Arm CPU hardware. 


With the flags above you can run `llama-cli` on an Arm CPU that supports NEON dot product and 8-bit integer multiply (i8mm) instructions.  

The `-static` and `-g` options are also specified to produce a statically linked executable, so it can run on different Arm64 Linux/Android environments without needing shared libraries and to include debug information, which makes source code and function-level profiling in Streamline much easier.  

Now you can build the project using `cmake`: 

```bash
cd ~/llama.cpp/build
cmake --build ./ --config Release
```

After the building process completes, you can find the `llama-cli` in the `~/llama.cpp/build/bin/` directory.

You now have an annotated version of `llama-cli` ready for Streamline.