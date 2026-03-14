---
title: Deploy and test on FRDM-IMX93
weight: 11

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This section is where the heterogeneous system comes together.
Linux on the application cores manages the lifecycle of Cortex-M33 through RemoteProc, and your Cortex-M33 firmware brings up ExecuTorch and the Ethos-U65 delegate.

Your success criteria is simple and observable: the remoteproc trace buffer shows a completed inference run with no bus errors.

## Prerequisites

Before deploying, verify the following on your FRDM-IMX93 board:

1. **Ethos-U kernel driver is loaded.** The Linux `ethosu` driver must be bound so the NPU is powered and clocked:

   ```bash { command_line="root@frdm-imx93" output_lines="2" }
   ls /dev/ethosu*
   /dev/ethosu0
   ```

   If `/dev/ethosu0` does not exist, the NPU is not powered and the firmware will hang at NPU initialization.

2. **DDR memory is reserved for the CM33.** The NXP BSP reserves two DDR regions by default:

   ```dts
   reserved-memory {
       model@c0000000 {
           reg = <0 0xc0000000 0 0x400000>;   /* 4MB for .pte model */
           no-map;
       };
       ethosu_region@A8000000 {
           reg = <0 0xa8000000 0 0x8000000>;  /* 128MB for NPU working memory */
           no-map;
       };
   };
   ```

## Copy files to the board

From the `Executorch_runner_cm33` project, copy both the firmware and the `.pte` model to the board:

```bash
scp debug/executorch_runner_cm33.elf root@<board-ip>:/lib/firmware/
scp mobilenetv2_u65.pte root@<board-ip>:/tmp/
```

## Connect to the board

SSH into the board for the remaining steps:

```bash
ssh root@<board-ip>
```

Replace `<board-ip>` with your board's actual IP address.

## Load the model to DDR

The `executor_runner` firmware reads the `.pte` model from DDR at address `0xC0000000`. Write the model into DDR using `/dev/mem`:

```bash { command_line="root@frdm-imx93" output_lines="8" }
python3 -c "
import mmap, os
pte = open('/tmp/mobilenetv2_u65.pte', 'rb').read()
fd = os.open('/dev/mem', os.O_RDWR | os.O_SYNC)
m = mmap.mmap(fd, len(pte), mmap.MAP_SHARED, mmap.PROT_WRITE, offset=0xC0000000)
m.write(pte)
m.close()
os.close(fd)
print(f'Wrote {len(pte)} bytes to 0xC0000000')
"
Wrote 3507872 bytes to 0xC0000000
```

{{% notice Note %}}
You can also load the model via U-Boot if the `.pte` file is on the SD card's first partition. At the U-Boot prompt, run `fatload mmc 0:1 0xc0000000 mobilenetv2_u65.pte` followed by `boot`. The model remains in DDR across Linux boot because the region is marked `no-map`.
{{% /notice %}}

## Run inference

Start the Cortex-M33 firmware through RemoteProc. RemoteProc is the control plane for this platform: it gives you a consistent way to stop, replace, and start the Cortex-M33 image without manually resetting the system.

```bash { command_line="root@frdm-imx93" }
echo stop > /sys/class/remoteproc/remoteproc0/state
echo executorch_runner_cm33.elf > /sys/class/remoteproc/remoteproc0/firmware
echo start > /sys/class/remoteproc/remoteproc0/state
sleep 15
cat /sys/kernel/debug/remoteproc/remoteproc0/trace0
```

{{% notice Note %}}
If no firmware is running, the `stop` command prints an error. That is expected and can be ignored.
{{% /notice %}}

## Expected output

You should see output similar to:

```output
NPU config match
NPU arch match
cmd_end_reached 0x1
bus_status_error 0x0
1 inferences finished
Output[0]: dtype=6, numel=1000, nbytes=4000
Program complete, exiting.
```

The key indicators of a successful inference run:

| Output | Meaning |
|--------|---------|
| `NPU config match` | The compiled model's NPU configuration matches the hardware |
| `NPU arch match` | The compiled model's architecture version matches the hardware |
| `cmd_end_reached 0x1` | The NPU executed all 116 operators in the command stream |
| `bus_status_error 0x0` | No AXI bus errors during NPU memory access |
| `numel=1000` | MobileNet V2 output: 1000 ImageNet classification scores (one per class) |

The model runs with uninitialized input data, so the output scores do not correspond to a real image classification. To get meaningful predictions, feed a real 224x224 RGB image as input.

{{% notice Note %}}
If the trace buffer shows `Program identifier '' != expected 'ET12'`, the `.pte` model was not loaded into DDR at `0xC0000000`. Reload the model using the steps above.
{{% /notice %}}

## Re-run inference

The `executor_runner` runs inference once when the firmware starts. To re-run, reload the firmware:

```bash { command_line="root@frdm-imx93" }
echo stop > /sys/class/remoteproc/remoteproc0/state
sleep 2
echo start > /sys/class/remoteproc/remoteproc0/state
sleep 15
cat /sys/kernel/debug/remoteproc/remoteproc0/trace0
```

The trace buffer resets at the start of each firmware load, so you always see fresh output.

## What you've accomplished and what's next

In this section:

- You used Linux RemoteProc to load and boot a custom Cortex-M33 firmware image
- You validated an end-to-end ExecuTorch inference run that delegates computation to the Ethos-U65 NPU

Next, you can iterate on `.pte` models (and measure how operator coverage and model shape affect runtime behavior) while keeping the firmware bring-up path stable.

## Update the firmware

To deploy a new version of the firmware:

1. Build the updated firmware on your development machine
2. Copy to the board:

```bash
scp debug/executorch_runner_cm33.elf root@<board-ip>:/lib/firmware/
```

3. Re-run inference on the board:

```bash { command_line="root@frdm-imx93" }
echo stop > /sys/class/remoteproc/remoteproc0/state
sleep 2
echo start > /sys/class/remoteproc/remoteproc0/state
sleep 15
cat /sys/kernel/debug/remoteproc/remoteproc0/trace0
```

## Troubleshooting

**RemoteProc fails to load firmware:**

Check that the file exists and has correct permissions:

```bash { command_line="root@frdm-imx93" }
ls -la /lib/firmware/executorch_runner_cm33.elf
chmod 644 /lib/firmware/executorch_runner_cm33.elf
```

**`Program identifier '' != expected 'ET12'`:**

The `.pte` model is not present at DDR address `0xC0000000`. Reload the model using the `/dev/mem` method or via U-Boot.

**Firmware hangs (no trace output):**

Verify the Ethos-U kernel driver is loaded:

```bash { command_line="root@frdm-imx93" }
ls /dev/ethosu*
dmesg | grep ethosu
```

If `/dev/ethosu0` does not exist, the NPU is not powered and the firmware cannot initialize it.

**Memory allocation failed for planned buffer:**

This occurs when a large model's activation tensors exceed the DTCM method allocator. The firmware automatically uses DDR for models that need more than 12KB of planned buffers. If you see this error, verify the `ethosu_region@A8000000` (128MB) is reserved in the device tree.

**BUS FAULT or vtable corruption:**

The SDK linker script patch has not been applied. Run the patch script and rebuild:

```bash
./patches/apply_patches.sh
cmake --preset debug
cmake --build debug
```

**Firmware crashes after NPU init:**

Check kernel logs:

```bash { command_line="root@frdm-imx93" }
dmesg | grep -i error | tail
```

This might indicate memory configuration issues. Verify that both DDR regions (`0xC0000000`--`0xC03FFFFF` and `0xA8000000`--`0xAFFFFFFF`) are reserved in the device tree.
