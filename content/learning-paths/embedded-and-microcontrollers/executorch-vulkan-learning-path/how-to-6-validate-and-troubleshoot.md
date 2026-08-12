---
title: Validate Vulkan execution and troubleshoot
description: Confirm that the model is using Vulkan on-device and resolve common deployment and runtime issues.
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Validate that Vulkan is in use

You can validate the run at three different levels.

### Process library check

During a long generation, capture the process ID and inspect the mapped libraries:

```bash
PID=$(adb shell pidof llama_main | tr -d '\r')
adb shell "cat /proc/$PID/maps | grep -Ei 'vulkan|mali'"
```

Seeing `libvulkan` and the Mali driver libraries confirms that the process loaded the Vulkan stack. It does not prove that every expensive model op ran on the GPU, but it is a fast sanity check.

### ExecuTorch ETDump and Inspector

For stronger backend evidence, rebuild with tracing enabled:

```text
-DEXECUTORCH_BUILD_DEVTOOLS=ON
-DEXECUTORCH_ENABLE_EVENT_TRACER=ON
```

Then capture ETDump data from the runner and inspect it with ExecuTorch Inspector to see delegated regions and delegate-call timings.

### Perfetto or Android Performance Analyzer

For a graphical view, collect a trace with Perfetto or Android Performance Analyzer and inspect the Vulkan and GPU queue tracks during inference.

## Known warnings and their meaning

| Observed warning or behavior | Interpretation |
|---|---|
| Tokenizer JSON parse error | The runner first tried a Hugging Face JSON tokenizer, then logged that it loaded the TikToken tokenizer and continued successfully. |
| Failed to open `/sys/devices/soc0/image_version` | CPU topology probing could not read a vendor-specific path. The runner still selected an 8-thread thread pool and continued. |
| Could not open `/sys/module/mali_kbase/parameters/large_page_conf` | A Mali driver diagnostic path was unavailable to the process. This did not block the measured run. |
| `vulkan_renderengine: false` | SurfaceFlinger was not using Vulkan for display composition. That is separate from application Vulkan compute. |
| Repeated `Paris is the capital...` output | The initial test used a raw completion-style prompt with an instruct model and a long generation limit. Use the chat template plus `max_new_tokens`. |

## Repeatable checklist

- Android SDK and NDK `r28c` installed and exported through `ANDROID_HOME` and `ANDROID_NDK`
- ExecuTorch `release/1.4` checkout present with submodules
- Python virtual environment active and `torch.__version__` verified as `2.13.0+cpu`
- Llama original files available under `~/Llama-3.2-1B-Instruct/original`
- `adb devices` shows the Vivo as `device`
- The phone advertises `android.hardware.vulkan.compute`
- Host Vulkan SDK loaded and `which glslc` resolves to the LunarG SDK
- Vulkan `.pte` exported with `8da4w`, group size `64`, and context length `2048`
- Android runtime built with `EXECUTORCH_BUILD_VULKAN=ON` and `EXECUTORCH_BUILD_LLAMA_JNI=OFF`
- `llama_main` built as an Android `aarch64` executable
- Model, tokenizer, and runner pushed to `/data/local/tmp/llama`
- Inference produces text and the expected performance counters
