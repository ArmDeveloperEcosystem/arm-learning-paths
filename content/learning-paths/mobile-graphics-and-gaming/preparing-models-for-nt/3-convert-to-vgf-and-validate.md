---
title: Export the reference model with the ExecuTorch VGF backend
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the VGF workflow

`.vgf` is the deployable format used by Arm neural technology with ML Extensions for Vulkan. In this section, you'll use the ExecuTorch VGF backend to generate deployable artifacts directly from the exported PyTorch model. You'll then run a quick validation pass.

This is the path to use first because it matches the model preparation workflow you'll use before connecting a model to downstream Vulkan samples, engine integrations, or the Scenario Runner. Tensor Operator Set Architecture (TOSA) is still useful, but treat it as the deeper inspection step when you need to debug what happened between PyTorch export and backend output.

## Lower directly with the ExecuTorch VGF backend

Create a Python file named `export_vgf.py`:

```python
import os
import torch

from executorch.backends.arm.vgf import VgfCompileSpec, VgfPartitioner
from executorch.exir import (
    EdgeCompileConfig,
    ExecutorchBackendConfig,
    to_edge_transform_and_lower,
)
from executorch.extension.export_util.utils import save_pte_program

os.makedirs("executorch-model", exist_ok=True)

exported_model = torch.export.load("add_sigmoid.pt2")

compile_spec = VgfCompileSpec()
compile_spec.dump_intermediate_artifacts_to("executorch-model")
partitioner = VgfPartitioner(compile_spec)

edge_pm = to_edge_transform_and_lower(
    exported_model,
    partitioner=[partitioner],
    compile_config=EdgeCompileConfig(_check_ir_validity=False),
)

et_pm = edge_pm.to_executorch(
    config=ExecutorchBackendConfig(extract_delegate_segments=False)
)

pte_path = os.path.abspath("as-vgf.pte")
save_pte_program(et_pm, pte_path)
print("Wrote:", pte_path)
```

Run the script:

```bash
python export_vgf.py
```

After this step, inspect the `.vgf` artifacts in `executorch-model/` and the generated `as-vgf.pte` file.

## (Optional) Build and run VKML runtime validation

From the `preparing-models-for-nt` working directory, build the runner:

```bash
cd repo/executorch
source ./examples/arm/arm-scratch/setup_path.sh
cd ./examples/arm

cmake \
  -DCMAKE_INSTALL_PREFIX=cmake-out \
  -DCMAKE_BUILD_TYPE=Debug \
  -DEXECUTORCH_BUILD_EXTENSION_DATA_LOADER=ON \
  -DEXECUTORCH_BUILD_EXTENSION_MODULE=ON \
  -DEXECUTORCH_BUILD_EXTENSION_NAMED_DATA_MAP=ON \
  -DEXECUTORCH_BUILD_EXTENSION_FLAT_TENSOR=ON \
  -DEXECUTORCH_BUILD_EXTENSION_TENSOR=ON \
  -DEXECUTORCH_BUILD_KERNELS_QUANTIZED=ON \
  -DEXECUTORCH_BUILD_XNNPACK=OFF \
  -DEXECUTORCH_BUILD_VULKAN=ON \
  -DEXECUTORCH_BUILD_VGF=ON \
  -DEXECUTORCH_ENABLE_LOGGING=ON \
  -DPYTHON_EXECUTABLE=python \
  -B../../cmake-out-vkml ../..

cmake --build ../../cmake-out-vkml --target executor_runner

cd ../../..
```

This confirms that you can build the binary used to execute the generated `.pte`. To connect this validation step to a full ML Extensions for Vulkan workflow, see [Setting up the ML Emulation Layers for Vulkan](/learning-paths/mobile-graphics-and-gaming/vulkan-ml-sample/2-ml-ext-for-vulkan/) and [Setting up the emulation layers for NSS in Unreal Engine](/learning-paths/mobile-graphics-and-gaming/nss-unreal/2-emulation-layer/).

Create a Python file named `run_vgf_pte.py` to run the generated `.pte`:

```python
import os
import subprocess

cwd_dir = os.getcwd()
script_dir = os.path.join(cwd_dir, "repo", "executorch", "backends", "arm", "scripts")
et_dir = os.path.join(cwd_dir, "repo", "executorch")
pte_path = os.path.abspath("as-vgf.pte")

args = f"--model={pte_path}"
subprocess.run(
    os.path.join(script_dir, "run_vkml.sh") + " " + args,
    shell=True,
    cwd=et_dir,
    check=True,
)
```

Run the script:

```bash
python run_vgf_pte.py
```

For an input tensor of ones, `x + y = 2`, so the expected output is close to `sigmoid(2) = 0.880797`.

If you want to run a packaged end-to-end sample after validating this toy model, see [Running a test with the Scenario Runner](/learning-paths/mobile-graphics-and-gaming/vulkan-ml-sample/4-scenario-runner/). For toy ML Extensions for Vulkan run command, see [Simple Tensor and Data Graph](/learning-paths/mobile-graphics-and-gaming/vulkan-ml-sample/3-first-sample/).

## What you've accomplished and what's next

You've now exported the `AddSigmoid` model with the ExecuTorch VGF backend, generated `.vgf` artifacts, and optionally built and run the VKML validation path.

Next, you'll inspect the generated model artifacts in Model Explorer to confirm the graph structure, tensor shapes, and backend output.
