---
title: Flash and run on hardware
weight: 8
layout: learningpathall
---

## Overview

This section covers programming the Alif Ensemble E8 DevKit using J-Link and SETOOLS, viewing debug output via UART, and verifying successful deployment.

## Prerequisites

### Hardware Setup

Ensure you have:
- ✅ Alif E8 DevKit connected via PRG USB port
- ✅ Serial terminal configured for UART debugging (optional)
- ✅ SW4 switch position noted (SEUART for flashing, UART2 for debug)

### Software Requirements

Verify tools are installed:

```bash
JLinkExe --version    # Should show 7.94+
app-write-mram -d     # Should detect your silicon
```

## Memory Map Reference

| Region | Address | Size | Purpose |
|--------|---------|------|---------|
| MRAM | 0x80000000 | 5.5 MB (E7) / 2 MB (E8) | Non-volatile code storage |
| SRAM0 | 0x02000000 | 4 MB | General-purpose data |
| SRAM1 | 0x08000000 | 4 MB | NPU-accessible memory |
| ITCM | 0x00000000 | 256 KB | Fast instruction memory |
| DTCM | 0x20000000 | 256 KB | Fast data memory |

## Method 1: J-Link Direct (Recommended for Development)

J-Link loads binaries directly to MRAM for quick iteration.

### Step 1: Generate Binary

From your built project:

```bash
cd ~/alif-e8-mnist-npu/alif_project

# For E7 silicon
arm-none-eabi-objcopy -O binary \
    out/executorch_mnist/E7-HE/debug/executorch_mnist.elf \
    out/executorch_mnist/E7-HE/debug/executorch_mnist.bin

# For E8 silicon
arm-none-eabi-objcopy -O binary \
    out/executorch_mnist/E8-HE/debug/executorch_mnist.elf \
    out/executorch_mnist/E8-HE/debug/executorch_mnist.bin
```

### Step 2: Create J-Link Script

Create `flash_executorch.jlink`:

```bash
# For E7 silicon
cat > flash_executorch.jlink << 'EOF'
si swd
speed 4000
device AE722F80F55D5AS_M55_HE
r
h
loadbin out/executorch_mnist/E7-HE/debug/executorch_mnist.bin, 0x80000000
r
g
exit
EOF
```

Or for E8 silicon:

```bash
cat > flash_executorch.jlink << 'EOF'
si swd
speed 4000
device AE722F80F55D5LS_M55_HE
r
h
loadbin out/executorch_mnist/E8-HE/debug/executorch_mnist.bin, 0x80000000
r
g
exit
EOF
```

### Step 3: Flash the Binary

```bash
JLinkExe -CommandFile flash_executorch.jlink
```

Expected output:
```output
SEGGER J-Link Commander V7.94
Connecting to target...
Connected to target
Reset and halt successful
Loading binary file...
Comparing flash   [100%] Done.
Erasing flash     [100%] Done.
Programming flash [100%] Done.
O.K.
Reset and run
```

## Method 2: SETOOLS (Production/Persistent)

SETOOLS writes to MRAM via the Secure Enclave, providing persistent storage.

### Step 1: Set SW4 to SEUART

Move the SW4 switch to the **SEUART** position (required for SETOOLS communication).

### Step 2: Generate TOC (Table of Contents)

Create `build-config.json`:

```bash
cat > build-config.json << 'EOF'
{
    "MRAM_TOC1": {
        "cpu0_app": {
            "file": "out/executorch_mnist/E7-HE/debug/executorch_mnist.elf",
            "core": "M55_HE",
            "flags": "0x1"
        }
    }
}
EOF
```

Generate TOC:

```bash
app-gen-toc -f build-config.json
```

### Step 3: Write to MRAM

```bash
app-write-mram -p
```

Or specify the port explicitly:

```bash
# macOS
app-write-mram -p -P /dev/cu.usbmodem*

# Linux
app-write-mram -p -P /dev/ttyACM0
```

Expected output:
```output
Device Part# AE722F80F55D5AS Rev A1
MRAM Size (KB) = 5632
Writing TOC1...
Programming M55_HE application...
Programming complete
```

## View Debug Output

### Option A: UART Serial Terminal

#### Hardware Setup

1. Connect USB-to-Serial adapter:
   - TX → P3_17 (UART2_RX)
   - RX → P3_16 (UART2_TX)
   - GND → GND

2. Set SW4 to **UART2** position

3. Reset the board (press reset button)

#### Open Serial Terminal

{{< tabpane code=true >}}
{{< tab header="macOS" language="bash" >}}
# Find serial port
ls /dev/cu.usbserial*

# Connect with picocom
picocom -b 115200 /dev/cu.usbserial-XXXX

# Or with screen
screen /dev/cu.usbserial-XXXX 115200
{{< /tab >}}
{{< tab header="Linux" language="bash" >}}
# Find serial port
ls /dev/ttyUSB*

# Connect with picocom
picocom -b 115200 /dev/ttyUSB0

# Or with minicom
minicom -D /dev/ttyUSB0 -b 115200
{{< /tab >}}
{{< tab header="Windows" language="text" >}}
Use PuTTY:
1. Select "Serial" connection type
2. Enter COM port (check Device Manager)
3. Set speed to 115200
4. Click Open
{{< /tab >}}
{{< /tabpane >}}

To exit picocom: Press `Ctrl+A` then `Ctrl+X`

#### Expected Output

```output
========================================
  ExecuTorch MNIST NPU Demo
  Alif Ensemble E8 - Cortex-M55 HE
========================================

Initializing SRAM0 power...
SRAM0 enabled successfully

Loading model (143872 bytes)...
[ET] Initializing with model (143872 bytes)
[ET] Initialized successfully

Running inference...
[ET] Running inference (input: 784 bytes, output: 10 bytes)
[ET] Inference complete

Inference completed!
Predicted digit: 7 (confidence: 78%)

Output scores:
  Digit 0: 10
  Digit 1: 10
  Digit 2: 10
  Digit 3: 10
  Digit 4: 10
  Digit 5: 10
  Digit 6: 10
  Digit 7: 100
  Digit 8: 10
  Digit 9: 10

Demo complete. System halted.
```

### Option B: RTT (Real-Time Transfer)

RTT provides debug output without additional hardware via J-Link.

#### Start RTT Server

**Terminal 1** - Start J-Link:

```bash
# For E7 silicon
JLinkExe -device AE722F80F55D5AS_M55_HE -if swd -speed 4000

# For E8 silicon
JLinkExe -device AE722F80F55D5LS_M55_HE -if swd -speed 4000
```

In J-Link console:

```
J-Link> connect
J-Link> r
J-Link> g
```

**Terminal 2** - Start RTT Client:

```bash
JLinkRTTClient
```

Debug output appears in the RTT Client terminal.

## LED Indicator Reference

Observe the RGB LED on the DevKit:

| Color | Meaning |
|-------|---------|
| Red | Initializing or error state |
| Blue | Model loaded, ready for inference |
| Green | Inference running or completed successfully |

## Verification Commands

### Check if Program is Running

Create `check_running.jlink`:

```bash
# For E7 silicon
cat > check_running.jlink << 'EOF'
si swd
speed 4000
device AE722F80F55D5AS_M55_HE
sleep 3000
h
regs
exit
EOF
```

Run the check:

```bash
JLinkExe -CommandFile check_running.jlink
```

If running normally, PC should be in valid code range (0x80xxxxxx for MRAM).

### Read Memory Contents

```bash
# For E7 silicon
cat > read_memory.jlink << 'EOF'
si swd
speed 4000
device AE722F80F55D5AS_M55_HE
h
mem32 0x80000000 16
exit
EOF

JLinkExe -CommandFile read_memory.jlink
```

## Common Issues

### "Failed to power up DAP"

**Solution:**
1. Power cycle the board (unplug USB, wait 5 seconds, replug)
2. Try connecting again
3. Set SW4 to SEUART and retry

### No Serial Output

**Solution:**
1. Verify USB-to-Serial wiring (TX ↔ RX crossover)
2. Check SW4 is set to **UART2** (not SEUART)
3. Verify baud rate is 115200
4. Press reset button on DevKit

### Program Crashes Immediately

**Solution:**
1. Verify you built for correct silicon type (E7 vs E8)
2. Check SRAM0 power is enabled in code
3. See troubleshooting section for HardFault diagnosis

### SETOOLS Cannot Detect Device

**Solution:**
1. Use **PRG USB** port (not DEBUG USB)
2. Set SW4 to **SEUART**
3. Check USB cable is not damaged
4. Verify device enumeration: `ls /dev/cu.usbmodem*` (macOS) or `ls /dev/ttyACM*` (Linux)

## Quick Reference: J-Link Scripts

### Flash and Run

```jlink
si swd
speed 4000
device AE722F80F55D5AS_M55_HE
r
h
loadbin path/to/binary.bin, 0x80000000
r
g
exit
```

### Reset Only

```jlink
si swd
speed 4000
device AE722F80F55D5AS_M55_HE
r
g
exit
```

### Halt and Inspect

```jlink
si swd
speed 4000
device AE722F80F55D5AS_M55_HE
h
regs
exit
```

## Development Workflow

Typical development iteration:

1. **Edit code** in your project
2. **Build**: `cbuild alif.csolution.yml -c executorch_mnist.debug+E7-HE --rebuild`
3. **Flash**: `JLinkExe -CommandFile flash_executorch.jlink`
4. **Set SW4** to UART2 (if using UART debugging)
5. **Open serial terminal** and press reset
6. **View output** and verify behavior
7. Repeat

## Summary

You have:
- ✅ Flashed firmware to Alif E8 using J-Link
- ✅ Configured UART debugging with serial terminal
- ✅ Viewed printf() debug output
- ✅ Verified ExecuTorch MNIST inference
- ✅ Observed LED status indicators
- ✅ Learned alternative flashing with SETOOLS

In the next section, you'll find troubleshooting guidance for common issues.
