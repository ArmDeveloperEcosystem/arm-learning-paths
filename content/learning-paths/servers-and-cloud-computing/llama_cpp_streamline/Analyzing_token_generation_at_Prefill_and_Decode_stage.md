---
title: Analyze token generation at Prefill and Decode stage
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Analyze token generation at Prefill and Decode stage
To get a visible token generation view at Prefill and Decode stage, Annotation Marker feature of Streamline is used and the Annotation Marker generation code is integrated to the llama.cpp project. 
You can find more information about Annotation Marker feature here, https://developer.arm.com/documentation/101816/9-7/Annotate-your-code?lang=en. 

## Steps of llama.cpp integration and Streamline setup

### Step 1: Build Streamline Annotation library
Install ArmDS or Arm Streamline on your host PC first. 
You can get Streamline Annotation support code in the installation directory such as *"Arm\Development Studio 2024.1\sw\streamline\gator\annotate"*. 
You also can get the Annotation support code here, https://github.com/ARM-software/gator/tree/main , please download the right code that matches the version of Streamline tool on your host PC.

Then you can build the Streamline Annotation Library by running 
```bash
make CROSS_COMPILE=/path/to/aarch64_linux_gcc_tool 
```

for example,
```bash
make CROSS_COMPILE=./Work/arm-gnu-toolchain-13.3.rel1-x86_64-aarch64-none-linux-gnu/bin/aarch64-none-linux-gnu- 
```
You can get the aarch64 gcc compiler toolchain here, https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads .

The static linked library, libstreamline_annotate.a, will be produced. 

### Step 2: Integrate Annotation Marker code to llama.cpp
Download llama.cpp code from  https://github.com/ggml-org/llama.cpp/archive/refs/tags/b6202.tar.gz 
Go to llama.cpp root directory and create a directory ‘streamline_annotation’ there. 
```bash
cd ./llama.cpp
mkdir streamline_annotation
```

Copy the library ‘libstreamline_annotate.a’ and the header file ‘streamline_annotate.h’ from Step 1 to the directory ‘streamline_annotation’.

To link 'libstreamline_annotate.a' library when building llama-cli, change *llama.cpp\CMakeLists.txt* by adding following lines,

```makefile
set(STREAMLINE_LIB_PATH  ${CMAKE_SOURCE_DIR}/streamline_annotation/libstreamline_annotate.a)
target_include_directories(llama-cli PRIVATE ${CMAKE_SOURCE_DIR}/streamline_annotation)
target_link_libraries(${TARGET} PRIVATE ${STREAMLINE_LIB_PATH} )
```

To add Annotation Markers to llama-cli, change the llama-cli code *llama.cpp/tools/main/main.cpp* by adding
```c
#include "streamline_annotate.h" 
```
and the Annotation Marker code in the 'main' function,

Firstly, add the Streamline Annotation setup code after *common_init*, 
```c
    common_init();
 
    //Add the Annotation setup code
    ANNOTATE_SETUP;

```


then add the Annotation Marker generation code here, 


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

A string is added to the Annotation Marker to record the position of input tokens and numbr of tokens to be processed.

### Step 3: Build llama-cli executable 
For convenience, llama-cli is static linked. 

Firstly, create a new directory ‘build’ understand llama.cpp root directory and go into it.
```bash
mkdir ./build & cd ./build
```
Then configure the project by running 
```bash
cmake .. -DCMAKE_SYSTEM_NAME=Linux  -DCMAKE_SYSTEM_PROCESSOR=arm -DCMAKE_C_COMPILER=aarch64-none-linux-gnu-gcc -DCMAKE_CXX_COMPILER=aarch64-none-linux-gnu-g++ -DLLAMA_NATIVE=OFF -DLLAMA_F16C=OFF  -DLLAMA_GEMM_ARM=ON -DBUILD_SHARED_LIBS=OFF  -DCMAKE_EXE_LINKER_FLAGS="-static -g" -DGGML_OPENMP=OFF -DCMAKE_C_FLAGS="-march=armv8.2-a+i8mm+dotprod -g" -DCMAKE_CXX_FLAGS="-march=armv8.2-a+dotprod+i8mm -g" -DGGML_CPU_KLEIDIAI=ON -DGGML_OPENMP=OFF -DLLAMA_BUILD_TESTS=OFF -DLLAMA_BUILD_EXAMPLES=ON  -DLLAMA_CURL=OFF
```

Set CMAKE_C_COMPILER and DCMAKE_CXX_COMPILER to your cross compiler path. Make sure that “-march” in DCMAKE_C_FLAGS and CMAKE_CXX_FLAGS matches your Arm CPU hardware. 

In this guide, we run llama-cli on an Arm CPU which supports NEON Dotprod and I8MM instructions, so ‘-march’ is specified as ‘armv8.2-a+dotprod+i8mm’. We also specify ‘-static’ and ‘-g’ options so that the llama-cli executable is static linked and with debug info. This makes source code/function level profiling easier and the llama-cli executable runnable on various version of Arm64 Linux/Android.

Now, we can build the project by running
```bash
cmake --build ./ --config Release
```

After the building process, you should find the llama-cli executable in *./build/bin/* directory.

### Step 4: Run llama-cli and analyze the data with Streamline
Copy following files to your Arm64 platform,
* llama-cli executable 
* the ‘gatord’ executable in Arm DS or Streamline installation folder, such as *Arm\Development Studio 2024.1\sw\streamline\bin\linux\arm64*  for Linux and *Arm\Development Studio 2024.1\sw\streamline\bin\android\arm64* for Android
* the LLM model, Qwen1_5-0_5b-chat-q4_0.gguf

Then run the gatord on your Arm64 target
```bash
./gatord
```
You should see similar messages as below, 

``` bash
Streamline Data Recorder v9.4.0 (Build 9b1e8f8)
Copyright (c) 2010-2024 Arm Limited. All rights reserved.
Gator ready
```

Then launch the Streamline application on your host PC, connect to the gatord running on your Arm64 target with either TCP or ADB connection. You can select PMU events to be monitored at this point. 

![text#center](images/streamline_capture.png "Figure 6. Streamline Start Capture ")

Set the path of llama-cli executable for Streamline so that its debug info can be used for analysis.

![text#center](images/streamline_capture_image.png "Figure 7. Streamline image path")

Click ‘Start Capture’ button on Streamline to start collecting data from the Arm64 target.

*Note: This guide is not intended to introduce how to use Streamline, if you encounter any issue during setting up gatord or Streamline, please seek for help from Arm support.*

Now, run the llama-cli executable as below,

``` bash
./llama-cli -m qwen1_5-0_5b-chat-q4_0.gguf -p "<|im_start|>system\nYou are a helpful AI assistant.<|im_end|>\n<|im_start|>user\nTell me a story about a fox and a crow? Please do not tell the traditional story in Aesop's fables. Please tell me a positive story about friendship and love. The story should have no more than 400 words<|im_end|>\n<|im_start|>assistant\n" -st -t 1
``` 

After a while, you can stop the Streamline data collection by clicking ‘Stop’ button on Streamline. Then Streamline tool on your host PC will start the data analysis.

## Analyze the data with Streamline
From the timeline view of Streamline, we can see some Annotation Markers. Since we add an Annotation Marker before llama_decode function, each Annotation Marker marks the start time of a token generation. 

![text#center](images/annotation_marker_1.png "Figure 8. Annotation Marker")

The string in the Annotation Marker can be shown when clicking those Annotation Markers. For example,

![text#center](images/annotation_marker_2.png "Figure 9. Annotation String")

The number after ‘past’ indicates the position of input tokens, the number after ‘n_eval’ indicates the number of tokens to be processed this time.

As shown in the timeline view below, with help of Annotation Markers, we can clearly identify the Prefill stage and Decode stage. 

![text#center](images/annotation_marker_prefill.png "Figure 10. Annotation Marker at Prefill and Decode stage")

By checking the string of Annotation Marker, the first token generation at Prefill stage has 'past 0, n_eval 78', which means that the position of input tokens starts at 0 and there are 78 input tokens to be processed. 
We can see that the first token generated at Prefill stage takes more time, since 78 input tokens have to be processed at Prefill stage, it performs lots of GEMM operations. At Decode stage, tokens are generated one by one at mostly equal speed, one token takes less time than that of Prefill stage, thanks to the effect of KV cache. At Decode stage, it performs many GEMV operations.

We can further investigate it with PMU event counters that are captured by Streamline. At Prefill stage, the amount of computation, which are indicated by PMU event counters that count number of Advanced SIMD (NEON), Floating point, Integer data processing instruction, is large. However, the memory access is relatively low. Especially, the number of L3 cache refill/miss is much lower than that of Decode stage.

At Decode stage, the amount of computation is relatively less (since the time of each token is less), but the number of L3 cache refill/miss goes much higher.
By monitoring other PMU events, Backend Stall Cycles and Backend Stall Cycles due to Memory stall, 

![text#center](images/annotation_pmu_stall.png "Figure 11. Backend stall PMU event")

We can see that at Prefill stage, Backend Stall Cycles due to Memory stall are only about 10% of total Backend Stall Cycles. However, at Decode stage, Backend Stall Cycles due to Memory stall are around 50% of total Backend Stall Cycles.
All those PMU event counters indicate that it is compute-bound at Prefill stage and memory-bound at Decode stage.

Now, let us further profile the code execution with Streamline. In the ‘Call Paths’ view of Streamline, we can see the percentage of running time of functions that are orginized in form of call stack.

![text#center](images/annotation_prefill_call_stack.png "Figure 12. Call stack")

In the ‘Functions’ view of Streamline, we can see the overall percentage of running time of functions.

![text#center](images/annotation_prefill_functions.png "Figure 13. Functions view")

As we can see, the function, graph_compute, takes the largest portion of the running time. It shows that large amounts of GEMM and GEMV operations take most of the time. With Qwen1_5-0_5b-chat-q4_0 model,
* The computation (GEMM and GEMV) of Q, K, V vectors and most of FFN layers: their weights are with Q4_0 data type and the input activations are with FP32 data type. The computation is forwarded to KleidiAI trait by *ggml_cpu_extra_compute_forward*. KleidiAI ukernels implemented with NEON Dotprod and I8MM vector instructions are used to accelerate the computation.
    - At Prefill stage, *kai_run_matmul_clamp_f32_qsi8d32p4x8_qsi4c32p4x8_16x4_neon_i8mm* KleidiAI ukernel is used for GEMM (Matrix Multiply) operators. It takes the advantage of NEON I8MM instruction. Since Prefill stage only takes small percentage of the whole time, the percentage of this function is small as shown in figures above. However, if we focus on Prefill stage only, with ‘Samplings’ view in Timeline. We can see *kai_run_matmul_clamp_f32_qsi8d32p4x8_qsi4c32p4x8_16x4_neon_i8mm* takes the largest portion of the whole Prefill stage.

    ![text#center](images/Prefill_only.png "Figure 14. Prefill only view")

    - At Decode stage, *kai_run_matmul_clamp_f32_qsi8d32p1x8_qsi4c32p4x8_1x4x32_neon_dotprod* KleidiAI ukernel is used for GEMV operators. It takes advantage of NEON Dotprod instruction. If we focus on Decode stage only, we can see this function takes the second largest portion. 

    ![text#center](images/Decode_only.png "Figure 15. Decode only view")

* There is a result_output linear layer in Qwen1_5-0_5b-chat-q4_0 model, the wights are with Q6_K data type. The layer computes a huge [1, 1024] x [1024, 151936] GEMV operation, where 1024 is the embedding size and 151936 is the vocabulary size. This operation cannot be handled by KleidiAI yet, it is handled by the ggml_vec_dot_q6_K_q8_K function in ggml-cpu library.
* The tensor nodes for computation of Multi-Head attention are presented as three-dimension matrices with FP16 data type (KV cache also holds FP16 values), they are computed by ggml_vec_dot_f16 function in ggml-cpu library.
* The computation of RoPE, Softmax, RMSNorm layers does not take significant portion of the running time.