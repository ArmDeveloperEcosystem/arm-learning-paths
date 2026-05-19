---
title: Add Zephyr board support for Corstone-320 MPS4 platform
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Port Zephyr and run an application on Corstone-320 MPS4

###  CS320 MPS4 Platform overview

The Arm® Corstone™ SSE-320 FPGA Image for MPS4 (FI101) provides an FPGA implementation that runs on the MPS4 board. The image includes an Arm Cortex-M85 processor, an Arm Ethos-U85 NPU, and an Arm CoreLink DMA-350 direct memory access (DMA) controller. This setup provides a practical environment for developing and evaluating embedded applications, including machine learning workloads.

Download the latest Corstone-320 FPGA image and review the platform documentations:
* [Arm® Corstone™ SSE-320 with Cortex®-M85 and Ethos™-U85 : Example FPGA (FI101)](https://developer.arm.com/downloads/view/FI101)
* [SSE-320 FPGA Image for MPS4 Application Note](https://developer.arm.com/documentation/109762/0100/?lang=en) 
* [Arm® MPS4 FPGA Prototyping Board Technical Reference Manual](https://developer.arm.com/documentation/102577/latest/)
* [Arm® Corstone™ SSE-320 Example Subsystem Software Programmers Guide](https://developer.arm.com/documentation/109759/latest/)


###  Add Zephyr board support for Corstone-320 MPS4

#### Understanding Zephyr board support architecture
Zephyr organizes hardware support in a hierarchy:

```
Board → SoC → CPU Cluster → CPU Core → Architecture
```

For Corstone-320 MPS4, this hierarchy looks like:
- **Board**: `mps4` (your custom board name in Zephyr)
- **SoC**: `corstone320` (Corstone-320 subsystem)
- **CPU Cluster**: `m85` (Cortex-M85 cluster)
- **CPU Core**: Single Cortex-M85 core
- **Architecture**: ARMv8.1-M with Helium

#### Create the board directory structure

Create a board directory under boards/arm/mps4/. Use the following structure:

```
boards/arm/mps4/
├── board.yml                          # Board metadata
├── board.cmake                        # Build system integration
├── doc/                               # Optional documentation
│   ├── index.rst                      
├── Kconfig.mps4                       # Board Kconfig entry
├── Kconfig.defconfig                  # Default Kconfig settings
├── mps4_corstone320_fpga_defconfig    # Board defconfig fragment
├── mps4_corstone320_fpga.dts          # Device tree source
└── mps4_corstone320_fpga.yaml         # Test runner metadata
```

#### Add the essential board files

- board.yml
board.yml is board metadata, use board.yml to describe the board name, vendor, SoC, and variants.

```
board:
  name: mps4
  full_name: MPS4
  vendor: arm
  socs:
  - name: 'corstone320'
    variants:
    - name: 'fpga'
```

- mps4_corstone320_fpga.dts

The device tree describes the Corstone-320 MPS4 hardware. Base on the content on [SSE-320 FPGA Image for MPS4 Application Note](https://developer.arm.com/documentation/109762/0100/?lang=en) and tailor it to the peripherals and memory map you use.

The following example shows a device tree that defines memory regions and enables UART and Ethos-U:


```dts
/dts-v1/;

#include <arm/armv8.1-m.dtsi>
#include <zephyr/dt-bindings/i2c/i2c.h>
#include <zephyr/dt-bindings/input/input-event-codes.h>
#include <mem.h>

{
	compatible = "arm,mps4-fpga";
	#address-cells = <1>;
	#size-cells = <1>;

	chosen {
		zephyr,console = &uart0;
		zephyr,shell-uart = &uart0;
		zephyr,sram = &sram;
		zephyr,flash = &isram;
	};

	cpus {
		#address-cells = <1>;
		#size-cells = <0>;

		cpu@0 {
			device_type = "cpu";
			compatible = "arm,cortex-m85";
			reg = <0>;
			#address-cells = <1>;
			#size-cells = <1>;

			mpu: mpu@e000ed90 {
				compatible = "arm,armv8.1m-mpu";
				reg = <0xe000ed90 0x40>;
			};
		};
	};

	ethosu {
		#address-cells = <1>;
		#size-cells = <0>;
		interrupt-parent = <&nvic>;

		ethosu0: ethosu@50004000 {
			compatible = "arm,ethos-u";
			reg = <0x50004000>;
			interrupts = <16 3>;
			secure-enable;
			privilege-enable;
			status = "okay";
		};
	};

	
	itcm: itcm@10000000 {   
		compatible = "zephyr,memory-region";
		reg = <0x10000000 DT_SIZE_K(32)>;
		zephyr,memory-region = "ITCM";
	};

	sram: sram@12000000 {    
		compatible = "zephyr,memory-region", "mmio-sram";
		reg = <0x12000000 DT_SIZE_M(2)>;
		zephyr,memory-region = "SRAM";
	};

	rom: rom@11000000 {
		compatible = "zephyr,memory-region";
		reg = <0x11000000 DT_SIZE_K(128)>;
		zephyr,memory-region = "ROM";
	};

	dtcm: dtcm@30000000 {    
		compatible = "zephyr,memory-region";
		reg = <0x30000000 DT_SIZE_K(32)>;
		zephyr,memory-region = "DTCM";
	};

	isram: sram@31000000 {   
		compatible = "zephyr,memory-region", "mmio-sram";
		reg = <0x31000000 DT_SIZE_M(4)>;
		zephyr,memory-region = "ISRAM";
	};


	soc {
		peripheral@50000000 {
			#address-cells = <1>;
			#size-cells = <1>;
			ranges = <0x0 0x50000000 0x10000000>;

			#include "mps4_common_soc_peripheral_fpga.dtsi"
		};
	};
};

#include "mps4_common.dtsi"
```
- mps4_common_soc_peripheral_fpga.dtsi

This file defines the SoC peripherals for the MPS4 FPGA build. The following example configures a fixed system clock and two UART instances.

```
sysclk: system-clock {
	compatible = "fixed-clock";
	clock-frequency = <50000000>;
	#clock-cells = <0>;
};

uart0: uart@9303000 {
	compatible = "arm,cmsdk-uart";
	reg = <0x9303000 0x1000>;
	interrupts = <34 3 49 3>;
	interrupt-names = "tx", "rx";
	clocks = <&sysclk>;
	current-speed = <115200>;
};

uart1: uart@9304000 {
	compatible = "arm,cmsdk-uart";
	reg = <0x9304000 0x1000>;
	interrupts = <36 3 35 3>;
	interrupt-names = "tx", "rx";
	clocks = <&sysclk>;
	current-speed = <115200>;
};

pinctrl: pinctrl {
	compatible = "arm,mps4-pinctrl";
	status = "okay";
};

```

- Kconfig Files

Zephyr uses Kconfig to configure build-time features. The MPS4 platform uses three Kconfig-related files:

- Kconfig.mps4
- Kconfig.defconfig
- Kconfig

Kconfig.mps4 is the base configuration, it selects the SoC series and the specific SoC variant.

```kconfig.mps4 
config BOARD_MPS4
    select SOC_SERIES_MPS4
    select SOC_MPS4_CORSTONE315 if BOARD_MPS4_CORSTONE315_FVP || BOARD_MPS4_CORSTONE315_FVP_NS
    select SOC_MPS4_CORSTONE320 if BOARD_MPS4_CORSTONE320_FVP || BOARD_MPS4_CORSTONE320_FVP_NS || BOARD_MPS4_CORSTONE320_FPGA

```

Kconfig.defconfig and Kconfig are to provide default values for features and drivers that your board requires.

```kconfig.defconfig 
if BOARD_MPS4_CORSTONE315_FVP || BOARD_MPS4_CORSTONE320_FVP || BOARD_MPS4_CORSTONE320_FPGA

config UART_INTERRUPT_DRIVEN
    default y          # 串口默认启用中断驱动

config ROMSTART_REGION_ADDRESS
    default $(dt_nodelabel_reg_addr_hex,rom)  if BOARD_MPS4_CORSTONE320_FPGA
    default $(dt_nodelabel_reg_addr_hex,itcm) 

config ROMSTART_REGION_SIZE
    default $(dt_nodelabel_reg_size_hex,rom,0,k)  if BOARD_MPS4_CORSTONE320_FPGA
    default $(dt_nodelabel_reg_size_hex,itcm,0,k)

```

The mps4_corstone320_fpga_defconfig file is a Kconfig fragment that Zephyr merges into the final .config when you build an application for this board. The following example enables TrustZone, MPU support, GPIO, and console over UART, and it builds a Secure image that relocates the ROM start region.

```kconfig
CONFIG_RUNTIME_NMI=y
CONFIG_ARM_TRUSTZONE_M=y
CONFIG_ARM_MPU=y

# GPIOs
CONFIG_GPIO=y

# Serial
CONFIG_CONSOLE=y
CONFIG_UART_CONSOLE=y
CONFIG_SERIAL=y

# Build a Secure firmware image
CONFIG_TRUSTED_EXECUTION_SECURE=y
# ROMSTART_REGION address and size are defined in Kconfig.defconfig
CONFIG_ROMSTART_RELOCATION_ROM=y

``` 

