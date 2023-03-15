---
title: "link.ld"
weight: 4

# FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Create `link.ld`

The `link.ld` contains instructions for GCC on how to produce
a firmware executable. It contains memory addresses for flash and RAM,
size of flash and RAM, and how exactly to layout text and data sections
in the final binary.

Create a new `link.ld` file and copy/paste the following:

```
ENTRY(Reset_Handler);
MEMORY {
  flash(rx) : ORIGIN = 0x08000000, LENGTH = 2048k
  sram(rwx) : ORIGIN = 0x24000000, LENGTH = 512k  /* AXI SRAM in domain D1 */
}
_estack     = ORIGIN(sram) + LENGTH(sram);    /* stack points to end of SRAM */

SECTIONS {
  .vectors  : { KEEP(*(.isr_vector)) }  > flash
  .text     : { *(.text* .text.*) }     > flash
  .rodata   : { *(.rodata*) }           > flash

  .data : {
    _sdata = .;   /* for init_ram() */
    *(.first_data)
    *(.data SORT(.data.*))
    _edata = .;  /* for init_ram() */
  } > sram AT > flash
  _sidata = LOADADDR(.data);

  .bss : {
    _sbss = .;              /* for init_ram() */
    *(.bss SORT(.bss.*) COMMON)
    _ebss = .;              /* for init_ram() */
  } > sram

  . = ALIGN(8);
  _end = .;     /* for cmsis_gcc.h and init_ram() */
}
```

Note: for the STM32F4 Nucleo board, change the MEMORY part to be like this:

```
  flash(rx) : ORIGIN = 0x08000000, LENGTH = 2048k
  sram(rwx) : ORIGIN = 0x20000000, LENGTH = 192k  /* remaining 64k in a separate address space */
```

Note: the the STM32F7 Nucleo board, change the Memory part to be like this:

```
  flash(rx) : ORIGIN = 0x08000000, LENGTH = 1024k
  sram(rwx) : ORIGIN = 0x20000000, LENGTH = 320k
```
