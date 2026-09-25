---
title: Install MLIA and discover capabilities

description: Install the MLIA Ethos-U plugin, inspect target profiles and backends, and download the model artifacts used in the analysis examples.

weight: 3

### FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Check your environment

Use Ubuntu 22.04 LTS or another compatible Linux environment with Python 3.10 or later.

Check that Git Large File Storage (LFS) is installed:

```bash
git lfs version
```

If the command fails, install Git LFS and the Python development package:

```bash
sudo apt update
sudo apt install -y git-lfs python3.10-dev
```

## Create a Python environment

Create a virtual environment so that the Arm ML Inference Advisor (MLIA) packages don't conflict with any existing ML framework environment:

```bash
python3 -m venv mlia_env
source mlia_env/bin/activate
python -m pip install --upgrade pip
```

## Install MLIA

MLIA uses plugins. The example target in the Learning Path is Ethos-U, so install the Ethos-U plugin package:

```bash
pip install mlia-ethos-u
```

The Ethos-U plugin package depends on a compatible MLIA core package. Installing the target plugin is the recommended starting point because it brings in the matching MLIA core dependency.

## Confirm the CLI works

Display top-level help:

```bash
mlia --help
```

The output is similar to:

```output
  check     Generate compatibility/performance advice for a model
  backend   Manage MLIA backends
  target    Manage MLIA targets
```

The `mlia check` command is the main command you'll use to ask MLIA compatibility and performance questions about model artifacts.

## Discover target profiles

MLIA target profiles describe the target configuration used for analysis. List the target profiles available in your environment:

```bash
mlia target list
```

For Ethos-U, typical bundled profiles include:

| Target profile | Ethos-U NPU | MACs per cycle |
| --- | --- | --- |
| `ethos-u55-128` | Ethos-U55 | 128 |
| `ethos-u55-256` | Ethos-U55 | 256 |
| `ethos-u65-256` | Ethos-U65 | 256 |
| `ethos-u65-512` | Ethos-U65 | 512 |
| `ethos-u85-128` | Ethos-U85 | 128 |
| `ethos-u85-256` | Ethos-U85 | 256 |
| `ethos-u85-512` | Ethos-U85 | 512 |
| `ethos-u85-1024` | Ethos-U85 | 1024 |
| `ethos-u85-2048` | Ethos-U85 | 2048 |


One Ethos-U85 profile (`ethos-u85-256`) is used in the examples. Use a different profile if you want MLIA to evaluate the same model for a different Ethos-U configuration.

## Discover backends

Backends perform the work behind an MLIA analysis flow. List available and installed backends:

```bash
mlia backend list
```

For this Ethos-U demonstration, expect Vela and Corstone backend options:

```output
Name          Installed  Installable
corstone-300  no         yes
corstone-310  no         yes
corstone-320  no         yes
vela          no         yes
```

Use Vela for LiteRT and Tensor Operator Set Architecture (TOSA) checks. Use Corstone for packaged ExecuTorch `.pte` checks.

When you later use `mlia check`, any missing backends required by your target will be installed.

## Clone model artifacts

Clone prebuilt artifacts from the Arm ML model artifacts repository:

```bash
git lfs install
git clone --filter=blob:none --sparse https://github.com/arm-education/ml-model-artifacts.git
cd ml-model-artifacts
git sparse-checkout set pte tflite tosa
git lfs pull \
  --include="pte/toy_conditional_select_int8_ethos_u55_256.pte,pte/toy_conditional_select_int8_ethos_u85_256.pte,tflite/mv2_fp32.tflite,tflite/mv2_int8.tflite,tosa/mv2_fp32.tosa,tosa/mv2_int8.tosa" \
  --exclude=""
git lfs checkout
```

This downloads only the artifacts that are required for you to complete the Learning Path. It avoids larger unrelated files, such as transformer `.pte`, `.etdp`, and `.etrecord` artifacts.

Confirm that the artifacts are real model files rather than Git LFS pointer files:

```bash
wc -c tflite/mv2_int8.tflite
```

The output is a size of several megabytes, similar to:

```output
3942808 tflite/mv2_int8.tflite
```

If the file is about 100 to 200 bytes, it's still a Git LFS pointer file. Run the `git lfs pull` command again from the `ml-model-artifacts` directory, then rerun the size check.

The model artifacts are provided for learning and analysis exercises. Use the artifacts to explore MLIA workflows, model formats, and target-aware advice rather than accuracy reference models.

The repository contains model artifacts such as:

```output
ml-model-artifacts/
├── pte/
│   ├── toy_conditional_select_int8_ethos_u55_256.pte
│   └── toy_conditional_select_int8_ethos_u85_256.pte
├── tflite/
│   ├── mv2_fp32.tflite
│   └── mv2_int8.tflite
└── tosa/
    ├── mv2_fp32.tosa
    └── mv2_int8.tosa
```

## What you've accomplished and what's next

You've installed MLIA, along with the Ethos-U plugin. You've also discovered available target profiles and backends from the CLI, and cloned model artifacts for analysis.

Next, you'll run your first MLIA compatibility and performance checks.
