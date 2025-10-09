---
title: Run the model on Corstone-320 FVP
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Compile and run the rock-paper-scissors model on Corstone-320 FVP

This section shows how to compile your trained rock-paper-scissors model and run it on the Corstone-320 Fixed Virtual Platform (FVP), a simulated Arm-based edge device. This completes the end-to-end workflow for deploying a TinyML model for on-device inference.

## Compile and build the executable

Use the Ahead-of-Time (AoT) Arm compiler to convert your PyTorch model to an ExecuTorch program optimized for Arm and the Ethos-U NPU. This process (delegation) offloads supported parts of the neural network to the NPU for efficient inference.

Set up environment variables:

```bash
export ET_HOME=$HOME/executorch
export executorch_DIR=$ET_HOME/build
```

Use the AOT Arm compiler to generate the optimized `.pte` file. This command delegates the model to the Ethos-U85 NPU, applies quantization to reduce model size and improve performance, and specifies the memory configuration. Run it from the ExecuTorch root directory.

```bash
cd $ET_HOME
python -m examples.arm.aot_arm_compiler --model_name=examples/arm/rps_tiny.py \
--delegate --quantize --target=ethos-u85-128 \
--system_config=Ethos_U85_SYS_DRAM_Mid --memory_mode=Dedicated_Sram
```

You should see:

```output
PTE file saved as rps_tiny_arm_delegate_ethos-u85-128.pte
```

Next, build the Ethos-U runner - a bare-metal executable that includes the ExecuTorch runtime and your compiled model. Configure the build with CMake:

```bash
cd $HOME/executorch/examples/arm/executor_runner

cmake -DCMAKE_BUILD_TYPE=Release \
      -S "$ET_HOME/examples/arm/executor_runner" \
      -B "$ET_HOME/examples/arm/executor_runner/cmake-out" \
      -DCMAKE_TOOLCHAIN_FILE="$ET_HOME/examples/arm/ethos-u-setup/arm-none-eabi-gcc.cmake" \
      -DTARGET_CPU=cortex-m85 \
      -DET_DIR_PATH="$ET_HOME" \
      -DET_BUILD_DIR_PATH="$ET_HOME/arm_test/cmake-out" \
      -DET_PTE_FILE_PATH="$ET_HOME/rps_tiny_arm_delegate_ethos-u85-128.pte" \
      -DETHOS_SDK_PATH="$ET_HOME/examples/arm/ethos-u-scratch/ethos-u" \
      -DETHOSU_TARGET_NPU_CONFIG=ethos-u85-128 \
      -DSYSTEM_CONFIG=Ethos_U85_SYS_DRAM_Mid
```

You should see configuration output similar to:

```bash
-- *******************************************************
-- PROJECT_NAME                           : ethos-u-corstone-320
-- TR_ARENA_SIZE                          :
-- MESSAGE_HANDLER_ARENA_SIZE             :
-- *******************************************************
-- ET_ARM_BAREMETAL_SCRATCH_TEMP_ALLOCATOR_POOL_SIZE = 0x200000
-- ET_ARM_BAREMETAL_FAST_SCRATCH_TEMP_ALLOCATOR_POOL_SIZE =
-- Configuring done (17.1s)
-- Generating done (0.2s)
-- Build files have been written to: ~/executorch/examples/arm/executor_runner/cmake-out
```

Build the executable:

```bash
cmake --build "$ET_HOME/examples/arm/executor_runner/cmake-out" -j --target arm_executor_runner
```

## Run the model on the FVP
With the `arm_executor_runner` executable ready, you can now run it on the Corstone-320 FVP to see the model on a simulated Arm device.

```bash
FVP_Corstone_SSE-320 \
-C mps4_board.subsystem.ethosu.num_macs=128 \
-C mps4_board.visualisation.disable-visualisation=1 \
-C vis_hdlcd.disable_visualisation=1                \
-C mps4_board.telnetterminal0.start_telnet=0        \
-C mps4_board.uart0.out_file='-'                    \
-C mps4_board.uart0.shutdown_on_eot=1               \
-a "$ET_HOME/examples/arm/executor_runner/cmake-out/arm_executor_runner"
```

{{% notice Note %}}
`mps4_board.visualisation.disable-visualisation=1` disables the FVP GUI and can reduce launch time
{{% /notice %}}

You should see logs indicating that the model file loads and inference begins:

```output
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
telnetterminal5: Listening for serial connection on port 5003
I [executorch:arm_executor_runner.cpp:489 main()] PTE in 0x70000000 $ Size: 433968 bytes
I [executorch:arm_executor_runner.cpp:514 main()] PTE Model data loaded. Size: 433968 bytes.
I [executorch:arm_executor_runner.cpp:527 main()] Model buffer loaded, has 1 methods
I [executorch:arm_executor_runner.cpp:535 main()] Running method forward
I [executorch:arm_executor_runner.cpp:546 main()] Setup Method allocator pool. Size: 62914560 bytes.
I [executorch:arm_executor_runner.cpp:563 main()] Setting up planned buffer 0, size 3920.
I [executorch:EthosUBackend.cpp:116 init()] data:0x70000070
```

{{% notice Note %}}
Inference might take longer with a model of this size on the FVP; this does not reflect real device performance.
{{% /notice %}}

You have now built, optimized, and deployed a computer vision model on a simulated Arm-based system. In a future Learning Path, you can compare performance and latency before and after optimization and analyze CPU and memory usage during inference for deeper insight into ExecuTorch on edge devices.
