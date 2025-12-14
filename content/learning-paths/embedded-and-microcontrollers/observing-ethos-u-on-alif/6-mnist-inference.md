---
# User change
title: "Run MNIST Inference with Ethos-U NPU"

weight: 7

# Do not modify these elements
layout: "learningpathall"
---

Now that you've verified your build environment works, you'll run the full MNIST digit classification demo using the Arm Ethos-U85 NPU.

## Understanding the MNIST Demo

The demo application:
- Classifies handwritten digits (0-9) using a TFLite model
- Runs inference on the Ethos-U85 NPU for hardware acceleration
- Outputs results via UART with LED visual feedback
- Demonstrates real-world ML inference on embedded devices

### Model Specifications

- **Model**: MNIST digit classifier
- **Format**: TFLite (TensorFlow Lite)
- **Size**: 14 KB (quantized INT8)
- **Input**: 28x28 grayscale image
- **Output**: 10 class probabilities (digits 0-9)
- **Quantization**: INT8 for optimal NPU performance

## Build the MNIST Demo

The MNIST demo uses the same build process as the RTT Hello World:

```bash
cd alif-e8-mnist-npu/alif_project
cbuild alif.csolution.yml -c blinky.debug+E8-HE --rebuild
```

## Flash the MNIST Firmware

Flash using the same JLink procedure:

```bash
JLinkExe -device Cortex-M55 -if SWD -speed 4000 -autoconnect 1 -CommandFile flash_mnist.jlink
```

Or create a `flash_mnist.jlink` script with:

```
r
h
loadfile out/blinky/E8-HE/debug/blinky.elf
SetPC 0x800007C0
w4 0xE000ED08 0x80000000
g
exit
```

## Monitor UART Output

### Find the Correct Baud Rate

The project includes a baud rate scanner to find the correct serial settings:

```bash
./scan_baud.sh
```

Or connect manually:

```bash
screen /dev/cu.usbserial-XXXX 115200
```

Replace `/dev/cu.usbserial-XXXX` with your USB-TTL device name.

### Expected UART Output

When the demo runs, you'll see:

```output
========================================
  MNIST NPU - Alif E8
========================================
[SYS] Board initialized
[SYS] UART2 @ 115200
[LED] RGB initialized
[LED] Startup
[MODEL] Size: 14336 bytes
[MODEL] Test digit: 7
[TEST] Running 10 tests...

--- Test 1/10 ---
[INF] Scores: 0:-50 1:-50 2:-50 3:-50 4:-50 5:-50 6:-50 7:100 8:-50 9:-50
[RES] Pred:7 Exp:7 -> PASS

--- Test 2/10 ---
[INF] Scores: 0:-50 1:-50 2:-50 3:100 4:-50 5:-50 6:-50 7:-50 8:-50 9:-50
[RES] Pred:3 Exp:3 -> PASS

...

========================================
  RESULTS: 10/10 passed
========================================
[SYS] All PASSED - Green LED
[SYS] Heartbeat started
[HB] 10
[HB] 20
```

## Understanding the Output

**Inference Scores:**
- Each digit (0-9) gets a confidence score
- Scores range from -50 to 100
- Highest score indicates the predicted digit
- Example: `7:100` means 100% confidence it's a 7

**Results:**
- `Pred:7` - Model prediction
- `Exp:7` - Expected (ground truth) value
- `PASS` - Correct prediction
- `FAIL` - Incorrect prediction

## LED Status Indicators

The RGB LED provides visual feedback during inference:

| LED Color/Pattern | Meaning |
|-------------------|---------|
| White flash (startup) | Board initialized |
| Blue solid | Processing inference |
| Green blink | Correct prediction |
| Red blink | Incorrect prediction |
| Binary display | Shows predicted digit (R=bit0, G=bit1, B=bit2) |
| Blue blink (1 Hz) | Heartbeat when idle |

### Binary LED Display

After inference, the RGB LED displays the predicted digit in binary:

| Digit | Binary | R | G | B |
|-------|--------|---|---|---|
| 0 | 000 | Off | Off | Off |
| 1 | 001 | Off | Off | On |
| 2 | 010 | Off | On | Off |
| 3 | 011 | Off | On | On |
| 4 | 100 | On | Off | Off |
| 5 | 101 | On | Off | On |
| 6 | 110 | On | On | Off |
| 7 | 111 | On | On | On |

## Performance Analysis

The Ethos-U85 NPU provides significant acceleration compared to CPU-only inference:

- **NPU Acceleration**: ~10-50x faster than CPU
- **Power Efficiency**: Lower power consumption per inference
- **Real-time Capable**: Suitable for real-time ML applications

{{% notice Note %}}
Exact performance depends on model complexity, quantization, and system configuration. The MNIST model is relatively small, but demonstrates the NPU's capabilities.
{{% /notice %}}

## Understanding the Code

### Main Components

The application consists of several key components:

**1. UART Driver** (`main.c:44-88`)
- UART2 at 115200 baud (100MHz clock source)
- Interrupt-driven TX with callback
- Formatted debug output

**2. LED Control** (`main.c:106-183`)
- RGB LED initialization and control
- Status indication patterns
- Binary digit display

**3. Inference Engine** (`main.c:185-208`)
- TFLite Micro integration
- Model loading and execution
- Result interpretation

**4. Main Loop** (`main.c:210-302`)
- Runs 10 inference tests
- Displays results via UART and LEDs
- Heartbeat indicator when complete

### Model Integration

The model is embedded in the firmware:

```c
#include "mnist_model_data.h"  // Contains the TFLite model array
#include "test_data.h"          // Contains test images

// Model size: 14,336 bytes
const unsigned char g_model_data[14336] = { ... };
```

## Modifying the Demo

### Change Test Images

Edit `test_data.h` to use different MNIST images:

```c
// Add your own 28x28 INT8 grayscale images
const int8_t test_image[784] = {
    0, 0, 0, ...,  // 28x28 = 784 pixels
};
```

### Adjust Inference Count

In `main.c`, change the number of test runs:

```c
#define NUM_TESTS 10  // Change to desired count
```

### Customize LED Patterns

Modify the LED control functions in `main.c` to create custom status indicators.

## Troubleshooting

**No UART output:**
- Check USB-TTL connections (GND, TX, RX)
- Verify 1.8V logic level converter
- Try different baud rates with `scan_baud.sh`
- Check TX/RX pins aren't swapped

**Garbled UART output:**
- Baud rate mismatch - use `scan_baud.sh`
- Check clock configuration in code
- Verify USB-TTL voltage level (must be 1.8V)

**Inference fails:**
- Model may not fit in memory
- Check TFLite Micro integration
- Verify NPU is properly initialized
- Review memory configuration

**LED doesn't show expected pattern:**
- Check RGB LED pin configuration
- Verify GPIO initialization
- Test with simple on/off patterns first

## Next Steps

You've successfully:
- ✅ Set up the Alif E8 development environment
- ✅ Built and flashed embedded firmware
- ✅ Run ML inference on the Ethos-U85 NPU
- ✅ Monitored results via UART and LEDs

To learn more about creating your own TinyML models and deploying them to Arm-based devices, see:

- [Introduction to TinyML on Arm using PyTorch and ExecuTorch](/learning-paths/embedded-and-microcontrollers/introduction-to-tinyml-on-arm/)
- [Visualize Ethos-U NPU performance with ExecuTorch on Arm FVPs](/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/)
