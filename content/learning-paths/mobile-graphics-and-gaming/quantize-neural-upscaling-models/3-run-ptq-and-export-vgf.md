---
title: Apply PTQ and export a quantized VGF model
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you apply post-training quantization (PTQ) to an image-to-image model and export a `.vgf` artifact.

The default workflow in this Learning Path is end to end: you run a complete CIFAR-10-based example, generate a `.vgf` artifact, and validate that the Arm backend export path works on your machine.

After that, you take the same PTQ export logic and apply it to your own model and calibration data.

## Run the end-to-end PTQ example

Create a file called `quantize_and_export_vgf.py` and add the following code.

This example uses CIFAR-10 as a convenient image source. It constructs a low-resolution input by downsampling an image, then trains the model to reconstruct the original image. This is a practical proxy for a real neural upscaler.

```python
import torch
from torch.utils.data import DataLoader
from torch import nn
from torchvision import datasets, transforms

import torch.nn.functional as F

from executorch.backends.arm.tosa.specification import TosaSpecification
from executorch.backends.arm.vgf.compile_spec import VgfCompileSpec
from executorch.backends.arm.vgf.partitioner import VgfPartitioner
from executorch.backends.arm.quantizer.arm_quantizer import (
    get_symmetric_quantization_config,
    TOSAQuantizer,
)
from executorch.exir import to_edge_transform_and_lower

from torchao.quantization.pt2e.quantize_pt2e import (
    convert_pt2e,
    prepare_pt2e,
)


class SmallUpscalerModel(nn.Module):
    """Small image-to-image model for upscaling workflows."""

    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 3, kernel_size=3, padding=1),
        )

    def forward(self, x_lowres):
        # Upscale input first, then refine.
        x = F.interpolate(x_lowres, scale_factor=2.0, mode="bilinear", align_corners=False)
        x = self.net(x)
        return x


def get_data_loaders(root="./data", batch_size=64):
    tfm = transforms.Compose([
        transforms.ToTensor(),
    ])
    train_ds = datasets.CIFAR10(root=root, train=True, download=True, transform=tfm)
    test_ds = datasets.CIFAR10(root=root, train=False, download=True, transform=tfm)
    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True, drop_last=True)
    test_loader = DataLoader(test_ds, batch_size=batch_size, shuffle=False)
    return train_loader, test_loader


def make_lowres_input(x_hr: torch.Tensor):
    # Simulate a game render at lower resolution.
    return F.interpolate(x_hr, scale_factor=0.5, mode="bilinear", align_corners=False)


@torch.no_grad()
def evaluate_psnr(model, loader, device="cpu", max_batches=50):
    psnr_sum = 0.0
    count = 0

    for i, (x_hr, _y) in enumerate(loader):
        if max_batches is not None and i >= max_batches:
            break

        x_hr = x_hr.to(device)
        x_lr = make_lowres_input(x_hr)
        pred = model(x_lr)

        mse = F.mse_loss(pred, x_hr)
        psnr = 10.0 * torch.log10(1.0 / mse.clamp_min(1e-12))

        psnr_sum += psnr.item()
        count += 1

    return psnr_sum / max(1, count)


def train_model(
    model: nn.Module,
    train_loader: DataLoader,
    test_loader: DataLoader | None = None,
    device: str = "cpu",
    epochs: int = 1,
    lr: float = 1e-3,
    log_every: int = 50,
):
    model.to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)

    for epoch in range(epochs):
        model.train()

        for step, (x_hr, _y) in enumerate(train_loader):
            x_hr = x_hr.to(device)
            x_lr = make_lowres_input(x_hr)

            optimizer.zero_grad()
            pred = model(x_lr)
            loss = F.mse_loss(pred, x_hr)
            loss.backward()
            optimizer.step()

            if log_every and (step % log_every == 0):
                print(f"epoch={epoch+1} step={step} loss={loss.item():.6f}")

        if test_loader is not None:
            model.eval()
            psnr = evaluate_psnr(model, test_loader, device=device, max_batches=50)
            print(f"epoch={epoch+1} end psnr={psnr:.2f} dB")
            model.train()

    return model


def make_example_input_from_loader(loader, batch_size=1):
    x_hr, _y = next(iter(loader))

    # Use channels_last to reduce transpose noise in the exported graph.
    x_hr = x_hr[:batch_size].to("cpu").to(memory_format=torch.channels_last)
    x_lr = make_lowres_input(x_hr)

    return (x_lr,)


def make_calibration_batches(loader: DataLoader, num_batches: int):
    cal = []
    for i, (x_hr, _y) in enumerate(loader):
        if i >= num_batches:
            break
        x_lr = make_lowres_input(x_hr.to("cpu"))
        cal.append(x_lr)

    if len(cal) == 0:
        raise RuntimeError("Calibration set is empty; check loader/num_batches.")

    return cal


def ptq_example(device="cpu"):
    """PTQ example: calibrate, convert, then export to VGF."""

    # 1) Train (or load) a baseline model.
    model = SmallUpscalerModel()
    train_loader, test_loader = get_data_loaders()

    # Keep training short for the tutorial.
    model = train_model(model, train_loader, test_loader, device=device, epochs=1)

    model = model.to("cpu")
    model.eval()

    # 2) Export the FP32 model.
    example_input = make_example_input_from_loader(train_loader, batch_size=1)
    exported_model = torch.export.export(model, example_input, strict=True).module(check_guards=False)

    # 3) Configure the Arm backend quantizer.
    tosa_spec = "TOSA-1.00+INT"
    quantizer = TOSAQuantizer(TosaSpecification.create_from_string(tosa_spec))
    quantizer.set_global(get_symmetric_quantization_config(is_qat=False))

    # 4) Prepare for PTQ.
    quantized_export_model = prepare_pt2e(exported_model, quantizer)

    # 5) Calibrate with representative inputs.
    calibration_loader, _ = get_data_loaders(batch_size=1)
    calibration_data = make_calibration_batches(calibration_loader, num_batches=500)

    with torch.no_grad():
        for x_lr in calibration_data:
            quantized_export_model(x_lr)

    # 6) Convert to an INT8 model.
    quantized_export_model = convert_pt2e(quantized_export_model)

    # 7) Export again so the quantized graph is captured.
    aten_dialect = torch.export.export(
        quantized_export_model,
        args=example_input,
        strict=True,
    )

    # 8) Partition and dump a `.vgf` artifact.
    compile_spec = VgfCompileSpec(TosaSpecification.create_from_string(tosa_spec))
    vgf_partitioner = VgfPartitioner(
        compile_spec.dump_intermediate_artifacts_to("./output/")
    )

    to_edge_transform_and_lower(aten_dialect, partitioner=[vgf_partitioner])


if __name__ == "__main__":
    ptq_example(device="cpu")
```

## Run the PTQ example

Run the script:

```bash
python quantize_and_export_vgf.py
```

The output is similar to:

```output
epoch=1 step=0 loss=0.208134
epoch=1 step=50 loss=0.053812
epoch=1 end psnr=19.42 dB
```

You should also see files created under `./output/`. The exact filenames depend on your ExecuTorch version and backend configuration, but the directory should include an exported `.vgf` artifact.

{{% notice Tip %}}
If export fails because of `bilinear` resize, switch the interpolation modes in `make_lowres_input()` and `forward()` to `mode="nearest"`. This keeps the tutorial flow intact while you investigate backend operator support.
{{% /notice %}}

## Advanced: export PTQ to VGF in your own project

Once the end-to-end example works, the next step is to apply the same flow to your own model. 

{{% notice Note %}}
If you don't have a workflow or model, you can skip this section and proceed to the next page.
{{% /notice %}}


If you already have a trained model, this is the minimal PTQ-to-`.vgf` flow. Start from your FP32 PyTorch module (`model_fp32`), an `example_input` tuple that matches your real inference inputs, and a list of representative `calibration_batches` (typically 100–500 samples).

```python
import torch

from executorch.backends.arm.tosa.specification import TosaSpecification
from executorch.backends.arm.vgf.compile_spec import VgfCompileSpec
from executorch.backends.arm.vgf.partitioner import VgfPartitioner
from executorch.backends.arm.quantizer.arm_quantizer import (
    get_symmetric_quantization_config,
    TOSAQuantizer,
)
from executorch.exir import to_edge_transform_and_lower

from torchao.quantization.pt2e.quantize_pt2e import convert_pt2e, prepare_pt2e


def export_vgf_int8_ptq(
    model_fp32: torch.nn.Module,
    example_input: tuple[torch.Tensor, ...],
    calibration_batches: list[torch.Tensor],
    output_dir: str,
    tosa_spec: str = "TOSA-1.00+INT",
):
    model_fp32 = model_fp32.to("cpu")
    model_fp32.eval()

    exported = torch.export.export(model_fp32, example_input, strict=True).module(check_guards=False)

    quantizer = TOSAQuantizer(TosaSpecification.create_from_string(tosa_spec))
    quantizer.set_global(get_symmetric_quantization_config(is_qat=False))
    q = prepare_pt2e(exported, quantizer)

    with torch.no_grad():
        for x in calibration_batches:
            q(x)

    q = convert_pt2e(q)
    aten_dialect = torch.export.export(q, args=example_input, strict=True)

    compile_spec = VgfCompileSpec(TosaSpecification.create_from_string(tosa_spec))
    vgf_partitioner = VgfPartitioner(compile_spec.dump_intermediate_artifacts_to(output_dir))
    to_edge_transform_and_lower(aten_dialect, partitioner=[vgf_partitioner])
```

When you use your own model, the most important input is the calibration set. Treat it like a contract: if it does not look like your actual inference data, PTQ quality can degrade.

Next, you will repeat the flow with QAT.
