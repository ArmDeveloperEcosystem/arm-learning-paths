---
title: Create and quantize convolution layer benchmark model
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In the previous section, we discussed that both INT8-quantized Conv2d and pointwise (1×1) Conv2d operators can be accelerated using KleidiAI’s matrix-multiplication micro-kernels.


| XNNPACK GEMM Variant | Input DataType| Filter DataType | Output DataType                      |
| ------------------  | ---------------------------- | --------------------------------------- | ---------------------------- |
| pqs8_qc8w_gemm | Asymmetric INT8 quantization(NHWC) | Per-channel or per-tensor symmetric INT8 quantization | Asymmetric INT8 quantization(NHWC) |
| pf32_gemm    | FP32                         | FP32, pointwise (1×1)                   | FP32                         |

To evaluate the performance of Conv2d operators across multiple hardware platforms, we create a set of benchmark models that utilize different GEMM implementation variants within the convolution operators for systematic comparative analysis.


### INT8-quantized Conv2d benchmark model

The following example defines a simple model to generate INT8-quantized Conv2d nodes that can be accelerated by KleidiAI.

By adjusting some of the model’s input parameters, we can also simulate the behavior of nodes that appear in real-world models.


```python
import torch
import torch.nn as nn

class DemoQInt8Conv2dModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 6, 3)

    def forward(self,x):
         x = self.conv(x)
         return x

    def get_example_inputs(self,dtype=torch.float32):
        return (torch.randn(1, 3, 16, 16, dtype=dtype),)

```

The following code can be used to quantize and export the model:

```python
from executorch.backends.xnnpack.partition.xnnpack_partitioner import XnnpackPartitioner
from executorch.backends.xnnpack.partition.config.xnnpack_config import ConfigPrecisionType
from executorch.exir import to_edge_transform_and_lower
from torchao.quantization.pt2e.quantize_pt2e import convert_pt2e, prepare_pt2e
from executorch.backends.xnnpack.quantizer.xnnpack_quantizer import (
    get_symmetric_quantization_config,
    XNNPACKQuantizer,
)

def export_int8_quantize_conv2d_model(model_name: str):
    mode_file_name = "model/" + model_name
    pte_file = mode_file_name + ".pte"
    etr_file = mode_file_name + ".etrecord"

    model = DemoQInt8Conv2dModel().eval().to(torch.float32)
    example_inputs = model.get_example_inputs(torch.float32)

    #Quantizer model
    model = torch.export.export(model, example_inputs).module()
    quantizer = XNNPACKQuantizer()
    operator_config = get_symmetric_quantization_config(
        is_per_channel=False,
        is_dynamic=False
    )

    quantizer.set_global(operator_config)
    quantize_model = prepare_pt2e(model, quantizer)
    quantize_model(*example_inputs)
    quantize_model = convert_pt2e(quantize_model)

    #export model
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

export_int8_quantize_conv2d_model("qint8_conv2d_pqs8_qc8w_gemm");


```

### PointwiseConv2d benchmark model

In the following example model, we use simple model to generate pointwise Conv2d nodes that can be accelerated by Kleidiai. 

As before, input parameters can be adjusted to simulate real-world model behavior.


``` python 
import torch
import torch.nn as nn
class DemoConv2dModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.pointwiseconv = torch.nn.Conv2d(3, 2, 1,groups=1)

    def forward(self,x):
         x = self.pointwiseconv(x)
         return x

    def get_example_inputs(self,dtype=torch.float32):
        return (torch.randn(1, 3, 16, 16, dtype=dtype),)

```

The following code can be used to lower and export the model:

```python 
from executorch.backends.xnnpack.partition.xnnpack_partitioner import XnnpackPartitioner
from executorch.backends.xnnpack.partition.config.xnnpack_config import ConfigPrecisionType
from executorch.exir import to_edge_transform_and_lower

def export_pointwise_model(model_name: str):
    mode_file_name = "model/" + model_name
    pte_file = mode_file_name + ".pte"
    etr_file = mode_file_name + ".etrecord"

    model = DemoConv2dModel().eval().to(torch.float32)
    example_inputs = model.get_example_inputs(torch.float32)

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

export_pointwise_model("pointwise_conv2d_pf32_gemm")

```

**NOTES:** 

When exporting models, the generate_etrecord option is enabled to produce the .etrecord file alongside the .pte model file.
These ETRecord files are essential for subsequent model analysis and performance evaluation.

After running this script, both the PTE model file and the etrecord file are generated.

``` bash 
$ ls model/ -1
qint8_conv2d_pqs8_qc8w_gemm.etrecord
qint8_conv2d_pqs8_qc8w_gemm.pte
pointwise_conv2d_pf32_gemm.etrecord
pointwise_conv2d_pf32_gemm.pte
```

The complete source code is available [here](../export-conv2d.py).
