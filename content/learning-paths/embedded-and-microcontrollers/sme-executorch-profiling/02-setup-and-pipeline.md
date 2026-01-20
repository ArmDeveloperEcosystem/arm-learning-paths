---
title: "Setup + pipeline: environment and runner build"
weight: 3
layout: "learningpathall"
---

## Goal: Set up workspace and build runners

This page covers the foundation that you set up once and reuse for all models: environment setup and runner building.

**The key principle**: The profiling pipeline is model-agnostic. Once you have a `.pte` file, the same pipeline commands work for any model. The runner build, config generation, execution, and analysis scripts remain unchanged across models. Only the model export step is model-specific, and sometimes requires code edits. This means you can profile many models with the same tooling, making the pipeline a reusable asset rather than a one-off script.

What you'll do:

1. Set up the environment: Install ExecuTorch from source and create a Python virtual environment
2. Build runners: Build SME2-on/off runners (done once, works for all models)

The workflow is: setup once → build runners once → reuse for all models.

## 1. Recommended workspace layout

In your workspace, this learning path expects the following directories to exist (created by the scripts as you run them):

```text
<executorch_sme2_kit_root>/
├── model_profiling/
│   ├── scripts/        # export + run + analyze entrypoints
│   ├── configs/        # JSON configs (templates + examples)
│   ├── export/         # model export script
│   ├── models/         # model source code (model definitions, registration)
│   ├── out_<model>/    # exported artifacts per model (created during export)
│   │   ├── artifacts/     # .pte files and optional .etrecord
│   │   └── runs/          # run outputs for this model (etdump, metrics, reports)
│   ├── tools/          # analysis tools (ETDump conversion, operator categorization)
│   └── pipeline/        # pipeline internals
├── executorch/       # ExecuTorch checkout (created during setup; name cannot be changed, CMake requires it)
│   └── cmake-out/      # CMake build outputs (created after building runners)
│       ├── mac-arm64/executor_runner              # SME2-on runner
│       ├── mac-arm64-sme2-off/executor_runner      # SME2-off runner
│       ├── android-arm64-v9a/executor_runner       # Android SME2-on runner (if built)
│       └── android-arm64-v9a-sme2-off/executor_runner  # Android SME2-off runner (if built)
└── .venv/            # Python virtual environment
```

Why this layout: 
- `executorch/` must be named exactly `executorch/` (not `executorch_v1/` or `my_executorch/`) because ExecuTorch's CMake build system hardcodes paths relative to this directory name. The CMake configuration expects to find submodules, backends, and build scripts at specific relative paths from `executorch/`. Renaming it would break the build.
- `executorch/cmake-out/` keeps runners with their ExecuTorch version, making it easy to trace which ExecuTorch commit/config was used to build each runner. This is especially valuable when comparing performance across ExecuTorch versions or debugging issues tied to specific commits.
- This enables working with multiple ExecuTorch versions in parallel (e.g., `executorch_v1/`, `executorch_v2/`) for the same model profiling work. Each checkout maintains its own `cmake-out/` directory with its own runners, so you can profile the same model against different ExecuTorch versions without conflicts.
- `out_<model>/` keeps exported artifacts separate from source code
- `out_<model>/runs/` keeps run outputs with the model they profile (model-specific data stays together)

## 2. Setup (minimal, happy path)

Run this once:

```bash
bash model_profiling/scripts/setup_repo.sh
```

This script automates the ExecuTorch installation process. See [`setup_repo.sh`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/scripts/setup_repo.sh) for the implementation. For detailed information about building ExecuTorch from source, see the [official ExecuTorch documentation](https://docs.pytorch.org/executorch/1.0/using-executorch-building-from-source.html).

What it does:

- creates `.venv/` and activates it
- clones `executorch/` (tracks `origin/main`) if missing, or updates existing checkout
- initializes submodules: `cd executorch && git submodule sync && git submodule update --init --recursive`
- installs ExecuTorch in editable mode: `cd executorch && pip install -e .`

**Why editable mode**: The export script needs to import ExecuTorch modules and patch the model registry. Editable installs make this work without copying code around. More importantly, editable mode enables easy PR testing: you can checkout different ExecuTorch branches or PRs in the `executorch/` directory, and the export script will automatically use the currently checked-out code without reinstalling. This is essential when testing how new ExecuTorch changes affect model export and profiling.

Manual equivalent (if you prefer step-by-step):

```bash
# 1) Create venv
python3 -m venv .venv
source .venv/bin/activate

# 2) Clone/update ExecuTorch
if [ ! -d executorch ]; then
  git clone https://github.com/pytorch/executorch.git executorch
fi
cd executorch
git fetch origin main --depth 1
git checkout -B main origin/main

# 3) Initialize submodules (required for XNNPACK, KleidiAI, etc.)
git submodule sync
git submodule update --init --recursive

# 4) Install ExecuTorch in editable mode
pip install -e .
cd ..
```

Verify it worked:

```bash
# Check venv exists and ExecuTorch is importable
source .venv/bin/activate
python -c "import executorch; print(f'ExecuTorch: {executorch.__file__}')"

# Check executorch/ directory and submodules exist
ls -d executorch/
ls -d executorch/backends/xnnpack/third-party/XNNPACK  # Verify submodule initialized
```

## 3. Build runners (once for all models)

After setup, build the ExecuTorch runners. This is done once and works for all models, unless you need to change CMake build configurations (e.g., enabling trace logging, changing optimization flags):

```bash
bash model_profiling/scripts/build_runners.sh
```

See [`build_runners.sh`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/scripts/build_runners.sh) for the implementation.

This produces runners in `executorch/cmake-out/`:
- `executorch/cmake-out/mac-arm64/executor_runner` (SME2-on)
- `executorch/cmake-out/mac-arm64-sme2-off/executor_runner` (SME2-off)
- Recommended: Android runners if `ANDROID_NDK` is set (mobile devices provide more realistic edge ML performance due to different CPU architectures, memory bandwidth, and thermal constraints compared to Mac)

**Why this is done once**: The runners are model-agnostic. They can execute any `.pte` file, so you build them once and reuse them for all models you profile. You only need to rebuild if you change CMake build configurations (e.g., enabling XNNPACK kernel trace logging for kernel-level analysis).

**Critical compatibility requirement**: The model export and runner building must use the same or compatible ExecuTorch version. If you export a model with one ExecuTorch version and build runners with a different version, the `.pte` file may not be compatible with the runner. This is why runners stay in `executorch/cmake-out/` alongside their ExecuTorch checkout—it ensures version consistency.

**The two-run workflow**: You need two types of runners for complete profiling:
- Timing-only runners (default): No trace logging overhead → accurate latency measurements
- XNNPACK kernel trace runners: Enable `xnntrace` logging → kernel-level insights (logging impacts timing, use only for kernel analysis)

The build script produces timing-only runners by default. For kernel-level analysis, you'll need separate trace-enabled runners built with XNNPACK kernel logging flags.

How it works: ExecuTorch ships with a default `CMakePresets.json`, but we add custom presets for SME2 profiling (SME2-on/off variants, platform-specific configs). The build script merges our custom presets ([`model_profiling/assets/cmake_presets.json`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/assets/cmake_presets.json)) into ExecuTorch's default file, then uses `cmake --preset` commands. This approach keeps ExecuTorch's defaults intact while adding our profiling-specific configurations. No manual CMake flags needed.

Example preset (SME2-on for macOS):

```json
{
  "name": "mac-arm64",
  "displayName": "Mac arm64 with XNNPACK (SME2 ON, timing)",
  "generator": "Ninja",
  "binaryDir": "${sourceDir}/cmake-out/mac-arm64",
  "cacheVariables": {
    "EXECUTORCH_BUILD_XNNPACK": "ON",
    "EXECUTORCH_BUILD_DEVTOOLS": "ON",
    "EXECUTORCH_BUILD_EXECUTOR_RUNNER": "ON",
    "EXECUTORCH_ENABLE_LOGGING": "ON",
    "EXECUTORCH_ENABLE_EVENT_TRACER": "ON",
    "EXECUTORCH_BUILD_KERNELS_QUANTIZED": "ON",
    "EXECUTORCH_BUILD_KERNELS_QUANTIZED_AOT": "ON",
    "EXECUTORCH_XNNPACK_ENABLE_KLEIDI": "ON",
    "CMAKE_BUILD_TYPE": "RelWithDebInfo"
  }
}
```

Key settings explained:

- `EXECUTORCH_ENABLE_EVENT_TRACER: ON` - Enables ETDump trace generation (required for profiling)
- `EXECUTORCH_BUILD_DEVTOOLS: ON` - Enables profiling tools
- `EXECUTORCH_BUILD_EXECUTOR_RUNNER: ON` - Builds the runner binary
- `EXECUTORCH_XNNPACK_ENABLE_KLEIDI: ON` - Enables Arm KleidiAI kernels
- `EXECUTORCH_BUILD_KERNELS_QUANTIZED: ON` - Enables quantized kernel support for INT8 models

**Note:** SME2 acceleration is enabled by default in XNNPACK when building for Arm architectures, so `XNNPACK_ENABLE_ARM_SME2` is not needed in this example.

## 4. Pipeline components: what stays the same across models

The profiling pipeline is the end-to-end workflow that:

1. Runs your model with specified configurations
2. Collects performance data (timing measurements and ETDump traces)
3. Analyzes results to produce operator-level breakdowns and comparison reports

The pipeline is model-agnostic and experiment-driven. You define experiments in JSON configs, and the same scripts run them for any model. This enables repeatable, systematic profiling across different configurations without modifying the pipeline code.

The workflow (quick summary):

1. Create a JSON config pointing to your `.pte` file and desired experiments
2. Run the pipeline script
3. Analyze the results

Swap the `.pte` file and config, everything else stays the same. See 03 – Model onboarding + profiling for the complete workflow.

### 4.1 Config-driven experiments

JSON configs define repeatable experiments with different settings. Each config can define multiple experiments in a single run, making it easy to compare configurations side-by-side.

Key configuration options:

- Runner selection: SME2-on vs SME2-off runners, timing-only vs trace-enabled runners
- Model variants: Different `.pte` files (FP16, INT8, different quantization schemes)
- Runtime settings: Number of CPU threads, warmup runs, measurement runs
- Logging level: Timing-only mode vs full ETDump trace mode (trace mode impacts timing, use for kernel-level insights)
- Analysis comparisons: Which experiment pairs to compare (e.g., SME2-on vs SME2-off)

### 4.2 Pipeline scripts

The pipeline scripts are model-agnostic—they work with any `.pte` file:

Run scripts:
- [`model_profiling/scripts/mac_pipeline.py`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/scripts/mac_pipeline.py) - macOS profiling pipeline
- [`model_profiling/scripts/android_pipeline.py`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/scripts/android_pipeline.py) - Android profiling pipeline

These scripts read JSON configs, execute all experiments defined in the config, and collect ETDump traces and timing logs. Point the config to a different `.pte` file, and the same scripts work for any model.

Analysis scripts:
- [`model_profiling/scripts/analyze_results.py`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/scripts/analyze_results.py) - Processes ETDump traces and logs

This script generates operator-level breakdowns, category-level summaries, and comparison reports. It parses structured data (ETDump, CSV, JSON) produced by the runners, regardless of which model generated them.

### 4.3 Output structure

All runs follow the same directory layout: `out_<model>/runs/<platform>/<experiment_name>/...`

This consistent structure makes it easy to:
- Compare results across models
- Track experiment history
- Generate reports from structured outputs
