---
title: "Overview & Quickstart"
weight: 2
layout: "learningpathall"
---

## Goal: Identify Where Your Model Spends Time

This learning path provides a hands-on, reproducible workflow for analyzing ExecuTorch model performance on Arm-based devices and identifying optimization opportunities after enabling SME2 acceleration.

When SME2 acceleration is enabled, inference latency often improves significantly. Just as importantly, faster compute exposes how execution time is distributed across the rest of the model. Model Inference time is typically spent in several broad operator categories:
   * Matrix compute (for example, convolution and GEMM)
   * Non-linear operations (elementwise activations, normalization)
   * Data movement (transpose, reshape, layout conversion, memory copies)
In many models, matrix compute dominates latency, making it the primary bottleneck.

SME2 accelerates CONV and GEMM operations,often by 3–15x,removing the primary compute bottleneck. Once compute is faster, data movement costs become visible and may emerge as the next dominant contributor to latency.

Key idea:
End-to-end latency alone tells you that a model is faster, but not why or where time is still spent. Operator-level profiling reveals how execution time shifts across categories when SME2 is enabled, making it clear which operations should be optimized next.

## 1. What You Will Build

You will construct a model-agnostic performance analysis pipeline for ExecuTorch models running on Arm-based devices:

1. Export any PyTorch model to ExecuTorch `.pte` format
2. Run the same model with SME2 enabled and disabled for an apples-to-apples comparison
3. Collect ETDump traces with operator-level timing
4. Aggregate operators into high-level categories (CONV, GEMM, Data Movement, Elementwise, Other)
5. Identify where bottlenecks move after SME2 acceleration

Key principle: Once you have a .pte file, the same pipeline and commands apply to any model. Only the export step is model-specific.

## 2. Get the Code Package

All profiling and analysis steps in this Learning Path are performed using a single, shared code repository. This repository contains the scripts, configuration, and example models used to export ExecuTorch models, run profiling with SME2 enabled and disabled, and analyze the resulting performance data.
The repository you will use throughout this Learning Path is [sme-executorch-profiling](https://github.com/ArmDeveloperEcosystem/sme-executorch-profiling). The repository includes:
  * Example models (EdgeTAM image segmentation and a video-focused segmentation model)
  * Predefined ExecuTorch runners
  * Scripts for profiling, trace collection, and analysis

Clone the performance analysis kit repository:

```bash
mkdir -p ~/sme2_analysis_work
cd ~/sme2_analysis_work
git clone https://github.com/ArmDeveloperEcosystem/sme-executorch-profiling.git executorch_sme2_kit
cd executorch_sme2_kit
```

This gives you a self-contained folder with all scripts, configs, and model scaffolding. Your `.venv/`, `executorch/` (with runners in `executorch/cmake-out/`), `models/`, and `runs/` will live alongside the kit.

## 3. The stack: PyTorch, ExecuTorch, XNNPACK, Arm KleidiAI, and SME2

The performance analysis kit works with a specific execution stack. Before running the pipeline, understanding how these components connect will help you interpret your performance analysis results. The diagram below summarizes the CPU execution stack used in this workflow.

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

**Operator-level analysis reveals backend behavior**: ExecuTorch's ETDump performance measurement captures timing for each operator in the execution graph. This gives you visibility into what XNNPACK is doing: which operators are delegated, how long they take, and which kernel implementations are selected (SME2-accelerated vs standard). The analysis categorizes operators into groups (CONV, GEMM, Data Movement, etc.) to show where SME2 acceleration appears and where it doesn't. This operator-level view is essential because it reveals what happens inside the XNNPACK backend. You can see which operations benefit from KleidiAI's SME2 kernels and which remain as data movement bottlenecks.

## 4. Quickstart: Run the pipeline

This learning path supports performance analysis on both **Android** (for real-world edge ML performance on mobile devices) and **macOS** (included for developer accessibility). The pipeline is identical for both platforms—only the runner binaries and execution environment differ.

**Platform context**: This learning path demonstrates analyzing ExecuTorch model performance on SME2-enabled devices using Android as the mobile device example. Android runs provide realistic edge ML performance with actual device constraints (memory bandwidth, thermal throttling, device-specific optimizations). macOS is included because most developers have Mac access, making it convenient for learning the workflow and initial testing. For production validation and accurate performance measurements, Android runs on real SME2-enabled devices provide the most representative results.

Quickstart (macOS for initial testing, or Android if you have an SME2-enabled device):

```bash
# 1) Create venv + clone/install ExecuTorch (requires network, ~30 min)
bash model_profiling/scripts/setup_repo.sh

# 2) Build SME2-on/off runners (~20 min)
#    - macOS: Built automatically
#    - Android: Requires ANDROID_NDK environment variable set
bash model_profiling/scripts/build_runners.sh

# 3) Run the smoke test end-to-end (export → run → validate, ~5 min)
#    - macOS: Runs locally
#    - Android: Requires device connected via adb
python model_profiling/scripts/run_quick_test.py

# 4) View results (analysis is automatic, but you can re-run if needed)
#    The pipeline automatically generates CSV files and analysis_summary.json
#    Optional: python model_profiling/scripts/analyze_results.py --run-dir model_profiling/out_toy_cnn/runs/mac
```

Scripts: [`setup_repo.sh`](https://github.com/ArmDeveloperEcosystem/sme-executorch-profiling/blob/main/model_profiling/scripts/setup_repo.sh), [`build_runners.sh`](https://github.com/ArmDeveloperEcosystem/sme-executorch-profiling/blob/main/model_profiling/scripts/build_runners.sh), [`run_quick_test.py`](https://github.com/ArmDeveloperEcosystem/sme-executorch-profiling/blob/main/model_profiling/scripts/run_quick_test.py), [`analyze_results.py`](https://github.com/ArmDeveloperEcosystem/sme-executorch-profiling/blob/main/model_profiling/scripts/analyze_results.py)

Expected outcome: You'll see a category breakdown showing CONV, GEMM, Data Movement, Elementwise, and Other operations, with timing for SME2-on vs SME2-off. This is the foundation for understanding where bottlenecks live.

## 5. What you will produce: Artifacts

After running the pipeline, you'll have these artifacts:

- Model artifacts
  - `out_<model>/artifacts/<model>_xnnpack_fp16.pte` (runnable ExecuTorch model)
  - `out_<model>/artifacts/<model>_xnnpack_fp16.pte.etrecord` (optional; operator metadata for better attribution)
- Run artifacts
  - `out_<model>/runs/<platform>/<experiment>/*.etdump` (ETDump traces, the primary data source)
  - `out_<model>/runs/<platform>/<experiment>/*.log` (runner stdout/stderr)
  - `out_<model>/runs/<platform>/<experiment>/*.csv` (CSV files generated automatically by pipeline: timeline, operator stats)
  - `out_<model>/runs/<platform>/manifest.json` (optional; run metadata for reproducibility)
  - `out_<model>/runs/<platform>/metrics.json` (optional; summary latencies)
  - `out_<model>/runs/<platform>/<model_stem>_pipeline_summary.json` (pipeline summary with robust statistics)
  - `out_<model>/runs/<platform>/<model_stem>_pipeline_summary.md` (pipeline summary markdown)
- Analysis artifacts
  - `out_<model>/runs/<platform>/analysis_summary.json` (operator-category breakdown, generated automatically by pipeline)

**Critical insight**: The `.etdump` files are the primary data source. Everything else is derived from them. The JSON files are convenience logs, but analysis scripts work directly with ETDump.

## 6. Expected results: Case study insights

After analyzing your artifacts, you'll see two key insights: end-to-end latency improvements and the bottleneck shift. The case study below shows results from SqueezeSAM, an interactive image segmentation model, running on an SME2-enabled Android device. The performance analysis kit includes EdgeTAM's image segmentation module as the example model, which is a more recent video-focused segmentation model that demonstrates advanced model onboarding patterns.

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
- If you want to onboard a model and analyze its performance (workflow, per model): go to 03 – Model onboarding + performance analysis. This page covers model onboarding, export, running the performance analysis pipeline, and analyzing results.
- If you want to run all of this through an AI coding assistant: go to 04 – Agent skills. This page points to structured, verifiable skills for automation.
