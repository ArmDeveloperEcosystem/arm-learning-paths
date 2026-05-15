---
title: Create a reference model
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Start with a small model

Before using a production NSS model, it helps to validate the toolchain with a small graph that is easy to inspect.

In this section, you'll use a minimal `AddSigmoid` model so you can focus on the conversion flow:

1. PyTorch export
2. VGF export with the ExecuTorch backend
3. Artifact inspection in Model Explorer
4. Optional TOSA inspection when you need to debug the lowering path
5. Runtime validation with an ExecuTorch runner

Neural graphics models sit between ML tooling and real-time graphics runtimes. In Arm's neural accelerator ecosystem, a trained PyTorch model usually needs to become a deployable artifact that can be consumed by ML Extensions for Vulkan. It then needs to be inspected with graphics-oriented tooling and validated before it is integrated into an engine or sample application. 

This is the same workflow pattern used in other NX Learning Paths, including [Quantize neural upscaling models with ExecuTorch](/learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/) and [Fine-tune neural graphics models using Model Gym](/learning-paths/mobile-graphics-and-gaming/model-training-gym/).

### Create and export an AddSigmoid model

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

## What you've accomplished and what's next

You've now created and exported a minimal `AddSigmoid` PyTorch model that you'll use to validate the model preparation workflow.

Next, you'll export this model with the ExecuTorch VGF backend.