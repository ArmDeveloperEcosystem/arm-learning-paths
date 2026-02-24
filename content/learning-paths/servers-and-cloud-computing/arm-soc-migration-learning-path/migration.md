---
title: Migrate using Arm SoC Migration Power
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Use Arm SoC Migration Power for AI-guided migration

In this section you will learn how to use the Arm SoC Migration Power to migrate your application between Arm-based platforms. The example demonstrates migration from:

- **Source:** AWS Graviton3 (Neoverse-V1, Arm64 Linux, cloud deployment)
- **Target:** Raspberry Pi 5 (BCM2712, Cortex-A76, edge deployment)

However, the workflow applies to any Arm-to-Arm migration.

For each step below, an example prompt for the Graviton-to-Pi-5 scenario is provided alongside a general pattern you can adapt for other platform pairs. Being explicit in your prompts improves the quality of the Power's architectural reasoning.

### Initiate migration

Open Kiro and describe your migration clearly using the Arm SoC Migration Power.

Example prompt:
```
I want to use the Arm SoC Migration Power to migrate my sensor monitoring 
application from AWS Graviton3 to Raspberry Pi 5 (BCM2712). The application 
currently uses simulated sensors on Graviton and needs to work with real 
GPIO and SPI hardware on the Pi 5.
```

The general pattern for other Arm-based platform migrations:
```
I want to migrate my [application type] from [source Arm SoC] to [target Arm SoC].
The application uses [source-specific features] and needs [target-specific features].
```

### Discovery phase

The Power will prompt you for information about your platforms:

**Example for Graviton → Raspberry Pi 5:**
```
Source Platform: AWS Graviton3 (Neoverse-V1, cloud development)
Target Platform: Raspberry Pi 5 (BCM2712, Cortex-A76, edge deployment)
Hardware Requirements: GPIO for LEDs, SPI for temperature sensor
```
Next, instruct the Power to analyze your codebase for platform dependencies:

Example prompt:
```
Scan my codebase for Graviton-specific code that needs migration to BCM2712. 
Focus on sensor interfaces and any cloud-specific assumptions.
```

The general pattern for other Arm-based platform migrations:
```
Scan my codebase for [source platform]-specific code that needs migration to [target platform].
Focus on [platform-specific features].
```
This step ensures migration is systematic rather than ad hoc.


### Architecture analysis

Now compare the architectural characteristics of the platforms.

Example prompt:
```
Compare Graviton3 and BCM2712 architecture capabilities. What are the key 
differences I need to handle for cloud-to-edge migration?
```

For Graviton3 to Pi 5, the Power identifies key differences such as CPU architecture (Neoverse-V1 vs Cortex-A76), available memory (cloud 64 GB+ vs edge 4–8 GB), SIMD capabilities (SVE vs NEON), and peripheral requirements (none vs GPIO/SPI/I2C). The Power analyzes these differences for any Arm SoC pair and identifies the migration challenges you need to address.

### Design the Hardware Abstraction Layer (HAL)

Now formalize a platform-independent interface. Ask the Power to design a Hardware Abstraction Layer (HAL) for your platforms:

Example prompt:
```
Help me design a HAL layer that supports both Graviton (cloud mocks) and 
BCM2712 (real hardware). I need GPIO and SPI abstraction.
```

The general pattern for other Arm-based platform migrations:

```
Help me design a HAL layer that supports both [source platform] and [target platform].
I need [feature] abstraction.
```
The Power may propose a structured abstraction such as the example shown in `hal/sensor.h`:

```c
typedef struct {
    int (*init)(void);
    float (*read_temperature)(void);
    void (*cleanup)(void);
} sensor_hal_t;

extern const sensor_hal_t *sensor_hal;
```

### Implement target platform support

Now generate or refactor platform-specific code using the Power:

Example prompt:
```
Help me refactor my sensor code for BCM2712 compatibility. Show me how to 
implement real SPI sensor communication for the Pi 5.
```

The general pattern for other Arm-based platform migrations:
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

### Update the build system

Ask the Power to update your build system for multi-platform support:

Example prompt:
```
Update my build system for dual Graviton/BCM2712 support with proper 
platform selection and cross-compilation.
```

The general pattern for other Arm-based platform migrations:
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

## What you've accomplished and what's next

In this section:

- You used the Arm SoC Migration Power to analyze architecture differences between Graviton3 and BCM2712
- You designed a HAL that abstracts platform differences and preserves portability
- You generated platform-specific code for the target device
- You updated the build system for multi-platform support

In the next section, you'll validate the migration by building for both platforms and running the application on the Raspberry Pi 5.
