---
title: Create matrix multiply layer benchmark model
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Learn how batch matrix multiply accelerates deep learning on Arm

The batch matrix multiply operator (`torch.bmm`) is commonly used for efficient matrix operations in deep learning models. When running on Arm systems with XNNPACK, this operator is lowered to a general matrix multiplication (GEMM) implementation. If your input shapes and data types match supported patterns, XNNPACK can automatically dispatch these operations to KleidiAI micro-kernels, which are optimized for Arm hardware.

To compare the performance of different GEMM variants on various Arm platforms, you'll build a set of benchmark models. These models use the batch matrix multiply operator and allow you to evaluate how each GEMM implementation performs, helping you identify the best configuration for your workload.


## Define a matrix multiply benchmark model for KleidiAI and ExecuTorch

The following example defines a simple model to generate nodes that can be accelerated by KleidiAI.

By adjusting the input parameters, this model can also simulate the behavior of nodes commonly found in real-world models:


```python
class DemoBatchMatMulModel(nn.Module):
    def forward(self, x,y):
        return torch.bmm(x, y)

    def get_example_inputs(self,dtype=torch.float32):
        return (torch.randn(1, 256, 256, dtype=dtype),torch.randn(1, 256, 256, dtype=dtype))

```

## Export FP16 and FP32 models for pf16_gemm and pf32_gemm variants

| XNNPACK GEMM Variant | Input A DataType| Input B DataType |Output DataType |
| ------------------  | ---------------------------- | --------------------------------------- |--------------------------------------- |
| pf32_gemm    | FP32                         | FP32                         | FP32 | 
| pf16_gemm    | FP16                         | FP16                         | FP16 |

The following code snippet demonstrates how to lower the model that leverages the pf16_gemm and pf32_gemm variant to accelerate computation:

``` python 
from executorch.backends.xnnpack.partition.xnnpack_partitioner import XnnpackPartitioner
from executorch.backends.xnnpack.partition.config.xnnpack_config import ConfigPrecisionType
from executorch.exir import to_edge_transform_and_lower

def export_mutrix_mul_model(dtype: torch.dtype, model_name: str):
    mode_file_name = "model/" + model_name
    pte_file = mode_file_name + ".pte"
    etr_file = mode_file_name + ".etrecord"

    model = DemoBatchMatMulModel().eval().to(dtype)
    example_inputs = model.get_example_inputs(dtype)

    exported_program = torch.export.export(model, example_inputs)

    partitioner = XnnpackPartitioner()
    edge_program = to_edge_transform_and_lower(
        exported_program,
        partitioner=[partitioner],
        generate_etrecord=True
    )

    et_program = edge_program.to_executorch()
    with open(pte_file, "wb") as f:
        f.write(et_program.buffer)

    # Get and save ETRecord
    etrecord = et_program.get_etrecord()
    etrecord.save(etr_file)

export_mutrix_mul_model(torch.float16,"matrix_mul_pf16_gemm")
export_mutrix_mul_model(torch.float32,"matrix_mul_pf32_gemm")

```

{{%notice Note%}}
When exporting models, the **generate_etrecord** option is enabled to produce the .etrecord file alongside the .pte model file.
These ETRecord files are essential for subsequent model analysis and performance evaluation.
{{%/notice%}}

## Run the complete benchmark model script
Instead of executing each export block manually, you can download and run the full matrix-multiply benchmark script.
This script automatically builds and exports both FP16 and FP32 models, performing all necessary partitioning, lowering, and ETRecord generation:

```bash
wget https://raw.githubusercontent.com/pareenaverma/arm-learning-paths/refs/heads/content_review/content/learning-paths/mobile-graphics-and-gaming/measure-kleidiai-kernel-performance-on-executorch/export-matrix-mul.py
chmod +x export-matrix-mul.py
python3 ./export-matrix-mul.py
```

## Verify the output

After running this script, both the PTE model file and the etrecord file are generated.

``` bash 
$ ls model/ -1
model/matrix_mul_pf16_gemm.etrecord
model/matrix_mul_pf16_gemm.pte
model/matrix_mul_pf32_gemm.etrecord
model/matrix_mul_pf32_gemm.pte
```
These files are the inputs for upcoming executor_runner benchmarks, where you’ll measure and compare KleidiAI micro-kernel performance.

The [complete source code](../export-matrix-mul.py) is available.
