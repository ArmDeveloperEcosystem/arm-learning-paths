---
title: Develop on source platform
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Develop application on the source Arm platform

In this section, you will build and validate the application on the source Arm platform before performing any migration steps.

This example uses AWS Graviton3 as the source platform. The same principles apply to any Arm-to-Arm migration scenario, such as Raspberry Pi 4 to Raspberry Pi 5 or i.MX8 to Jetson.

### Download the application (local machine)

Download the `sensor-monitor` application to your local machine (where Kiro IDE is installed). You inspect the project locally, then build and validate it on the Graviton3 instance.

```bash
wget https://github.com/ArmDeveloperEcosystem/arm-learning-paths/raw/main/content/learning-paths/servers-and-cloud-computing/arm-soc-migration-learning-path/projects/sensor-monitor.tar.gz
tar -xzf sensor-monitor.tar.gz
cd sensor-monitor
```

The archive includes the complete source code, a Makefile, and platform-specific implementations. You will analyze and migrate this code using the Arm SoC Migration Power.

### Upload to the Graviton instance for testing

Before migrating, verify that the application builds and runs correctly on the source Arm platform.

Upload the archive to the Graviton instance:

```bash
scp -i graviton-migration-key.pem sensor-monitor.tar.gz ec2-user@$(aws ec2 describe-instances --filters "Name=tag:Name,Values=graviton-migration-source" "Name=instance-state-name,Values=running" --query 'Reservations[0].Instances[0].PublicIpAddress' --output text):~
```

### Build and test on Graviton

Connect to the instance:

```bash
ssh -i graviton-migration-key.pem ec2-user@$(aws ec2 describe-instances --filters "Name=tag:Name,Values=graviton-migration-source" "Name=instance-state-name,Values=running" --query 'Reservations[0].Instances[0].PublicIpAddress' --output text)
```

Build the application on the Graviton instance:

```bash
tar -xzf sensor-monitor.tar.gz
cd sensor-monitor
make
./sensor_monitor
```

If successful, the application compiles for AArch64 using GCC and displays simulated sensor readings.

This confirms:

- The toolchain is functional
- The application builds cleanly on Arm64 Linux

This validated build becomes your migration baseline. Any functional differences after migration can be compared against this known-good state.

### Application overview

The `sensor-monitor` application demonstrates a common embedded/edge design pattern: business logic separated from platform-specific hardware interaction.

**Project Structure:**
```
sensor-monitor/
├── src/main.c                          # Main application logic
├── include/sensor.h                    # Sensor interface
├── platform/graviton/sensor_graviton.c # Graviton implementation
├── platform/rpi5/                      # Target platform (created during migration)
├── Makefile                            # Build configuration
└── README.md                           # Documentation
```

**Key components:**

`src/main.c` - Main application that reads sensor data in a loop
`include/sensor.h` - Hardware abstraction interface
`platform/graviton/sensor_graviton.c` - Simulated sensor for cloud development

## What you've accomplished and what's next

In this section:

- You built and ran the sensor-monitor application on the Graviton3 source platform
- You confirmed the toolchain and build process work correctly on Arm64 Linux
- You established your baseline for migration validation

In the next section, you'll use the Arm SoC Migration Power to analyze the codebase and migrate it to the target platform.
