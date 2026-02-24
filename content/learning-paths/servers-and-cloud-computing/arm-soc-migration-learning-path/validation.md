---
title: Validate migration with testing
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Validate migration using the Power's testing recommendations

Migration is not complete until the application is validated on both source and target platforms.

In this section, you will use the Arm SoC Migration Power's testing recommendations to:

- Verify functional correctness
- Confirm platform compatibility
- Validate hardware interaction
- Compare performance characteristics

The example shows Graviton to Raspberry Pi 5, but the validation approach applies to any Arm platform migration.

### Source platform build verification

After introducing abstraction layers and multi-platform build support, first confirm that the original platform still behaves correctly:

Example prompt:
```
Help me verify my Graviton build still works after adding BCM2712 support.
```
The general pattern for other Arm-based platforms:
```
Help me verify my [source platform] build still works after adding [target platform] support.
```

Follow the power's guidance. Example for Graviton:

```bash
cmake -DTARGET_PLATFORM=GRAVITON -B build-graviton
cmake --build build-graviton
./build-graviton/sensor_monitor
```

### Cross-compile for the target platform

Ask the Power for cross-compilation guidance:

Example prompt:
```
Guide me through cross-compiling for BCM2712 and deploying to Raspberry Pi 5.
```

The general pattern for other Arm-based platforms:
```
Guide me through cross-compiling for [target platform] and deploying to [target device].
```

Follow the Power's commands. Example for Raspberry Pi 5:

```bash
cmake -DTARGET_PLATFORM=BCM2712 -B build-bcm2712
cmake --build build-bcm2712
```
Deploy to target device:
```bash
scp build-bcm2712/sensor_monitor pi@raspberrypi5:~/
```

### Target platform functional testing

Now validate behavior on the actual hardware:

Example prompt:
```
What tests should I run on the Raspberry Pi 5 to validate the migration?
```

The general pattern for other Arm-based platforms:
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

### Performance comparison

Ask the Power to compare platform performance:

Example prompt:
```
Compare performance between Graviton development and BCM2712 deployment.
```

The general pattern for other Arm-based platforms:
```
Compare performance between [source platform] and [target platform] for my application.
```

The power will analyze platform-specific characteristics. Example analysis:
- CPU performance differences
- Memory usage comparison
- I/O timing characteristics
- Power consumption differences

## What you've accomplished

You've completed the full migration workflow: you validated the source platform build, cross-compiled for the target, ran platform-specific tests, and compared performance between Graviton3 and Raspberry Pi 5. The Arm SoC Migration Power guided each step with architecture-aware recommendations rather than generic advice.

The Discovery → Analysis → Planning → Implementation → Validation workflow you followed here applies to any Arm SoC migration, whether cloud-to-edge, edge-to-edge, or between any pair of Arm-based platforms. The HAL pattern preserves your application's business logic across different Arm SoCs so you can adapt the same codebase without starting from scratch.
