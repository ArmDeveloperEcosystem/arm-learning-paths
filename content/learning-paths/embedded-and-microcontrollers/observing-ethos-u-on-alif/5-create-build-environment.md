---
# User change
title: "Build and Flash Your First Project"

weight: 6

# Do not modify these elements
layout: "learningpathall"
---

Now that you have all the tools installed, you'll build and flash a simple RTT (Real-Time Transfer) Hello World application to verify your setup.

## Clone the Example Project

Clone the ready-to-build MNIST inference project:

```bash
git clone https://github.com/fidel-makatia/alif-e8-mnist-npu.git
cd alif-e8-mnist-npu/alif_project
```

The repository contains:
- Complete MNIST digit classification demo
- SEGGER RTT library for debug output
- Pre-configured CMSIS build files
- JLink flash scripts

## Understanding the Project Structure

```
alif_project/
├── blinky/
│   ├── main.c              # Main application code
│   ├── mnist_model_data.h  # TFLite model (14KB, quantized INT8)
│   └── test_data.h         # Test image data
├── device/                 # Device configuration files
├── libs/
│   └── SEGGER_RTT_V796h/  # RTT library for debug output
├── flash_rtt.jlink        # JLink flash script
├── alif.csolution.yml     # CMSIS solution file
└── README.md
```

## Build the Project

Use the CMSIS Toolbox to build the project:

```bash
cbuild alif.csolution.yml -c blinky.debug+E8-HE --rebuild
```

Expected output:
```output
Building context: "blinky.debug+E8-HE"
...
Build summary: 1 succeeded, 0 failed
```

The build creates an ELF file at: `out/blinky/E8-HE/debug/blinky.elf`

### Alternative Build Method

If `cbuild` fails, use the CMake workflow:

```bash
cbuild2cmake alif.csolution.yml -c blinky.debug+E8-HE
cmake -B out/blinky/E8-HE/debug -S out/blinky/E8-HE/debug
ninja -C out/blinky/E8-HE/debug
```

## Flash the Firmware

Use JLink to flash the compiled firmware to the board.

### Method 1: Using JLink Script (Recommended)

```bash
JLinkExe -device Cortex-M55 -if SWD -speed 4000 -autoconnect 1 -CommandFile flash_rtt.jlink
```

### Method 2: Manual JLink Commands

If you prefer interactive flashing:

```bash
JLinkExe -device Cortex-M55 -if SWD -speed 4000 -autoconnect 1
```

Then enter these commands at the JLink prompt:

```
r                   # Reset
h                   # Halt
loadfile out/blinky/E8-HE/debug/blinky.elf
SetPC 0x800007C0    # Set program counter
w4 0xE000ED08 0x80000000  # Set VTOR (Vector Table Offset Register)
g                   # Run
exit
```

Expected output:
```output
Connecting to target via SWD
Found SW-DP with ID 0x...
Scanning AP map to find all available APs
...
Loading binary file out/blinky/E8-HE/debug/blinky.elf
...
O.K.
```

## Verify LED Indicators

After flashing, observe the RGB LED on the board:

1. **White flash** (500ms) - Board initialized
2. **Green flash** (500ms) - RTT ready  
3. **Blue blink** (1 Hz) - Application running

If you see these LED sequences, the firmware is running correctly.

## Test RTT Debug Output

SEGGER RTT (Real-Time Transfer) provides fast debug output without needing UART connections.

Start the RTT client:

```bash
JLinkRTTClient
```

Expected RTT output:
```output
========================================
  RTT TEST - Hello World!
  Alif E8 HE Core
========================================
[RTT] Hello World! Count: 1
[RTT] Hello World! Count: 2
[RTT] Hello World! Count: 3
...
```

The counter increments every second, confirming the application is running.

{{% notice Tip %}}
Press `Ctrl+C` to exit JLinkRTTClient.
{{% /notice %}}

## Build Configuration Details

The project targets the Alif E8 board with these specifications:

- **Device**: AlifSemiconductor AE822FA0E5597LS0
- **Core**: ARM Cortex-M55 HE (High Efficiency)
- **Board**: DevKit-E8
- **Compiler**: GCC (ARM)
- **Optimization**: None (debug build)
- **Debug**: Enabled

## Memory Configuration

The Cortex-M55 HE core has:

| Region | Address | Size | Usage |
|--------|---------|------|-------|
| ITCM | 0x00000000 | 256 KB | Fast code execution |
| DTCM | 0x20000000 | 256 KB | Fast data access |
| MRAM | 0x80000000 | 5.5 MB | Program storage |
| SRAM | 0x02000000 | 2 MB | General purpose RAM |

## Troubleshooting

**Build fails with "DFP not found":**
```bash
cpackget add AlifSemiconductor::Ensemble@2.0.4
```

**JLink cannot connect:**
- Check USB cable is connected to PRG port
- Verify board is powered (LED should be on)
- Try resetting the board
- Check JLink drivers are installed

**No RTT output:**
- Ensure firmware flashed successfully
- Reset the device: `r` then `g` in JLinkExe
- Restart JLinkRTTClient
- Verify blue LED is blinking (indicates app is running)

**Build succeeds but device doesn't run:**
- Check VTOR was set correctly: `w4 0xE000ED08 0x80000000`
- Verify program counter: `SetPC 0x800007C0`
- Try erasing flash before loading: `erase` in JLinkExe

## Next Steps

Now that you've successfully built and flashed a simple application, you're ready to run the MNIST inference demo and observe Ethos-U NPU performance.

## Create a Linux Container

1. Install and start [Docker Desktop](https://www.docker.com/)

2. Create a RTOS project directory:

   ```bash
   mkdir alif-rtos-starter
   ```

3. Create a `dockerfile` in the `alif-rtos-starter` directory:

   ```bash
   cd alif-rtos-starter
   touch dockerfile
   ```

4. Open the `dockerfile`:
   ```bash
   nano dockerfile
   ```

   and add the following commands:

   ```dockerfile
   FROM arm64v8/ubuntu:24.04

   # Basics
   FROM arm64v8/ubuntu:24.04

   # Basics
   RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
       build-essential cmake ninja-build git python3 python3-pip \
       wget unzip curl ca-certificates pkg-config && \
       rm -rf /var/lib/apt/lists/*

   # Arm GNU toolchain for the Alif Ensemble E8 Cortex-M
   RUN apt-get update
   RUN apt-get install -y --no-install-recommends gcc-arm-none-eabi

   # cmsis-toolbox (optional, handy for packs/csolution projects)
   RUN wget -q https://github.com/Open-CMSIS-Pack/cmsis-toolbox/releases/download/2.11.0/cmsis-toolbox-linux-arm64.tar.gz \
       && tar -xzf cmsis-toolbox-linux-arm64.tar.gz -C /opt \
       && ln -s /opt/cmsis-toolbox/csolution /usr/local/bin/csolution

   WORKDIR /work
   ```

   {{% notice Arm GNU Toolchain Compatibility %}}

   ###### The Alif Ensemble E8 needs a very specific [Arm GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain):
   * The Micro-Controller Unit (MCU) you are targeting is Cortex-M55
   * The Cortex-M55’s Arm architurecture version is [Armv8.1-M](https://developer.arm.com/documentation/107656/0101/Introduction-to-Armv8-M-architecture)
   * This is a 32-bit instruction set (AArch32) for bare-metal deployment

   ###### You need to compile software especially for the Cortex-M55 build target:
   * You need to cross-compile any code that you want to run on the Ensemble E8 board, to the AArch32, bare-metal Cortex-M55 target
   * Since your build container is AArch64 Linux, you will need a cross-compiler that runs on "AArch64 Linux", building for an "AArch32 bare-metal" target
   * The specific [Arm GNU Toolchain Download](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads) you want is:
     * Dev environment: "aarch64 Linux hosted cross toolchains"
     * Build target: "AArch32 bare-metal target (arm-none-eabi)"
     * Download file: [arm-gnu-toolchain-14.3.rel1-aarch64-arm-none-eabi.tar.xz](https://developer.arm.com/-/media/Files/downloads/gnu/14.3.rel1/binrel/arm-gnu-toolchain-14.3.rel1-aarch64-arm-none-eabi.tar.xz)
	
   ###### Just use apt-get in your dockerfile
   * It's far easier to just install the correct toolchain in your dev container using `apt-get install`, like in the above `dockerfile`:
   ```bash
   apt-get install -y --no-install-recommends gcc-arm-none-eabi
   ```

   {{% /notice %}}

5. Create the `alif-rtos-starter` container:

   ```bash
   docker build -t alif-rtos-starter .
   ```

6. Run the `alif-rtos-starter`:

   ```bash { output_lines = "2-3" }
   docker run --rm -it -v "$PWD:/work" alif-rtos-starter bash
   # Output will be the Docker container prompt
   root@<CONTAINER ID>:/work#
   ```

   [OPTIONAL] If you already have an existing container:
   - Get the existing CONTAINER ID:
     ```bash { output_lines = "2-4" }
     docker ps -a
     # Output
     CONTAINER ID  IMAGE                    COMMAND      CREATED        STATUS                       PORTS  NAMES
     0123456789ab  alif-rtos-starter  "/bin/bash"  27 hours ago   Exited (255) 59 minutes ago.        container_name
     ```
   - Log in to the existing container:
     ```bash
     docker start 0123456789ab
     docker exec --rm -it -v "$PWD:/work" alif-rtos-starter bash
     ```

## Make an Arm Toolchain Build File (CMake)

1. From inside the `alif-rtos-starter` container