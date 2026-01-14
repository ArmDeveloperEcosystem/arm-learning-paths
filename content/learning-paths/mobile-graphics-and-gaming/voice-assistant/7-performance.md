---

title: Performance

weight: 9

### FIXED, DO NOT MODIFY

layout: learningpathall

---

## Benchmarking LLM on Android phone

You can also benchmark the LLM functionality on Android phone outside of RTVA application. For this, you can use the Large Language Models repository:

```
https://gitlab.arm.com/kleidi/kleidi-examples/large-language-models
```

and build for your chosen LLM backend, ensure that `NDK_PATH` is set properly. SME kernels are enabled by default, so let's first build with SME disabled:

```
cmake --preset=x-android-aarch64 -B build/ -DBUILD_BENCHMARK=ON -DLLM_FRAMEWORK=mnn -DMNN_SME2=OFF
cmake --build ./build
```

{{% notice %}}
For troubleshooting any build issues, refer to [large-language-models README](https://gitlab.arm.com/kleidi/kleidi-examples/large-language-models/-/blob/main/README.md?ref_type=heads)
{{% /notice %}}

### Phone setup

Now that you have all the libraries and executables needed, you can create a benchmarking directory and push the needed libraries to the phone:

```sh
adb shell mkdir /data/local/tmp/benchmark_test/
adb push build/lib/* /data/local/tmp/benchmark_test/
```
```output
build/lib/archive/: 9 files pushed. 140.0 MB/s (36970298 bytes in 0.252s)
build/lib/libMNN.so: 1 file pushed. 139.5 MB/s (4973176 bytes in 0.034s)
build/lib/libarm-llm-jni.so: 1 file pushed. 153.8 MB/s (3832152 bytes in 0.024s)
11 files pushed. 137.0 MB/s (45775626 bytes in 0.319s)
```

This will copy the executables you can run:
```sh
adb push build/bin/* /data/local/tmp/benchmark_test/
```
```output
build/bin/arm-llm-bench-cli: 1 file pushed. 134.3 MB/s (3415344 bytes in 0.024s)
build/bin/llm-cpp-tests: 1 file pushed. 157.7 MB/s (17783848 bytes in 0.108s)
build/bin/llm_bench: 1 file pushed. 22.6 MB/s (85688 bytes in 0.004s)
build/bin/llm_demo: 1 file pushed. 12.6 MB/s (34656 bytes in 0.003s)
4 files pushed. 141.7 MB/s (21319536 bytes in 0.143s)
```
Finally, copy the models to benchmark:
```sh
adb push resources_downloaded/models/mnn/ /data/local/tmp/benchmark_test/
```

### Benchmarking the models

To make sure the screen stays on and the CPU is not throttled use the following commands:

```sh
adb shell svc power stayon true
adb shell dumpsys deviceidle disable
```

You can now run the executable in ADB shell, providing the path to libraries and the number of iterations to benchmark:

```sh
adb shell
cd /data/local/tmp/benchmark_test/
LD_LIBRARY_PATH=./ ./arm-llm-bench-cli -m mnn/llama-3.2-1b/ -i 128 -o 128 -t 1 -n 5 -w 1
```

As you see in the output, the flags used by executable are listed below:
* `-m` : path to the specific model or a directory with model and configuration files
* `-i` : number input tokens to use
* `-o` : number output tokens to generate
* `-t` : number of threads to use
* `-n` : number of iterations used for benchmarking
* `-w` : number of warmup iterations, not included in benchmarking

```output

=== ARM LLM Benchmark ===

Parameters:
  model_path         : mnn/llama-3.2-1b/
  num_input_tokens   : 128
  num_output_tokens  : 128
  num_threads        : 1
  num_iterations     : 5
  num_warmup         : 1


======= Results =========

| Framework          | Threads | Test   | Performance                |
| ------------------ | ------- | ------ | -------------------------- |
| mnn                | 1       | pp128  |   196.446 ±  0.377 (t/s)   |
| mnn                | 1       | tg128  |    27.222 ±  0.369 (t/s)   |
| mnn                | 1       | TTFT   |   687.931 ±  2.279 (ms)    |
| mnn                | 1       | Total  |  5354.526 ± 63.163 (ms)    |

```

To get benchmark numbers with use of SME kernels, you can rerun the full Benchmarking LLM on Android phone section without using `MNN_SME` flag as follows, which will leave SME instructions enabled by default:

```
cmake --preset=x-android-aarch64 -B build/ -DBUILD_BENCHMARK=ON -DLLM_FRAMEWORK=mnn
cmake --build ./build
```


## Example performance with a Vivo X300 Android phone

The table table shows the measurements taken on a Vivo X300 Android phone:

| LLM Framework     | Model                 | Threads | Without SME2   | With SME2 | Uplift   |
|-------------------|-----------------------|---------|----------------|-----------|----------|
| mnn               | qwen25vl-3b           | 1       | 33             | 134       | 306.06 % |
|                   |                       | 2       | 51             | 140       | 174.51 % |
|                   | llama-3.2-1B          | 1       | 196            | 339       | 72.96 %  |
|                   |                       | 2       | 275            | 396       | 44.00 %  |
| llama.cpp	    | qwen-2-VL             | 1       | 113            | 146       | 29.20 %  |
|                   |                       | 2       | 92             | 139       | 51.09 %  |
|                   | llama-3.2-1B          | 1       | 148            | 173       | 16.89 %  |
|                   |                       | 2       | 124            | 191       | 54.03 %  |
|                   | phi-2                 | 1       | 58             | 77        | 32.76 %  |
|                   |                       | 2       | 46             | 60        | 30.43 %  |


{{% notice Note %}}
The Android system enforces throttling, so your own results may vary slightly.
{{% /notice %}}

These measurements show how fast the model processes (encodes) 128 input tokens when running on a single CPU thread. As the results illustrate, SME2 delivers a significant performance boost even when using just one or two CPU cores on an Android phone, meaning faster processing without needing to involve multiple CPU cores.

