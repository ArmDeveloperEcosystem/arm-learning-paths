---
title: Defining your own use cases
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Beyond NSS: working with your own model

While NSS is a powerful demonstration of neural graphics, Model Gym is designed to support custom models for various use cases. You can add your own model architecture, register it with the toolkit, and run the same training, evaluation, and export workflows you used for NSS.

This section walks you through the process of integrating a custom model into Model Gym, using the Python API you used in previous sections.

### Create a custom model

To add a custom model to the Model Gym, you need to:

1. Create a Python class that inherits from `BaseNGModel`
2. Mark it with the `@register_model()` decorator
3. Implement required methods
4. Accept `params` as a constructor argument

The resulting structure looks like this:

```python
from ng_model_gym.core.model.base_ng_model import BaseNGModel
from ng_model_gym.core.model.model_registry import register_model
from ng_model_gym.core.utils.config_model import ConfigModel

@register_model(name="custom_model", version="1")
class CustomModel(BaseNGModel):
    def __init__(self, params: ConfigModel):
        super().__init__(params)
        # Define your model architecture here
        
    def forward(self, x):
        # Implement forward pass
        pass
```

The `@register_model()` decorator makes your model discoverable by Model Gym. The `name` and `version` parameters will be used later in your configuration file.

### Register your model

For your model to be available in Model Gym, the file defining it must be imported. This triggers the registration process.

Place your model file in the `src/ng_model_gym/usecases/` directory within the Model Gym installation. To find the installed location, make sure the virtual environment you used with the example notebooks is activated. Then, run the following:

```bash
whereis ng_model_gym
```

This should point to your `nb-env` virtual environment. The Model Gym source code in this case will sit in the following directory:

```output
<path-to>/nb-env/lib/python3.12/site-packages/ng_model_gym/usecases
```

Each use case directory must contain an `__init__.py` file. To understand how the configuration files work, revisit the example notebooks for NSS in previous sections.

Verify registration succeeded by listing registered models:

```python
from ng_model_gym.core.model.model_registry import MODEL_REGISTRY

MODEL_REGISTRY.list_registered()
```

### Update your configuration file

You've already worked with the configuration file in the training and evaluation notebooks. To use your custom model, update the same JSON configuration file to reference the model name and version you used when registering. You can generate a new config template with `ng-model-gym init`, or modify an existing one.

Update the model section:

```json
{
  "model": {
    "name": "custom_model",
    "version": "1"
  }
}
```

If you're working in Python, set these values programmatically:

```python
import ng_model_gym as ngmg
from pathlib import Path

config = ngmg.load_config_file(Path("config.json"))
config.model.name = "custom_model"
config.model.version = "1"
```

### Run training with your custom model

Once your model is registered and your config is updated, you can use all the standard Model Gym workflows that were covered in previous sections. For example training:

```bash
trained_model_path = ngmg.do_training(config, training_mode=TrainEvalMode.FP32)
```

Your custom model will go through the same pipeline as NSS: training, quantization, evaluation, and export to `.vgf` format.

### Add custom datasets

Similar to models, you can register custom datasets by marking your dataset class with the `@register_dataset()` decorator:

```python
from torch.utils.data import Dataset
from ng_model_gym.core.data.dataset_registry import register_dataset

@register_dataset(name="custom_dataset", version="1")
class CustomDataset(Dataset):
    def __init__(self, config):
        # Initialize your dataset
        pass
        
    def __len__(self):
        # Return dataset size
        pass
        
    def __getitem__(self, idx):
        # Return a single sample
        pass
```

Place the dataset implementation in the same `usecases` directory as your model. Then, update your configuration to use the custom dataset:

```json
{
  "dataset": {
    "name": "custom_dataset",
    "version": "1"
  }
}
```

## Summary of self-defined use cases

You can group related models, datasets, and configurations into custom use cases. This is useful when working on a specific neural graphics application. To understand what the final structure should look like, use the NSS use case as a reference implementation. Your use case logic executes when you specify its model and dataset in your configuration file.

## Explore the example notebook

The `neural-graphics-model-gym-examples` repository includes a walkthrough notebook called `custom_model_example.ipynb`. This notebook demonstrates:

- How to structure a custom model class
- Registration and verification steps
- Modifying configuration files
- Running training workflows with custom models

To work through the example, follow the same process as before:

```bash
cd neural-graphics-model-gym-examples
source nb-env/bin/activate
jupyter lab
```

Navigate to `tutorials/nss/custom_model_example.ipynb` and step through the cells. 

## Wrapping up

You've now learned how to extend Model Gym beyond NSS with your own models and datasets. This opens up possibilities for experimenting with different neural graphics techniques: denoising, frame interpolation, or custom upscaling approaches tailored to your content.

For more information on model registration, dataset integration, and use case development, see the [Model Gym GitHub repository](https://github.com/arm/neural-graphics-model-gym).

Through this Learning Path, you’ve learned what neural graphics is and why it matters for game performance. You’ve stepped through the process of training and evaluating a model using PyTorch and the Model Gym, and seen how to export that model into VGF (.vgf) for real-time deployment. You’ve also explored how to visualize and inspect the model’s structure using Model Explorer. You can now explore the Model Training Gym repository for deeper integration and to keep building your skills.