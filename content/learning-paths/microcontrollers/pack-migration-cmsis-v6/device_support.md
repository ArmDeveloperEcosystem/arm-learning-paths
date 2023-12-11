---
title: Device support
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Supported toolchains

CMSIS v6 supports the following toolchains:

- [Arm Compiler for Embedded (v6 and above)](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded)
- [Arm GNU Toolchain (v12 and above)](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain)
- [LLVM Toolchain (v16 and above)](https://developer.arm.com/Tools%20and%20Software/LLVM%20Toolchain)
- [IAR Embedded Workbench for Arm (v9.30 and above)](https://www.iar.com/ewarm)

Before migrating your project, please make sure that you use one of these toolchains. In this learning path, you will use the Arm Compiler for Embedded v6 toolchain.

## Update the device support

To update the device support, you will need to follow the steps outlined below:

- Switch from assembly based code to [C-based startup files](#create-c-based-startup-code).
- [Create scatter files](#scatter-file-creation) to [place the stack and heap](https://developer.arm.com/documentation/101754/latest/armlink-Reference/Scatter-loading-Features/The-scatter-loading-mechanism/Placing-the-stack-and-heap-with-a-scatter-file).
- [Update the pack](#cmsis-pack-update) with the new contents.

### Create C-based startup code

In CMSIS v6, assembly-based startup code is deprecated. You must move your `startup_device.s` files to `startup_device.c`. This section explains the necessary steps.

1. Copy the `startup_ARMCMx.c` file from the [CMSIS-DFP repo](https://github.com/ARM-software/CMSIS-DFP) into your device support repo. In this example, a Cortex-M4-based device is used (and therefore, the [startup_ARMCM4.c](https://github.com/ARM-software/CMSIS-DFP/blob/main/Device/ARMCM4/Source/startup_ARMCM4.c) is taken from CMSIS-DFP/Device/ARMCM4/source).
2. Copy all the interrupt handler names and wrap them into `void handler_name (void) __attribute__ ((weak, alias("Default_Handler")));`. Place them around line 58 of the template file.

   **Code Example**
   ```asm
   ; Interrupt Handlers for Service Requests (SR) from Peripherals */
                   Entry   SCU_0_IRQHandler            ; Handler name for SR SCU_0     
                   Entry   ERU0_0_IRQHandler           ; Handler name for SR ERU0_0    
                   Entry   ERU0_1_IRQHandler           ; Handler name for SR ERU0_1    
                   Entry   ERU0_2_IRQHandler           ; Handler name for SR ERU0_2    
                   Entry   ERU0_3_IRQHandler           ; Handler name for SR ERU0_3     
                   Entry   ERU1_0_IRQHandler           ; Handler name for SR ERU1_0    
                   Entry   ERU1_1_IRQHandler           ; Handler name for SR ERU1_1    
                   Entry   ERU1_2_IRQHandler           ; Handler name for SR ERU1_2    
                   Entry   ERU1_3_IRQHandler           ; Handler name for SR ERU1_3    
                   DCD     0                           ; Not Available                 
                   DCD     0                           ; Not Available                 
                   DCD     0                           ; Not Available                 
                   Entry   PMU0_0_IRQHandler           ; Handler name for SR PMU0_0    
                   DCD     0                           ; Not Available                 
                   Entry   VADC0_C0_0_IRQHandler       ; Handler name for SR VADC0_C0_0  
                   Entry   VADC0_C0_1_IRQHandler       ; Handler name for SR VADC0_C0_1  
                   Entry   VADC0_C0_2_IRQHandler       ; Handler name for SR VADC0_C0_1  
                   Entry   VADC0_C0_3_IRQHandler       ; Handler name for SR VADC0_C0_3  
   ```
   
   Translates to:
   
   ```c
   void SCU_0_IRQHandler      (void) __attribute__ ((weak, alias("Default_Handler")));
   void ERU0_0_IRQHandler     (void) __attribute__ ((weak, alias("Default_Handler")));
   void ERU0_1_IRQHandler     (void) __attribute__ ((weak, alias("Default_Handler")));
   void ERU0_2_IRQHandler     (void) __attribute__ ((weak, alias("Default_Handler")));
   void ERU0_3_IRQHandler     (void) __attribute__ ((weak, alias("Default_Handler")));
   void ERU1_0_IRQHandler     (void) __attribute__ ((weak, alias("Default_Handler")));
   void ERU1_1_IRQHandler     (void) __attribute__ ((weak, alias("Default_Handler")));
   void ERU1_2_IRQHandler     (void) __attribute__ ((weak, alias("Default_Handler")));
   void ERU1_3_IRQHandler     (void) __attribute__ ((weak, alias("Default_Handler")));
   void PMU0_0_IRQHandler     (void) __attribute__ ((weak, alias("Default_Handler")));
   void VADC0_C0_0_IRQHandler (void) __attribute__ ((weak, alias("Default_Handler")));
   void VADC0_C0_1_IRQHandler (void) __attribute__ ((weak, alias("Default_Handler")));
   void VADC0_C0_2_IRQHandler (void) __attribute__ ((weak, alias("Default_Handler")));
   void VADC0_C0_3_IRQHandler (void) __attribute__ ((weak, alias("Default_Handler")));
   ```
3. Copy the list of names with the empty handlers to the `__VECTOR_TABLE_ATTRIBUTE` separated by commas (around line 99 in the template). Starting from the same assembly exception list as in the previous point, this translates to:
   ```c
   extern const VECTOR_TABLE_Type __VECTOR_TABLE[240];
          const VECTOR_TABLE_Type __VECTOR_TABLE[240] __VECTOR_TABLE_ATTRIBUTE = {
     (VECTOR_TABLE_Type)(&__INITIAL_SP),       /*     Initial Stack Pointer */
     Reset_Handler,                            /*     Reset Handler */
     NMI_Handler,                              /* -14 NMI Handler */
     HardFault_Handler,                        /* -13 Hard Fault Handler */
     MemManage_Handler,                        /* -12 MPU Fault Handler */
     BusFault_Handler,                         /* -11 Bus Fault Handler */
     UsageFault_Handler,                       /* -10 Usage Fault Handler */
     0,                                        /*     Reserved */
     0,                                        /*     Reserved */
     0,                                        /*     Reserved */
     0,                                        /*     Reserved */
     SVC_Handler,                              /*  -5 SVC Handler */
     DebugMon_Handler,                         /*  -4 Debug Monitor Handler */
     0,                                        /*     Reserved */
     PendSV_Handler,                           /*  -2 PendSV Handler */
     SysTick_Handler,                          /*  -1 SysTick Handler */
   
     /* Interrupts */
     SCU_0_IRQHandler,
     ERU0_0_IRQHandler,
     ERU0_1_IRQHandler,
     ERU0_2_IRQHandler,
     ERU0_3_IRQHandler,
     ERU1_0_IRQHandler,
     ERU1_1_IRQHandler,
     ERU1_2_IRQHandler,
     ERU1_3_IRQHandler,
     0,
     0,
     0,
     PMU0_0_IRQHandler,
     0,
     VADC0_C0_0_IRQHandler,
     VADC0_C0_1_IRQHandler,
     VADC0_C0_2_IRQHandler,
     VADC0_C0_3_IRQHandler
     /* Further interrupts are left out */
   };
   ```
4. Make sure that additional functions (`boot code`, for example) are implemented in C.
5. If you have conditional assembly, replace it with conditional compilation:

   **Code Example**
   ```asm
   IF (USE_CHIP=SOME_CHIP)
     DCD  WDT_IRQHandler
   ELSE
     DCD  _RESERVED
   ENDIF
   ```
   
   Translates to:
   
   ```c
   #if (USE_CHIP=SOME_CHIP)
   WDT_IRQHandler,
   #else
   0,
   #endif
   ```
6. Save your new `startup_device.c` file. If you have entries for stack and heap size in the assembly startup file, save these and add them in the next step to the now mandatory scatter file.

### Scatter file creation

1. Copy the scatter file template from the CMSIS-DFP repo into your device support repo. The scatter file template for the Cortex-M4 is called [ARMCM4_ac6.sct](https://github.com/ARM-software/Cortex_DFP/blob/main/Device/ARMCM4/Config/ARMCM4_ac6.sct).

2. Edit the template according to your device settings. These values need to be set:

```c
#define __ROM_BASE      0x00000000
#define __ROM_SIZE      0x00080000

#define __RAM_BASE      0x20000000
#define __RAM_SIZE      0x00040000

#define __STACK_SIZE    0x00000200
#define __HEAP_SIZE     0x00000C00
```

### CMSIS-Pack update

1. Make the necessary changes to your PDSC file. Replace the `startup_device.s` file with the new `startup_device.c` file and add the device's scatter file as follows:

```xml
          <!-- startup / system / scatter files -->
          <file category="sourceC"      name="path/to/startup_device.c"      version="1.0.1" attr="config"/>
          <file category="linkerScript" name="path/to/device_ac6.sct" version="1.0.0" attr="config" condition="ARMCC6"/>
```

2. Finally, create a new pack with the updated device support so that you can migrate the projects to Arm Compiler 6.
