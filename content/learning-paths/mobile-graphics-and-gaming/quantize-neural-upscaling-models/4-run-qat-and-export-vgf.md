---
title: Apply QAT and export a quantized VGF model
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you run quantization-aware training (QAT) so the model learns to be robust to quantization effects.

The default workflow is to extend the runnable CIFAR-10 example from the PTQ step so you can compare PTQ and QAT outputs using the same model and data.

## Run the end-to-end QAT example (extend the CIFAR-10 script)

In `quantize_and_export_vgf.py`, update your TorchAO imports to include the QAT helpers:

```python
from torchao.quantization.pt2e.quantize_pt2e import (
    convert_pt2e,
    prepare_qat_pt2e,
)
from torchao.quantization.pt2e import (
    move_exported_model_to_eval,
    move_exported_model_to_train,
)
```

Then add the QAT training function and example entry point. This code prepares the exported model for QAT, fine-tunes for a small number of epochs, converts to INT8, and exports to `.vgf`.

```python
def train_model_qat(
    model: nn.Module,
    train_loader: DataLoader,
    test_loader: DataLoader | None = None,
    device: str = "cpu",
    epochs: int = 1,
    lr: float = 1e-4,
    log_every: int = 50,
):
    model.to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)

    for epoch in range(epochs):
        move_exported_model_to_train(model)

        for step, (x_hr, _y) in enumerate(train_loader):
            x_hr = x_hr.to(device)
            x_lr = make_lowres_input(x_hr)

            optimizer.zero_grad()
            pred = model(x_lr)
            loss = F.mse_loss(pred, x_hr)
            loss.backward()
            optimizer.step()

            if log_every and (step % log_every == 0):
                print(f"qat epoch={epoch+1} step={step} loss={loss.item():.6f}")

        if test_loader is not None:
            move_exported_model_to_eval(model)
            psnr = evaluate_psnr(model, test_loader, device=device, max_batches=50)
            print(f"qat epoch={epoch+1} end psnr={psnr:.2f} dB")

    return model


def qat_example(device="cpu"):
    """QAT example: prepare for QAT, fine-tune, convert, then export to VGF."""

    # 1) Train (or load) a baseline FP32 model.
    model = SmallUpscalerModel()
    train_loader, test_loader = get_data_loaders()
    model = train_model(model, train_loader, test_loader, device=device, epochs=1)

    # 2) Export the FP32 model.
    example_input = make_example_input_from_loader(train_loader, batch_size=1)
    exported_model = torch.export.export(model, example_input, strict=True).module(check_guards=False)

    # 3) Configure the Arm backend quantizer.
    tosa_spec = "TOSA-1.00+INT"
    quantizer = TOSAQuantizer(TosaSpecification.create_from_string(tosa_spec))
    quantizer.set_global(get_symmetric_quantization_config(is_qat=True))

    # 4) Prepare for QAT.
    qat_ready_model = prepare_qat_pt2e(exported_model, quantizer)

    # 5) Fine-tune with fake-quant enabled.
    qat_ready_model = train_model_qat(
        qat_ready_model,
        train_loader,
        test_loader,
        device=device,
        epochs=1,
        lr=1e-4,
    )

    # 6) Convert to an INT8 model.
    qat_ready_model = qat_ready_model.to("cpu")
    move_exported_model_to_eval(qat_ready_model)
    qat_int8_model = convert_pt2e(qat_ready_model)

    # 7) Export again so the quantized graph is captured.
    aten_dialect = torch.export.export(
        qat_int8_model,
        args=example_input,
        strict=True,
    )

    # 8) Partition and dump a `.vgf` artifact.
    compile_spec = VgfCompileSpec(TosaSpecification.create_from_string(tosa_spec))
    vgf_partitioner = VgfPartitioner(
        compile_spec.dump_intermediate_artifacts_to("./output_qat/")
    )

    to_edge_transform_and_lower(aten_dialect, partitioner=[vgf_partitioner])
```

## Run the QAT example

Update `__main__` to call `qat_example()` and run the script:

```bash
python quantize_and_export_vgf.py
```

{{% notice Tip %}}
If export fails with a missing model converter error, you likely forgot to source the Arm backend `setup_path.sh` in your current terminal session.
{{% /notice %}}

As the script runs, you should see QAT training logs (prefixed with `qat`). When export completes, you should see `.vgf` output under `./output_qat/`.

## Advanced: drop-in QAT export to VGF for your own project

If PTQ introduces visible artifacts, QAT is the next step. The workflow is the same as PTQ, but you insert a short fine-tuning phase after you prepare the model for QAT.

In practice, you already have a training loop for your upscaler. The simplest way to use QAT is to reuse that loop and point it at the QAT-prepared exported model.

The snippet below gives you a minimal structure you can drop into your project. You supply:

- `model_fp32`: your baseline FP32 model
- `example_input`: a tuple of input tensors
- `fine_tune_qat`: a function that runs your fine-tuning loop (one or more epochs)

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

from torchao.quantization.pt2e.quantize_pt2e import convert_pt2e, prepare_qat_pt2e
from torchao.quantization.pt2e import move_exported_model_to_eval


def export_vgf_int8_qat(
    model_fp32: torch.nn.Module,
    example_input: tuple[torch.Tensor, ...],
    fine_tune_qat,
    output_dir: str,
    tosa_spec: str = "TOSA-1.00+INT",
):
    model_fp32 = model_fp32.to("cpu")
    model_fp32.eval()

    exported = torch.export.export(model_fp32, example_input, strict=True).module(check_guards=False)

    quantizer = TOSAQuantizer(TosaSpecification.create_from_string(tosa_spec))
    quantizer.set_global(get_symmetric_quantization_config(is_qat=True))
    qat_ready = prepare_qat_pt2e(exported, quantizer)

    # Run your fine-tuning loop here. This is where QAT earns its keep.
    fine_tune_qat(qat_ready)

    qat_ready = qat_ready.to("cpu")
    move_exported_model_to_eval(qat_ready)
    q = convert_pt2e(qat_ready)
    aten_dialect = torch.export.export(q, args=example_input, strict=True)

    compile_spec = VgfCompileSpec(TosaSpecification.create_from_string(tosa_spec))
    vgf_partitioner = VgfPartitioner(compile_spec.dump_intermediate_artifacts_to(output_dir))
    to_edge_transform_and_lower(aten_dialect, partitioner=[vgf_partitioner])
```

Next, you will validate your model files by visualizing them in the Model Explorer.
