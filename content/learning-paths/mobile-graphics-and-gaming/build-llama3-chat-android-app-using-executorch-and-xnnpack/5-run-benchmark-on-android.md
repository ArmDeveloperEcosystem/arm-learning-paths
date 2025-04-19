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
    -DCMAKE_INSTALL_PREFIX=cmake-out-android \
    -DEXECUTORCH_ENABLE_LOGGING=1 \
    -DCMAKE_BUILD_TYPE=Release \
    -DEXECUTORCH_BUILD_EXTENSION_DATA_LOADER=ON \
    -DEXECUTORCH_BUILD_EXTENSION_MODULE=ON \
    -DEXECUTORCH_BUILD_EXTENSION_TENSOR=ON \
    -DEXECUTORCH_BUILD_XNNPACK=ON \
    -DEXECUTORCH_BUILD_KERNELS_OPTIMIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_QUANTIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_CUSTOM=ON \
    -DEXECUTORCH_XNNPACK_ENABLE_KLEIDI=ON \
    -DXNNPACK_ENABLE_ARM_BF16=OFF \
    -Bcmake-out-android .

cmake --build cmake-out-android -j7 --target install --config Release
```
{{% notice Note %}}
Make sure you add -DEXECUTORCH_XNNPACK_ENABLE_KLEIDI=ON option to enable support for KleidiAI kernels in ExecuTorch with XNNPack.
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
    -DEXECUTORCH_BUILD_XNNPACK=ON \
    -DEXECUTORCH_BUILD_KERNELS_OPTIMIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_QUANTIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_CUSTOM=ON \
    -DEXECUTORCH_USE_TIKTOKEN=ON \
    -Bcmake-out-android/examples/models/llama \
    examples/models/llama

cmake --build cmake-out-android/examples/models/llama -j16 --config Release
```

You should now have `llama_main` available for Android.

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
adb push llama3_1B_kv_sdpa_xnn_qe_4_128_1024_embedding_4bit.pte /data/local/tmp/llama/
adb push $HOME/.llama/checkpoints/Llama3.2-1B-Instruct/tokenizer.model /data/local/tmp/llama/
adb push cmake-out-android/examples/models/llama/llama_main /data/local/tmp/llama/
```


### 3. Run the model

Use the Llama runner to execute the model on the phone with the `adb` command:

``` bash
adb shell "cd /data/local/tmp/llama && ./llama_main --model_path llama3_1B_kv_sdpa_xnn_qe_4_64_1024_embedding_4bit.pte --tokenizer_path tokenizer.model --prompt "<|start_header_id|>system<|end_header_id|>\nYour name is Cookie. you are helpful, polite, precise, concise, honest, good at writing. You always give precise and brief answers up to 32 words<|eot_id|><|start_header_id|>user<|end_header_id|>\nHey Cookie! how are you today?<|eot_id|><|start_header_id|>assistant<|end_header_id|>" --warmup=1 --cpu_threads=5
```

The output should look something like this.

```
I 00:00:00.003316 executorch:main.cpp:69] Resetting threadpool with num threads = 5
I 00:00:00.009329 executorch:runner.cpp:59] Creating LLaMa runner: model_path=llama3_1B_kv_sdpa_xnn_qe_4_64_1024_embedding_4bit.pte, tokenizer_path=tokenizer.model
I 00:00:03.569399 executorch:runner.cpp:88] Reading metadata from model
I 00:00:03.569451 executorch:runner.cpp:113] Metadata: use_sdpa_with_kv_cache = 1
I 00:00:03.569455 executorch:runner.cpp:113] Metadata: use_kv_cache = 1
I 00:00:03.569459 executorch:runner.cpp:113] Metadata: get_vocab_size = 128256
I 00:00:03.569461 executorch:runner.cpp:113] Metadata: get_bos_id = 128000
I 00:00:03.569464 executorch:runner.cpp:113] Metadata: get_max_seq_len = 1024
I 00:00:03.569466 executorch:runner.cpp:113] Metadata: enable_dynamic_shape = 1
I 00:00:03.569469 executorch:runner.cpp:120] eos_id = 128009
I 00:00:03.569470 executorch:runner.cpp:120] eos_id = 128001
I 00:00:03.569471 executorch:runner.cpp:120] eos_id = 128006
I 00:00:03.569473 executorch:runner.cpp:120] eos_id = 128007
I 00:00:03.569475 executorch:runner.cpp:168] Doing a warmup run...
I 00:00:03.838634 executorch:text_prefiller.cpp:53] Prefill token result numel(): 128256
 
I 00:00:03.892268 executorch:text_token_generator.h:118]
Reached to the end of generation
I 00:00:03.892281 executorch:runner.cpp:267] Warmup run finished!
I 00:00:03.892286 executorch:runner.cpp:174] RSS after loading model: 1269.445312 MiB (0 if unsupported)
<|start_header_id|>system<|end_header_id|>\nYour name is Cookie. you are helpful, polite, precise, concise, honest, good at writing. You always give precise and brief answers up to 32 words<|eot_id|><|start_header_id|>user<|end_header_id|>\nHey Cookie! how are you today?<|eot_id|><|start_header_id|>assistant<|end_header_id|>I 00:00:04.076905 executorch:text_prefiller.cpp:53] Prefill token result numel(): 128256
 
 
I 00:00:04.078027 executorch:runner.cpp:243] RSS after prompt prefill: 1269.445312 MiB (0 if unsupported)
I'm doing great, thanks! I'm always happy to help, communicate, and provide helpful responses. I'm a bit of a cookie (heh) when it comes to delivering concise and precise answers. What can I help you with today?<|eot_id|>
I 00:00:05.399304 executorch:text_token_generator.h:118]
Reached to the end of generation
 
I 00:00:05.399314 executorch:runner.cpp:257] RSS after finishing text generation: 1269.445312 MiB (0 if unsupported)
PyTorchObserver {"prompt_tokens":54,"generated_tokens":51,"model_load_start_ms":1710296339487,"model_load_end_ms":1710296343047,"inference_start_ms":1710296343370,"inference_end_ms":1710296344877,"prompt_eval_end_ms":1710296343556,"first_token_ms":1710296343556,"aggregate_sampling_time_ms":49,"SCALING_FACTOR_UNITS_PER_SECOND":1000}
I 00:00:05.399342 executorch:stats.h:111] 	Prompt Tokens: 54    Generated Tokens: 51
I 00:00:05.399344 executorch:stats.h:117] 	Model Load Time:		3.560000 (seconds)
I 00:00:05.399346 executorch:stats.h:127] 	Total inference time:		1.507000 (seconds)		 Rate: 	33.842070 (tokens/second)
I 00:00:05.399348 executorch:stats.h:135] 		Prompt evaluation:	0.186000 (seconds)		 Rate: 	290.322581 (tokens/second)
I 00:00:05.399350 executorch:stats.h:146] 		Generated 51 tokens:	1.321000 (seconds)		 Rate: 	38.607116 (tokens/second)
I 00:00:05.399352 executorch:stats.h:154] 	Time to first generated token:	0.186000 (seconds)
I 00:00:05.399354 executorch:stats.h:161] 	Sampling time over 105 tokens:	0.049000 (seconds)
```

You have successfully run the Llama 3.1 1B Instruct model on your Android smartphone with ExecuTorch using KleidiAI kernels.
