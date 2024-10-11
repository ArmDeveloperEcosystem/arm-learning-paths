---
# User change
title: "Build a Simple PyTorch Model"

weight: 9 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

With our Environment ready, we will create a simple program to test our setup. This example will define a simple feedforward neural network for a classification task. The model consists of 2 linear layers with ReLU activation in between. Create a file called simple_nn.py with the following code:

```python
import torch
from torch.export import export
from executorch.exir import to_edge

# Define a simple Feedforward Neural Network
class SimpleNN(torch.nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleNN, self).__init__()
        self.fc1 = torch.nn.Linear(input_size, hidden_size)
        self.relu = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(hidden_size, output_size)
        
    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

# Create the model instance
input_size = 10   # example input features size
hidden_size = 5   # hidden layer size
output_size = 2   # number of output classes

model = SimpleNN(input_size, hidden_size, output_size)

# Example input tensor (batch size 1, input size 10)
x = torch.randn(1, input_size)

# torch.export: Defines the program with the ATen operator set for SimpleNN.
aten_dialect = export(model, (x,))

# to_edge: Make optimizations for edge devices. This ensures the model runs efficiently on constrained hardware.
edge_program = to_edge(aten_dialect)

# to_executorch: Convert the graph to an ExecuTorch program
executorch_program = edge_program.to_executorch()

# Save the compiled .pte program
with open("simple_nn.pte", "wb") as file:
    file.write(executorch_program.buffer)

print("Model successfully exported to simple_nn.pte")
```

Run it from your terminal:

```console
python3 simple_nn.py
```

If everything runs successfully, the output will be:
```bash { output_lines = "1" }
Model successfully exported to simple_nn.pte
```
Finally, the model is saved as a .pte file, which is the format used by ExecuTorch for deploying models to the edge.

Now, we will run the ExecuTorch version, first run: 

```console
# Clean and configure the build system
rm -rf cmake-out && mkdir cmake-out && cd cmake-out && cmake ..

# Build the executor_runner target
cmake --build cmake-out --target executor_runner -j9
```

You should see an output similar to:
```bash { output_lines = "1" }
[100%] Built target executor_runner
```

Now, run the executor_runner with the Model:
```console
./cmake-out/executor_runner --model_path simple_nn.pte
```

Expected Output: Since the model is a simple feedforward model, you can expect a tensor of shape [1, 2]

```bash { output_lines = "1-3" }
Input tensor shape: [1, 10]
Output tensor shape: [1, 2]
Inference output: tensor([[0.5432, -0.3145]]) #will vary due to random initialization
```

If the model execution completes successfully, you’ll see confirmation messages similar to those above, indicating successful loading, inference, and output tensor shapes.

