---
title: Troubleshoot common issues
weight: 9
layout: learningpathall
---

## Overview

This section covers common issues encountered when developing ExecuTorch applications for the Alif Ensemble E8 and their solutions.

## Build Issues

### DTCM Overflow Error

{{% notice Warning %}}
**Error:**

```output
section `.bss' will not fit in region `DTCM'
region `DTCM' overflowed by XXXXX bytes
```

**Cause:** Large buffers (ExecuTorch tensor arena, model data) are being placed in DTCM (256 KB) instead of SRAM0 (4 MB).
{{% /notice %}}

**Solution:** Modify the linker script to place `.bss.noinit` sections in SRAM0.

Edit `device/ensemble/RTE/Device/AE722F80F55D5LS_M55_HE/linker_gnu_mram.ld.src`:

```ld
#if __HAS_BULK_SRAM
  .bss.at_sram0 (NOLOAD) : ALIGN(8)
  {
    *(.bss.noinit)
    *(.bss.noinit.*)
    *(.bss.tensor_arena)
    *(.bss.model_data)
  } > SRAM0
#endif
```

Also update the zero table:

```ld
.zero.table : ALIGN(4)
{
  __zero_table_start__ = .;
  LONG (ADDR(.bss))
  LONG (SIZEOF(.bss)/4)
#if __HAS_BULK_SRAM
  LONG (ADDR(.bss.at_sram0))
  LONG (SIZEOF(.bss.at_sram0)/4)
#endif
  __zero_table_end__ = .;
  . = ALIGN(16);
} > MRAM
```

**Verification:** After rebuild, check memory usage:

```bash
arm-none-eabi-size out/executorch_mnist/E7-HE/debug/executorch_mnist.elf
```

Expected output:
```output
   text    data     bss     dec     hex filename
 234860   12345   25824  273029   42a55 executorch_mnist.elf
```

The `bss` section should now be small enough for DTCM.

---

### Missing Arm Backend Error

{{% notice Warning %}}
**Error:**

```output
ImportError: No module named 'executorch.backends.arm'
```
{{% /notice %}}

**Solution:** Install the Arm backend in your Python environment:

```bash
source ~/executorch-venv/bin/activate
cd $ET_HOME
pip install -e backends/arm
```

---

### Vela Compilation Fails

{{% notice Warning %}}
**Error:**

```output
vela: error: Model is not fully quantized
```

**Cause:** Model has floating-point operations that Ethos-U doesn't support.
{{% /notice %}}

**Solution:** Ensure full INT8 quantization during export:

```bash
python3 -m examples.arm.aot_arm_compiler \
    --model_name=/path/to/model.py \
    --delegate \
    --quantize \
    --target=ethos-u55-128 \
    --output=/path/to/output.pte
```

---

### cbuild Target Not Found

{{% notice Warning %}}
**Error:**

```output
error: target-type 'E8-HE' not found
```
{{% /notice %}}

**Solution:** Verify target exists in `alif.csolution.yml`:

```yaml
target-types:
  - type: E7-HE
    device: AlifSemiconductor::AE722F80F55D5AS
```

Build with correct target:

```bash
# For E7 silicon (most common on E8-Alpha DevKits)
cbuild alif.csolution.yml -c executorch_mnist.debug+E7-HE --rebuild

# For actual E8 silicon
cbuild alif.csolution.yml -c executorch_mnist.debug+E8-HE --rebuild
```

---

## Hardware/Flashing Issues

### E7 vs E8 Silicon Confusion

{{% notice Important %}}
**Symptom:** SETOOLS shows different device than expected.

**Explanation:** The DK-E8-Alpha DevKit board may contain E7 silicon (AE722F80F55D5AS) instead of E8. This is normal for Alpha development kits.
{{% /notice %}}

**Check Your Silicon:**

```bash
app-write-mram -d
```

**Output shows:**
- **E7 silicon**: `Device Part# AE722F80F55D5AS`
- **E8 silicon**: `Device Part# AE722F80F55D5LS`

**Solution:** Always build for the detected silicon type:

```bash
# If SETOOLS shows AE722F80F55D5AS (E7)
cbuild alif.csolution.yml -c executorch_mnist.debug+E7-HE --rebuild

# If SETOOLS shows AE722F80F55D5LS (E8)
cbuild alif.csolution.yml -c executorch_mnist.debug+E8-HE --rebuild
```

---

### "Failed to power up DAP"

{{% notice Warning %}}
**Error:**

```output
****** Error: Failed to power up DAP
J-Link connection not established
```

**Cause:** Device is locked up, likely due to a HardFault or invalid code execution.
{{% /notice %}}

**Solutions (try in order):**

1. **Power cycle the board:**
   - Unplug USB-C cable
   - Wait 5 seconds
   - Replug USB-C cable

2. **Reset via J-Link:**
   ```bash
   JLinkExe -device AE722F80F55D5AS_M55_HE -if swd -speed 4000
   ```
   In J-Link console:
   ```
   J-Link> r
   J-Link> g
   J-Link> exit
   ```

3. **Set SW4 to SEUART:**
   - Move SW4 switch to SEUART position
   - Power cycle the board
   - Try flashing again

4. **Use SETOOLS recovery:**
   ```bash
   app-write-mram -p
   ```

---

### "Unknown Device" Error

{{% notice Warning %}}
**Error:**

```output
****** Error: M55_HE is unknown to this software version
```

**Cause:** J-Link software is outdated.
{{% /notice %}}

**Solution:** Update J-Link:

{{< tabpane code=true >}}
  {{< tab header="macOS" language="bash">}}
brew upgrade --cask segger-jlink
  {{< /tab >}}
  {{< tab header="Linux / Windows" language="text">}}
Download latest version from https://www.segger.com/downloads/jlink/

Required version: 7.94 or later.
  {{< /tab >}}
{{< /tabpane >}}

---

### "Target did not respond"

{{% notice Warning %}}
**Error (SETOOLS):**

```output
Target did not respond
Error: Failed to communicate with target
```
{{% /notice %}}

**Solutions:**

1. **Check USB connection:**
   - Use **PRG USB** port (not DEBUG USB)
   - Ensure cable is not damaged
   - Connect directly (not through hub)

2. **Check SW4 switch position:**
   - For SETOOLS: Set to **SEUART**
   - For UART output: Set to **UART2**

3. **Verify device enumeration:**
   ```bash
   # macOS
   ls /dev/cu.usbmodem*
   
   # Linux
   ls /dev/ttyACM*
   ```

---

### HardFault on Boot

{{% notice Warning %}}
**Symptom:** Program crashes immediately, LED doesn't light.
{{% /notice %}}

**Diagnosis:**

```bash
# Create check script
cat > check_cpu.jlink << 'EOF'
si swd
speed 4000
device AE722F80F55D5AS_M55_HE
sleep 2000
h
regs
exit
EOF

JLinkExe -CommandFile check_cpu.jlink
```

**Interpreting Results:**

If XPSR shows IPSR = 3 (HardFault):

```output
PC = 0xEFFFFFFE          <-- Invalid address (EXC_RETURN)
XPSR = 0x01000003        <-- IPSR = 3 = HardFault
```

**Common Causes and Solutions:**

| Cause | Solution |
|-------|----------|
| Wrong target | Build for correct target (E7 vs E8) |
| Memory access violation | Enable SRAM0 power before access |
| Stack overflow | Increase `__STACK_SIZE` in linker config |
| Missing vector table | Check linker script `.vectors` section |

---

## Runtime Issues

### SRAM0 Access Crashes

{{% notice Warning %}}
**Symptom:** Crash when accessing large buffers in SRAM0.

**Cause:** SRAM0 is powered off by default.
{{% /notice %}}

**Solution:** Enable SRAM0 power via Secure Enclave before any access:

```c
#include "se_services_port.h"
#include "services_lib_api.h"

int enable_sram0_power(void) {
    uint32_t service_error = 0;
    
    SERVICES_power_sram_t sram_config = {
        .sram_select = SRAM0_SEL,
        .power_enable = true
    };
    
    int32_t ret = SERVICES_power_request(&sram_config, &service_error);
    if (ret != SERVICES_REQ_SUCCESS || service_error != 0) {
        printf("SRAM0 power request failed: ret=%d, err=%u\r\n", ret, service_error);
        return -1;
    }
    
    return 0;
}

int main(void) {
    // Enable SRAM0 FIRST, before any buffer access
    if (enable_sram0_power() != 0) {
        printf("ERROR: Failed to enable SRAM0\r\n");
        while(1);
    }
    // ...
}
```

---

### Model Loading Fails

{{% notice Warning %}}
**Symptom:** `executorch_init()` returns error or hangs.
{{% /notice %}}

**Possible Causes:**

1. **Model too large for memory:**
   ```bash
   # Check model size
   ls -lh mnist_model_data.h
   
   # Ensure it fits in SRAM0 (4 MB available)
   ```

2. **Corrupted model data:**
   - Verify PTE file integrity
   - Re-export model if needed
   - Check `xxd` conversion was successful

3. **Incompatible ExecuTorch version:**
   - Ensure host export and device runtime use same ExecuTorch version
   - Both should be v1.0.0

---

### No UART Output

{{% notice Warning %}}
**Symptom:** Serial terminal shows no output after flashing.
{{% /notice %}}

**Solutions:**

1. **Check SW4 position:**
   - Must be set to **UART2** for debug output
   - Set to **SEUART** only when using SETOOLS

2. **Verify wiring:**
   - Adapter TX → DevKit RX (P3_17)
   - Adapter RX → DevKit TX (P3_16)
   - GND → GND

3. **Check baud rate:**
   - Must be 115200 in terminal software
   - Verify with: `picocom -b 115200 /dev/cu.usbserial*`

4. **Press reset button:**
   - Program may have already run
   - Reset to see boot output

---

### Inference Returns Wrong Results

{{% notice Warning %}}
**Symptom:** Model predictions are incorrect or random.
{{% /notice %}}

**Possible Causes:**

1. **Quantization mismatch:**
   - Ensure model was exported with `--quantize` flag
   - Check input data is INT8 format

2. **Input data format:**
   - MNIST expects 28×28 = 784 bytes
   - Values should be INT8 (-128 to 127)
   - Normalize input: `input[i] = (pixel_value - 128)`

3. **NPU not being used:**
   - Verify Vela compilation succeeded during export
   - Check `--delegate` flag was used
   - Review export log for "Compiling with Vela..."

---

## Debugging Tips

### Enable Verbose Logging

In `executorch_runner.cpp`, add debug prints:

```cpp
int executorch_run_inference(const int8_t* input_data, size_t input_size,
                              int8_t* output_data, size_t output_size)
{
    printf("[ET] Input: ");
    for (size_t i = 0; i < 10 && i < input_size; i++) {
        printf("%d ", input_data[i]);
    }
    printf("...\r\n");
    
    // ... inference code ...
    
    printf("[ET] Output: ");
    for (size_t i = 0; i < output_size; i++) {
        printf("%d ", output_data[i]);
    }
    printf("\r\n");
    
    return 0;
}
```

### Check Memory Layout

View memory map after build:

```bash
arm-none-eabi-nm -S -n out/executorch_mnist/E7-HE/debug/executorch_mnist.elf | grep -E "bss|data|text"
```

### Monitor Stack Usage

Add stack canary in linker script:

```ld
.stack (NOLOAD) : ALIGN(8)
{
  __stack_limit = .;
  . = . + __STACK_SIZE;
  __stack_top = .;
  PROVIDE(__stack = __stack_top);
} > DTCM
```

Check for stack corruption in code:

```c
extern uint32_t __stack_limit;
extern uint32_t __stack_top;

void check_stack(void) {
    uint32_t *sp;
    __asm__ volatile ("mov %0, sp" : "=r" (sp));
    uint32_t stack_used = (uint32_t)&__stack_top - (uint32_t)sp;
    printf("Stack used: %u / %u bytes\r\n", stack_used, __STACK_SIZE);
}
```

---

## Getting Help

If you encounter issues not covered here:

1. **Check the build log** for specific error messages
2. **Verify silicon type** matches build target
3. **Review memory usage** with `arm-none-eabi-size`
4. **Enable debug logging** in your code
5. **Use J-Link RTT** for real-time debugging
6. **Check Alif documentation** for hardware-specific issues

## Summary

Common issues and solutions:

| Issue | Quick Fix |
|-------|-----------|
| DTCM overflow | Move large buffers to SRAM0 in linker script |
| E7 vs E8 confusion | Use `app-write-mram -d` to detect silicon, build for correct target |
| Failed to power DAP | Power cycle board, set SW4 to SEUART |
| SRAM0 crashes | Enable SRAM0 power via Secure Enclave first |
| No UART output | Check SW4 is on UART2, verify wiring and baud rate |
| HardFault on boot | Check memory access, stack size, vector table |

You now have the knowledge to diagnose and fix common issues when developing ExecuTorch applications on the Alif Ensemble E8.
