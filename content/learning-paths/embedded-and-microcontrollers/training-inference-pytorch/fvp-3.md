---
title: Run the model on Corstone-320 FVP  
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

TODO: Ask Annie to try from her end
## Compile and build the executable

Start by setting some environment variables that are used by ExecuTorch.

```bash
export ET_HOME=$HOME/executorch
export executorch_DIR=$ET_HOME/build
```


Then, generate a `.pte` file using the Arm examples. The Ahead-of-Time (AoT) Arm compiler will enable optimizations for edge devices like the Raspberry Pi and the Corstone-320 FVP. Run it from the ExecuTorch root directory.

Navigate to the root directory using:

```bash
cd ../../
```
You are now in $HOME/executorch and ready to create the model file for ExecuTorch.

```bash
cd $ET_HOME
python -m examples.arm.aot_arm_compiler --model_name=examples/arm/tiny_sentiment.py \
--delegate --quantize --target=ethos-u85-256 \
--so_library=cmake-out-aot-lib/kernels/quantized/libquantized_ops_aot_lib.so \
--system_config=Ethos_U85_SYS_DRAM_Mid --memory_mode=Sram_Only
```

From the Arm Examples directory, you build an embedded Arm runner with the `.pte` included. This allows you to get the most performance out of your model, and ensures compatibility with the CPU kernels on the FVP. Finally, generate the executable `arm_executor_runner`.

```bash
cd $HOME/executorch/examples/arm/executor_runner


cmake -DCMAKE_BUILD_TYPE=Release \
-DCMAKE_TOOLCHAIN_FILE=$ET_HOME/examples/arm/ethos-u-setup/arm-none-eabi-gcc.cmake \
-DTARGET_CPU=cortex-m85 \
-DET_DIR_PATH:PATH=$ET_HOME/ \
-DET_BUILD_DIR_PATH:PATH=$ET_HOME/cmake-out \
-DET_PTE_FILE_PATH:PATH=$ET_HOME/tiny_sentiment_arm_delegate_ethos-u85-256.pte \
-DETHOS_SDK_PATH:PATH=$ET_HOME/examples/arm/ethos-u-scratch/ethos-u \
-DETHOSU_TARGET_NPU_CONFIG=ethos-u85-256 \
-DPYTHON_EXECUTABLE=$HOME/executorch-venv/bin/python3 \
-DSYSTEM_CONFIG=Ethos_U85_SYS_DRAM_Mid  \
-B $ET_HOME/examples/arm/executor_runner/cmake-out

cmake --build $ET_HOME/examples/arm/executor_runner/cmake-out --parallel -- arm_executor_runner

```

Run the model on the Corstone-320 with the following command:

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

The argument `mps4_board.visualisation.disable-visualisation=1` disables the FVP GUI. This can speed up launch time for the FVP.

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

You can now test the model. 

## Test the Model
Test the model with your own inputs with the following command:


TODO: Add commands

```bash

```


You've successfully trained and tested a CNN model for sentiment analysis on Arm hardware using Executorch.

Experiment with different inputs and data samples. This hands-on course showcases the power of TinyML and NLP on resource-constrained devices.

In the next Learning Path, we would compare different model performances and inference times, before and after optimization using ExecuTorch. We would also analyze CPU and memory usage during inference. 
