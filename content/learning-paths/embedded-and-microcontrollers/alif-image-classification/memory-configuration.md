---
title: Configure memory layout and flash settings
weight: 6

layout: "learningpathall"
---

## Why memory configuration matters

The default Alif VS Code template divides memory equally between the two Cortex-M55 cores and allocates modest stack/heap sizes suitable for simple examples like Blinky. A MobileNetV2 model with ExecuTorch needs significantly more:

- The embedded model is approximately 3.7 MB (stored in MRAM/flash).
- The ExecuTorch runtime, operator libraries, and application code add another 800 KB of code.
- Inference requires approximately 7.6 MB of SRAM for memory pools and intermediate tensors.

You need to reconfigure the MRAM allocation, stack/heap sizes, and linker script to fit this workload.

## Edit the memory region configuration

Open `device/ensemble/RTE/Device/AE822FA0E5597LS0_M55_HP/app_mem_regions.h`.

Change the following values from their defaults:

| Define | Default value | New value | Purpose |
|--------|--------------|-----------|---------|
| `APP_MRAM_HE_BASE` | `0x80000000` | `0x80580000` | Move HE core out of the way |
| `APP_MRAM_HE_SIZE` | `0x00200000` | `0x00000000` | Give HE core zero MRAM |
| `APP_MRAM_HP_BASE` | `0x80200000` | `0x80000000` | HP core starts at MRAM base |
| `APP_MRAM_HP_SIZE` | `0x00200000` | `0x00580000` | HP core gets full 5.5 MB |
| `APP_HP_STACK_SIZE` | `0x00002000` | `0x00004000` | 16 KB stack (doubled) |
| `APP_HP_HEAP_SIZE` | `0x00004000` | `0x00010000` | 64 KB heap (quadrupled) |

The default template splits MRAM 2 MB / 2 MB between the two cores. Since you're only using the HP core, you give it the entire 5.5 MB of available MRAM. The increased stack and heap accommodate ExecuTorch's initialization code, which uses more stack depth and a few small dynamic allocations.

## Edit the linker script

Open `device/ensemble/RTE/Device/AE822FA0E5597LS0_M55_HP/linker_gnu_mram.ld.src`.

Make the following three changes to this file.

### Add SRAM1 to the zero-initialization table

The application code places the 4 MB planned memory pool in SRAM1. The C runtime startup code needs to zero-initialize this region. Find the `.zero.table` section:

```text
#if __HAS_BULK_SRAM
    LONG (ADDR(.bss.at_sram0))
    LONG (SIZEOF(.bss.at_sram0)/4)
#endif
```

Add two lines for SRAM1 immediately after:

```text
#if __HAS_BULK_SRAM
    LONG (ADDR(.bss.at_sram0))
    LONG (SIZEOF(.bss.at_sram0)/4)
    LONG (ADDR(.bss.at_sram1))
    LONG (SIZEOF(.bss.at_sram1)/4)
#endif
```

### Add GOT sections to the data copy table

The precompiled ExecuTorch libraries use position-independent code (PIC), which relies on a Global Offset Table (GOT). The GOT must be copied from flash to RAM at startup, otherwise the table contains zeros and every indirect function call (including C++ vtable lookups) crashes with a BusFault.

Find the `.data.at_dtcm` section:

```text
  .data.at_dtcm : ALIGN(8)
  {
    *(vtable)
    *(.data)
    *(.data*)
    *arm_common_tables*(.data* .rodata*)

    KEEP(*(.jcr*))

    . = ALIGN(8);
```

Add the GOT entries after `KEEP(*(.jcr*))`:

```text
  .data.at_dtcm : ALIGN(8)
  {
    *(vtable)
    *(.data)
    *(.data*)
    *arm_common_tables*(.data* .rodata*)

    KEEP(*(.jcr*))

    /* GOT for PIC code in precompiled ExecuTorch libraries */
    *(.got)
    *(.got.plt)

    . = ALIGN(8);
```

{{% notice Note %}}
This issue can be difficult to diagnose. Without these two lines, the firmware boots and loads the model, but crashes with a BusFault when ExecuTorch calls a virtual function. The GOT stores addresses for indirect calls. If the startup code does not copy it from flash to RAM, those lookups resolve to address zero and the CPU faults.
{{% /notice %}}

### Add SRAM section wildcards

The application code uses `__attribute__((section(".bss.at_sram0")))` to place memory pools in SRAM. The stock linker script only has specific named sections for LCD and camera buffers. You need wildcard patterns to catch the ExecuTorch pools.

Find the `.bss.at_sram0` section:

```text
  .bss.at_sram0 (NOLOAD) : ALIGN(8)
  {
    *(.bss.lcd_crop_and_interpolate_buf)
    *(.bss.lcd_frame_buf)
    *(.bss.camera_frame_buf)
    *(.bss.camera_frame_bayer_to_rgb_buf)
  } > SRAM0
#endif
```

Replace it with expanded SRAM0 wildcards and a new SRAM1 section:

```text
  .bss.at_sram0 (NOLOAD) : ALIGN(8)
  {
    *(.bss.lcd_crop_and_interpolate_buf)
    *(.bss.lcd_frame_buf)
    *(.bss.camera_frame_buf)
    *(.bss.camera_frame_bayer_to_rgb_buf)
    *(.bss.at_sram0)
    *(.bss.at_sram0.*)
  } > SRAM0

  .bss.at_sram1 (NOLOAD) : ALIGN(8)
  {
    *(.bss.at_sram1)
    *(.bss.at_sram1.*)
  } > SRAM1
#endif
```

After these changes, the memory layout is:

| Region | Size | Usage |
|--------|------|-------|
| MRAM | 5.5 MB | Code + model (~4.5 MB used) |
| ITCM | 256 KB | Fast code (~89% used) |
| DTCM | 1 MB | Stack (16 KB) + heap (64 KB) + GOT + data |
| SRAM0 | 4 MB | Method pool (1.5 MB) + temp pool (1.5 MB) + float input buffer (~588 KB) |
| SRAM1 | 4 MB | Planned memory buffers |

## Configure the flash settings

The Security Toolkit needs a JSON configuration file that tells it where to load the binary in MRAM and which CPU should boot it.

Open (or create) `.alif/M55_HP_cfg.json` and set its contents to:

```json
{
  "DEVICE": {
    "disabled" : false,
    "binary": "app-device-config.json",
    "version" : "0.5.00",
    "signed": true
  },
  "USER_APP": {
    "binary": "alif-img.bin",
    "mramAddress": "0x80000000",
    "version": "1.0.0",
    "cpu_id": "M55_HP",
    "flags": ["boot"],
    "signed": false
  }
}
```

The key fields are:
- **`mramAddress`**: must match `APP_MRAM_HP_BASE` (0x80000000) from `app_mem_regions.h`.
- **`cpu_id`**: `M55_HP` tells the bootloader to start the High-Performance core.
- **`flags: ["boot"]`**: marks this application as the boot image.

You can view the completed versions of these edited files in the [workshop repository](https://github.com/ArmDeveloperEcosystem/workshop-ethos-u) for reference.

The memory layout and flash configuration are complete. The next section covers preparing the test image.
