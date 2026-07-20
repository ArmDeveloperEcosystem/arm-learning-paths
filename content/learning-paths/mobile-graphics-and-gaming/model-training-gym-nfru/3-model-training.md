---
title: Launch the training notebook
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## What Neural Frame Rate Upscaling is

Arm Neural Frame Rate Upscaling (NFRU) is a neural frame generation technique for real-time graphics. Instead of traditionally rendering every displayed frame, NFRU uses neural inference to synthesize intermediate frames between rendered frames. By using motion data and temporal information that already exists in the rendering pipeline, NFRU can increase perceived smoothness while reducing the amount of work that must be done by the GPU.

NFRU is designed for demanding graphics workloads where frame time is a major bottleneck, including scenes with advanced lighting, complex shading, or ray-traced effects. With Neural frame generation, the renderer can skip some full-frame rendering work and generate intermediate frames with a neural workload that's designed to run efficiently on Arm's neural graphics stack. You can, therefore, deliver smoother and more responsive gameplay within mobile power and thermal limits.

The technology is built with dedicated neural acceleration in mind. As neural accelerators become integrated into Arm GPUs, machine learning workloads can run alongside traditional graphics tasks, opening new options for real-time rendering pipelines.

The NFRU model is expected to use the same Model Gym workflow and formats as shown in the following table:

| Model format | File extension | Used for                                                                 |
|--------------|----------------|--------------------------------------------------------------------------|
| PyTorch      | `.pt`            | training, fine-tuning, or evaluation in notebooks or scripts using the Model Gym |
| VGF          | `.vgf`           | for deployment using ML Extensions for Vulkan on Arm-based hardware or emulation layers |

The NFRU examples include configuration files, model metadata, usage details, and a walkthrough notebook for the use case.

## Run the training notebook

With your environment set up, you're ready to launch the first step in the workflow: training your neural graphics model using the NFRU training notebook.

{{% notice Note %}}
You'll run two Jupyter notebooks. Return to the Learning Path when you're done to explore further resources and next steps.
{{% /notice %}}

You'll get familiarized with the following steps:

- Loading a model configuration
- Launching a full training pipeline
- Visualizing metrics with TensorBoard
- Saving intermediate checkpoints

### Start Jupyter Lab

Launch Jupyter Lab with the following command:

```bash
jupyter lab
```

You'll be prompted to open your browser to `http://localhost:8888` and enter the token that's printed in the terminal output. 

Navigate to `neural-graphics-model-gym-examples/tutorials/nfru/<nfru-training-notebook>.ipynb`.

Step through the notebook for training.

After training your model, you'll evaluate it. You'll measure accuracy, compare checkpoints, and prepare the model for export. 

Open the evaluation notebook located at `neural-graphics-model-gym-examples/tutorials/nfru/<nfru-evaluation-notebook>.ipynb`.

At the end, you'll see a visual comparison of the generated NFRU frame and the ground truth frame.

## What you've accomplished and what's next

You’ve now learned about NFRU and run two Jupyter notebooks to complete model training and evaluation. 

Next, you'll view the model structure and explore further resources.
