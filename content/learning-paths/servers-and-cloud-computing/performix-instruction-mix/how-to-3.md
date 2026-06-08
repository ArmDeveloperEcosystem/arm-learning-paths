---
title: Profile with instruction mix
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Find the code hotspot

Before you optimize, identify where the application spends most of its time. Use the Code Hotspots recipe to periodically sample the running application and build a profile of the functions that execute most often.

Open Arm Performix and select the **Code Hotspots** recipe. If this is your first run on the target, complete tool deployment as prompted.

Set the launch command to your baseline binary with the number of tokens (`-n`) set to 150. This value keeps startup overhead small compared to inference time, so the profile minimizes the time taken to load the model weights:

![Arm Performix Code Hotspots recipe configuration showing launch arguments for the GPT-2 baseline run with -n 150 to emphasize inference runtime.#center](./code_hotspot.webp "Code Hotspots recipe configuration for GPT-2 baseline")

The results show that `kernels::matmul_ref()` is the hottest function. Double-clicking on the function with show which lines of source code the samples are mostly attributed to the accumulate step of `kernels::matmul_ref()`.

![Arm Performix hotspot results table showing matmul_ref as the dominant runtime function during GPT-2 baseline inference.#center](./code_hotspot_results.webp "Hotspot results highlighting matmul_ref")

This confirms that matrix multiplication is the highest-impact optimization target.

## Assess compiler output

We can use online tools such as [Compiler Explorer](https://godbolt.org/) to conveniently see how this function is being compiled with the `-O2 -g` flags.


{{< godbolt width="100%" height="400px" mode="assembly" opt="-O2 -g" src="void matmul_ref(float *out, const float *x, const float *W, const float *b, int n_in, int n_out)\n{\n  for (int i = 0; i < n_out; i++) {\n    float acc = b ? b[i] : 0.f;\n    const float *row = W + (unsigned long long)i * (unsigned long long)n_in;\n    for (int j = 0; j < n_in; j++) {\n      acc += row[j] * x[j];\n    }\n    out[i] = acc;\n  }\n}" >}}

This view helps you spot missed vectorization opportunities. In an optimized build, you would expect the accumulation step to use SIMD instructions, for example `fmla v0.4s, v3.4s, v2.4s` with use of the vector register (`v0->v3`). However, assembly inspection has limitations. First, you need familiarity with SIMD mnemonics to recognize vectorized code. Second, this narrow snippet does not show whether changing compiler flags introduces regressions in other parts of the codebase. Third, and most importantly, this static view does not show which instructions in this function run most often on the CPU.

The Instruction Mix recipe helps fill this gap.

## Configure the Instruction Mix recipe

Open Arm Performix and select the **Instruction Mix** recipe. If this is your first run on the target, complete tool deployment as prompted.
Set the launch command to your baseline binary with the same runtime arguments used for baseline testing:

```output
</path/to/GPT-2-Example>/build/gpt2 --model gpt2-medium "Once upon a time" -n 150`
```

Use the same model and prompt arguments as your baseline terminal run so the measurements are comparable.

![Arm Performix recipe setup screen showing Instruction Mix recipe selected with launch settings configured for the GPT-2 baseline executable.#center](./configuring-performix.webp "Configure Arm Performix Instruction Mix recipe")

### Analyze static disassembly

After the run completes, review static disassembly first. This view is ordered by percentage contribution and provides a high-level profile of the application’s generated instruction stream. It can help you identify broad characteristics, such as whether the code is branch-heavy, dominated by memory operations, or making effective use of SIMD instructions. Use this static view to understand overall code generation patterns rather than to attribute performance to specific functions or source lines. Dynamic analysis is typically more relevant for optimization because it reflects the instructions that are actually executed at runtime.

![Arm Performix static disassembly view showing instruction category breakdown for GPT-2 hot paths, highlighting scalar-heavy sections in baseline matmul code.#center](./static_disassembly.webp "Static disassembly instruction classification")

### Dynamic analysis

Then inspect dynamic analysis bar chart to see where sampled runtime work is concentrated. Dynamic data is typically more useful for optimization because it reflects actual execution behavior for your input, runtime settings, and call frequencies.

![Arm Performix dynamic functions table showing most runtime samples in matmul-related functions for baseline GPT-2 inference.#center](./instruction_mix_dynamic_analysis.webp "Dynamic function sample distribution")

Finally, in dynamic functions, you can break down operation types to individual functions. This is particularly useful when no single function dominates the profile, allowing you to inspect dynamic instruction patterns for specific functions.

## What you've learned and what's next

You used Instruction Mix to confirm that baseline runtime is dominated by scalar-heavy `matmul` execution. Next, you will compare updated instruction mix and throughput across scalar, NEON, SVE, and KleidiAI variants.
