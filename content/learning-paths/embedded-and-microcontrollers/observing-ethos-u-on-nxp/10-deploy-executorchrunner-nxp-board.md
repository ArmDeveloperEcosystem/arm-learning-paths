---
title: Deploy and test on FRDM-IMX93
weight: 11

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Connect to the FRDM-IMX93 board

The FRDM-IMX93 board runs Linux on the Cortex-A55 cores. You need network or serial access to deploy the firmware.

Find your board's IP address using the serial console or check your router's DHCP leases.

Connect via SSH:

{{< tabpane code=false >}}
{{< tab header="Windows/Linux" >}}
```bash
ssh root@192.168.1.24
```

Alternative with PuTTY on Windows:
- Host: `192.168.1.24`
- Port: `22`
- Connection type: SSH
- Username: `root`
{{< /tab >}}
{{< tab header="macOS" >}}
```bash
ssh root@192.168.1.24
```
{{< /tab >}}
{{< /tabpane >}}

Replace `192.168.1.24` with your board's IP address.

## Copy the firmware to the board

Copy the built firmware file to the board's firmware directory:

{{< tabpane code=false >}}
{{< tab header="Windows/Linux" >}}
```bash
scp debug/executorch_runner_cm33.elf root@192.168.1.24:/lib/firmware/
```
{{< /tab >}}
{{< tab header="macOS" >}}
```bash
scp debug/executorch_runner_cm33.elf root@192.168.1.24:/lib/firmware/
```
{{< /tab >}}
{{< /tabpane >}}

Verify the file was copied:

```bash { command_line="root@frdm-imx93" output_lines="2" }
ls -lh /lib/firmware/executorch_runner_cm33.elf
-rw-r--r-- 1 root root 601K Oct 24 10:30 /lib/firmware/executorch_runner_cm33.elf
```

## Load the firmware on Cortex-M33

The Cortex-M33 firmware is managed by the RemoteProc framework running on Linux.

Stop any currently running firmware:

```bash { command_line="root@frdm-imx93" }
echo stop > /sys/class/remoteproc/remoteproc0/state
```

Set the new firmware:

```bash { command_line="root@frdm-imx93" }
echo executorch_runner_cm33.elf > /sys/class/remoteproc/remoteproc0/firmware
```

Start the Cortex-M33 with the new firmware:

```bash { command_line="root@frdm-imx93" }
echo start > /sys/class/remoteproc/remoteproc0/state
```

Verify the firmware loaded successfully:

```bash { command_line="root@frdm-imx93" output_lines="2-5" }
dmesg | grep remoteproc | tail -n 5
[12345.678] remoteproc remoteproc0: powering up imx-rproc
[12345.679] remoteproc remoteproc0: Booting fw image executorch_runner_cm33.elf, size 614984
[12345.680] remoteproc remoteproc0: header-less resource table
[12345.681] remoteproc remoteproc0: remote processor imx-rproc is now up
```

The message "remote processor imx-rproc is now up" confirms successful loading.

## Load a model to DDR memory

The executor_runner loads `.pte` model files from DDR memory at address 0x80100000.

Copy your `.pte` model to the board:

{{< tabpane code=false >}}
{{< tab header="Windows/Linux" >}}
```bash
scp model.pte root@192.168.1.24:/tmp/
```
{{< /tab >}}
{{< tab header="macOS" >}}
```bash
scp model.pte root@192.168.1.24:/tmp/
```
{{< /tab >}}
{{< /tabpane >}}

Write the model to DDR memory:

```bash { command_line="root@frdm-imx93" }
dd if=/tmp/model.pte of=/dev/mem bs=1M seek=2049
```

The seek value of 2049 corresponds to address 0x80100000 (2049 MB = 0x801 in hex).

Verify the model was written:

```bash { command_line="root@frdm-imx93" output_lines="2-5" }
xxd -l 64 -s 0x80100000 /dev/mem
80100000: 504b 0304 1400 0000 0800 0000 2100 a3b4  PK..........!...
80100010: 7d92 5801 0000 6c04 0000 1400 0000 7661  }.X...l.......va
80100020: 6c75 652f 7061 7261 6d73 2e70 6b6c 6500  lue/params.pkl.
80100030: ed52 cd4b 0241 1cfd 66de 49b6 9369 1ad9  .R.K.A..f.I..i..
```

Non-zero bytes confirm the model is present in memory.

## Monitor Cortex-M33 output

The executor_runner outputs debug information via UART. Connect a USB-to-serial adapter to the M33 UART pins on the FRDM board.

Open a serial terminal (115200 baud, 8N1):

{{< tabpane code=false >}}
{{< tab header="Windows/Linux" >}}
```bash
screen /dev/ttyUSB0 115200
```

Alternative with minicom:
```bash
minicom -D /dev/ttyUSB0 -b 115200
```
{{< /tab >}}
{{< tab header="macOS" >}}
```bash
screen /dev/tty.usbserial-* 115200
```

Alternative with minicom:
```bash
minicom -D /dev/tty.usbserial-* -b 115200
```
{{< /tab >}}
{{< /tabpane >}}

You should see output from the ExecuTorch runtime:

```output
ExecuTorch Runtime Starting...
Loading model from 0x80100000
Model loaded successfully
Initializing Ethos-U NPU delegate
NPU initialized
Running inference...
Inference complete: 45.2ms
```

{{% notice Tip %}}
If you don't see UART output, verify the serial connection settings (115200 baud, 8N1) and check that the UART pins are correctly connected.
{{% /notice %}}

## Test inference

The executor_runner automatically runs inference when it starts. Check the UART output for inference results and timing.

To restart inference, you can reload the firmware:

```bash { command_line="root@frdm-imx93" }
echo stop > /sys/class/remoteproc/remoteproc0/state
echo start > /sys/class/remoteproc/remoteproc0/state
```

Monitor the UART console to see the new inference run.

## Verify deployment success

Confirm your deployment is working correctly:

1. **RemoteProc status shows "running":**

```bash { command_line="root@frdm-imx93" output_lines="2" }
cat /sys/class/remoteproc/remoteproc0/state
running
```

2. **Firmware is loaded:**

```bash { command_line="root@frdm-imx93" output_lines="2" }
cat /sys/class/remoteproc/remoteproc0/firmware
executorch_runner_cm33.elf
```

3. **Model is in DDR memory** (non-zero bytes at 0x80100000)

4. **UART shows inference output** with timing information

## Troubleshooting

**RemoteProc fails to load firmware:**

Check file permissions:

```bash { command_line="root@frdm-imx93" }
chmod 644 /lib/firmware/executorch_runner_cm33.elf
```

Verify the file exists:

```bash { command_line="root@frdm-imx93" }
ls -la /lib/firmware/executorch_runner_cm33.elf
```

**Model not found error:**

Verify the model was written to memory:

```bash { command_line="root@frdm-imx93" }
xxd -l 256 -s 0x80100000 /dev/mem | head
```

If all zeros, re-run the `dd` command to write the model.

**No UART output:**

Check the serial connection:
- Baud rate: 115200
- Data bits: 8
- Parity: None
- Stop bits: 1

Try a different USB port or serial terminal program.

**Firmware crashes or hangs:**

Check kernel logs for errors:

```bash { command_line="root@frdm-imx93" }
dmesg | grep -i error | tail
```

This might indicate memory configuration issues. Reduce the memory pool sizes in `CMakeLists.txt` and rebuild.

## Update the firmware

To deploy a new version of the firmware:

1. Build the updated firmware on your development machine
2. Copy to the board: 

{{< tabpane code=false >}}
{{< tab header="Windows/Linux" >}}
```bash
scp debug/executorch_runner_cm33.elf root@<board-ip>:/lib/firmware/
```
{{< /tab >}}
{{< tab header="macOS" >}}
```bash
scp debug/executorch_runner_cm33.elf root@<board-ip>:/lib/firmware/
```
{{< /tab >}}
{{< /tabpane >}}

3. Restart RemoteProc:

```bash { command_line="root@frdm-imx93" }
echo stop > /sys/class/remoteproc/remoteproc0/state
echo start > /sys/class/remoteproc/remoteproc0/state
```

4. Monitor UART output to verify the new firmware is running
