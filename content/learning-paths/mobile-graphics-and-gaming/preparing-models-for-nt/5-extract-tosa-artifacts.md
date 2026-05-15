---
title: Inspect TOSA artifacts
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the role of TOSA

The primary workflow in this Learning Path is PyTorch export to `.vgf` with the ExecuTorch VGF backend. If you want to understand what happens in the middle, Tensor Operator Set Architecture (TOSA) is the stable intermediate representation (IR) between PyTorch export and backend-specific artifacts such as `.vgf`.

By extracting TOSA, you can:

- Check operator lowering before backend compilation
- Confirm tensor layout and shape flow
- Compare behavior when different backends produce different results

This is especially useful when you debug export issues before deployment to NX-enabled pipelines, but you don't need to start here for the normal model preparation workflow.

## Dump TOSA for the exported model

Create a Python file named `dump_tosa.py`. This script loads the `add_sigmoid.pt2` file created in [Create a reference model](/learning-paths/mobile-graphics-and-gaming/preparing-models-for-nt/2-create-reference-model/):

```python
from pathlib import Path

import torch

from executorch.backends.arm.tosa import TosaSpecification
from executorch.backends.arm.tosa.compile_spec import TosaCompileSpec
from executorch.backends.arm.util._factory import create_partitioner
from executorch.exir import EdgeCompileConfig, to_edge_transform_and_lower

BASE_DUMP = Path("tosa-dump")


def dump_tosa(ep, profile_str: str, label: str):
    BASE_DUMP.mkdir(parents=True, exist_ok=True)

    tosa_spec = TosaSpecification.create_from_string(profile_str)
    compile_spec = TosaCompileSpec(tosa_spec)
    compile_spec.dump_intermediate_artifacts_to(str(BASE_DUMP))

    partitioner = create_partitioner(compile_spec)

    _ = to_edge_transform_and_lower(
        ep,
        partitioner=[partitioner],
        compile_config=EdgeCompileConfig(_check_ir_validity=False),
    )

    tosa_files = list(BASE_DUMP.rglob("*.tosa"))
    print(f"\\n{label}")
    print(f"  Profile: {profile_str}")
    print(f"  Dump dir: {BASE_DUMP.resolve()}")
    print(f"  Total .tosa files so far: {len(tosa_files)}")


# FP profile used in this tutorial
# For INT flows, see the quantization LP.
exported_model = torch.export.load("add_sigmoid.pt2")
dump_tosa(exported_model, "TOSA-1.0+FP", "AddSigmoidModel (float)")
```

Run the script:

```bash
python dump_tosa.py
```

You should now have one or more `.tosa` files under `tosa-dump/` for inspection.

## (Optional) Convert TOSA to VGF with model_converter

The ExecuTorch VGF backend is the recommended path in this Learning Path. When you need to compare the intermediate TOSA route explicitly, create a Python file named `convert_tosa_to_vgf.py`:

```python
import pathlib
import subprocess

tosa_path = pathlib.Path("./tosa-dump/output_tag0_TOSA-1.0+FP.tosa")
vgf_path = pathlib.Path("./executorch-model/model-from-tosa.vgf")

vgf_path.parent.mkdir(parents=True, exist_ok=True)

subprocess.run(
    [
        "model_converter",
        "--input",
        str(tosa_path),
        "--output",
        str(vgf_path),
    ],
    check=True,
)

print("Wrote:", vgf_path.resolve())
```

Run the script:

```bash
python convert_tosa_to_vgf.py
```

You can now compare the direct ExecuTorch VGF backend output with the `.vgf` generated from TOSA.

## What you've accomplished

You've now completed a manual model preparation workflow for Arm neural technology. You set up the ExecuTorch environment and created and exported an `AddSigmoid` PyTorch reference model. You then lowered it with the ExecuTorch VGF backend, generated `.vgf` and `.pte` artifacts, validated the output with an ExecuTorch runner, and inspected the generated graph in Model Explorer. You also learned where TOSA fits in the workflow.

In addition to Model Gym for higher-level training, evaluation, and export workflows, you now have this manual ExecuTorch flow. 

Use [Model Gym](/learning-paths/mobile-graphics-and-gaming/model-training-gym/) when you want to:
- Fine-tune NSS quickly
- Work through notebook-based training and evaluation
- Standardize export pipelines with less backend-level tuning

Use the manual flow from this Learning Path when you need to:
- Debug export correctness at the TOSA level
- Control backend partitioning and artifact generation
- Validate backend/runtime behavior with custom test graphs
- Build confidence with a toy model before moving to Scenario Runner or engine-level validation

