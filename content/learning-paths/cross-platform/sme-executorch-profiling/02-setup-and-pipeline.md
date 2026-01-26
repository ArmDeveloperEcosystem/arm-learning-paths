---
title: "Set up the ExecuTorch profiling environment"
weight: 3
layout: "learningpathall"
---

## Set up your workspace and build ExecuTorch runners

This section covers the one-time setup required to run the performance analysis pipeline. Once completed, this setup can be reused for all models you analyze. The pipeline is model-agnostic: after exporting a model to `.pte` format, the same runners, scripts, and analysis steps apply regardless of model architecture. Only the model export step is model-specific.

You will complete two tasks. First, set up the development environment and install ExecuTorch from source. Second, build ExecuTorch runner binaries (SME2 on and SME2 off).

Perform this setup once and reuse it across all subsequent analyses.
## Organize your profiling workspace

The profiling scripts expect a consistent directory layout. The structure below is created automatically as you run the setup and build scripts.

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
│       ├── android-arm64-v9a/executor_runner       # Android SME2-on runner (for mobile device testing, if built)
│       ├── android-arm64-v9a-sme2-off/executor_runner  # Android SME2-off runner (for mobile device testing, if built)
│       ├── mac-arm64/executor_runner              # macOS SME2-on runner (developer accessibility)
│       └── mac-arm64-sme2-off/executor_runner      # macOS SME2-off runner (developer accessibility)
└── .venv/            # Python virtual environment
```

Why this layout matters: 
  - The executorch/ directory must be named exactly executorch/. ExecuTorch's CMake configuration uses hardcoded relative paths and fails if this directory is renamed.
  - The executorch/cmake-out/ directory keeps runner binaries associated with a specific ExecuTorch checkout. This makes it easy to correlate profiling results with the ExecuTorch version used.
  - Keeping model outputs under out_<model>/ ensures exported artifacts and profiling results remain grouped by model, simplifying comparison and reproducibility.

This layout also allows multiple ExecuTorch versions to be tested in parallel by maintaining separate workspaces.

## Set up the environment

This step installs ExecuTorch from source and creates a Python virtual environment. It is required only once per workspace.

```bash
bash model_profiling/scripts/setup_repo.sh
```

The script creates and activates a Python virtual environment under .venv/, clones the ExecuTorch repository if it doesn't already exist, updates the repository and initializes required submodules, and installs ExecuTorch in editable mode.

Editable installation ensures that changes to the ExecuTorch source tree (for example, switching branches or testing pull requests) are immediately reflected without reinstalling the package. This is essential when testing how new ExecuTorch changes affect model export and performance analysis.

**Optional: Manual setup** 
If you prefer to perform the setup step by step, the equivalent commands are shown below.

```bash
python3 -m venv .venv
source .venv/bin/activate

if [ ! -d executorch ]; then
  git clone https://github.com/pytorch/executorch.git executorch
fi
cd executorch
git fetch origin main --depth 1
git checkout -B main origin/main

git submodule sync
git submodule update --init --recursive

pip install -e .
cd ..
```

After setup, verify that ExecuTorch is importable and submodules are present.

```bash
source .venv/bin/activate
python -c "import executorch; print(f'ExecuTorch: {executorch.__file__}')"
```
Check that the executorch directory and submodules exist:
```bash
ls -d executorch/
ls -d executorch/backends/xnnpack/third-party/XNNPACK 
```

## Build ExecuTorch runners with SME2 support

Next, build the ExecuTorch runner binaries used for profiling. These runners are model-agnostic and can execute any .pte file.
Run the build script:

```bash
bash model_profiling/scripts/build_runners.sh
```
The script builds both SME2-enabled and SME2-disabled runners to support direct performance comparison.

This generates runners in `executorch/cmake-out/`:

**Android runners** :
- `executorch/cmake-out/android-arm64-v9a/executor_runner` (SME2-on)
- `executorch/cmake-out/android-arm64-v9a-sme2-off/executor_runner` (SME2-off)
  
Android builds are performed automatically if the ANDROID_NDK environment variable is set.

**macOS runners** :
- `executorch/cmake-out/mac-arm64/executor_runner` (SME2-on)
- `executorch/cmake-out/mac-arm64-sme2-off/executor_runner` (SME2-off)

macOS runners are included to make the workflow accessible without requiring a mobile device.

**Why runners are built once**: The runners are model-agnostic. They can execute any `.pte` file, so you build them once and reuse them for all models you analyze. You only need to rebuild if you change CMake build configurations (for example, enabling XNNPACK kernel trace logging for kernel-level analysis).

**Version compatibility**: Model export and runner builds must use the same ExecuTorch version. A .pte file exported with one ExecuTorch revision may not be compatible with a runner built from another revision. Keeping runners under `executorch/cmake-out/` ensures this relationship remains explicit.

**The two-run workflow**: You need two types of runners for complete performance analysis. Timing-only runners (default) have no trace logging overhead and provide accurate latency measurements. XNNPACK kernel trace runners enable `xnntrace` logging for kernel-level insights (logging impacts timing, use only for kernel analysis).

The build script produces timing-only runners by default. For kernel-level analysis, you need separate trace-enabled runners built with XNNPACK kernel logging flags.

How it works: ExecuTorch ships with a default `CMakePresets.json`, but you can add custom presets for SME2 performance analysis (SME2-on/off variants, platform-specific configs). The build script merges your custom presets ([`model_profiling/assets/cmake_presets.json`](https://github.com/ArmDeveloperEcosystem/sme-executorch-profiling/blob/main/model_profiling/assets/cmake_presets.json)) into ExecuTorch's default file, then uses `cmake --preset` commands. This approach keeps ExecuTorch's defaults intact while adding our performance analysis-specific configurations. No manual CMake flags needed.

Example presets:

**Android (for mobile device testing)**:
```json
{
  "name": "android-arm64-v9a",
  "displayName": "Android arm64 with XNNPACK (SME2 ON, timing)",
  "generator": "Ninja",
  "binaryDir": "${sourceDir}/cmake-out/android-arm64-v9a",
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

**macOS (developer accessibility)**:
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

- `EXECUTORCH_ENABLE_EVENT_TRACER: ON` - Enables ETDump trace generation (required for performance analysis)
- `EXECUTORCH_BUILD_DEVTOOLS: ON` - Enables performance analysis tools
- `EXECUTORCH_BUILD_EXECUTOR_RUNNER: ON` - Builds the runner binary
- `EXECUTORCH_XNNPACK_ENABLE_KLEIDI: ON` - Enables Arm KleidiAI kernels
- `EXECUTORCH_BUILD_KERNELS_QUANTIZED: ON` - Enables quantized kernel support for INT8 models

**Note:** SME2 acceleration is enabled by default in XNNPACK when building for Arm architectures, so `XNNPACK_ENABLE_ARM_SME2` is not needed in this example.

## Understand the pipeline components

The performance analysis pipeline consists of three stages. First, execute the model under defined configurations. Second, collect timing data and ETDump traces. Third, analyze traces into operator-level and category-level summaries.

All stages are driven by JSON configuration files and are independent of model architecture.

### Config-driven experiments

Each experiment is defined in a JSON configuration file. These configs specify:
  * Which runner to use (SME2 on/off, timing-only or trace-enabled)
  * Which .pte model to execute
  * Runtime parameters such as CPU thread count and warmup iterations
  * Logging level: Timing-only mode vs full ETDump trace mode (trace mode impacts timing, use for kernel-level insights)
  * Analysis comparisons: Which experiment pairs to compare (e.g., SME2-on vs SME2-off)

This approach enables repeatable, systematic performance analysis across multiple configurations without modifying pipeline code.

### Pipeline scripts

The following scripts execute the pipeline::
- [`model_profiling/scripts/android_pipeline.py`](https://github.com/ArmDeveloperEcosystem/sme-executorch-profiling/blob/main/model_profiling/scripts/android_pipeline.py) - Android performance analysis pipeline
- [`model_profiling/scripts/mac_pipeline.py`](https://github.com/ArmDeveloperEcosystem/sme-executorch-profiling/blob/main/model_profiling/scripts/mac_pipeline.py) - macOS performance analysis pipeline 

These scripts read the experiment configuration, run all defined experiments, and collect ETDump traces and logs.
Analysis is performed automatically after execution using [`model_profiling/scripts/analyze_results.py`](https://github.com/ArmDeveloperEcosystem/sme-executorch-profiling/blob/main/model_profiling/scripts/analyze_results.py) 

Manual invocation is only required if you want to reprocess existing traces.

This script generates operator-level breakdowns, category-level summaries, and comparison reports. It parses structured data (ETDump, CSV, JSON) produced by the runners, regardless of which model generated them.

### Output structure

All profiling runs follow a consistent output layout `out_<model>/runs/<platform>/<experiment_name>/`:

This consistent structure makes it easy to:
- Compare results across models
- Track experiment history
- Generate reports from structured outputs

At this point, you have a working ExecuTorch development environment, SME2-enabled and SME2-disabled runner binaries and reusable, model-agnostic profiling pipeline.

In the next section, you will export a model, define experiments, and analyze how SME2 changes its performance profile.
