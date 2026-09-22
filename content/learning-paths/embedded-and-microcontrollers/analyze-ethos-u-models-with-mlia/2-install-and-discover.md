---
title: Install MLIA and discover capabilities

description: Install the MLIA Ethos-U plugin, inspect target profiles and backends, and download the model artifacts used in the analysis examples.

weight: 3

### FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Check your environment

Use Ubuntu 22.04 LTS or another compatible Linux environment with Python 3.10 or later.

Check that Git LFS is installed:

```bash
git lfs version
```

If this command fails, install Git LFS and the Python development package:

```bash
sudo apt update
sudo apt install -y git-lfs python3.10-dev
```

## Create a Python environment

Create a virtual environment so the MLIA packages do not conflict with any existing ML framework environment.

```bash
python3 -m venv mlia_env
source mlia_env/bin/activate
python -m pip install --upgrade pip
```

## Install MLIA

MLIA uses plugins. The examples in this Learning Path use Ethos-U as the target, so install the Ethos-U plugin package:

```bash
pip install mlia-ethos-u
```

The Ethos-U plugin package depends on a compatible MLIA core package. Installing the target plugin is the recommended starting point because it brings in the matching MLIA core dependency.

## Confirm the CLI works

Display top-level help:

```bash
mlia --help
```

You should see commands similar to:

```output
  check     Generate compatibility/performance advice for a model
  backend   Manage MLIA backends
  target    Manage MLIA targets
```

The `mlia check` command is the main command you will use to ask MLIA compatibility and performance questions about model artifacts.

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

In this Learning Path, the examples use one Ethos-U85 profile:

```output
ethos-u85-256
```

Use a different profile if you want MLIA to evaluate the same model for a different Ethos-U configuration.

## Discover backends

Backends perform the work behind an MLIA analysis flow. List available and installed backends:

```bash
mlia backend list
```

For this Ethos-U demonstration, you should expect Vela and Corstone backend options. You use Vela for the LiteRT and TOSA checks, and Corstone for the packaged ExecuTorch `.pte` checks later in this Learning Path.

```output
Name          Installed  Installable
corstone-300  no         yes
corstone-310  no         yes
corstone-320  no         yes
vela          no         yes
```

When we later use `mlia check`, any missing backends required by your target will be installed.

## Clone model artifacts

This Learning Path uses prebuilt artifacts from the Arm ML model artifacts repository:

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

This downloads only the artifacts used in this Learning Path. It avoids larger unrelated files, such as transformer `.pte`, `.etdp`, and `.etrecord` artifacts.

Confirm that the artifacts are real model files, not Git LFS pointer files:

```bash
wc -c tflite/mv2_int8.tflite
```

You should see a size of several megabytes, similar to:

```output
3942808 tflite/mv2_int8.tflite
```

If the file is about 100 to 200 bytes, it is still a Git LFS pointer file. Run the `git lfs pull` command again from the `ml-model-artifacts` directory, then rerun the size check.

The model artifacts are provided for learning and analysis exercises. Use them to explore MLIA workflows, model formats, and target-aware advice, not as accuracy reference models.

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

## What you have learned

You have installed MLIA, along with the Ethos-U plugin, discovered available target profiles and backends from the CLI, and cloned model artifacts for analysis.

Next, you will run your first MLIA compatibility and performance checks.
