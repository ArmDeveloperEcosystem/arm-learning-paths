---
title: "Overview & Quickstart"
weight: 2
layout: "learningpathall"
---

## Goal: Find where your model spends time

This learning path supports the PyTorch blog post ["Accelerating On-Device Vision ML Inference in ExecuTorch with Arm SME2"](https://pytorch.org/blog/placeholder-link) (link to be updated). It provides a hands-on implementation guide to identify optimization opportunities and actionable improvements that enhance model performance and enrich application user experience. 

When you enable SME2 acceleration on Arm devices, you get faster models, and something equally valuable: clear visibility into where time is actually spent. Model inference time is usually spent across several categories: matrix compute (linear operations like CONV and GEMM), non-linear operations (elementwise activations, normalization), and data movement (transpose, reshape, layout conversions, memory copies). In most models, matrix compute dominates the latency, making it the primary bottleneck.

SME2 accelerates your CONV and GEMM operations (can be 3-15× faster), removing the major compute bottleneck. This reveals that data movement was always there, but hidden behind the compute bottleneck. Now that compute is faster, data movement can become visible as the next frontier for optimization.

**The insight**: To see this bottleneck shift and identify where to optimize next, you need operator-level profiling. End-to-end latency tells you "it's faster," but not *why* or *where* the remaining time is spent. This pipeline reveals the operator-category breakdown (matrix compute, non-linear operations, data movement) that makes the next optimization targets obvious, showing you exactly where to focus for additional speedups.

## 1. What you'll build

An end-to-end, model-agnostic profiling pipeline for ExecuTorch models running on Arm-based devices:

1. Export any PyTorch model to ExecuTorch `.pte` format
2. Run the same model with SME2 on and off (apples-to-apples comparison)
3. Collect ETDump traces with operator-level timing
4. Analyze results into operator categories (CONV, GEMM, Data Movement, Elementwise, Other)
5. Discover where bottlenecks actually live, often data movement after SME2 accelerates math

**Key principle**: The pipeline is model-agnostic. Once you have a `.pte` file, the same commands work for any model. Only the model export step is model-specific.

## 2. Get the code package

This repo is a Hugo content repo. The profiling kit (all runnable code) is in the [`executorch_sme2_kit/`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/tree/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit) folder. The kit includes EdgeTAM's image segmentation module as the example model, a more recent video-focused segmentation model, along with the model-agnostic profiling pipeline.

Clone the repository with sparse checkout to get only the profiling kit:

```bash
mkdir -p ~/sme2_profiling_work
cd ~/sme2_profiling_work
git clone --filter=blob:none --sparse https://github.com/ArmDeveloperEcosystem/arm-learning-paths.git temp_repo
cd temp_repo
git sparse-checkout set content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit
mv content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit ../executorch_sme2_kit
cd ..
rm -rf temp_repo
cd executorch_sme2_kit
```

This gives you a self-contained folder with all scripts, configs, and model scaffolding. Your `.venv/`, `executorch/` (with runners in `executorch/cmake-out/`), `models/`, and `runs/` will live alongside the kit.

## 3. The stack: PyTorch, ExecuTorch, XNNPACK, Arm KleidiAI, and SME2

The profiling kit works with a specific execution stack. Before running the pipeline, understanding how these components connect will help you interpret your profiling results. The diagram below summarizes the CPU execution stack used in this workflow.

<p>
  <img
    src="/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/images/sme2_stack_01062026.png"
    alt="PyTorch → ExecuTorch → XNNPACK → Arm KleidiAI kernels → SME2"
    class="content-uploaded-image centered"
    style="max-width: 880px; width: 100%; height: auto;"
  />
  <span class="content-image-caption centered">
    The execution stack: A model is defined in PyTorch, exported and run by ExecuTorch, and CPU compute is delegated to XNNPACK as the backend.
  </span>
</p>

**PyTorch to ExecuTorch export**: You define your model in PyTorch using standard PyTorch APIs. ExecuTorch's export tools convert this model into a portable `.pte` (Portable ExecuTorch Executable) format that can run on edge devices. During export, you specify backend delegation, in this case XNNPACK, which tells ExecuTorch which operators should be handled by the XNNPACK backend at runtime.

**ExecuTorch runtime and delegation**: When ExecuTorch executes the `.pte` model, it uses a delegation system to route operators to appropriate backends. Operators like Conv2d and Linear are delegated to XNNPACK, while ExecuTorch handles the model graph execution, tensor management, and operator scheduling. The XNNPACK backend, in turn, uses Arm KleidiAI kernels that leverage SME2 acceleration on supported hardware. This delegation happens transparently, so your model code doesn't need to change.

**Operator-level profiling reveals backend behavior**: ExecuTorch's ETDump profiling captures timing for each operator in the execution graph. This gives you visibility into what XNNPACK is doing: which operators are delegated, how long they take, and which kernel implementations are selected (SME2-accelerated vs standard). The analysis categorizes operators into groups (CONV, GEMM, Data Movement, etc.) to show where SME2 acceleration appears and where it doesn't. This operator-level view is essential because it reveals what happens inside the XNNPACK backend. You can see which operations benefit from KleidiAI's SME2 kernels and which remain as data movement bottlenecks.

## 4. Quickstart: Run the pipeline

This is the "happy path" on macOS (Apple Silicon). It exports a tiny toy model, builds SME2-on/off runners, runs the pipeline, and validates outputs.

```bash
# 1) Create venv + clone/install ExecuTorch (requires network, ~30 min)
bash model_profiling/scripts/setup_repo.sh

# 2) Build SME2-on/off runners (and Android runners if ANDROID_NDK is set, ~20 min)
bash model_profiling/scripts/build_runners.sh

# 3) Run the smoke test end-to-end (export → run → validate, ~5 min)
python model_profiling/scripts/run_quick_test.py

# 4) Produce a readable operator-category summary (~2 min)
python model_profiling/scripts/analyze_results.py \
  --run-dir model_profiling/out_toy_cnn/runs/mac
```

Scripts: [`setup_repo.sh`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/scripts/setup_repo.sh), [`build_runners.sh`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/scripts/build_runners.sh), [`run_quick_test.py`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/scripts/run_quick_test.py), [`analyze_results.py`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/scripts/analyze_results.py)

Expected outcome: You'll see a category breakdown showing CONV, GEMM, Data Movement, Elementwise, and Other operations, with timing for SME2-on vs SME2-off. This is the foundation for understanding where bottlenecks live.

## 5. What you will produce: Artifacts

After running the pipeline, you'll have these artifacts:

- Model artifacts
  - `out_<model>/artifacts/<model>_xnnpack_fp16.pte` (runnable ExecuTorch model)
  - `out_<model>/artifacts/<model>_xnnpack_fp16.pte.etrecord` (optional; operator metadata for better attribution)
- Run artifacts
  - `out_<model>/runs/<platform>/<experiment>/*.etdump` (ETDump traces, the primary data source)
  - `out_<model>/runs/<platform>/<experiment>/*.log` (runner stdout/stderr)
  - `out_<model>/runs/<platform>/manifest.json` (optional; run metadata for reproducibility)
  - `out_<model>/runs/<platform>/metrics.json` (optional; summary latencies)
- Analysis artifacts
  - `out_<model>/runs/<platform>/analysis_summary.json` (operator-category breakdown)

**Critical insight**: The `.etdump` files are the primary data source. Everything else is derived from them. The JSON files are convenience logs, but analysis scripts work directly with ETDump.

## 6. Expected results: Case study insights

After analyzing your artifacts, you'll see two key insights: end-to-end latency improvements and the bottleneck shift. The case study below shows results from SqueezeSAM, an interactive image segmentation model, running on an SME2-enabled Android device. The profiling kit includes EdgeTAM's image segmentation module as the example model, which is a more recent video-focused segmentation model that demonstrates advanced model onboarding patterns.

**End-to-end latency**: With SME2 enabled, FP16 inference improves by 3.9× (from 1,163 ms to 298 ms on a single CPU core), making on-device execution viable for interactive use cases. INT8 also sees substantial speedups (1.83×), demonstrating that SME2 accelerates both quantized and floating-point models.

**The bottleneck shift**: After SME2 accelerates CONV and GEMM operations, data movement operations (transpose, reshape, layout conversions) become the dominant cost. This is expected, as SME2 reveals the next optimization frontier. The operator-category breakdown makes it obvious where to focus next.

<div style="display: flex; gap: 20px; align-items: flex-start; flex-wrap: wrap;">
  <div style="flex: 1; min-width: 400px;">
    <img
      src="/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/images/squeeze_sam_latency_comparison.png"
      alt="End-to-end latency comparison with SME2 on vs off"
      class="content-uploaded-image"
      style="width: 100%; height: auto;"
    />
  </div>
  <div style="flex: 1; min-width: 400px;">
    <img
      src="/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/images/combined_operator_breakdown_stacked.png"
      alt="Operator-category breakdown showing data movement becoming dominant after SME2"
      class="content-uploaded-image"
      style="width: 100%; height: auto;"
    />
  </div>
</div>
<p style="text-align: center; margin-top: 10px;">
  <span class="content-image-caption">
    Case study results (SqueezeSAM on SME2-enabled Android device): Left, end-to-end latency drops dramatically with SME2 (FP16: 3.9× speedup). Right, operator-category breakdown shows CONV/GEMM shrink while data movement becomes the dominant cost after SME2 acceleration.
  </span>
</p>

What you'll learn: These visualizations make it obvious where to optimize next. If data movement dominates after SME2, you know to focus on transpose elimination, layout optimization, or memory access patterns.

## 7. Where to go next

- If you want to set up the environment and build runners (foundation, done once): go to 02 – Setup + pipeline. This page covers environment setup and building the model-agnostic runners.
- If you want to onboard a model and profile it (workflow, per model): go to 03 – Model onboarding + profiling. This page covers model onboarding, export, running the profiling pipeline, and analyzing results.
- If you want to run all of this through an AI coding assistant: go to 04 – Agent skills. This page points to structured, verifiable skills for automation.
