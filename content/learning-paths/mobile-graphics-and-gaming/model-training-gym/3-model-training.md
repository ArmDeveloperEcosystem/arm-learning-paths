---
title: Launch the training notebook
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## About NSS

In this section, you'll get hands-on with how you can use the model gym to fine-tune the NSS use-case.

Arm Neural Super Sampling (NSS) is an upscaling technique designed to solve a growing challenge in real-time graphics: delivering high visual quality without compromising performance or battery life. Instead of rendering every pixel at full resolution, NSS uses a neural network to intelligently upscale frames, freeing up GPU resources and enabling smoother, more immersive experiences on mobile devices.

The NSS model is available in two formats, as shown in the table below:

| Model format | File extension | Used for                                                                 |
|--------------|----------------|--------------------------------------------------------------------------|
| PyTorch      | `.pt`            | training, fine-tuning, or evaluation in or scripts using the Model Gym  |
| VGF          | `.vgf`           | for deployment using ML Extensions for Vulkan on Arm-based hardware or emulation layers |

Both formats are available in the [NSS repository on Hugging Face](https://huggingface.co/Arm/neural-super-sampling). You'll also be able to explore config files, model metadata, usage details and detailed documentation on the use-case.

Aside from the model in HuggingFace, the Neural Graphics Development Kit features [an NSS plugin for game engines such as Unreal](/learning-paths/mobile-graphics-and-gaming/nss-unreal).

## Run the training notebook

With your environment set up, you're ready to launch the first step in the workflow: training your neural graphics model using the `model_training_example.ipynb` notebook.

{{% notice Before you begin %}}
In this part of the Learning Path, you will run through two Jupyter Notebooks. Return to this tutorial when you're done to explore further resources and next steps.
{{% /notice %}}

You will get familiarized with the following steps:

- Loading a model configuration
- Launching a full training pipeline
- Visualizing metrics with TensorBoard
- Saving intermediate checkpoints

### Start Jupyter Lab

Launch Jupyter Lab with the following command:

```bash
jupyter lab
```

This will prompt you to open your browser to `http://localhost:8888`and enter the token that is printed in the terminal output. Navigate to:

```output
neural-graphics-model-gym-examples/tutorials/nss/model_training_example.ipynb
```

Step through the notebook for training.

Once your model is trained, the next step is evaluation. You'll measure accuracy, compare checkpoints, and prepare the model for export. Open the evaluation notebook located at the following location:

```output
neural-graphics-model-gym-examples/tutorials/nss/model_evaluation_example.ipynb
```

At the end you should see a visual comparison of the NSS upscaling and the ground truth image.


You’ve completed the training and evaluation steps. Proceed to the final section to view the model structure and explore further resources. 



