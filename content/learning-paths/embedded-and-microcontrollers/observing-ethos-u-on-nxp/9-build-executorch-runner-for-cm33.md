---
title: Build the executor_runner firmware
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up MCUXpresso for VS Code

Install the MCUXpresso extension in VS Code:

{{< tabpane code=false >}}
{{< tab header="Windows/Linux" >}}
1. Open VS Code and press `Ctrl+Shift+X` to open Extensions
2. Search for "MCUXpresso for VS Code"
3. Click **Install** on the NXP extension
{{< /tab >}}
{{< tab header="macOS" >}}
1. Open VS Code and press `Cmd+Shift+X` to open Extensions
2. Search for "MCUXpresso for VS Code"  
3. Click **Install** on the NXP extension
{{< /tab >}}
{{< /tabpane >}}

Configure the ARM toolchain path:

{{< tabpane code=false >}}
{{< tab header="Windows/Linux" >}}
1. Open Settings with `Ctrl+,`
2. Search for **MCUXpresso: Toolchain**
3. Set the toolchain path to: `/opt/arm-gnu-toolchain-14.2.rel1-x86_64-arm-none-eabi/bin`
{{< /tab >}}
{{< tab header="macOS" >}}
1. Open Settings with `Cmd+,`
2. Search for **MCUXpresso: Toolchain**
3. Set the toolchain path to: `/opt/arm-gnu-toolchain-14.2.rel1-x86_64-arm-none-eabi/bin`
{{< /tab >}}
{{< /tabpane >}}

Install the MCUXpresso SDK for FRDM-MIMX93:

{{< tabpane code=false >}}
{{< tab header="Windows/Linux" >}}
1. Open Command Palette: `Ctrl+Shift+P`
2. Type: **MCUXpresso: Install MCUXpresso SDK**
3. Search for "FRDM-MIMX93" or select **MCIMX93-EVK**
4. Select the latest SDK and click **Install**
{{< /tab >}}
{{< tab header="macOS" >}}
1. Open Command Palette: `Cmd+Shift+P`
2. Type: **MCUXpresso: Install MCUXpresso SDK**
3. Search for "FRDM-MIMX93" or select **MCIMX93-EVK**
4. Select the latest SDK and click **Install**
{{< /tab >}}
{{< /tabpane >}}

{{% notice Note %}}
If the FRDM-MIMX93 development board is not listed in the current MCUXpresso SDK catalog, you can alternatively select **MCIMX93-EVK** as they share the same i.MX93 SoC with Cortex-M33 core architecture. The SDK compatibility ensures seamless development across both platforms.
{{% /notice %}}

## Clone the executor_runner repository

Clone the ready-to-build executor_runner project:

```bash
git clone https://github.com/fidel-makatia/Executorch_runner_cm33.git
cd Executorch_runner_cm33
```

The repository contains the complete runtime source code and build configuration for Cortex-M33.

## Copy ExecuTorch libraries

The executor_runner requires prebuilt ExecuTorch libraries with Ethos-U NPU support from your Docker container.

Find your ExecuTorch build container:

```bash { output_lines = "2-3" }
docker ps -a
CONTAINER ID   IMAGE          COMMAND       CREATED        STATUS
abc123def456   executorch     "/bin/bash"   2 hours ago    Exited
```

Copy the libraries:

```bash
docker cp abc123def456:/home/ubuntu/executorch/cmake-out/lib/. ./executorch/lib/
docker cp abc123def456:/home/ubuntu/executorch/. ./executorch/include/executorch/
```

Replace `abc123def456` with your actual container ID.

{{% notice Note %}}
In some Docker containers, the `cmake-out` folder might not exist. If you don't see the libraries, run the following command to build them:

```bash
./examples/arm/run.sh --build-only
```

The libraries will be generated in `arm_test/cmake-out`.
{{% /notice %}}

Verify the libraries:

```bash { output_lines = "2-5" }
ls -lh executorch/lib/
-rw-r--r-- 1 user user 2.1M libexecutorch.a
-rw-r--r-- 1 user user 856K libexecutorch_core.a
-rw-r--r-- 1 user user 1.3M libexecutorch_delegate_ethos_u.a
```

## Configure the project for FRDM-MIMX93

Open the project in VS Code:

```bash
code .
```

Initialize the MCUXpresso project:

{{< tabpane code=false >}}
{{< tab header="Windows/Linux" >}}
1. Press `Ctrl+Shift+P` to open Command Palette
2. Type: **MCUXpresso: Import Repository**
3. Select the current folder
4. Choose **MIMX9352_cm33** as the target processor
{{< /tab >}}
{{< tab header="macOS" >}}
1. Press `Cmd+Shift+P` to open Command Palette
2. Type: **MCUXpresso: Import Repository**
3. Select the current folder
4. Choose **MIMX9352_cm33** as the target processor
{{< /tab >}}
{{< /tabpane >}}

VS Code generates the MCUXpresso configuration.

## Configure memory settings

The Cortex-M33 has 108KB of RAM. The default memory configuration allocates:
- 16KB for the method allocator (activation tensors)
- 8KB for the scratch allocator (temporary operations)

These settings are in `CMakeLists.txt`:

```cmake
target_compile_definitions(${MCUX_SDK_PROJECT_NAME} PRIVATE
  ET_ARM_BAREMETAL_METHOD_ALLOCATOR_POOL_SIZE=0x4000   # 16KB
  ET_ARM_BAREMETAL_SCRATCH_TEMP_ALLOCATOR_POOL_SIZE=0x2000  # 8KB
  ET_MODEL_PTE_ADDR=0x80100000  # DDR address for model
)
```

{{% notice Note %}}
If you see "region RAM overflowed" errors during build, reduce these pool sizes. For example, change to 0x2000 (8KB) and 0x1000 (4KB) respectively.
{{% /notice %}}

## Build the firmware

Configure the build system:

{{< tabpane code=false >}}
{{< tab header="Windows/Linux" >}}
1. Press `Ctrl+Shift+P`
2. Type: **CMake: Configure**
3. Select **ARM GCC** as the kit
4. Choose **Debug** or **Release**
{{< /tab >}}
{{< tab header="macOS" >}}
1. Press `Cmd+Shift+P`
2. Type: **CMake: Configure**
3. Select **ARM GCC** as the kit
4. Choose **Debug** or **Release**
{{< /tab >}}
{{< /tabpane >}}

Build the project:

Press `F7` or:

{{< tabpane code=false >}}
{{< tab header="Windows/Linux" >}}
1. Press `Ctrl+Shift+P`
2. Type: **CMake: Build**
{{< /tab >}}
{{< tab header="macOS" >}}
1. Press `Cmd+Shift+P`
2. Type: **CMake: Build**
{{< /tab >}}
{{< /tabpane >}}

Watch the build output:

```output
[build] Scanning dependencies of target executorch_runner_cm33.elf
[build] [ 25%] Building CXX object source/arm_executor_runner.cpp.obj
[build] [ 50%] Building CXX object source/arm_memory_allocator.cpp.obj
[build] [ 75%] Linking CXX executable executorch_runner_cm33.elf
[build] [100%] Built target executorch_runner_cm33.elf
[build] Build finished with exit code 0
```

Verify the build succeeded:

```bash { output_lines = "2" }
ls -lh build/executorch_runner_cm33.elf
-rwxr-xr-x 1 user user 601K executorch_runner_cm33.elf
```

Check memory usage to ensure it fits in the Cortex-M33:

```bash { output_lines = "2-3" }
arm-none-eabi-size build/executorch_runner_cm33.elf
   text	   data	    bss	    dec	    hex	filename
  52408	    724	  50472	 103604	  19494	executorch_runner_cm33.elf
```

The total RAM usage (data + bss) is approximately 51KB, well within the 108KB limit.

## Troubleshooting

**ARM toolchain not found:**

Add the toolchain to your PATH:

```bash
export PATH=/opt/arm-gnu-toolchain-14.2.rel1-x86_64-arm-none-eabi/bin:$PATH
```

**Cannot find ExecuTorch libraries:**

Verify the libraries were copied correctly:

```bash
ls executorch/lib/libexecutorch*.a
```

If missing, re-copy from the Docker container.

**Region RAM overflowed:**

Edit `CMakeLists.txt` and reduce the memory pool sizes:

```cmake
ET_ARM_BAREMETAL_METHOD_ALLOCATOR_POOL_SIZE=0x2000  # 8KB
ET_ARM_BAREMETAL_SCRATCH_TEMP_ALLOCATOR_POOL_SIZE=0x1000  # 4KB
```

Then rebuild with `F7`.