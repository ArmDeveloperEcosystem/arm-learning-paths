---
title: Add the application code
weight: 5

layout: "learningpathall"
---

## What the application code does

The application code initializes the Ethos-U85 NPU, loads the MobileNetV2 model through ExecuTorch, runs inference on an embedded test image, and prints the classification result over SEGGER RTT.

Rather than building this code line by line, you download the complete `main.cpp` from a reference repository and walk through its key sections.

## Download main.cpp

Download the working `main.cpp` from the workshop repository and place it in your project:

```bash
cd ~/alif/alif_vscode-template/mv2_runner
curl -L -o main.cpp \
  https://raw.githubusercontent.com/ArmDeveloperEcosystem/workshop-ethos-u/main/main.cpp
```

{{% notice Note %}}
If you prefer, you can clone the full repository with `git clone https://github.com/ArmDeveloperEcosystem/workshop-ethos-u.git` and copy `main.cpp` from there.
{{% /notice %}}

The following sections explain what the code does. The downloaded file is ready to build as-is.

## Fault handlers

The fault handlers (HardFault, MemManage, BusFault) print the stacked program counter and link register to SEGGER RTT when a crash occurs. This is essential for debugging on bare-metal systems where you don't have a console or operating system catching exceptions for you.

```cpp
extern "C" void Fault_Print(uint32_t *frame, uint32_t fault_type) {
    const char* names[] = {"HARDFAULT", "MEMMANAGE", "BUSFAULT"};
    SEGGER_RTT_printf(0, "*** %s ***\n", names[fault_type]);
    // ... prints CFSR, HFSR, PC, LR, R0-R3
    while (1) { __WFI(); }
}
```

If you ever see a fault message in RTT Viewer, the PC value tells you exactly which instruction caused the crash. You can cross-reference it with the `.map` file or use `arm-none-eabi-addr2line` to find the source line.

## NPU initialization

The Alif E8 has three NPUs, and you need to use the right one. The model was compiled for Ethos-U85, which is the NPU_HG (High-Grade) peripheral at base address `0x49042000`:

```cpp
static int npu_init(void) {
    if (ethosu_init(&ethos_drv,
                    (void*)NPU_HG_BASE,   // Ethos-U85
                    0, 0,                  // no fast memory
                    1, 1))                 // secure, privileged
    {
        SEGGER_RTT_printf(0, "ERROR: ethosu_init failed\n");
        return -1;
    }
    return 0;
}
```

{{% notice Note %}}
NPU_HP (at a different base address) is an Ethos-U55, not the U85. Using the wrong base address results in a product mismatch error from the NPU driver.
{{% /notice %}}

## NPU polling

The NPU_HG peripheral has no interrupt line routed to the M55_HP core's NVIC. The code works around this by overriding the `ethosu_semaphore_take()` function to poll the NPU status register directly:

```cpp
extern "C" int ethosu_semaphore_take(void *sem, uint64_t timeout) {
    struct ethosu_sem_t *s = (struct ethosu_sem_t *)sem;
    while (s->count == 0) {
        if (NPU_HG_STATUS & 0x2) {        // bit 1 = irq_raised
            ethosu_irq_handler(&ethos_drv);
        }
        __NOP();
    }
    s->count--;
    return 0;
}
```

The SysTick handler also polls this status register at 25 Hz as a backup path, and toggles the red LED so you can see the board is alive during inference.

## ExecuTorch Platform Abstraction Layer

ExecuTorch requires several platform functions to be implemented. These are thin wrappers that route logging through SEGGER RTT and use the standard library's `malloc`/`free` for the small dynamic allocations that ExecuTorch's initialization needs:

```cpp
extern "C" {
    void et_pal_init(void) {}
    ET_NORETURN void et_pal_abort(void) { __BKPT(0); while(1) {} }
    void et_pal_emit_log_message(...) {
        SEGGER_RTT_printf(0, "[%c] %s\n", (char)level, message);
    }
    void* et_pal_allocate(size_t size) { return malloc(size); }
    void et_pal_free(void* ptr) { free(ptr); }
}
```

## Memory pools

The ExecuTorch runtime uses three memory pools, placed in SRAM using linker section attributes:

```cpp
// SRAM0 (4 MB total)
__attribute__((section(".bss.at_sram0"), aligned(16)))
static uint8_t method_alloc_pool[1536 * 1024];       // 1.5 MB

__attribute__((section(".bss.at_sram0"), aligned(16)))
static uint8_t temp_alloc_pool[1536 * 1024];          // 1.5 MB

__attribute__((section(".bss.at_sram0"), aligned(16)))
static float input_float_buf[3 * 224 * 224];           // ~588 KB

// SRAM1 (4 MB total)
__attribute__((section(".bss.at_sram1"), aligned(16)))
static uint8_t planned_buffer_pool[4 * 1024 * 1024];  // 4 MB
```

The method allocator holds the loaded model graph. The temp allocator provides scratch memory for the Ethos-U backend (which needs approximately 1.44 MB). The planned buffer pool holds the intermediate tensors that ExecuTorch pre-plans at model load time.

## The inference pipeline

The `run_inference()` function handles the full pipeline from model loading to output. It starts by initializing the ExecuTorch runtime and creating a zero-copy data loader that reads the compiled `.pte` model directly from flash memory. The program is then parsed and method metadata queried to determine how much planned memory the model needs.

Memory is set up next: sub-allocations are carved from the SRAM1 pool for planned buffers, and a memory manager ties together the method, temp, and planned allocators. Once memory is in place, the `forward` method is loaded.

Before inference runs, the input tensor is prepared by converting the embedded int8 image data to float32. This is needed because the model's first operator is `quantize_per_tensor`, which expects float input. Inference then runs in three stages: the quantize operator executes on the CPU, the entire MobileNetV2 backbone runs as a single NPU command stream on the Ethos-U85, and the dequantize operator runs back on the CPU. Finally, the argmax of the 1000-class output vector gives the predicted ImageNet class.

The NPU handles the bulk of the computation. The CPU-side overhead of ExecuTorch loading, input conversion, and quantize/dequantize is small compared to the NPU workload.

The application code is in place. The next section configures the memory layout to accommodate the model and ExecuTorch runtime.
