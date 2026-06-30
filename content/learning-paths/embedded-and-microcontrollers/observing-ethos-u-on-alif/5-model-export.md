---
title: Export PyTorch model to ExecuTorch format
weight: 5
layout: learningpathall
---

## Overview

This section covers exporting PyTorch models to ExecuTorch `.pte` (PyTorch ExecuTorch) format with Ethos-U55 delegation for the Alif Ensemble E8.

## Prerequisites

Ensure you completed the previous section and verified:

```bash
# Inside Docker container
source ~/executorch-venv/bin/activate
source $ET_HOME/setup_arm_env.sh

# Verify tools
arm-none-eabi-gcc --version
vela --version
python3 -c "from executorch.exir import to_edge; print('ExecuTorch OK')"
```

## ExecuTorch Export Pipeline

The export pipeline converts PyTorch models through several stages:

```
PyTorch Model (.pt)
       │
       ▼
  ONNX/EXIR (graph capture)
       │
       ▼
  Edge Dialect (mobile optimizations)
       │
       ▼
  TOSA Delegate (Ethos-U backend)
       │
       ▼
  Vela Compiler (NPU optimization)
       │
       ▼
  .pte File (ready for Alif E8)
```

## Example 1: Simple Model Verification

Test the export pipeline with a built-in model:

```bash
cd $ET_HOME

python3 -m examples.arm.aot_arm_compiler \
    --model_name=add \
    --delegate \
    --quantize \
    --target=ethos-u55-128 \
    --system_config=Ethos_U55_High_End_Embedded \
    --memory_mode=Shared_Sram
```

Expected output:
```output
Exporting model add...
Lowering to TOSA...
Compiling with Vela...
PTE file saved as add_arm_delegate_ethos-u55-128.pte
```

Verify the file:
```bash
ls -la add_arm_delegate_ethos-u55-128.pte
```

## Example 2: MNIST Model for Digit Recognition

Create a custom MNIST model optimized for Ethos-U55.

### Step 1: Create the Model File

```bash
# Create directories (use full paths, not ~)
mkdir -p /home/developer/models
mkdir -p /home/developer/output

# Create the MNIST model
cat > /home/developer/models/mnist_model.py << 'EOF'
import torch
import torch.nn as nn

class MNISTModel(nn.Module):
    """
    Lightweight MNIST classifier optimized for Ethos-U55.
    - Uses Conv2d (NPU accelerated)
    - Uses ReLU activation (NPU accelerated)
    - Quantization-friendly architecture
    """
    def __init__(self):
        super(MNISTModel, self).__init__()
        
        # Convolutional layers (NPU accelerated)
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)  # 28x28 -> 14x14
        
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)  # 14x14 -> 7x7
        
        # Fully connected layers
        self.fc1 = nn.Linear(32 * 7 * 7, 64)
        self.relu3 = nn.ReLU()
        self.fc2 = nn.Linear(64, 10)  # 10 digit classes
    
    def forward(self, x):
        x = self.pool1(self.relu1(self.conv1(x)))
        x = self.pool2(self.relu2(self.conv2(x)))
        x = x.view(x.size(0), -1)  # Flatten
        x = self.relu3(self.fc1(x))
        x = self.fc2(x)
        return x

# REQUIRED: Create model instance
model = MNISTModel()

# REQUIRED: Define example input (batch=1, channels=1, height=28, width=28)
example_input = torch.randn(1, 1, 28, 28)

# REQUIRED: Export these variables for the AOT compiler
ModelUnderTest = model
ModelInputs = (example_input,)

print(f"MNIST Model - Parameters: {sum(p.numel() for p in model.parameters()):,}")
EOF
```

### Step 2: Export the Model

{{% notice Important %}}
Use full paths (`/home/developer/...`), not `~`. The tilde is not expanded by the AOT compiler.
{{% /notice %}}

```bash
cd $ET_HOME

python3 -m examples.arm.aot_arm_compiler \
    --model_name=/home/developer/models/mnist_model.py \
    --delegate \
    --quantize \
    --target=ethos-u55-128 \
    --system_config=Ethos_U55_High_End_Embedded \
    --memory_mode=Shared_Sram \
    --output=/home/developer/output/mnist_ethos_u55.pte
```

The export process shows:
```output
Loading model from /home/developer/models/mnist_model.py
MNIST Model - Parameters: 56,474
Exporting to EXIR...
Lowering to Edge dialect...
Delegating to ARM backend...
Quantizing to INT8...
Compiling with Vela for ethos-u55-128...
Vela: Optimizing for 128 MACs
PTE file saved: /home/developer/output/mnist_ethos_u55.pte
```

### Step 3: Verify the Output

```bash
ls -lh /home/developer/output/mnist_ethos_u55.pte
```

Expected output:
```output
-rw-r--r-- 1 developer developer 143K Dec 14 12:00 mnist_ethos_u55.pte
```

## AOT Compiler Options Reference

| Option | Description | Example Value |
|--------|-------------|---------------|
| `--model_name` | Path to model file or built-in name | `/home/developer/models/mnist.py` or `mv2` |
| `--delegate` | Enable Ethos-U delegation | (flag, no value) |
| `--quantize` | Apply INT8 quantization | (flag, no value) |
| `--target` | NPU target configuration | `ethos-u55-128` |
| `--system_config` | System performance profile | `Ethos_U55_High_End_Embedded` |
| `--memory_mode` | Memory access mode | `Shared_Sram` |
| `--output` | Output `.pte` file path | `/home/developer/output/model.pte` |
| `--debug` | Enable debug output | (flag, no value) |

{{% notice Important %}}
Always use full paths (`/home/developer/...`) for `--model_name` and `--output`. The `~` shortcut is not expanded.
{{% /notice %}}

### Target Configurations for Ethos-U55

| Target | MACs | Use Case |
|--------|------|----------|
| `ethos-u55-32` | 32 | Ultra-low power |
| `ethos-u55-64` | 64 | Low power |
| `ethos-u55-128` | 128 | **Alif E8 (use this)** |
| `ethos-u55-256` | 256 | High performance |

### Memory Modes

| Mode | Description |
|------|-------------|
| `Shared_Sram` | NPU and CPU share SRAM (default, recommended) |
| `Sram_Only` | NPU uses dedicated SRAM only |

## Supported Operators

The Ethos-U55 NPU accelerates these operators:

| Category | Operators |
|----------|-----------|
| **Convolution** | Conv2d, DepthwiseConv2d, TransposeConv2d |
| **Pooling** | MaxPool2d, AvgPool2d |
| **Activation** | ReLU, ReLU6, Sigmoid, Tanh, Softmax |
| **Normalization** | BatchNorm2d |
| **Element-wise** | Add, Sub, Mul |
| **Shape** | Reshape, Transpose, Concat, Split |
| **Fully Connected** | Linear |
| **Other** | Pad, Resize |

**Unsupported operators** automatically fall back to Cortex-M55 CPU execution.

### Operators to Avoid

These operators have limited or no NPU support:

- `GroupNorm` - Use `BatchNorm2d` instead
- `GELU` - Use `ReLU` instead
- `LayerNorm` - Use `BatchNorm2d` instead
- Complex attention mechanisms

## Generate C Header for Embedding

For embedding the model directly in firmware, convert to C header:

```bash
# Using xxd
xxd -i /home/developer/output/mnist_ethos_u55.pte > /home/developer/output/mnist_model_data.h
```

Or use Python for more control:

```bash
python3 << 'EOF'
pte_path = "/home/developer/output/mnist_ethos_u55.pte"
header_path = "/home/developer/output/mnist_model_data.h"

with open(pte_path, "rb") as f:
    data = f.read()

with open(header_path, "w") as f:
    f.write("// Auto-generated MNIST model for Alif E8 Ethos-U55\n")
    f.write("#ifndef MNIST_MODEL_DATA_H\n")
    f.write("#define MNIST_MODEL_DATA_H\n\n")
    f.write("#include <stdint.h>\n\n")
    f.write("static const uint8_t mnist_model_data[] = {\n")
    
    for i in range(0, len(data), 12):
        chunk = data[i:i+12]
        hex_str = ", ".join(f"0x{b:02x}" for b in chunk)
        f.write(f"    {hex_str},\n")
    
    f.write("};\n\n")
    f.write(f"static const unsigned int mnist_model_len = {len(data)};\n\n")
    f.write("#endif /* MNIST_MODEL_DATA_H */\n")

print(f"Generated: {header_path}")
print(f"Model size: {len(data):,} bytes")
EOF
```

Expected output:
```output
Generated: /home/developer/output/mnist_model_data.h
Model size: 143,872 bytes
```

## Inspect PTE File

Check the generated `.pte` file:

```bash
# File size
ls -lh /home/developer/output/*.pte

# Basic inspection
python3 << 'EOF'
pte_path = "/home/developer/output/mnist_ethos_u55.pte"
with open(pte_path, "rb") as f:
    data = f.read()
    print(f"File size: {len(data):,} bytes")
    print(f"Header (first 16 bytes): {data[:16].hex()}")
EOF
```

## Custom Model Template

For any custom PyTorch model, follow this template:

```python
# /home/developer/models/your_model.py

import torch
import torch.nn as nn

class YourModel(nn.Module):
    def __init__(self):
        super(YourModel, self).__init__()
        # Define layers here
        # Prefer Conv2d, ReLU, MaxPool2d for NPU acceleration
    
    def forward(self, x):
        # Define forward pass
        return x

# REQUIRED: Model instance
model = YourModel()

# REQUIRED: Example input matching your model's expected shape
example_input = torch.randn(batch_size, input_channels, height, width)

# REQUIRED: These exact variable names are expected by aot_arm_compiler
ModelUnderTest = model
ModelInputs = (example_input,)  # Must be a tuple
```

Export command (use full paths):
```bash
python3 -m examples.arm.aot_arm_compiler \
    --model_name=/home/developer/models/your_model.py \
    --delegate \
    --quantize \
    --target=ethos-u55-128 \
    --system_config=Ethos_U55_High_End_Embedded \
    --memory_mode=Shared_Sram \
    --output=/home/developer/output/your_model.pte
```

## Copy Output to Host

If you have Docker volumes mounted, files are automatically synced:

```bash
# Inside container - verify files
ls -la /home/developer/output/

# On host (outside container) - check mounted directory:
# ~/executorch-alif/output/
```

Your files are accessible at `~/executorch-alif/output/` on your host machine.

## Summary

You have:
- ✅ Exported a PyTorch model to `.pte` format
- ✅ Applied INT8 quantization for Ethos-U55
- ✅ Generated Vela-optimized model for 128 MACs
- ✅ Created C header file for firmware embedding
- ✅ Understood supported operators and NPU delegation

In the next section, you'll build the ExecuTorch runtime for Cortex-M55.
