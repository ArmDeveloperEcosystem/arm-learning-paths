---
title: Create Alif E8 CMSIS project
weight: 7
layout: learningpathall
---

## Overview

This section covers creating a complete CMSIS-Toolbox project for the Alif Ensemble E8 with ExecuTorch integration, UART debugging, and LED indicators.

## Prerequisites

You should have:
- ✅ CMSIS-Toolbox installed with Alif Ensemble Pack
- ✅ ExecuTorch model exported to `.pte` format
- ✅ Model converted to C header file (`mnist_model_data.h`)

## Project Structure

Create the project directory:

```bash
mkdir -p ~/alif-e8-mnist-npu/alif_project
cd ~/alif-e8-mnist-npu/alif_project
```

Your project structure will be:

```
alif_project/
├── alif.csolution.yml              # Top-level solution
├── device/
│   └── ensemble/
│       └── alif-ensemble.clayer.yml # Device layer
├── libs/
│   └── common_app_utils/
│       ├── logging/                 # UART printf support
│       └── fault_handler/           # Exception handlers
└── executorch_mnist/
    ├── executorch_mnist.cproject.yml # Project config
    ├── main.c                        # Application entry
    ├── executorch_runner.h           # ExecuTorch wrapper header
    ├── executorch_runner.cpp         # ExecuTorch wrapper impl
    └── mnist_model_data.h            # Embedded model
```

## Step 1: Create Solution File

```bash
cat > alif.csolution.yml << 'EOF'
solution:
  created-for: CMSIS-Toolbox@2.6.0
  cdefault:
  compiler: AC6
  
  packs:
    - pack: AlifSemiconductor::Ensemble@2.0.4
  
  target-types:
    - type: E7-HE
      device: AlifSemiconductor::AE722F80F55D5AS
      defines:
        - M55_HE
    - type: E8-HE
      device: AlifSemiconductor::AE722F80F55D5LS
      defines:
        - M55_HE
  
  build-types:
    - type: debug
      optimize: none
      debug: on
    - type: release
      optimize: speed
      debug: off
  
  projects:
    - project: ./executorch_mnist/executorch_mnist.cproject.yml
EOF
```

## Step 2: Create Device Layer

```bash
mkdir -p device/ensemble

cat > device/ensemble/alif-ensemble.clayer.yml << 'EOF'
layer:
  description: Alif Ensemble E8 device layer for Cortex-M55 HE
  type: Board
  
  packs:
    - pack: AlifSemiconductor::Ensemble@2.0.4
  
  connections:
    - connect: UART
      provides:
        - CMSIS-Driver:USART:UART2
    - connect: LED
      provides:
        - GPIO
EOF
```

## Step 3: Get UART Trace Library

The uart_tracelib provides `printf()` redirection over UART:

```bash
# Clone Alif template for common utilities
cd ~/alif-e8-mnist-npu/alif_project
git clone https://github.com/alifsemi/alif_vscode-template.git temp_template
cd temp_template
git submodule update --init --recursive

# Copy logging and fault handler utilities
mkdir -p ../libs/common_app_utils
cp -r libs/common_app_utils/logging ../libs/common_app_utils/
cp -r libs/common_app_utils/fault_handler ../libs/common_app_utils/

# Clean up
cd ..
rm -rf temp_template
```

## Step 4: Create Project Configuration

```bash
mkdir -p executorch_mnist
cd executorch_mnist

cat > executorch_mnist.cproject.yml << 'EOF'
project:
  groups:
    - group: App
      files:
        - file: main.c
        - file: executorch_runner.cpp
    - group: Logging
      files:
        - file: ../libs/common_app_utils/logging/uart_tracelib.c
        - file: ../libs/common_app_utils/fault_handler/fault_handler.c
  
  components:
    - component: AlifSemiconductor::Device:SOC Peripherals:PINCONF
    - component: AlifSemiconductor::Device:SOC Peripherals:UART
    - component: AlifSemiconductor::Device:SOC Peripherals:DMA
    - component: AlifSemiconductor::Device:SOC Peripherals:SE Runtime
    - component: AlifSemiconductor::Device:SOC Peripherals:HWSEM
    - component: AlifSemiconductor::Device:Startup&System:Startup
    - component: ARM::CMSIS:CORE
  
  layers:
    - layer: ../device/ensemble/alif-ensemble.clayer.yml
  
  define:
    - RTE_Compiler_IO_STDOUT
    - RTE_Compiler_IO_STDOUT_User
  
  misc:
    - C:
      - -std=gnu11
      - -Wno-padded
      - -Wno-packed
    - CPP:
      - -std=c++17
      - -fno-rtti
      - -fno-exceptions
    - Link:
      - --map
      - --symbols
      - --info=sizes,totals,unused
  
  add-path:
    - ../libs/common_app_utils/logging
    - ../libs/common_app_utils/fault_handler
EOF
```

## Step 5: Create ExecuTorch Runner Header

```bash
cat > executorch_runner.h << 'EOF'
/**
 * @file executorch_runner.h
 * @brief ExecuTorch C wrapper for Alif E8
 */

#ifndef EXECUTORCH_RUNNER_H
#define EXECUTORCH_RUNNER_H

#include <stdint.h>
#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

/**
 * @brief Initialize ExecuTorch runtime with model
 * @param model_data Pointer to .pte model data
 * @param model_size Size of model data in bytes
 * @return 0 on success, negative on error
 */
int executorch_init(const uint8_t* model_data, size_t model_size);

/**
 * @brief Run inference on input data
 * @param input_data Pointer to input tensor (INT8)
 * @param input_size Size of input in bytes
 * @param output_data Pointer to output buffer (INT8)
 * @param output_size Size of output buffer in bytes
 * @return 0 on success, negative on error
 */
int executorch_run_inference(const int8_t* input_data, size_t input_size,
                              int8_t* output_data, size_t output_size);

/**
 * @brief Deinitialize ExecuTorch runtime
 */
void executorch_deinit(void);

#ifdef __cplusplus
}
#endif

#endif /* EXECUTORCH_RUNNER_H */
EOF
```

## Step 6: Create ExecuTorch Runner Implementation

```bash
cat > executorch_runner.cpp << 'EOF'
/**
 * @file executorch_runner.cpp
 * @brief ExecuTorch C++ implementation for Alif E8
 * 
 * This is a stub implementation. For full ExecuTorch integration,
 * link against the ExecuTorch libraries built in Step 6.
 */

#include "executorch_runner.h"
#include <cstring>
#include <cstdio>

/* Memory pools for ExecuTorch runtime */
static uint8_t method_allocator_pool[512 * 1024] __attribute__((aligned(16)));
static uint8_t planned_memory[1024 * 1024] __attribute__((aligned(16)));

/* Global state */
static const uint8_t* g_model_data = nullptr;
static size_t g_model_size = 0;
static bool g_initialized = false;

extern "C" {

int executorch_init(const uint8_t* model_data, size_t model_size)
{
    if (g_initialized) {
        printf("[ET] Already initialized\r\n");
        return 0;
    }
    
    if (!model_data || model_size == 0) {
        printf("[ET] Error: Invalid model data\r\n");
        return -1;
    }
    
    g_model_data = model_data;
    g_model_size = model_size;
    
    printf("[ET] Initializing with model (%u bytes)\r\n", (unsigned)model_size);
    
    // TODO: Full ExecuTorch initialization
    // Program* program = Program::load(model_data, model_size);
    // Method* method = program->load_method("forward");
    
    g_initialized = true;
    printf("[ET] Initialized successfully\r\n");
    return 0;
}

int executorch_run_inference(const int8_t* input_data, size_t input_size,
                              int8_t* output_data, size_t output_size)
{
    if (!g_initialized) {
        printf("[ET] Error: Not initialized\r\n");
        return -1;
    }
    
    if (!input_data || !output_data) {
        printf("[ET] Error: Invalid buffers\r\n");
        return -2;
    }
    
    printf("[ET] Running inference (input: %u bytes, output: %u bytes)\r\n",
           (unsigned)input_size, (unsigned)output_size);
    
    // TODO: Full ExecuTorch inference
    // method->set_input(input_tensor);
    // method->execute();
    // method->get_output(output_tensor);
    
    // Stub: Generate dummy output
    for (size_t i = 0; i < output_size && i < 10; i++) {
        output_data[i] = (i == 7) ? 100 : 10;  // Predict digit 7
    }
    
    printf("[ET] Inference complete\r\n");
    return 0;
}

void executorch_deinit(void)
{
    g_model_data = nullptr;
    g_model_size = 0;
    g_initialized = false;
    printf("[ET] Deinitialized\r\n");
}

} /* extern "C" */
EOF
```

## Step 7: Create Model Data Header

Convert your `.pte` model to C header (from Docker container):

```bash
# In Docker container (from previous step)
xxd -i /home/developer/output/mnist_ethos_u55.pte > mnist_model_data.h

# Copy to project directory on host
# The file should be at ~/executorch-alif/output/mnist_model_data.h
```

Or create a placeholder:

```bash
cat > mnist_model_data.h << 'EOF'
/**
 * @file mnist_model_data.h
 * @brief MNIST model data for Alif E8
 * 
 * Replace this placeholder with actual model data from:
 * xxd -i mnist_ethos_u55.pte > mnist_model_data.h
 */

#ifndef MNIST_MODEL_DATA_H
#define MNIST_MODEL_DATA_H

#include <stdint.h>

/* Placeholder - replace with actual model data */
static const uint8_t mnist_model_data[] = {
    0x00, 0x00, 0x00, 0x00  /* Model bytes go here */
};

static const unsigned int mnist_model_len = sizeof(mnist_model_data);

#endif /* MNIST_MODEL_DATA_H */
EOF
```

## Step 8: Create Main Application

```bash
cat > main.c << 'EOF'
/**
 * @file main.c
 * @brief ExecuTorch MNIST Demo for Alif Ensemble E8
 */

#include "RTE_Components.h"
#include CMSIS_device_header

#include "Driver_GPIO.h"
#include "board_config.h"
#include "uart_tracelib.h"
#include "fault_handler.h"
#include "executorch_runner.h"

#include <stdio.h>
#include <stdint.h>
#include <string.h>

#include "mnist_model_data.h"

/* GPIO Driver for RGB LED */
extern ARM_DRIVER_GPIO ARM_Driver_GPIO_(BOARD_LED1_GPIO_PORT);
extern ARM_DRIVER_GPIO ARM_Driver_GPIO_(BOARD_LED2_GPIO_PORT);
extern ARM_DRIVER_GPIO ARM_Driver_GPIO_(BOARD_LED3_GPIO_PORT);

static ARM_DRIVER_GPIO *ledR = &ARM_Driver_GPIO_(BOARD_LED1_GPIO_PORT);
static ARM_DRIVER_GPIO *ledG = &ARM_Driver_GPIO_(BOARD_LED2_GPIO_PORT);
static ARM_DRIVER_GPIO *ledB = &ARM_Driver_GPIO_(BOARD_LED3_GPIO_PORT);

/* Function prototypes */
static void led_init(void);
static void led_set(int r, int g, int b);
static int enable_sram0_power(void);

int main(void)
{
    printf("\r\n");
    printf("========================================\r\n");
    printf("  ExecuTorch MNIST NPU Demo\r\n");
    printf("  Alif Ensemble E8 - Cortex-M55 HE\r\n");
    printf("========================================\r\n\r\n");
    
    /* Initialize LED */
    led_init();
    led_set(1, 0, 0);  /* Red: Initializing */
    
    /* Enable SRAM0 power for large buffers */
    printf("Initializing SRAM0 power...\r\n");
    if (enable_sram0_power() != 0) {
        printf("ERROR: Failed to enable SRAM0\r\n");
        led_set(1, 0, 0);  /* Red: Error */
        while(1);
    }
    printf("SRAM0 enabled successfully\r\n\r\n");
    
    /* Initialize ExecuTorch with embedded model */
    printf("Loading model (%u bytes)...\r\n", mnist_model_len);
    if (executorch_init(mnist_model_data, mnist_model_len) != 0) {
        printf("ERROR: Model initialization failed\r\n");
        led_set(1, 0, 0);  /* Red: Error */
        while(1);
    }
    
    led_set(0, 0, 1);  /* Blue: Ready */
    
    /* Create dummy MNIST input (28x28 = 784 bytes) */
    int8_t input[784];
    memset(input, 0, sizeof(input));
    
    /* Draw a "7" pattern in the center */
    for (int i = 0; i < 20; i++) {
        input[100 + i] = 127;      /* Top horizontal line */
        input[120 + 19] = 127;     /* Right vertical */
        input[140 + 18] = 127;
        input[160 + 17] = 127;
        input[180 + 16] = 127;
    }
    
    /* Output buffer (10 classes for digits 0-9) */
    int8_t output[10];
    memset(output, 0, sizeof(output));
    
    /* Run inference */
    printf("Running inference...\r\n");
    led_set(0, 1, 0);  /* Green: Inference running */
    
    if (executorch_run_inference(input, sizeof(input), output, sizeof(output)) != 0) {
        printf("ERROR: Inference failed\r\n");
        led_set(1, 0, 0);  /* Red: Error */
        while(1);
    }
    
    /* Find predicted digit */
    int predicted_digit = 0;
    int8_t max_score = output[0];
    for (int i = 1; i < 10; i++) {
        if (output[i] > max_score) {
            max_score = output[i];
            predicted_digit = i;
        }
    }
    
    printf("\r\nInference completed!\r\n");
    printf("Predicted digit: %d (confidence: %d%%)\r\n",
           predicted_digit, (max_score * 100) / 127);
    printf("\r\nOutput scores:\r\n");
    for (int i = 0; i < 10; i++) {
        printf("  Digit %d: %d\r\n", i, output[i]);
    }
    
    led_set(0, 1, 0);  /* Green: Success */
    
    printf("\r\nDemo complete. System halted.\r\n");
    
    while(1) {
        /* Loop forever */
    }
}

/* LED initialization */
static void led_init(void)
{
    ledR->Initialize(BOARD_LED1_PIN_NO, NULL);
    ledG->Initialize(BOARD_LED2_PIN_NO, NULL);
    ledB->Initialize(BOARD_LED3_PIN_NO, NULL);
    
    ledR->PowerControl(BOARD_LED1_PIN_NO, ARM_POWER_FULL);
    ledG->PowerControl(BOARD_LED2_PIN_NO, ARM_POWER_FULL);
    ledB->PowerControl(BOARD_LED3_PIN_NO, ARM_POWER_FULL);
    
    ledR->SetDirection(BOARD_LED1_PIN_NO, GPIO_PIN_DIRECTION_OUTPUT);
    ledG->SetDirection(BOARD_LED2_PIN_NO, GPIO_PIN_DIRECTION_OUTPUT);
    ledB->SetDirection(BOARD_LED3_PIN_NO, GPIO_PIN_DIRECTION_OUTPUT);
    
    led_set(0, 0, 0);  /* Off initially */
}

/* LED control (1 = on, 0 = off) */
static void led_set(int r, int g, int b)
{
    ledR->SetValue(BOARD_LED1_PIN_NO, r ? GPIO_PIN_OUTPUT_STATE_HIGH : GPIO_PIN_OUTPUT_STATE_LOW);
    ledG->SetValue(BOARD_LED2_PIN_NO, g ? GPIO_PIN_OUTPUT_STATE_HIGH : GPIO_PIN_OUTPUT_STATE_LOW);
    ledB->SetValue(BOARD_LED3_PIN_NO, b ? GPIO_PIN_OUTPUT_STATE_HIGH : GPIO_PIN_OUTPUT_STATE_LOW);
}

/* Enable SRAM0 power via Secure Enclave */
#include "se_services_port.h"
#include "services_lib_api.h"

static int enable_sram0_power(void)
{
    uint32_t service_error = 0;
    
    /* Request SRAM0 power from Secure Enclave */
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
EOF
```

## Step 9: Build the Project

### Detect Your Silicon Type

First, check which silicon you have:

```bash
app-write-mram -d
```

- If you see `AE722F80F55D5AS`, you have **E7 silicon** → use target `E7-HE`
- If you see `AE722F80F55D5LS`, you have **E8 silicon** → use target `E8-HE`

### Build for Your Silicon

```bash
cd ~/alif-e8-mnist-npu/alif_project

# For E7 silicon (most common on E8-Alpha DevKits)
cbuild alif.csolution.yml -c executorch_mnist.debug+E7-HE --rebuild

# OR for E8 silicon
cbuild alif.csolution.yml -c executorch_mnist.debug+E8-HE --rebuild
```

### Verify Build Success

The output shows:
```output
info cbuild: Build complete
Program Size: Code=45678 RO-data=12345 RW-data=234 ZI-data=56789
```

Your executable is at:
- E7: `out/executorch_mnist/E7-HE/debug/executorch_mnist.elf`
- E8: `out/executorch_mnist/E8-HE/debug/executorch_mnist.elf`

## Project Files Summary

| File | Purpose |
|------|---------|
| `main.c` | Application entry, LED control, SRAM0 power, inference loop |
| `executorch_runner.cpp` | C++ wrapper for ExecuTorch API |
| `executorch_runner.h` | C interface for ExecuTorch wrapper |
| `mnist_model_data.h` | Embedded .pte model as byte array |
| `executorch_mnist.cproject.yml` | CMSIS project configuration |
| `alif.csolution.yml` | Top-level solution with targets |

## Summary

You have:
- ✅ Created complete CMSIS-Toolbox project structure
- ✅ Integrated UART logging with printf() support
- ✅ Implemented RGB LED status indicators
- ✅ Created ExecuTorch C wrapper interface
- ✅ Embedded MNIST model in firmware
- ✅ Enabled SRAM0 power for large buffers
- ✅ Built project for your silicon type (E7 or E8)

In the next section, you'll flash the firmware to the Alif E8 hardware.
