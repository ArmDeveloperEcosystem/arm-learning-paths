---
title: Optimize code with AI-driven profiling feedback
description: Apply AI-suggested C++ optimizations from Performix hotspot results and re-profile each change to validate the measured speedup on Arm Neoverse.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Apply AI-suggested optimizations

In the previous section, the agent identified three optimization opportunities:

1. Replace `std::abs` with a squared-magnitude comparison to eliminate the `sqrt` in the hot path
2. Replace `std::complex<double>` with raw `double` arithmetic to remove all complex operator overhead
3. Build with `-O3` to enable inlining, loop unrolling, and auto-vectorization

You can ask the agent to apply each change when it has access to your source and build environment. Otherwise, apply and rebuild the change through your normal remote development workflow. The Arm Performix MCP server profiles the configured target and analyzes saved runs; it doesn't by itself provide remote source-editing or deployment tools.

After each change, use the agent to rerun Code Hotspots against the same target and workload. Compare the new profile evidence and elapsed time with the previous run before continuing.

{{% notice Note %}}
The agent will typically surface these optimizations itself based on the profiling results, without you needing to prompt it explicitly. The following prompts are for explicit reference. You can use them if the agent hasn't already proposed the change, or to direct it to a specific optimization.
{{% /notice %}}

### Eliminate the sqrt in the escape check

The inner loop in `Mandelbrot::getIterations` calls `std::abs(z)` on every iteration to check whether the point has escaped. `std::abs` for `std::complex<double>` computes $\sqrt{re^2 + im^2}$ via `hypotf64` — a full square root on every iteration. The escape condition $abs(z) > THRESHOLD$ is mathematically equivalent to $re^2 + im^2 > THRESHOLD^2$, so the square root is never needed.

Ask the agent to apply the fix, rebuild, and re-profile in one step. If the agent hasn't already proposed this change, use the following prompt:

```text
Replace the abs(z) > THRESHOLD escape check in
getIterations with a squared-magnitude comparison using a precomputed
threshold_sq = THRESHOLD * THRESHOLD. Rebuild the debug binary with
`make clean && make single_thread DEBUG=1`. Then use the Arm Performix MCP
server to re-run the Code Hotspots recipe on target "<target-name>" with
workload "/home/ec2-user/Mandelbrot-Example/build/mandelbrot_single_thread_debug".
Generate an AI insight for the new run and compare it with run ID "<previous-run-id>".
Has the proportion of samples in __complex_abs and hypotf64 changed?
```

Replace `<target-name>` and `<previous-run-id>` before sending the prompt. The agent creates a new run, generates an AI insight for its run ID, and compares the evidence. In the example results, the `std::__complex_abs` and `hypotf64` symbols disappear from the hotspot list because the squared-magnitude check doesn't call them.

The hotspot distribution shifts: `getIterations` drops from 28.5% to 18.4% self-time, and the freed CPU budget is now visible in `std::complex` operator symbols. The overall sample count is slightly lower, but the profile structure reveals that `std::complex` operator overhead is now the next bottleneck to address.

### Replace `std::complex<double>` with raw double arithmetic

With `hypotf64` and `__complex_abs` removed, the profile now shows `std::complex` operator symbols (`operator+`, `operator*=`, `operator*`, `operator+=`, `__muldc3`, `__rep`) collectively consuming the majority of CPU time. These are all function-call overhead: the debug build disables inlining, so every arithmetic operation on `std::complex<double>` dispatches through the C++ standard library machinery.

The fix is to replace `std::complex<double>` in `getIterations` with plain `double` variables for the real and imaginary parts. The Mandelbrot iteration $z_{n+1} = z_n^2 + c$ expands algebraically to:

$$re_{new} = re_z^2 - im_z^2 + re_c$$
$$im_{new} = 2 \cdot re_z \cdot im_z + im_c$$

The fix eliminates every `std::complex` method call from the inner loop. If the agent hasn't already proposed this change, use the following prompt to direct it:

```text
Rewrite the getIterations function in
src/mandelbrot_single_thread.cpp to use plain double variables zr and zi
instead of std::complex<double>, expanding z*z + c algebraically.
Rebuild with `make clean && make single_thread DEBUG=1`. Then use the Arm
Performix MCP server to re-run the Code Hotspots recipe on target
"<target-name>" with the same workload. Generate an AI insight for the new
run and compare it with run ID "<previous-run-id>". Have the std::complex
operator symbols disappeared from the hotspot list?
```

Replace the placeholders with the target name and the run ID from the previous step. In the example results, the `std::complex` functions—`__muldc3`, `operator*=`, `operator+=`, `operator+`, `operator*`, and `__rep`—disappear from the profile.

The example profile sample count drops from approximately 48,750 at baseline to approximately 11,457, a reduction of about 76%. With the same collection interval and workload, this suggests a shorter runtime. Confirm the improvement with an elapsed-time measurement.

### Enable compiler optimizations with `-O3`

Both previous changes were applied to the debug binary, compiled with `-O0` (no optimization). At `-O0`, the compiler doesn't inline any function calls, which is why `std::complex` operators appeared separately in the profile even after the algorithmic fix. 

Building with `-O3` lets the compiler inline `getIterations` into `draw`, unroll the inner loop, and auto-vectorize the scalar double arithmetic using the Arm NEON/ASIMD unit.

Ask the agent to rebuild with the release target and re-profile. If it hasn't already suggested this step, use the following prompt:

```text
Rebuild the application without the DEBUG flag using
`make clean && make single_thread`, then run the Code Hotspots recipe on
target "<target-name>" with workload
"/home/ec2-user/Mandelbrot-Example/build/mandelbrot_single_thread". Generate
an AI insight for the new run and compare it with run ID "<previous-run-id>".
How has the hotspot distribution changed, and what does the elapsed-time
measurement show?
```

Replace the placeholders before sending the prompt. In the example profile, the `getIterations` function no longer appears as a separate hotspot because the compiler has inlined it into `draw`. The sample count drops to approximately 3,997, about 12 times fewer samples than the baseline. Treat this as profile evidence and use elapsed time to confirm the runtime improvement.

The only remaining hotspot is `Mandelbrot::draw` itself at ~98.6% of samples, which now includes both the iteration and colorizing passes. The colorizing pass calls `pow(255, hue)` per pixel — visible as `powf64` at ~0.7% — but this is a small fraction of total time at this scale.

## What you've accomplished

You've applied AI-suggested optimizations such as replacing `std::complex<double>` with plain `double` arithmetic, enabling `-O3`, and eliminating the square root in the escape check.

In the example profiles, the cumulative result is a reduction from approximately 48,750 baseline samples to approximately 3,997. The table summarizes the relative sample-count reduction across three changes. Your values will vary, and you should use elapsed time to measure speedup.

| Step | Profile samples | Sample-count reduction vs baseline |
|---|---|---|
| Baseline (`-O0`, `std::complex`, `abs` check) | ~48,750 | Baseline |
| After squared-magnitude check | ~47,535 | About 3% fewer |
| After raw double arithmetic | ~11,457 | About 76% fewer |
| After `-O3` | ~3,997 | About 92% fewer |

You can apply the same evidence-driven loop to other C++ applications on Arm Neoverse. Run Code Hotspots to locate the hottest functions, use the agent to relate evidence to source code, apply one change, and re-profile the same workload. Compare profile evidence and elapsed time before accepting the optimization.
