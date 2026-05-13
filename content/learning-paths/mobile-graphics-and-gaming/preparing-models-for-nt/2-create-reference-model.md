---
title: Create a reference model
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why start with a small model?

Before using a production NSS model, it helps to validate the toolchain with a small graph that is easy to inspect.

This page uses a minimal `AddSigmoid` model so you can focus on the conversion flow:
- PyTorch export
- VGF export with the ExecuTorch backend
- Artifact inspection in Model Explorer
- Optional TOSA inspection when you need to debug the lowering path
- Runtime validation with an ExecuTorch runner

This matters because neural graphics models sit between ML tooling and real-time graphics runtimes. In Arm's neural accelerator ecosystem, a trained PyTorch model typically needs to become a deployable artifact that can be consumed by ML Extensions for Vulkan, inspected with graphics-oriented tooling, and validated before it is integrated into an engine or sample application. This is the same workflow pattern used in other NX learning paths, including [Quantize neural upscaling models with ExecuTorch](/learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/) and [Fine-tune neural graphics models using Model Gym](/learning-paths/mobile-graphics-and-gaming/model-training-gym/).

## Create and export the model

Create a Python file named `create_reference_model.py`:

```python
import torch


class AddSigmoid(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
        return self.sigmoid(x + y)


example_inputs = (torch.ones(1, 1, 1, 1), torch.ones(1, 1, 1, 1))

model = AddSigmoid().eval()
exported_model = torch.export.export(model, example_inputs)
graph_module = exported_model.module(check_guards=False)

_ = graph_module.print_readable()

torch.export.save(exported_model, "add_sigmoid.pt2")
print("Wrote: add_sigmoid.pt2")
```

Run the script:

```bash
python create_reference_model.py
```

The printed graph confirms the model was exported correctly. The saved `add_sigmoid.pt2` file is the input to the backend lowering steps that follow.
