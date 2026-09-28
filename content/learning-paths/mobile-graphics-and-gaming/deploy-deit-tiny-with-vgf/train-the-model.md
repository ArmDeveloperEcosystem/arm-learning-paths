---
title: Fine-tune DeiT-Tiny on pet images
description: Train a DeiT-Tiny classifier for 37 pet breeds and prepare its checkpoint for the VGF export script.
weight: 4
layout: "learningpathall"
---

## Train the pet classifier

The training script loads `facebook/deit-tiny-patch16-224` and replaces its classification head for the dataset's 37 breeds. It uses a fixed dataset revision and seed, reserving ten percent of the training split for validation.

Run three training epochs and save the log:

```bash
python examples/arm/image_classification_example_vgf/model_export/train_deit.py \
  --output-dir arm_test/deit_vgf/deit-tiny-oxford-pet \
  --num-epochs 3 \
  2>&1 | tee arm_test/deit_vgf/train.log
```

The first run downloads the model weights and dataset. At completion, the script prints `Test set accuracy:` and saves the selected model under `arm_test/deit_vgf/deit-tiny-oxford-pet/final_model/`.

Record the accuracy from your run. Training speed and final accuracy depend on your environment; a single fixed accuracy value is not a completion requirement.

## Prepare the checkpoint for export

At the pinned revision, the trainer saves `model.safetensors`, but `export_deit.py` loads with `use_safetensors=False`. Use the Learning Path helper to create the compatible PyTorch weight file:

```bash
python arm_test/deit_vgf/deit_vgf_helper.py checkpoint
```

The helper creates `pytorch_model.bin` in `final_model/` without changing the trained weights. Keep `config.json` beside the weights because it contains the model configuration and breed labels.

## What you've accomplished

You have fine-tuned DeiT-Tiny and prepared a checkpoint that the example exporter can load. Next, you will quantize the model and generate the `.pte` program.
