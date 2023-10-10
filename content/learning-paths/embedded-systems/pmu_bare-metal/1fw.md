---
title: Add PMU support to the firmware
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## About PMU

The Performance Monitor Unit (PMU) in Armv8-A CPU provides hardware-level performance monitoring and profiling capabilities. The PMU collects hardware event counts through counters. The counters include cycle counter and event counters. It is configurable for each event counter to count specified hardware events. In addition, it is configurable for each counter to collect hardware events from workloads at various CPU Exception levels and states. This is referred to as event filtering.

A set of system registers are used for configuring PMU counters and retrieving profiling statistics. You can use [MSR](https://developer.arm.com/documentation/dui0489/i/arm-and-thumb-instructions/msr--arm-register-to-system-coprocessor-register-) to write a system register, and [MRS](https://developer.arm.com/documentation/dui0489/i/arm-and-thumb-instructions/mrs--system-coprocessor-register-to-arm-register-) to read a system register.

For more details of PMU, you can refer to the [Arm Architecture Reference Manual for A-profile architecture (ARM-ARM)](https://developer.arm.com/documentation/ddi0487/latest/?lang=en).

## About PMU library

Tools like perf use PMU to profile Linux applications running on Armv8-A CPU. However, there is not a common way to use PMU for profiling the firmware, as it runs in the bare-metal environment.

To profile the firmware with PMU, a straightforward approach is to add PMU support in the form of a library. In this learning path, we provide a PMU library as a reference implementation. This library has been verified in the Armv8.0-A CPU. You can find it in the [PMU library implementation](../4code).

In this learning path, we provide the guidance on how to add PMU support in the firmware and profile the firmware with PMU. The Trusted Firmware-A (TF-A) and U-Boot are used as example firmware.

The table below lists components of the PMU library.

File name               | Description
----------------------- | -----------------------------------------------------
`arch.h`                | System registers bit field definitions
`arch_helpers.h`        | Inline functions for system registers access (MRS/MSR)
`armv8_pmuv3_events.h`  | Structures for PMU event definitions
`armv8_pmuv3_fn.c`      | Armv8-A CPU PMU functions implementation
`armv8_pmuv3_fn.h`      | Profiling interfaces
`jevents.py`            | Python script to acquire supporting PMU events for a specified CPU and generate `armv8_pmuv3_events.c`

## Add PMU support to the firmware

First, use the following commands to create all the files listed in the table within the path `lib/pmu` in the firmware. Then, copy the implementation from [PMU library implementation](../4code). You can leave the file `armv8_pmuv3_events.c` blank for now.

``` bash
mkdir -p ${FIRMWARE_PATH}/lib/pmu
touch lib/pmu/arch.h
touch lib/pmu/arch_helpers.h
touch lib/pmu/armv8_pmuv3_events.c
touch lib/pmu/armv8_pmuv3_events.h
touch lib/pmu/armv8_pmuv3_fn.c
touch lib/pmu/armv8_pmuv3_fn.h
touch lib/pmu/jevents.py
```

Depending on the firmware you are working with, you need to make specific changes to the `Makefile` file as follows.

* TF-A

    Modify the existing `Makefile` file located in the root path of TF-A as follows.

    ``` Makefile
    BL_COMMON_SOURCES += lib/pmu/armv8_pmuv3_fn.c lib/pmu/armv8_pmuv3_events.c
    INCLUDES += -Ilib/pmu
    ```

* U-Boot

    Modify the existing `Makefile` file located in the root path of U-Boot as follows.

    ``` Makefile
    UBOOTINCLUDE += -Ilib/pmu 
    ```

    Then, create a `Makefile` file in the same directory with the PMU library. Fill the `Makefile` file as follows.

    ``` Makefile
    obj-y += armv8_pmuv3_fn.o armv8_pmuv3_events.o
    ```

After that, you can rebuild the firmware. If you build it successfully, you can move to the next section.