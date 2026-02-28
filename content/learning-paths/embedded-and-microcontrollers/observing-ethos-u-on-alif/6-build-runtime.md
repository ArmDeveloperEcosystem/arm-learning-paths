---
title: Build ExecuTorch runtime for Arm
weight: 6
layout: learningpathall
---

## Overview

This section covers cross-compiling the ExecuTorch runtime for the Alif Ensemble E8's Cortex-M55 processor with Ethos-U55 NPU support.

## Prerequisites

Ensure you completed the previous section and have:
- ExecuTorch and Arm toolchain installed
- Model exported to `.pte` format

Verify your environment:

```bash
# Inside Docker container
source ~/executorch-venv/bin/activate

# Check ET_HOME is set
echo $ET_HOME
# Should output: /home/developer/executorch

# Verify toolchain
arm-none-eabi-gcc --version
# Should show: arm-none-eabi-gcc (Arm GNU Toolchain 13.3.Rel1...)

# Verify model exists
ls -la /home/developer/output/mnist_ethos_u55.pte
```

## Build Overview

Building the runtime requires two stages:

**Stage 1: Build ExecuTorch ARM Libraries** - Cross-compile core libraries for Cortex-M55

**Stage 2: Build Executor Runner** - Link libraries with your model into a single ELF

```
┌─────────────────────────────────────────────────────────────────┐
│                    Build Pipeline                                │
├─────────────────────────────────────────────────────────────────┤
│  Stage 1: ARM Libraries                                          │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │ executorch_core │  │ portable_kernels│  │ cortex_m_kernels│  │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘  │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │ ethos_u_delegate│  │ quantized_ops   │  │ flatccrt        │  │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘  │
├─────────────────────────────────────────────────────────────────┤
│  Stage 2: Executor Runner                                        │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │  ARM Libraries + Ethos-U SDK + Model (.pte)                 ││
│  │                       ↓                                      ││
│  │              arm_executor_runner.elf                         ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

## Stage 1: Build ExecuTorch ARM Libraries

### Step 1.1: Configure and Build

```bash
cd $ET_HOME

# Clean any previous ARM build
rm -rf cmake-out-arm

# Configure for ARM Cortex-M55 bare-metal
cmake -DCMAKE_TOOLCHAIN_FILE=$ET_HOME/examples/arm/ethos-u-setup/arm-none-eabi-gcc.cmake \
      -DCMAKE_INSTALL_PREFIX=$ET_HOME/cmake-out-arm \
      -DEXECUTORCH_BUILD_ARM_BAREMETAL=ON \
      -DEXECUTORCH_SELECT_OPS_LIST=aten::add.out,aten::_softmax.out \
      -DEXECUTORCH_ENABLE_LOGGING=ON \
      -DFLATC_EXECUTABLE=$(which flatc) \
      -DPYTHON_EXECUTABLE=$(which python3) \
      -B cmake-out-arm

# Build (ignore executor_runner link error - it's expected)
cmake --build cmake-out-arm --parallel $(nproc) || true
```

{{% notice Note %}}
The build will show an error at the end about `ethosu_core_driver` - this is expected. The libraries we need are already built.
{{% /notice %}}

### Step 1.2: Verify Libraries Built

```bash
# Check that key libraries exist
ls $ET_HOME/cmake-out-arm/libexecutorch.a
ls $ET_HOME/cmake-out-arm/libexecutorch_core.a
ls $ET_HOME/cmake-out-arm/backends/arm/libexecutorch_delegate_ethos_u.a
ls $ET_HOME/cmake-out-arm/backends/cortex_m/libcortex_m_kernels.a
ls $ET_HOME/cmake-out-arm/backends/cortex_m/libcortex_m_ops_lib.a
```

Expected output shows all files exist.

### Step 1.3: Set Up Install Directory

The CMake install target fails, so manually organize the libraries:

```bash
# Create install directory structure
mkdir -p $ET_HOME/cmake-out-arm/lib/cmake/ExecuTorch
mkdir -p $ET_HOME/cmake-out-arm/include/executorch

# Copy all libraries to lib directory
for lib in $(find $ET_HOME/cmake-out-arm -name "*.a" -type f); do
    base=$(basename "$lib")
    if [ ! -f "$ET_HOME/cmake-out-arm/lib/$base" ]; then
        cp "$lib" "$ET_HOME/cmake-out-arm/lib/"
    fi
done

# Verify key libraries
ls $ET_HOME/cmake-out-arm/lib/libexecutorch.a
ls $ET_HOME/cmake-out-arm/lib/libcortex_m_kernels.a
ls $ET_HOME/cmake-out-arm/lib/libexecutorch_delegate_ethos_u.a
```

### Step 1.4: Set Up CMake Config

```bash
# Copy CMake export files
cp $ET_HOME/cmake-out-arm/CMakeFiles/Export/9691d906f7e19b59f3b4ca44eacce0c7/*.cmake \
   $ET_HOME/cmake-out-arm/lib/cmake/ExecuTorch/

# Create executorch-config.cmake
cat > $ET_HOME/cmake-out-arm/lib/cmake/ExecuTorch/executorch-config.cmake << 'EOF'
get_filename_component(EXECUTORCH_INSTALL_PREFIX "${CMAKE_CURRENT_LIST_DIR}/../../.." ABSOLUTE)
set(EXECUTORCH_LIBRARIES
    ${EXECUTORCH_INSTALL_PREFIX}/lib/libexecutorch.a
    ${EXECUTORCH_INSTALL_PREFIX}/lib/libexecutorch_core.a
)
set(EXECUTORCH_INCLUDE_DIRS
    ${EXECUTORCH_INSTALL_PREFIX}/..
    ${EXECUTORCH_INSTALL_PREFIX}/../third-party/flatcc/include
)
include(${CMAKE_CURRENT_LIST_DIR}/ExecuTorchTargets.cmake OPTIONAL)
EOF
```

### Step 1.5: Set Up Include Directory

```bash
# Create symlinks to source headers
ln -sf $ET_HOME/runtime $ET_HOME/cmake-out-arm/include/executorch/
ln -sf $ET_HOME/extension $ET_HOME/cmake-out-arm/include/executorch/
ln -sf $ET_HOME/kernels $ET_HOME/cmake-out-arm/include/executorch/
ln -sf $ET_HOME/backends $ET_HOME/cmake-out-arm/include/executorch/
ln -sf $ET_HOME/schema $ET_HOME/cmake-out-arm/include/executorch/
```

## Stage 2: Build Executor Runner

### Step 2.1: Set Environment and Build

```bash
cd $ET_HOME

# IMPORTANT: Set the library path
export executorch_DIR=$ET_HOME/cmake-out-arm/lib/cmake/ExecuTorch

# Build executor runner with your model
# NOTE: Use full path, not ~ (tilde doesn't expand in the build script)
./backends/arm/scripts/build_executor_runner.sh \
    --pte=/home/developer/output/mnist_ethos_u55.pte \
    --target=ethos-u55-128 \
    --system_config=Ethos_U55_High_End_Embedded \
    --memory_mode=Shared_Sram \
    --build_type=Release
```

{{% notice Note %}}
This build may take 5-10 minutes as it compiles the entire ExecuTorch runtime and links it with your model.
{{% /notice %}}

### Step 2.2: Verify Build Success

The build should complete with output like:

```output
[100%] Linking CXX executable arm_executor_runner
[./backends/arm/scripts/build_executor_runner.sh] Generated arm-none-eabi-gcc elf file:
/home/developer/output/mnist_ethos_u55/cmake-out/arm_executor_runner
executable_text: 234860 bytes
executable_data: 65127416 bytes
executable_bss:  25824 bytes
```

### Step 2.3: Generate Binary Files and Copy to Output

```bash
# Check the ELF file
arm-none-eabi-size /home/developer/output/mnist_ethos_u55/cmake-out/arm_executor_runner

# Copy to output directory
cp /home/developer/output/mnist_ethos_u55/cmake-out/arm_executor_runner /home/developer/output/

# Generate binary for flashing
arm-none-eabi-objcopy -O binary \
    /home/developer/output/mnist_ethos_u55/cmake-out/arm_executor_runner \
    /home/developer/output/arm_executor_runner.bin

# Generate Intel HEX format (alternative)
arm-none-eabi-objcopy -O ihex \
    /home/developer/output/mnist_ethos_u55/cmake-out/arm_executor_runner \
    /home/developer/output/arm_executor_runner.hex

# Copy map file for debugging
cp /home/developer/output/mnist_ethos_u55/cmake-out/arm_executor_runner.map /home/developer/output/

# Verify outputs
ls -lh /home/developer/output/arm_executor_runner*
```

Expected output:
```output
-rwxr-xr-x 1 developer developer  65M Dec 14 12:00 arm_executor_runner
-rw-r--r-- 1 developer developer  65M Dec 14 12:00 arm_executor_runner.bin
-rw-r--r-- 1 developer developer 130M Dec 14 12:00 arm_executor_runner.hex
-rw-r--r-- 1 developer developer 1.2M Dec 14 12:00 arm_executor_runner.map
```

## Build Outputs

| File | Purpose |
|------|---------|
| `arm_executor_runner` | ELF executable with debug symbols |
| `arm_executor_runner.bin` | Raw binary for flashing with J-Link |
| `arm_executor_runner.hex` | Intel HEX format for flashing |
| `arm_executor_runner.map` | Memory map for debugging |

## Understanding What You Built

The `arm_executor_runner` is built for **Arm Corstone-300 FVP** (Fixed Virtual Platform), which contains:
- Cortex-M55 processor (same as Alif E8)
- Ethos-U55 NPU (same as Alif E8)
- Simulated memory and peripherals (different from Alif E8)

```
┌─────────────────────────────────────────────────────────────┐
│                    arm_executor_runner                       │
├─────────────────────────────────────────────────────────────┤
│  Target: Corstone-300 FVP                                    │
│  CPU: Cortex-M55 (compatible with Alif E8)                   │
│  NPU: Ethos-U55-128 (compatible with Alif E8)                │
│  HAL: Corstone-300 (NOT compatible with Alif E8)             │
├─────────────────────────────────────────────────────────────┤
│  Contents:                                                   │
│  • ExecuTorch runtime libraries                              │
│  • Ethos-U delegate and driver                               │
│  • Cortex-M optimized kernels                                │
│  • Embedded MNIST model (.pte)                               │
│  • Corstone-300 startup and HAL code                         │
└─────────────────────────────────────────────────────────────┘
```

**Key Point**: The runner works in FVP simulation but needs HAL adaptation for real Alif E8 hardware. In the next section, you'll integrate with Alif SDK.

## Memory Layout Analysis

Check memory usage:

```bash
arm-none-eabi-size -A /home/developer/output/arm_executor_runner
```

Expected output shows:
```output
section              size        addr
.text             234860  0x00000000
.data              12345  0x20000000
.bss               25824  0x20003039
```

## Troubleshooting

### Build Error: "ethosu_core_driver not found"

This error at the end of Stage 1 is expected. The libraries needed for Stage 2 are already built.

### Build Error: "Cannot find -lexecutorch"

Set the library path:

```bash
export executorch_DIR=$ET_HOME/cmake-out-arm/lib/cmake/ExecuTorch
```

### Large Binary Size

The binary includes the embedded model and all runtime libraries. This is normal for bare-metal applications.

## Copy Files to Host

Files in `/home/developer/output/` are automatically synced to `~/executorch-alif/output/` on your host machine (if Docker volumes are mounted correctly).

Verify on your host:

```bash
# On your host machine (outside Docker)
ls -lh ~/executorch-alif/output/
```

## Summary

You have:
- ✅ Built ExecuTorch ARM libraries for Cortex-M55
- ✅ Compiled the executor runner with embedded MNIST model
- ✅ Generated binary files for flashing (.bin, .hex)
- ✅ Created debug files (.map) for troubleshooting
- ✅ Understood the Corstone-300 FVP target

In the next section, you'll create an Alif E8 CMSIS-Toolbox project with proper hardware abstraction.
