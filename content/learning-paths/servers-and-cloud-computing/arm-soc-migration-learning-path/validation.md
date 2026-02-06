---
title: Validate migration with testing
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Validate migration using power's testing recommendations

This section guides you through validating your ARM SoC migration using the ARM SoC Migration Power's testing recommendations. The example shows Graviton to Raspberry Pi 5, but the validation approach applies to any ARM platform migration.

### Source Platform Build Verification

Ask the power to verify your source platform build:

**Example:**
```
Help me verify my Graviton build still works after adding BCM2712 support.
```

**General pattern:**
```
Help me verify my [source platform] build still works after adding [target platform] support.
```

Follow the power's guidance. Example for Graviton:

```bash
cmake -DTARGET_PLATFORM=GRAVITON -B build-graviton
cmake --build build-graviton
./build-graviton/sensor_monitor
```

### Cross-Compilation for Target Platform

Ask the power for cross-compilation guidance:

**Example:**
```
Guide me through cross-compiling for BCM2712 and deploying to Raspberry Pi 5.
```

**General pattern:**
```
Guide me through cross-compiling for [target platform] and deploying to [target device].
```

Follow the power's commands. Example for Raspberry Pi 5:

```bash
cmake -DTARGET_PLATFORM=BCM2712 -B build-bcm2712
cmake --build build-bcm2712

# Deploy to target device
scp build-bcm2712/sensor_monitor pi@raspberrypi5:~/
```

### Target Platform Testing

Ask the power for platform-specific tests:

**Example:**
```
What tests should I run on the Raspberry Pi 5 to validate the migration?
```

**General pattern:**
```
What tests should I run on [target platform] to validate the migration from [source platform]?
```

The power will recommend platform-appropriate tests. Example for Raspberry Pi 5:
- GPIO functionality tests
- SPI communication validation
- Real sensor reading verification
- Timing consistency checks

Run the application on your target platform. Example:

```bash
ssh pi@raspberrypi5
./sensor_monitor
```

### Performance Comparison

Ask the power to compare platform performance:

**Example:**
```
Compare performance between Graviton development and BCM2712 deployment.
```

**General pattern:**
```
Compare performance between [source platform] and [target platform] for my application.
```

The power will analyze platform-specific characteristics. Example analysis:
- CPU performance differences
- Memory usage comparison
- I/O timing characteristics
- Power consumption differences

## Expected Output

After completing validation, you should have:
- Validated source platform build
- Cross-compiled target platform binary
- Power-verified platform-specific tests passing
- Performance comparison report

## Key Takeaways

1. **AI-Assisted Migration is Powerful** - The ARM SoC Migration Power provides expert guidance for any ARM-to-ARM migration, with automated architecture analysis and code generation following best practices.

2. **Platform Abstraction is Essential** - HAL layers enable development on one platform while maintaining compatibility with others. The same business logic runs across different ARM SoCs.

3. **The Power Enforces Safety** - It preserves functional behavior during migration, validates architecture compatibility, and recommends proper testing strategies for your specific platforms.

4. **Workflow is Universal** - Discovery → Analysis → Planning → Implementation → Validation applies to any ARM SoC migration, whether cloud-to-edge, edge-to-edge, or cloud-to-cloud.

5. **Example is Adaptable** - While this learning path uses Graviton to Raspberry Pi 5 as an example, the same workflow applies to migrations like i.MX8 to Jetson, Raspberry Pi 4 to Pi 5, or any other ARM platform combination.
