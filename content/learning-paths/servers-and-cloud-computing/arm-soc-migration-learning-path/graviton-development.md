---
title: Develop on source platform
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Develop application on the source Arm platform
In this section, you will build and validate the application on the source Arm platform before performing any migration steps.

This example uses AWS Graviton3 as the source platform, however the same principles apply to any Arm-Arm migration scenario (e.g., from Raspberry Pi 4 to Pi 5, from i.MX8 to Jetson, etc.).

Your development environment (Kiro IDE) remains local. The Graviton instance acts as the remote Arm test platform. This mirrors real-world workflows where development occurs locally and deployment targets remote Arm systems.

### Download the Application (Local Machine)

Download the `sensor-monitor` application to your local machine (where Kiro IDE is installed).

```bash
wget https://github.com/ArmDeveloperEcosystem/arm-learning-paths/raw/main/content/learning-paths/servers-and-cloud-computing/arm-soc-migration-learning-path/projects/sensor-monitor.tar.gz
tar -xzf sensor-monitor.tar.gz
cd sensor-monitor
```

The package includes the complete source code, a Makefile, and platform-specific implementations. You will analyze and migrate this code using the ARM SoC Migration Power.

### Upload to the Graviton Instance for Testing

Before migrating, verify that the application builds and runs correctly on the source Arm platform.

Upload the archive to the Graviton instance:

```bash
scp -i graviton-migration-key.pem sensor-monitor.tar.gz ec2-user@$(aws ec2 describe-instances --filters "Name=tag:Name,Values=graviton-migration-source" "Name=instance-state-name,Values=running" --query 'Reservations[0].Instances[0].PublicIpAddress' --output text):~
```

### Build and Test on Graviton

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
If successful, the application will compile with GCC (AArch64 target) and display simulated sensor readings.

This confirms:
  * The toolchain is functional
  * The application builds cleanly on Arm64 Linux
    
This state becomes your baseline reference for migration validation.

### Application Overview

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

**Key Components:**

`src/main.c` - Main application that reads sensor data in a loop
`include/sensor.h` - Hardware abstraction interface
`platform/graviton/sensor_graviton.c` - Simulated sensor for cloud development

## Expected Outcome

At this stage, you should have:
  - A working application running on the source Arm platform
  - Simulated sensor output from the Graviton instance
  - A validated baseline for functional comparison
    
You are now ready to analyze the code using the ARM SoC Migration Power and begin adapting it for the target platform (Raspberry Pi 5).

This establishes your baseline application before migration to the target platform.
