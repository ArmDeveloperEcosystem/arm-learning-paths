# ARM SoC Migration Learning Path - Project Files

This directory contains downloadable project files for the ARM SoC Migration Learning Path.

## sensor-monitor.tar.gz

Complete sensor monitoring application for the migration tutorial.

**Contents:**
- Source code for sensor monitoring application
- Platform-specific implementations (Graviton and Raspberry Pi 5)
- Makefile for easy building
- Complete project structure

**Usage on Graviton EC2:**
```bash
wget https://github.com/ArmDeveloperEcosystem/arm-learning-paths/raw/main/content/learning-paths/servers-and-cloud-computing/arm-soc-migration-learning-path/projects/sensor-monitor.tar.gz
tar -xzf sensor-monitor.tar.gz
cd sensor-monitor
make
./sensor_monitor
```

**What's included:**
- `src/main.c` - Main application logic
- `include/sensor.h` - Sensor hardware abstraction interface
- `platform/graviton/sensor_graviton.c` - Graviton-specific implementation
- `platform/rpi5/` - Directory for Raspberry Pi 5 target (populated during migration)
- `Makefile` - Build configuration
- `README.md` - Detailed documentation

This pre-built package eliminates manual file creation and lets users focus on the migration workflow.
