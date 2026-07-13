---
title: Add Zephyr board support for the Arm Corstone-320 MPS4 platform
description: Add Corstone-320 MPS4 FPGA board metadata, device tree files, and Kconfig settings so Zephyr can build for the physical MPS4 board.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the Arm Corstone-320 MPS4 platform 

The Arm Corstone SSE-320 FPGA Image for MPS4 (FI101) provides an FPGA implementation that runs on the MPS4 board. The image includes an Arm Cortex-M85 processor, an Arm Ethos-U85 NPU, and an Arm CoreLink DMA-350 direct memory access (DMA) controller. With this setup, you get a practical environment for developing and evaluating embedded applications, including machine learning workloads.

Download the latest Corstone-320 FPGA image and review the platform documentation:

- [Arm Corstone SSE-320 with Cortex-M85 and Ethos-U85: Example FPGA (FI101)](https://developer.arm.com/downloads/view/FI101)
- [SSE-320 FPGA Image for MPS4 Application Note](https://developer.arm.com/documentation/109762/0100/?lang=en)
- [Arm MPS4 FPGA Prototyping Board Technical Reference Manual](https://developer.arm.com/documentation/102577/latest/)
- [Arm Corstone SSE-320 Example Subsystem Software Programmers Guide](https://developer.arm.com/documentation/109759/latest/)

## Understand Zephyr board support architecture

Zephyr organizes hardware support in the following hierarchy:

```output
Board → SoC → CPU Cluster → CPU Core → Architecture
```

For Corstone-320 MPS4, this hierarchy maps as follows:

| Level | Value | Description |
|-------|-------|-------------|
| Board | `mps4` | Board name used with `west build -b` |
| SoC | `corstone320` | Corstone-320 subsystem |
| CPU Cluster | `m85` | Cortex-M85 cluster |
| CPU Core | — | Single Cortex-M85 core |
| Architecture | — | ARMv8.1-M with Helium |

## Add files to the existing board directory

The `boards/arm/mps4/` directory already exists in the Zephyr tree with support for the Corstone-315 and Corstone-320 FVP variants. In this section, you'll add the Corstone-320 FPGA variant by modifying three existing files and creating three new ones.

Navigate to the MPS4 board directory:

```bash
cd ~/zephyrproject/zephyr/boards/arm/mps4
```

You'll modify or create the following files:

```text
boards/arm/mps4/
├── board.yml                            # Board metadata (modify)
├── Kconfig.mps4                         # Board Kconfig entry (modify)
├── Kconfig.defconfig                    # Default Kconfig settings (modify)
├── mps4_corstone320_fpga_defconfig      # Board defconfig fragment (new)
├── mps4_corstone320_fpga.dts            # Device tree source (new)
└── mps4_common_soc_peripheral_fpga.dtsi # SoC peripheral definitions (new)
```

### board.yml

`board.yml` describes the board name, vendor, SoC, and supported variants. Zephyr reads this file to recognize the board target that you pass to `west build`.

The existing `board.yml` already defines the FVP variants. Add the `fpga` variant under the `corstone320` SoC entry so the file looks like this:

```yaml
board:
  name: mps4
  full_name: MPS4
  vendor: arm
  socs:
  - name: 'corstone315'
    variants:
    - name: 'fvp'
      variants:
      - name: 'ns'
  - name: 'corstone320'
    variants:
    - name: 'fvp'
      variants:
      - name: 'ns'
    - name: 'fpga'
```

### mps4_corstone320_fpga.dts

The device tree source file describes the Corstone-320 MPS4 hardware: memory regions, CPU configuration, peripherals, and how Zephyr should use them. Use the [SSE-320 FPGA Image for MPS4 Application Note](https://developer.arm.com/documentation/109762/0100/?lang=en) as the reference for the memory map and peripheral addresses, and tailor the file to the peripherals your application needs.

Create `boards/arm/mps4/mps4_corstone320_fpga.dts` with the following content:

```dts
/dts-v1/;

#include <arm/armv8.1-m.dtsi>
#include <zephyr/dt-bindings/i2c/i2c.h>
#include <zephyr/dt-bindings/input/input-event-codes.h>
#include <mem.h>

/ {
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
### mps4_common_soc_peripheral_fpga.dtsi

This file defines the SoC peripherals for the MPS4 FPGA build and is included by `mps4_corstone320_fpga.dts`. It's not a standalone file — the `.dts` file pulls it in during compilation with `#include`.

The `boards/arm/mps4/mps4_common_soc_peripheral_fpga.dtsi` file is used to configure the 50 MHz peripheral clock and two UART instances using the MPS4 peripheral addresses from the [SSE-320 FPGA Image for MPS4 Application Note](https://developer.arm.com/documentation/109762/0100/?lang=en). Create the file with the following content:

```dts
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


### Kconfig.defconfig

`Kconfig.defconfig` sets default values for drivers and features your board needs. Zephyr merges this file with the rest of the Kconfig configuration at build time, so these values apply automatically without requiring manual configuration.

The existing `boards/arm/mps4/Kconfig.defconfig` handles the FVP variants. Replace it with the following content to add FPGA support:

```kconfig
if BOARD_MPS4_CORSTONE315_FVP || BOARD_MPS4_CORSTONE320_FVP || BOARD_MPS4_CORSTONE320_FPGA

if SERIAL

config UART_INTERRUPT_DRIVEN
	default y

endif # SERIAL

if ROMSTART_RELOCATION_ROM && (BOARD_MPS4_CORSTONE315_FVP || BOARD_MPS4_CORSTONE320_FVP)

config ROMSTART_REGION_ADDRESS
	default $(dt_nodelabel_reg_addr_hex,itcm)

config ROMSTART_REGION_SIZE
	default $(dt_nodelabel_reg_size_hex,itcm,0,k)

endif

if ROMSTART_RELOCATION_ROM && BOARD_MPS4_CORSTONE320_FPGA

config ROMSTART_REGION_ADDRESS
	default $(dt_nodelabel_reg_addr_hex,rom)

config ROMSTART_REGION_SIZE
	default $(dt_nodelabel_reg_size_hex,rom,0,k)

endif

endif
```

### Kconfig.mps4

`Kconfig.mps4` is the base software configuration for selecting SoC and other board and SoC related settings. Add the FPGA support in the file:

```kconfig
config BOARD_MPS4
        select SOC_SERIES_MPS4
        select SOC_MPS4_CORSTONE315 if BOARD_MPS4_CORSTONE315_FVP || BOARD_MPS4_CORSTONE315_FVP_NS
        select SOC_MPS4_CORSTONE320 if BOARD_MPS4_CORSTONE320_FVP || BOARD_MPS4_CORSTONE320_FVP_NS || BOARD_MPS4_CORSTONE320_FPGA
```


### mps4_corstone320_fpga_defconfig

`mps4_corstone320_fpga_defconfig` is a Kconfig fragment that Zephyr merges into the final `.config` when building for this board target. The fragment enables TrustZone, MPU support, GPIO, and console over UART. It configures the build as a secure image with ROM-region relocation.

Create `boards/arm/mps4/mps4_corstone320_fpga_defconfig` with the following content:

```kconfig
CONFIG_RUNTIME_NMI=y
CONFIG_ARM_TRUSTZONE_M=y
CONFIG_ARM_MPU=y

# GPIO
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
## What you've accomplished and what's next

You've now created and updated board support files, including device tree and Kconfig configuration, to port Zephyr RTOS to the Corstone-320 MPS4 platform.

Next, you'll build the `hello_world` sample for your new board target.