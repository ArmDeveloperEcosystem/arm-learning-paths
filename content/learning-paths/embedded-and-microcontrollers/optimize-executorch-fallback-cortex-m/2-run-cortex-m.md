---
title: Establish the Cortex-M baseline
weight: 3
description: Adapt TinyCNN and inspect how its convolutions and topk operation run without Ethos-U delegation.

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Use a simple convolution example

The CMSIS-Executorch repository starts with a TinyCNN model that can be delegated completely to
Ethos-U. To make fallback visible, you will retain its input and output
interface while changing the operations happening inside it.

Replace the original model:

{{< tabpane code=true >}}
  {{< tab header="Linux" language="bash">}}
cp mixed_backend_cnn.py model/model.py
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
Copy-Item .\mixed_backend_cnn.py .\model\model.py
  {{< /tab >}}
{{< /tabpane >}}

The model still accepts one `16 x 16` RGB image in NHWC order and returns ten
values. Keeping that interface means the supplied bare-metal runner needs no
changes.

The important part of `model/model.py` now looks like this:

```python
self.conv1 = nn.Conv2d(
    channels, 4, kernel_size=3, stride=1, padding=1, bias=False
)
self.conv2 = nn.Conv2d(
    4, num_classes, kernel_size=3, stride=4, padding=1, bias=False
)

values = torch.relu(self.conv1(values))
values = self.conv2(values)
values = torch.flatten(values, start_dim=2)
values, _ = torch.topk(values, k=1, dim=-1)
```

The *stride* controls how far a convolution filter moves between positions. A
stride of one visits adjacent positions. A stride of four moves four positions
at a time and produces a smaller output. For this U55 target and tensor shape,
the first convolution can be delegated to the NPU, while the stride-four convolution
remains outside the delegate. `topk` selects the largest spatial response for
each of the ten output channels.

## Export the Cortex-M baseline

Before we demonstrate fallback, it is useful to know which operations could be optimized by the Cortex-M backend itself. 
Therefore, as a useful first step, we will specify `--mode cortex-m`, such that no operation is offered to the NPU. Run the diagnostic exporter from the repository root:

{{< tabpane code=true >}}
  {{< tab header="Linux" language="bash">}}
python export_cortex_m_fallback.py \
  --mode cortex-m \
  --model-file model/model.py \
  --output-dir artifacts
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
python .\export_cortex_m_fallback.py `
  --mode cortex-m `
  --model-file model/model.py `
  --output-dir artifacts
  {{< /tab >}}
{{< /tabpane >}}

The relevant output is:

```output
Relevant targets before Cortex-M lowering:
aten.convolution.default: 2
aten.topk.default: 1

Relevant targets after Cortex-M lowering:
aten.topk.default: 1
cortex_m.dequantize_per_tensor.default: 2
cortex_m.quantize_per_tensor.default: 2
cortex_m.quantized_conv2d_nhwc.default: 2
cortex_m.transpose.default: 1
```

Before lowering, the graph contained two general convolution operations (Stride-1 and Stride-4). The `aten` prefix identifies PyTorch’s ATen operator namespace. These operators describe the computation, but not the hardware or kernel that will perform it. Lowering replaces both with `cortex_m.quantized_conv2d_nhwc`, an INT8 convolution using NHWC layout.

`aten.topk` is unchanged, so it will use the portable CPU kernel. The `cortex_m.quantize_*`
and `cortex_m.dequantize_*` operators mark boundaries between floating-point (FP32) and INT8
regions. 

Confirm the generated artifacts from the export script:

{{< tabpane code=true >}}
  {{< tab header="Linux" language="bash">}}
ls -lh artifacts/stride4_cortex_m.*
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
Get-ChildItem .\artifacts\stride4_cortex_m.*
  {{< /tab >}}
{{< /tabpane >}}

The expected output contains:

```output
stride4_cortex_m.json
stride4_cortex_m.pte
```

## What you've accomplished and what's next

You have separated two CPU execution routes without involving the NPU. Both
convolutions use Cortex-M operators backed by CMSIS-NN, while `topk` remains a
portable ExecuTorch operation.

Next, you will offer the same graph to the Ethos-U delegate first and inspect
what remains for the CPU.
