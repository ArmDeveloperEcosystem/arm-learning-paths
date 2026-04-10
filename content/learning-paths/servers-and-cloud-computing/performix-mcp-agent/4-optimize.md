---
title: Optimize code with AI-driven profiling feedback
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Apply AI-suggested optimizations

In the previous section, the agent identified three optimization opportunities:

1. Replace `std::abs` with a squared-magnitude comparison to eliminate the `sqrt` in the hot path
2. Replace `std::complex<double>` with raw `double` arithmetic to remove all complex operator overhead
3. Build with `-O3` to enable inlining, loop unrolling, and auto-vectorization

Rather than making these changes manually, you can ask the agent to apply each one for you. Because the Arm MCP Server connects to your remote target over SSH, the agent can edit the source files directly on the server, rebuild, and re-profile — all in a single turn. You'll validate each change by asking the agent to compare the new profiling results against the previous run before moving on.

{{% notice Note %}}
The agent will typically surface these optimizations itself based on the profiling results, without you needing to prompt it explicitly. The prompts shown in each section below are for explicit reference — you can use them if the agent hasn't already proposed the change, or to direct it to a specific optimization.
{{% /notice %}}

## Optimization 1: Eliminate the sqrt in the escape check

The inner loop in `Mandelbrot::getIterations` calls `std::abs(z)` on every iteration to check whether the point has escaped. `std::abs` for `std::complex<double>` computes $\sqrt{re^2 + im^2}$ via `hypotf64` — a full square root on every iteration. The escape condition `abs(z) > THRESHOLD` is mathematically equivalent to `re² + im² > THRESHOLD²`, so the square root is never needed.

Ask the agent to apply the fix, rebuild, and re-profile in one step. If the agent hasn't already proposed this change, use the following prompt:

```text
On the remote server, replace the abs(z) > THRESHOLD escape check in
getIterations with a squared-magnitude comparison using a precomputed
threshold_sq = THRESHOLD * THRESHOLD. Rebuild the debug binary with
`make clean && make single_thread DEBUG=1`, then re-run the Code Hotspots
recipe on /home/ec2-user/Mandelbrot-Example/build/mandelbrot_single_thread_debug
and compare with the previous run. Has the proportion of samples in
__complex_abs and hypotf64 changed?
```

The agent calls `arm-mcp/apx_recipe_run` again and returns the comparison. The `std::__complex_abs` and `hypotf64` symbols disappear from the hotspot list entirely. Both functions are gone because the squared-magnitude check never calls them. The hotspot distribution shifts: `getIterations` drops from 28.5% to 18.4% self-time, and the freed CPU budget is now visible in `std::complex` operator symbols. The overall sample count is slightly lower, but the profile structure reveals that `std::complex` operator overhead is now the next bottleneck to address.

## Optimization 2: Replace `std::complex<double>` with raw double arithmetic

With `hypotf64` and `__complex_abs` removed, the profile now shows `std::complex` operator symbols (`operator+`, `operator*=`, `operator*`, `operator+=`, `__muldc3`, `__rep`) collectively consuming the majority of CPU time. These are all function-call overhead: the debug build disables inlining, so every arithmetic operation on `std::complex<double>` dispatches through the C++ standard library machinery.

The fix is to replace `std::complex<double>` in `getIterations` with plain `double` variables for the real and imaginary parts. The Mandelbrot iteration $z_{n+1} = z_n^2 + c$ expands algebraically to:

$$re_{new} = re_z^2 - im_z^2 + re_c$$
$$im_{new} = 2 \cdot re_z \cdot im_z + im_c$$

The fix eliminates every `std::complex` method call from the inner loop. If the agent hasn't already proposed this change, use the following prompt to direct it:

```text
On the remote server, rewrite the getIterations function in
src/mandelbrot_single_thread.cpp to use plain double variables zr and zi
instead of std::complex<double>, expanding z*z + c algebraically.
Rebuild with `make clean && make single_thread DEBUG=1`, then re-run the
Code Hotspots recipe and compare with the previous run. Have the
std::complex operator symbols disappeared from the hotspot list?
```

The agent calls `arm-mcp/apx_recipe_run` and returns the comparison. Every `std::complex` function—`__muldc3`, `operator*=`, `operator+=`, `operator+`, `operator*`, `__rep`—is gone from the profile. Total profile sample count drops from approximately 48,750 (baseline) to approximately 11,457, a reduction of ~76% and a measured ~4x speedup.

## Optimization 3: Enable compiler optimizations with `-O3`

Both previous changes were applied to the debug binary, compiled with `-O0` (no optimization). At `-O0`, the compiler doesn't inline any function calls, which is why `std::complex` operators appeared separately in the profile even after the algorithmic fix. Building with `-O3` lets the compiler inline `getIterations` into `draw`, unroll the inner loop, and auto-vectorize the scalar double arithmetic using the Arm NEON/ASIMD unit.

Ask the agent to rebuild with the release target and re-profile. If it hasn't already suggested this step, use the following prompt:

```text
On the remote server, rebuild the application without the DEBUG flag using
`make clean && make single_thread`, then run the Code Hotspots recipe on
/home/ec2-user/Mandelbrot-Example/build/mandelbrot_single_thread and compare
with the previous run. How has the hotspot distribution changed and what is
the runtime improvement?
```

The agent calls `arm-mcp/apx_recipe_run` on the new binary path and returns the result. The `getIterations` function no longer appears as a separate hotspot because the compiler has inlined it completely into `draw`. Total profile sample count drops to approximately 3,997 — roughly 12x fewer samples than the original baseline of ~48,750, indicating a ~12x speedup.

The only remaining hotspot is `Mandelbrot::draw` itself at ~98.6% of samples, which now includes both the iteration and colorizing passes. The colorizing pass calls `pow(255, hue)` per pixel — visible as `powf64` at ~0.7% — but this is a small fraction of total time at this scale.

## Summary

In this Learning Path, you combined the Arm MCP Server's `apx_recipe_run` tool with an AI agent to drive the complete Code Hotspots workflow. Starting from a single-threaded C++ baseline, the agent:

- Ran the Code Hotspots recipe through a GitHub Copilot prompt file and retrieved structured profiling results, identifying `getIterations` and the sqrt-based escape check as the dominant hotspots
- Eliminated `__complex_abs` and `hypotf64` by replacing `abs(z) > THRESHOLD` with a squared-magnitude check, removing ~33% of CPU overhead
- Replaced `std::complex<double>` with plain `double` arithmetic, removing all std::complex operator call overhead and delivering a ~4x speedup over the original baseline
- Enabled `-O3` to let the compiler inline `getIterations`, unroll the loop, and auto-vectorize, delivering a further 3x improvement

The cumulative result, measured by profile sample counts, was a reduction from approximately 48,750 baseline samples to approximately 3,997 — a ~12x speedup — through three rounds of code changes, each validated by a re-profile before moving to the next.

| Step | Profile samples | Speedup vs baseline |
|---|---|---|
| Baseline (`-O0`, `std::complex`, `abs` check) | ~48,750 | 1× |
| After squared-magnitude check | ~47,535 | ~1× |
| After raw double arithmetic | ~11,457 | ~4× |
| After `-O3` | ~3,997 | ~12× |

The same pattern applies to any C++ application on Arm Neoverse. Run the Code Hotspots recipe to locate the hottest functions, let the agent cross-reference the source and the Arm knowledge base, apply the suggested changes, and re-profile to confirm. This evidence-driven loop is faster and less error-prone than manual profiling because the AI maintains context across all steps and keeps the profiling data visible alongside the code throughout.
