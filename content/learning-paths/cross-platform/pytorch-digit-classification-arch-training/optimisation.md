---
# User change
title: "Run optimization"

weight: 13

layout: "learningpathall"
---

To optimize the model, use the `pytorch-digits-model-optimizations.ipynb` to add the following lines:

```python
from torch.utils.mobile_optimizer import optimize_for_mobile

# Instantiate the model without Dropout layers
model_for_quantization = NeuralNetwork(use_dropout=False)

# Load the trained state_dict (excluding Dropout parameters)
model_for_quantization.load_state_dict(model.state_dict())
model_for_quantization.eval()
    
# Define quantization configuration
model.qconfig = torch.quantization.get_default_qconfig('qnnpack')

# Fuse modules
modules_to_fuse = [['linear1', 'relu1'], ['linear2', 'relu2']]
torch.quantization.fuse_modules(model_for_quantization, modules_to_fuse, inplace=True)

# Prepare for static quantization
torch.quantization.prepare(model_for_quantization, inplace=True)

# Calibrate the model 
with torch.no_grad():
    for inputs, _ in train_dataloader:
        model_for_quantization(inputs)

# Convert to quantized model
torch.quantization.convert(model, inplace=True)

# Trace and optimize the quantized model
example_input = torch.rand(1, 1, 28, 28)
traced_quantized_model = torch.jit.trace(model, example_input)
optimized_model = optimize_for_mobile(traced_quantized_model)

# Save the optimized model
optimized_model._save_for_lite_interpreter("optimized_model.ptl")
```

In this code, the neural network model is being prepared for optimization and quantization to make it more suitable for mobile deployment. 

First, the model is instantiated without Dropout layers by setting `use_dropout=False`, as dropout is typically disabled during inference. The model's trained weights are then loaded using the `load_state_dict()` function, ensuring that it retains the knowledge learned during training. The model is set to evaluation mode with `eval()` to prepare it for inference.

Next, the quantization process is configured. 

A quantization configuration is applied using the `qnnpack` backend, which is designed for efficient quantization on mobile devices. Certain layers of the model, specifically the linear layers and their corresponding activation functions (ReLU), are fused using `torch.quantization.fuse_modules()`. This fusion reduces the computational overhead by combining operations, a common optimization technique.

After fusing the layers, the model is prepared for static quantization with `torch.quantization.prepare()`, which involves calibrating the model on the training data to collect statistics needed for quantization. The calibration phase runs the model on some training data without updating the weights.

Once calibration is complete, the model is converted to a quantized version using `torch.quantization.convert()`. The quantized model is then traced with `torch.jit.trace()`, which captures the model’s computational graph. 

Finally, the traced model is optimized for mobile using `optimize_for_mobile()`, further refining it for performance on mobile devices. 

The optimized model is saved in a format suitable for the PyTorch Lite Interpreter for efficient deployment on mobile platforms. 

The result is an optimized and quantized model stored as `"optimized_model.ptl"`, ready for deployment.
