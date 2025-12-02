---
title: KleidiAI Integration for Arm Optimization
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is KleidiAI?

KleidiAI is Arm's performance library that provides highly optimized kernels for AI workloads on Arm CPUs. It delivers significant performance improvements for:
- **Matrix Multiplication (GEMM)**: Optimized for Arm Neoverse and Cortex-A processors
- **Quantized Operations**: Accelerated int8 and int4 inference
- **Mobile AI**: Specifically tuned for Android devices with Arm processors

When combined with ExecuTorch, KleidiAI can provide **2-3x faster inference** compared to generic implementations.

## Why KleidiAI for Mobile LLMs?

Large Language Models are compute-intensive, especially on mobile devices. KleidiAI addresses this by:

1. **Leveraging Arm Instructions**: Uses specialized instructions like `i8mm` (int8 matrix multiply) available on modern Arm CPUs
2. **Cache Optimization**: Kernels are designed to maximize L1/L2 cache utilization
3. **Low Power**: Optimized algorithms reduce energy consumption during inference
4. **Quantization Support**: Native support for 4-bit and 8-bit quantized models

## Enabling KleidiAI in ExecuTorch

### Step 1: Verify Device Compatibility

First, check if your Android device supports the required Arm features:

```bash
adb shell cat /proc/cpuinfo | grep Features
```

Look for `i8mm` in the output. This indicates your device supports int8 matrix multiplication acceleration.

### Step 2: Build ExecuTorch with KleidiAI Backend

When building ExecuTorch for Android, enable the KleidiAI backend:

```bash
cd executorch

# Install KleidiAI dependencies
git submodule update --init --recursive

# Build with KleidiAI support
cmake -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake \
      -DANDROID_ABI=arm64-v8a \
      -DANDROID_PLATFORM=android-23 \
      -DEXECUTORCH_BUILD_KERNELS_OPTIMIZED=ON \
      -DEXECUTORCH_BUILD_XNNPACK=ON \
      -DEXECUTORCH_BUILD_KLEIDIAI=ON \
      -Bcmake-out-android .

cmake --build cmake-out-android -j16
```

### Step 3: Export Model with KleidiAI Optimizations

When exporting your Llama model, specify the KleidiAI backend:

```python
python3 -m examples.models.llama.export_llama \
--checkpoint $HOME/.llama/checkpoints/Llama3.2-1B-Instruct/consolidated.00.pth \
--params $HOME/.llama/checkpoints/Llama3.2-1B-Instruct/params.json \
-kv --use_sdpa_with_kv_cache \
-X --xnnpack-extended-ops \
--kleidiai \
-qmode 8da4w \
--group_size 64 \
-d fp32 \
--metadata '{"get_bos_id":128000, "get_eos_ids":[128009, 128001, 128006, 128007]}' \
--embedding-quantize 4,32 \
--output_name="llama3_1B_kleidiai_optimized.pte" \
--max_seq_length 1024
```

**Key flags:**
- `--kleidiai`: Enables KleidiAI optimized kernels
- `--xnnpack-extended-ops`: Uses XNNPACK with extended operations
- `-qmode 8da4w`: 8-bit dynamic activation, 4-bit weights (optimal for KleidiAI)

### Step 4: Android App Configuration

In your Android app's `build.gradle`, ensure you're linking the KleidiAI libraries:

```gradle
android {
    defaultConfig {
        ndk {
            abiFilters 'arm64-v8a'  // KleidiAI requires 64-bit Arm
        }
    }
    
    externalNativeBuild {
        cmake {
            arguments "-DEXECUTORCH_BUILD_KLEIDIAI=ON"
        }
    }
}

dependencies {
    implementation 'org.pytorch:executorch:0.3.0'
    // KleidiAI is bundled with ExecuTorch when built with the flag
}
```

## Performance Benchmarking

After integrating KleidiAI, benchmark your model to verify the speedup:

```kotlin
// ModelBenchmark.kt
class ModelBenchmark(private val modelRunner: ModelRunner) {
    
    fun benchmarkInference(prompt: String, iterations: Int = 10): BenchmarkResult {
        val latencies = mutableListOf<Long>()
        
        repeat(iterations) {
            val startTime = System.nanoTime()
            modelRunner.generate(prompt)
            val endTime = System.nanoTime()
            
            latencies.add((endTime - startTime) / 1_000_000) // Convert to ms
        }
        
        return BenchmarkResult(
            avgLatency = latencies.average(),
            minLatency = latencies.minOrNull() ?: 0.0,
            maxLatency = latencies.maxOrNull() ?: 0.0,
            tokensPerSecond = calculateTPS(latencies.average())
        )
    }
}
```

### Expected Performance Gains

On a typical Arm-based Android device (e.g., Pixel 8/9 with Tensor G3):

| Configuration | Tokens/Second | Latency (50 tokens) |
|--------------|---------------|---------------------|
| Baseline (FP32) | ~5 tok/s | ~10s |
| XNNPACK Only | ~15 tok/s | ~3.3s |
| **XNNPACK + KleidiAI** | **~30-40 tok/s** | **~1.5s** |

## Troubleshooting

### Issue: KleidiAI not being used

**Check logs:**
```bash
adb logcat | grep -i kleidiai
```

You should see:
```
ExecuTorch: Using KleidiAI optimized kernels for GEMM operations
```

If not, verify:
1. Device has `i8mm` support
2. Model was exported with `--kleidiai` flag
3. ExecuTorch library was built with `-DEXECUTORCH_BUILD_KLEIDIAI=ON`

### Issue: Performance not improving

- Ensure you're using quantized models (4-bit or 8-bit)
- Check that `arm64-v8a` ABI is being used (not `armeabi-v7a`)
- Verify thermal throttling isn't limiting performance

## Next Steps

With KleidiAI integrated, your Agentic AI chatbot now has:
- Optimized inference on Arm Android devices
- Reduced latency for real-time interactions
- Lower power consumption for better battery life

In the next section, we'll build the complete Android application with the agentic loop!
