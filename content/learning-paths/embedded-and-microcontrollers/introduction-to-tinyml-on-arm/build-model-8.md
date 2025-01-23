---
# User change
title: "Build a Simple PyTorch Model"

weight: 7 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

TODO connect this part with the FVP/board?
With our environment ready, you can create a simple program to test the setup.

This example defines a small feedforward neural network for a classification task. The model consists of 2 linear layers with ReLU activation in between.

Use a text editor to create a file named `simple_nn.py` with the following code:

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

Run the model from the Linux command line:

```console
python3 simple_nn.py
```

The output is:

```output
Model successfully exported to simple_nn.pte
```

The model is saved as a .pte file, which is the format used by ExecuTorch for deploying models to the edge.

Run the ExecuTorch version, first build the executable:

```console
# Clean and configure the build system
(rm -rf cmake-out && mkdir cmake-out && cd cmake-out && cmake ..)

# Build the executor_runner target
cmake --build cmake-out --target executor_runner -j$(nproc)
```

You see the build output and it ends with:

```output
[100%] Linking CXX executable executor_runner
[100%] Built target executor_runner
```

When the build is complete, run the executor_runner with the model as an argument:

```console
./cmake-out/executor_runner --model_path simple_nn.pte
```

Since the model is a simple feedforward model, you see a tensor of shape [1, 2]

```output
I 00:00:00.006598 executorch:executor_runner.cpp:73] Model file simple_nn.pte is loaded.
I 00:00:00.006628 executorch:executor_runner.cpp:82] Using method forward
I 00:00:00.006635 executorch:executor_runner.cpp:129] Setting up planned buffer 0, size 320.
I 00:00:00.007225 executorch:executor_runner.cpp:152] Method loaded.
I 00:00:00.007237 executorch:executor_runner.cpp:162] Inputs prepared.
I 00:00:00.012885 executorch:executor_runner.cpp:171] Model executed successfully.
I 00:00:00.012896 executorch:executor_runner.cpp:175] 1 outputs:
Output 0: tensor(sizes=[1, 2], [-0.105369, -0.178723])
```

When the model execution completes successfully, you’ll see confirmation messages similar to those above, indicating successful loading, inference, and output tensor shapes.

