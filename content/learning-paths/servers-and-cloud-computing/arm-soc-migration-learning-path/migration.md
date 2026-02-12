---
title: Migrate using ARM SoC Migration Power
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Use ARM SoC Migration Power for AI-guided migration

This section demonstrates how to use the ARM SoC Migration Power to migrate your application between ARM SoCs. The example shows migration from AWS Graviton to Raspberry Pi 5, but the workflow applies to any ARM-to-ARM migration.

### Initiate Migration

Open Kiro and tell the ARM SoC Migration Power about your migration. Specify your source and target platforms:

**Example prompt:**
```
I want to use the ARM SoC Migration Power to migrate my sensor monitoring 
application from AWS Graviton3 to Raspberry Pi 5 (BCM2712). The application 
currently uses simulated sensors on Graviton and needs to work with real 
GPIO and SPI hardware on the Pi 5.
```

**General pattern:**
```
I want to migrate my [application type] from [source ARM SoC] to [target ARM SoC].
The application uses [source-specific features] and needs [target-specific features].
```

### Discovery Phase

The power will prompt you for information about your platforms:

**Example for Graviton → Raspberry Pi 5:**
```
Source Platform: AWS Graviton3 (Neoverse-V1, cloud development)
Target Platform: Raspberry Pi 5 (BCM2712, Cortex-A76, edge deployment)
Hardware Requirements: GPIO for LEDs, SPI for temperature sensor
```

Then ask the power to scan your codebase:

**Example:**
```
Scan my codebase for Graviton-specific code that needs migration to BCM2712. 
Focus on sensor interfaces and any cloud-specific assumptions.
```

**General pattern:**
```
Scan my codebase for [source platform]-specific code that needs migration to [target platform].
Focus on [platform-specific features].
```

### Architecture Analysis

Ask the power to compare your source and target platforms:

**Example:**
```
Compare Graviton3 and BCM2712 architecture capabilities. What are the key 
differences I need to handle for cloud-to-edge migration?
```

**Example output for Graviton → Pi 5:**
- CPU differences (Neoverse-V1 vs Cortex-A76)
- Memory constraints (cloud 64GB+ vs edge 4-8GB)
- SIMD capabilities (SVE vs NEON)
- Peripheral requirements (none vs GPIO/SPI/I2C)

The power analyzes architecture differences for any ARM SoC pair and identifies migration challenges.

### HAL Design

Ask the power to design a Hardware Abstraction Layer for your platforms:

**Example:**
```
Help me design a HAL layer that supports both Graviton (cloud mocks) and 
BCM2712 (real hardware). I need GPIO and SPI abstraction.
```

**General pattern:**
```
Help me design a HAL layer that supports both [source platform] and [target platform].
I need [feature] abstraction.
```

The power will guide you to create platform-agnostic interfaces. Example `hal/sensor.h`:

```c
typedef struct {
    int (*init)(void);
    float (*read_temperature)(void);
    void (*cleanup)(void);
} sensor_hal_t;

extern const sensor_hal_t *sensor_hal;
```

### Implementation

Ask the power for target platform-specific implementation:

**Example:**
```
Help me refactor my sensor code for BCM2712 compatibility. Show me how to 
implement real SPI sensor communication for the Pi 5.
```

**General pattern:**
```
Help me implement [feature] for [target platform]. Show me how to [specific requirement].
```

The power will provide target platform-specific code. Example for `platform/bcm2712/sensor_bcm2712.c`:

```c
#include "hal/spi.h"

int sensor_init(void) {
    return spi_init(0, 1000000);  // SPI bus 0, 1MHz
}

float sensor_read_temperature(void) {
    uint8_t data[2];
    spi_read(data, 2);
    // Convert raw SPI data to temperature
    int16_t raw = (data[0] << 8) | data[1];
    return raw * 0.0625;  // Typical temp sensor conversion
}

void sensor_cleanup(void) {
    spi_cleanup();
}
```

### Build Configuration

Ask the power to update your build system for multi-platform support:

**Example:**
```
Update my build system for dual Graviton/BCM2712 support with proper 
platform selection and cross-compilation.
```

**General pattern:**
```
Update my build system for [source platform]/[target platform] support with proper
platform selection and cross-compilation.
```

The power will generate a platform-aware build configuration. Example `CMakeLists.txt`:

```cmake
cmake_minimum_required(VERSION 3.16)
project(sensor_monitor)

set(TARGET_PLATFORM "GRAVITON" CACHE STRING "Target Platform")
set_property(CACHE TARGET_PLATFORM PROPERTY STRINGS "GRAVITON" "BCM2712")

# Common sources
set(COMMON_SOURCES src/main.c)

# Platform-specific sources
if(TARGET_PLATFORM STREQUAL "GRAVITON")
    set(PLATFORM_SOURCES platform/graviton/sensor_graviton.c)
elseif(TARGET_PLATFORM STREQUAL "BCM2712")
    set(CMAKE_C_COMPILER aarch64-linux-gnu-gcc)
    set(PLATFORM_SOURCES 
        platform/bcm2712/sensor_bcm2712.c
        platform/bcm2712/spi_bcm2712.c)
endif()

add_executable(sensor_monitor ${COMMON_SOURCES} ${PLATFORM_SOURCES})
```

## Expected Output

After this section, you should have:
- Power-analyzed architecture differences between your source and target platforms
- Power-designed HAL interfaces that abstract platform differences
- Power-generated platform-specific code for both platforms
- Power-configured build system with platform selection

This workflow applies to any ARM SoC migration, not just Graviton to Raspberry Pi 5.
