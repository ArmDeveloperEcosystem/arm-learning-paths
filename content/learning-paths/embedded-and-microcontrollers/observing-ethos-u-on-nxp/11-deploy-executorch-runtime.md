---
# User change
title: "Deploy the ExecuTorch Files to the NXP Board"

weight: 12 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

1. Copy the `executor_runner_aarch64_linux_gnu` and `mv2_arm.pte` files to the NXP board using a USB thumb drive:

   {{% notice macOS %}}

   First copy the two files from your Docker container to your local machine:
   ```bash
   docker cp <containerId>:/executorch/examples/arm/executor_runner_aarch64_linux_gnu/cmake-out/executor_runner_aarch64_linux_gnu .
   docker cp <containerId>:/path/to/executorch/mv2/mv2_arm.pte .
   ```

   {{% /notice %}}

   - Transfer the two files from your computer to the thumb drive (drag-and-drop, etc.)
   - Transfer the two files from the thumb drive to the NXP board:
     - Insert the USB thumb drive into the NXP board's USB A port
     - Mount the thumb drive and then copy the files to the board:
       ```bash { output_lines = "1" }
       # Execute these commands on the board, individually
       mount /dev/sda1 /mnt
       cp /mnt/executor_runner_aarch64_linux_gnu .
       cp /mnt/mv2_arm.pte .
       ```

   - [optional] Unmount the thumbdrive and then remove it from the NXP board
     ```bash
     umount /mnt
     ```

2. Run inference, executing all of the following commands on the NXP board:
   - Enable debugging and profiling, logs should appear in `/sys/class/ethosu`:
     ```bash
     export ET_LOG_LEVEL=debug
     ```

   - Make sure the `executor_runner_aarch64_linux_gnu` is executable:
     ```bash
     chmod +x ./executor_runner_aarch64_linux_gnu
     ```

   - Run inference:
     ```bash
     ./executor_runner_aarch64_linux_gnu --model_path=mv2_arm.pte
     ```

   The NXP output should be similar to an [Arm Fixed Virtual Platform's output](http://localhost:1313/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/6-evaluate-output/) (see section "Observe Test Batch Performance"):

   ```bash { output_lines = "1-3" }
   Model loaded
   Running method forward...
   Inference complete. Output: [class logits]
   ```

3. Validate correctness:
   - Compare the output logits from i.MX93 to those you got on FVP
   - They should match closely (within quantization tolerance)