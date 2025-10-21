---
# User change
title: "Build a simple PyTorch model"

weight: 7 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Define a small neural network using Python

With your development environment set up, you can create a simple PyTorch model to test the setup.

This example defines a small feedforward neural network for a classification task. The model consists of two linear layers with ReLU activation in between.

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
input_size = 10   # example input feature size
hidden_size = 5   # hidden layer size
output_size = 2   # number of output classes

model = SimpleNN(input_size, hidden_size, output_size)

# Example input tensor (batch size 1, input size 10)
x = (torch.randn(1, input_size),)

# Add arguments to be parsed by the Ahead-of-Time (AoT) Arm compiler
ModelUnderTest = model
ModelInputs = x

print("Model successfully exported to simple_nn.pte")
```

## Run the model on the Corstone-320 FVP

The final step is to take the Python-defined model and run it on the Corstone-320 FVP. This was done upon running the `run.sh` script in a previous section. To wrap up the Learning Path, you will perform these steps separately to better understand what happened under the hood. Start by setting some environment variables that are used by ExecuTorch.

```bash
export ET_HOME=$HOME/executorch
export executorch_DIR=$ET_HOME/build
```

Generate a model in ExecuTorch `.pte` format using the Arm examples. The AoT Arm compiler enables optimizations for devices such as the Grove Vision AI Module V2 and the Corstone-320 FVP. Run the compiler from the ExecuTorch root directory:

```bash
cd $ET_HOME
python -m examples.arm.aot_arm_compiler --model_name=examples/arm/simple_nn.py --delegate --quantize --target=ethos-u85-256 --system_config=Ethos_U85_SYS_DRAM_Mid --memory_mode=Sram_Only
```

From the Arm Examples directory, you can build an embedded Arm runner with the `.pte` included. This allows you to optimize the performance of your model, and ensures compatibility with the CPU kernels on the FVP. Finally, build the ExecuTorch libraries and generate the executable `arm_executor_runner`.

```bash
cmake -S "${ET_HOME}" \
      -B "${executorch_DIR}" \
      --preset arm-baremetal \
      -DCMAKE_BUILD_TYPE=Release

cmake --build "$executorch_DIR" --target install --parallel

cd $HOME/executorch/examples/arm/executor_runner

cmake -S "${ET_HOME}/examples/arm/executor_runner" \
      -B "${ET_HOME}/examples/arm/executor_runner/cmake-out" \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_TOOLCHAIN_FILE=$ET_HOME/examples/arm/ethos-u-setup/arm-none-eabi-gcc.cmake \
      -DTARGET_CPU=cortex-m85 \
      -DET_PTE_FILE_PATH:PATH=$ET_HOME/simple_nn_arm_delegate_ethos-u85-256.pte \
      -DETHOS_SDK_PATH:PATH=$ET_HOME/examples/arm/ethos-u-scratch/ethos-u \
      -DETHOSU_TARGET_NPU_CONFIG=ethos-u85-256 \
      -DPYTHON_EXECUTABLE=$HOME/executorch-venv/bin/python3 \
      -DSYSTEM_CONFIG=Ethos_U85_SYS_DRAM_Mid \

cmake --build $ET_HOME/examples/arm/executor_runner/cmake-out --parallel -- arm_executor_runner

```

Run the model on Corstone-320:

```bash
FVP_Corstone_SSE-320 \
-C mps4_board.subsystem.ethosu.num_macs=256 \
-C mps4_board.visualisation.disable-visualisation=1 \
-C vis_hdlcd.disable_visualisation=1                \
-C mps4_board.telnetterminal0.start_telnet=0        \
-C mps4_board.uart0.out_file='-'                    \
-C mps4_board.uart0.shutdown_on_eot=1               \
-a "$ET_HOME/examples/arm/executor_runner/cmake-out/arm_executor_runner"
```

{{% notice Note %}}
The argument `mps4_board.visualisation.disable-visualisation=1` disables the FVP GUI and can speed up launch time
{{% /notice %}}

Observe that the FVP loads the model file.
```output
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
telnetterminal5: Listening for serial connection on port 5003
I [executorch:arm_executor_runner.cpp:412] Model in 0x70000000 $
I [executorch:arm_executor_runner.cpp:414] Model PTE file loaded. Size: 3360 bytes.
```

You have now set up your environment for TinyML development on Arm and tested a small PyTorch model with ExecuTorch on the Corstone-320 FVP. In the next Learning Path, you learn how to optimize neural networks to run efficiently on Arm.
