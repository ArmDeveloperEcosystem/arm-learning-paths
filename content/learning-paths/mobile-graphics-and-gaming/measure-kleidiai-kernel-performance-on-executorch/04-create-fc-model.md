---
title: Create and quantize linear layer benchmark model
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In the previous section, we discussed that the Fully Connected operator supports multiple GEMM (General Matrix Multiplication) variants.

To evaluate the performance of these variants across different hardware platforms, we will construct a series of benchmark models that utilize the Fully Connected operator with different GEMM implementations for comparative analysis.


### Fully connected benchmark model

In the following example model, we use simple model to generate nodes that can be accelerated by Kleidiai. 

By adjusting some of the model’s input parameters, we can also simulate the behavior of nodes that appear in real-world models.


```python
import torch
import torch.nn as nn
class DemoLinearModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256,256)

    def forward(self, x):
        y = self.linear(x)
        return y

    def get_example_inputs(self,dtype=torch.float32):
        return (torch.randn(1, 256, dtype=dtype),)

```

### Export FP16/FP32 model for pf16_gemm/pf32_gemm Variants

| XNNPACK GEMM Variant | Activations DataType| Weights DataType | Output DataType                      |
| ------------------  | ---------------------------- | --------------------------------------- | ---------------------------- |
| pf16_gemm    | FP16                         | FP16                                    | FP16                         |
| pf32_gemm    | FP32                         | FP32                                    | FP32                         |

The following code demonstrates how to lower and export a model that leverages the pf16_gemm variant to accelerate computation:

``` python 
from executorch.backends.xnnpack.partition.xnnpack_partitioner import XnnpackPartitioner
from executorch.backends.xnnpack.partition.config.xnnpack_config import ConfigPrecisionType
from executorch.exir import to_edge_transform_and_lower

def export_executorch_model(dtype: torch.dtype, model_name: str):
    mode_file_name = "model/" + model_name
    pte_file = mode_file_name + ".pte"
    etr_file = mode_file_name + ".etrecord"

    model = DemoLinearModel().eval().to(dtype)
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

export_executorch_model(torch.float16,"linear_model_pf16_gemm")

```

To generate a model that uses the pf32_gemm variant, simply change the dtype in the previous code to torch.float32, as shown below:

```python 

export_executorch_model(torch.float32,"linear_model_pf32_gemm")

```

### Export int8 quantized model for pqs8_qc8w_gemm and qp8_f32_qc8w_gemm variant

| XNNPACK GEMM Variant | Activations DataType| Weights DataType | Output DataType                      |
| ------------------  | ---------------------------- | --------------------------------------- | ---------------------------- |
| qp8_f32_qc8w_gemm | Asymmetric INT8 per-row quantization | Per-channel symmetric INT8 quantization | FP32                         |
| pqs8_qc8w_gemm    | Asymmetric INT8 quantization | Per-channel symmetric INT8 quantization | Asymmetric INT8 quantization |


The following code demonstrates how to quantized a model that leverages the pqs8_qc8w_gemm/qp8_f32_qc8w_gemm  variant to accelerate computation:

```python 

from torchao.quantization.pt2e.quantize_pt2e import convert_pt2e, prepare_pt2e
from executorch.backends.xnnpack.quantizer.xnnpack_quantizer import (
    get_symmetric_quantization_config,
    XNNPACKQuantizer,
)

def export_int8_quantize_model(dynamic: bool, model_name: str):
    mode_file_name = "model/" + model_name
    pte_file = mode_file_name + ".pte"
    etr_file = mode_file_name + ".etrecord"

    model = DemoLinearModel().eval().to(torch.float32)
    example_inputs = model.get_example_inputs(torch.float32)

    #Quantizer model
    model = torch.export.export(model, example_inputs).module()
    quantizer = XNNPACKQuantizer()
    operator_config = get_symmetric_quantization_config(
        is_per_channel=True,
        is_dynamic=dynamic
    )

    quantizer.set_global(operator_config)
    quantize_model = prepare_pt2e(model, quantizer)
    quantize_model(*example_inputs)
    quantize_model = convert_pt2e(quantize_model)

    #lower and export model
    exported_program = torch.export.export(quantize_model, example_inputs)

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

export_int8_quantize_model(False,"linear_model_pqs8_qc8w_gemm");
export_int8_quantize_model(True,"linear_model_qp8_f32_qc8w_gemm");

```

### Export int4 quantized model for qp8_f32_qb4w_gemm variant
| XNNPACK GEMM Variant | Activations DataType| Weights DataType | Output DataType                      |
| ------------------  | ---------------------------- | --------------------------------------- | ---------------------------- |
| qp8_f32_qb4w_gemm | Asymmetric INT8 per-row quantization | INT4 (signed), shared blockwise quantization | FP32                         |


The following code demonstrates how to quantized a model that leverages the qp8_f32_qb4w_gemm variant to accelerate computation:

```python 
from torchao.quantization.granularity import PerGroup, PerAxis
from torchao.quantization.quant_api import (
    IntxWeightOnlyConfig,
    Int8DynamicActivationIntxWeightConfig,
    quantize_,
)

def export_int4_quantize_model(dynamic: bool, model_name: str):
    mode_file_name = "model/" + model_name
    pte_file = mode_file_name + ".pte"
    etr_file = mode_file_name + ".etrecord"

    model = DemoLinearModel().eval().to(torch.float32)
    example_inputs = model.get_example_inputs(torch.float32)

    #Quantizer model

    linear_config = Int8DynamicActivationIntxWeightConfig(
        weight_dtype=torch.int4,
        weight_granularity=PerGroup(32),
    )

    quantize_(model, linear_config)

    #lower and export model
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

export_int4_quantize_model(False,"linear_model_qp8_f32_qb4w_gemm");


```

**NOTE:**

When exporting models, the **generate_etrecord** option is enabled to produce the .etrecord file alongside the .pte model file.
These ETRecord files are essential for subsequent model inspection and performance analysis using the ExecuTorch Inspector API.


After running this script, both the PTE model file and the etrecord file are generated.

``` bash 
$ ls model/ -1
linear_model_pf16_gemm.etrecord
linear_model_pf16_gemm.pte
linear_model_pf32_gemm.etrecord
linear_model_pf32_gemm.pte
linear_model_pqs8_qc8w_gemm.etrecord
linear_model_pqs8_qc8w_gemm.pte
linear_model_qp8_f32_qb4w_gemm.etrecord
linear_model_qp8_f32_qb4w_gemm.pte
linear_model_qp8_f32_qc8w_gemm.etrecord
linear_model_qp8_f32_qc8w_gemm.pte
```

The complete source code is available [here](../export-linear-model.py).
