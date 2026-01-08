---
title: Convert the model to ExecuTorch format
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a virtual environment

Create and activate a Python virtual environment to manage dependencies. Python 3.10 is recommended for compatibility with the required packages:

```bash
cd $WORKSPACE/ML-examples/kleidiai-examples/audiogen-et/
python3.10 -m venv .venv
source .venv/bin/activate
```

## Install ExecuTorch

Install the ExecuTorch package version 1.0.0:

```bash
pip install executorch==1.0.0
```

Alternatively, you can clone the ExecuTorch repository and run the installation script:

```bash
git clone https://github.com/pytorch/executorch.git
cd executorch
git checkout v1.0.0
bash ./install_executorch.sh
cd ..
```

## Install Stable Audio tools

Install the Stable Audio Open tools dependency:

```bash
pip install git+https://github.com/Stability-AI/stable-audio-tools.git@31932349d98c550c48711e7a5a40b24aa3d7c509
```

## Export the model submodules

Now you can export the three model submodules to ExecuTorch format using the provided script.

Run the export script from the `audiogen-et` directory:

```bash
python ./scripts/export_sao.py --ckpt_path $WORKSPACE/model.ckpt --model_config $WORKSPACE/model_config.json
```

The script converts all three submodules (Conditioners, DiT, and AutoEncoder) and exports them to `.pte` files.

### Troubleshooting conversion issues

If you see a `FileNotFoundError` related to missing `.fbs` files during conversion:

```output
FileNotFoundError: [Errno 2] No such file or directory: '../kleidiai-examples/audiogen-et/scripts/executorch/exir/_serialize/program.fbs'
```

Run these commands to copy the required schema files:

```bash
export EXECUTORCH_ROOT=<PATH-TO-EXECUTORCH>
cp $EXECUTORCH_ROOT/schema/program.fbs $EXECUTORCH_ROOT/exir/_serialize/program.fbs
cp $EXECUTORCH_ROOT/schema/scalar_type.fbs $EXECUTORCH_ROOT/exir/_serialize/scalar_type.fbs
```

Then retry the export script.

## Verify exported models

After successful conversion, three `.pte` model files are created in the current directory:
- `conditioners_model.pte`
- `dit_model.pte`
- `autoencoder_model.pte`

These files are required to run the audio generation application on Android or macOS.

Verify the files were created:

```bash
ls -lh conditioners_model.pte dit_model.pte autoencoder_model.pte
```

The files should be in `$WORKSPACE/ML-examples/kleidiai-examples/audiogen-et/`.


In this section, you installed Executorch and the Stable Audio tools dependencies. You converted the three Stable Audio Open Small submodules to ExecuTorch format.

In the following sections, you will build the audio generation application for your target platform (Android or macOS).
