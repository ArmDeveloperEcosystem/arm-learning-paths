---
title: Fine-tune and export a quantized model
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Fine-tune with quantization-aware training

The training and evaluation notebooks create and inspect PyTorch checkpoints, but they do not export a VGF model. To create a model for deployment, use the `model_qat_example.ipynb` notebook. This is the only example notebook that includes the export step.

Quantization-aware training (QAT) simulates lower-precision inference during fine-tuning. This helps preserve model accuracy when the model is quantized to INT8 for efficient deployment.

Post-training quantization (PTQ) is usually faster to try because it calibrates an already-trained model without another training phase. QAT adds fine-tuning so the model can adapt to quantization effects, making it useful when PTQ causes unacceptable accuracy or visual-quality regressions. To explore that tradeoff and the lower-level TorchAO and ExecuTorch export workflow, see [Quantize neural upscaling models with ExecuTorch](/learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/).

In the notebook, you will:

- Load the NSS model configuration
- Fine-tune pretrained FP32 weights using QAT INT8 mode
- Export the quantized model to VGF

{{% notice GPU memory %}}
QAT uses additional GPU memory. If you encounter an out-of-memory error, reduce the training batch size in the notebook.
{{% /notice %}}

## Run the QAT notebook

If Jupyter Lab is not already running, start it from the `neural-graphics-model-gym-examples` directory:

```bash
jupyter lab
```

In Jupyter Lab, open:

```output
neural-graphics-model-gym-examples/tutorials/model_qat_example.ipynb
```

Run the notebook cells in order. The notebook starts from pretrained FP32 NSS weights, applies QAT fine-tuning, and exports the resulting INT8 model.

When the notebook completes, the exported `.vgf` file is available in:

```output
neural-graphics-model-gym-examples/tutorials/output/vgf
```

You now have an exported VGF model whose graph you can inspect with Model Explorer.
