---
title: Fine-tune DeiT-Tiny on pet images
description: Train a DeiT-Tiny classifier for 37 pet breeds and prepare its checkpoint for the VGF export script.
weight: 4
layout: "learningpathall"
---

## Train the pet classifier

Fine-tuning adapts a pretrained model to the pet classification task. The training script loads `facebook/deit-tiny-patch16-224` and replaces its classification head for the dataset's 37 breeds. It uses a fixed dataset revision and seed. The script reserves ten percent of the training split for validation.

Validation checks progress during training. The separate test split measures the trained model’s classification accuracy. Each epoch is one pass through the training data.

Run three epochs and save the log:

```bash
python examples/arm/image_classification_example_vgf/model_export/train_deit.py \
  --output-dir arm_test/deit_vgf/deit-tiny-oxford-pet \
  --num-epochs 3 \
  2>&1 | tee arm_test/deit_vgf/train.log
```

The first run downloads the model weights and dataset. When training finishes, the script prints `Test set accuracy:` and saves the selected model under `arm_test/deit_vgf/deit-tiny-oxford-pet/final_model/`.

Record the accuracy from your run. Training speed and final accuracy depend on your environment. A single fixed accuracy value isn't a completion requirement.

## Prepare the checkpoint for export

At the pinned revision, the trainer saves `model.safetensors`, but `export_deit.py` loads with `use_safetensors=False`. The downloadable helper for the Learning Path converts the weight-file format for export without retraining the model.

Download the [helper](../deit_vgf_helper.py), which also prepares images and decodes predictions:

```bash
curl --fail --location \
  --output arm_test/deit_vgf/deit_vgf_helper.py \
  https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/mobile-graphics-and-gaming/deploy-deit-tiny-with-vgf/deit_vgf_helper.py
```

Review the downloaded file, then prepare the checkpoint:

```bash
python arm_test/deit_vgf/deit_vgf_helper.py checkpoint
```

The output is similar to:

```output
Export weights: arm_test/deit_vgf/deit-tiny-oxford-pet/final_model/pytorch_model.bin
Original weights preserved: arm_test/deit_vgf/deit-tiny-oxford-pet/final_model/model.safetensors
Export checkpoint ready: arm_test/deit_vgf/deit-tiny-oxford-pet/final_model
```

The helper creates `pytorch_model.bin` in `final_model/` without changing the trained weights. Keep `config.json` beside the weights because it contains the model configuration and breed labels.

## What you've accomplished and what's next

You've fine-tuned DeiT-Tiny and prepared a checkpoint that the example exporter can load.

Next, you'll quantize the model and generate the `.pte` program.
