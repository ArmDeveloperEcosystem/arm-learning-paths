---
title: Develop on source platform
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Develop application on source ARM platform

This section demonstrates developing an application on your source ARM platform. The example uses AWS Graviton as the source platform, but the principles apply to any ARM SoC migration (e.g., from Raspberry Pi 4 to Pi 5, from i.MX8 to Jetson, etc.).

The workflow keeps your development environment (Kiro IDE) local while using the Graviton instance as a test platform. This mirrors real-world scenarios where you develop locally and deploy to remote ARM systems.

### Download Application on Local Machine

Download the sensor-monitor application to your local machine where Kiro IDE is running. This allows you to inspect the code and use Kiro's migration tools.

```bash
wget https://github.com/ArmDeveloperEcosystem/arm-learning-paths/raw/main/content/learning-paths/servers-and-cloud-computing/arm-soc-migration-learning-path/projects/sensor-monitor.tar.gz
tar -xzf sensor-monitor.tar.gz
cd sensor-monitor
```

The package includes complete source code, Makefile, and platform-specific implementations.

### Upload to Graviton Instance for Testing

Transfer the application to your Graviton instance to verify it works on the source ARM platform before migration.

Upload the application to your Graviton instance:

```bash
scp -i graviton-migration-key.pem sensor-monitor.tar.gz ec2-user@$(aws ec2 describe-instances --filters "Name=tag:Name,Values=graviton-migration-source" "Name=instance-state-name,Values=running" --query 'Reservations[0].Instances[0].PublicIpAddress' --output text):~
```

### Build and Test on Graviton

Now verify the application builds and runs correctly on the Graviton platform. This establishes your baseline before migration.

SSH to your Graviton instance and build the application:

```bash
ssh -i graviton-migration-key.pem ec2-user@$(aws ec2 describe-instances --filters "Name=tag:Name,Values=graviton-migration-source" "Name=instance-state-name,Values=running" --query 'Reservations[0].Instances[0].PublicIpAddress' --output text)
```

On the Graviton instance:

```bash
tar -xzf sensor-monitor.tar.gz
cd sensor-monitor
make
./sensor_monitor
```

### Application Overview

The sensor-monitor application demonstrates a typical embedded/IoT pattern:

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

## Expected Output

You should see:
- Working application on your source ARM platform (Graviton in this example)
- Simulated sensor readings
- Validated business logic

This establishes your baseline application before migration to the target platform.
