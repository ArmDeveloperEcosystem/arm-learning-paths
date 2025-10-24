---
# User change
title: "Build the ExecuTorch executor_runtime Runtime File"

weight: 9 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

You will build the Arm Executor Runner, which runs the `mv2_arm.pte` model on the NXP board.

1. Build the Arm Executor Runner components:

   ```bash
   mkdir examples/arm/executor_runner_aarch64_linux_gnu/cmake-out
   cd examples/arm/executor_runner_aarch64_linux_gnu/cmake-out
   cmake ..
   ```

2. Build the Arm Executor Runner
   ```bash
   cmake --build . --target executor_runner_aarch64_linux_gnu -j1
   ```

3. Check that the `executor_runner_aarch64_linux_gnu` file was generated:
   
   ```bash
   ls examples/arm/executor_runner_aarch64_linux_gnu/cmake-out/executor_runner_aarch64_linux_gnu
   ```