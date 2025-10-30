---
title: Run Benchmark on Android phone
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build Llama runner binary for Android

Cross-compile Llama runner to run on Android using the steps below.

### 1. Set Android NDK

Set the environment variable to point to the Android NDK:

``` bash
export ANDROID_NDK=$ANDROID_HOME/ndk/28.0.12433566/
```

{{% notice Note %}}
Make sure you can confirm $ANDROID_NDK/build/cmake/android.toolchain.cmake is available for CMake to cross-compile.
{{% /notice %}}

### 2. Build ExecuTorch and associated libraries for Android with KleidiAI

You are now ready to build ExecuTorch for Android by taking advantage of the performance optimization provided by the [KleidiAI](https://gitlab.arm.com/kleidi/kleidiai) kernels.

Use `cmake` to cross-compile ExecuTorch:

``` bash
cmake -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake \
    -DANDROID_ABI=arm64-v8a \
    -DANDROID_PLATFORM=android-23 \
    -DEXECUTORCH_BUILD_EXTENSION_NAMED_DATA_MAP=ON \
    -DCMAKE_INSTALL_PREFIX=cmake-out-android \
    -DEXECUTORCH_ENABLE_LOGGING=1 \
    -DCMAKE_BUILD_TYPE=Release \
    -DEXECUTORCH_BUILD_EXTENSION_DATA_LOADER=ON \
    -DEXECUTORCH_BUILD_EXTENSION_MODULE=ON \
    -DEXECUTORCH_BUILD_EXTENSION_TENSOR=ON \
    -DEXECUTORCH_BUILD_EXTENSION_FLAT_TENSOR=ON \
    -DEXECUTORCH_BUILD_XNNPACK=ON \
    -DEXECUTORCH_BUILD_KERNELS_OPTIMIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_QUANTIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_CUSTOM=ON \
    -DEXECUTORCH_BUILD_KERNELS_LLM=ON \
    -DEXECUTORCH_BUILD_EXTENSION_LLM_RUNNER=ON \
    -DEXECUTORCH_BUILD_EXTENSION_LLM=ON \
    -DEXECUTORCH_BUILD_EXTENSION_RUNNER_UTIL=ON \
    -DEXECUTORCH_XNNPACK_ENABLE_KLEIDI=ON \
    -DXNNPACK_ENABLE_ARM_BF16=OFF \
    -DBUILD_TESTING=OFF \
    -Bcmake-out-android .

cmake --build cmake-out-android -j7 --target install --config Release
```
{{% notice Note %}}
Starting with Executorch version 0.7 beta, KleidiAI is enabled by default. The -DEXECUTORCH_XNNPACK_ENABLE_KLEIDI=ON option is enabled and adds default support for KleidiAI kernels in ExecuTorch with XNNPack.
{{% /notice %}}

### 3. Build Llama runner for Android

Use `cmake` to cross-compile Llama runner:

``` bash
cmake  -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake \
    -DANDROID_ABI=arm64-v8a \
    -DANDROID_PLATFORM=android-23 \
    -DCMAKE_INSTALL_PREFIX=cmake-out-android \
    -DCMAKE_BUILD_TYPE=Release \
    -DPYTHON_EXECUTABLE=python \
    -DEXECUTORCH_BUILD_KERNELS_OPTIMIZED=ON \
    -DBUILD_TESTING=OFF \
    -Bcmake-out-android/examples/models/llama \
    examples/models/llama

cmake --build cmake-out-android/examples/models/llama -j16 --config Release
```

You should now have `llama_main` available for Android.

{{% notice Note %}}
If you notice that Gradle cannot find the Android SDK, add the sdk.dir path to executorch/extension/android/local.properties.
{{% /notice %}}

## Run on Android via adb shell
You will need an Arm-powered smartphone with the i8mm feature running Android, with 16GB of RAM. The following steps were tested on a Google Pixel 8 Pro phone.

### 1. Connect your Android phone

Connect your phone to your computer using a USB cable.

You need to enable USB debugging on your Android device. You can follow [Configure on-device developer options](https://developer.android.com/studio/debug/dev-options) to enable USB debugging.

Once you have enabled USB debugging and connected via USB, run:

```
adb devices
```

You should see your device listed to confirm it is connected.

### 2. Copy the model, tokenizer, and Llama runner binary to the phone

``` bash
adb shell mkdir -p /data/local/tmp/llama
adb push llama3_1B_kv_sdpa_xnn_qe_4_64_1024_embedding_4bit.pte /data/local/tmp/llama/
adb push $HOME/.llama/checkpoints/Llama3.2-1B-Instruct/tokenizer.model /data/local/tmp/llama/
adb push cmake-out-android/examples/models/llama/llama_main /data/local/tmp/llama/
```


### 3. Run the model

Use the Llama runner to execute the model on the phone with the `adb` command:

``` bash
adb shell "cd /data/local/tmp/llama && ./llama_main --model_path llama3_1B_kv_sdpa_xnn_qe_4_64_1024_embedding_4bit.pte --tokenizer_path tokenizer.model --prompt '<|start_header_id|>system<|end_header_id|>\nYour name is Cookie. you are helpful, polite, precise, concise, honest, good at writing. You always give precise and brief answers up to 32 words<|eot_id|><|start_header_id|>user<|end_header_id|>\nHey Cookie! how are you today?<|eot_id|><|start_header_id|>assistant<|end_header_id|>' --warmup=1 --cpu_threads=5"
```

The output should look something like this.

```
I tokenizers:regex.cpp:27] Registering override fallback regex
I 00:00:00.003288 executorch:main.cpp:87] Resetting threadpool with num threads = 5
I 00:00:00.006393 executorch:runner.cpp:44] Creating LLaMa runner: model_path=llama3_1B_kv_sdpa_xnn_qe_4_64_1024_embedding_4bit.pte, tokenizer_path=tokenizer.model
E tokenizers:hf_tokenizer.cpp:60] Error parsing json file: [json.exception.parse_error.101] parse error at line 1, column 1: syntax error while parsing value - invalid literal; last read: 'I'
I 00:00:00.131486 executorch:llm_runner_helper.cpp:57] Loaded TikToken tokenizer
I 00:00:00.131525 executorch:llm_runner_helper.cpp:167] Reading metadata from model
I 00:00:00.186538 executorch:llm_runner_helper.cpp:110] Metadata: use_sdpa_with_kv_cache = 1
I 00:00:00.186574 executorch:llm_runner_helper.cpp:110] Metadata: use_kv_cache = 1
I 00:00:00.186578 executorch:llm_runner_helper.cpp:110] Metadata: get_max_context_len = 1024
I 00:00:00.186584 executorch:llm_runner_helper.cpp:110] Metadata: get_max_seq_len = 1024
I 00:00:00.186588 executorch:llm_runner_helper.cpp:110] Metadata: enable_dynamic_shape = 1
I 00:00:00.186596 executorch:llm_runner_helper.cpp:140] eos_id = 128009
I 00:00:00.186597 executorch:llm_runner_helper.cpp:140] eos_id = 128001
I 00:00:00.186599 executorch:llm_runner_helper.cpp:140] eos_id = 128006
I 00:00:00.186600 executorch:llm_runner_helper.cpp:140] eos_id = 128007
I 00:00:01.086570 executorch:text_llm_runner.cpp:89] Doing a warmup run...
I 00:00:01.087836 executorch:text_llm_runner.cpp:152] Max new tokens resolved: 128, given start_pos 0, num_prompt_tokens 54, max_context_len 1024
I 00:00:01.292740 executorch:text_prefiller.cpp:93] Prefill token result numel(): 128256

I 00:00:02.264371 executorch:text_token_generator.h:123]
Reached to the end of generation
I 00:00:02.264379 executorch:text_llm_runner.cpp:209] Warmup run finished!
I 00:00:02.264384 executorch:text_llm_runner.cpp:95] RSS after loading model: 1122.187500 MiB (0 if unsupported)
I 00:00:02.264624 executorch:text_llm_runner.cpp:152] Max new tokens resolved: 74, given start_pos 0, num_prompt_tokens 54, max_context_len 1024
<|start_header_id|>system<|end_header_id|>\nYour name is Cookie. you are helpful, polite, precise, concise, honest, good at writing. You always give precise and brief answers up to 32 words<|eot_id|><|start_header_id|>user<|end_header_id|>\nHey Cookie! how are you today?<|eot_id|><|start_header_id|>assistant<|end_header_id|>I 00:00:02.394162 executorch:text_prefiller.cpp:93] Prefill token result numel(): 128256


I 00:00:02.394373 executorch:text_llm_runner.cpp:179] RSS after prompt prefill: 1122.187500 MiB (0 if unsupported)
I'm doing great, thanks for asking! I'm always ready to help, whether it's answering a question or providing a solution. What can I help you with today?<|eot_id|>
I 00:00:03.072966 executorch:text_token_generator.h:123]
Reached to the end of generation

I 00:00:03.072972 executorch:text_llm_runner.cpp:199] RSS after finishing text generation: 1122.187500 MiB (0 if unsupported)
PyTorchObserver {"prompt_tokens":54,"generated_tokens":36,"model_load_start_ms":1756473387815,"model_load_end_ms":1756473388715,"inference_start_ms":1756473389893,"inference_end_ms":1756473390702,"prompt_eval_end_ms":1756473390023,"first_token_ms":1756473390023,"aggregate_sampling_time_ms":22,"SCALING_FACTOR_UNITS_PER_SECOND":1000}
I 00:00:03.072993 executorch:stats.h:108] 	Prompt Tokens: 54    Generated Tokens: 36
I 00:00:03.072995 executorch:stats.h:114] 	Model Load Time:		0.900000 (seconds)
I 00:00:03.072996 executorch:stats.h:124] 	Total inference time:		0.809000 (seconds)  Rate: 	44.499382 (tokens/second)
I 00:00:03.072998 executorch:stats.h:132] 	Prompt evaluation:	0.130000 (seconds)          Rate: 	415.384615 (tokens/second)
I 00:00:03.073000 executorch:stats.h:143] 	Generated 36 tokens:	0.679000 (seconds)      Rate: 	53.019146 (tokens/second)
I 00:00:03.073002 executorch:stats.h:151] 	Time to first generated token:	0.130000 (seconds)
I 00:00:03.073004 executorch:stats.h:158] 	Sampling time over 90 tokens:	0.022000 (seconds)
```

You have successfully run the Llama 3.1 1B Instruct model on your Android smartphone with ExecuTorch using KleidiAI kernels.
