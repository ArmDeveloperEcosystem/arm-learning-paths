---
title: "Build the Zephyr sensor application and firmware component"
description: Compile BMP280 temperature acquisition and compensation, UART telemetry, and the Linux remoteproc shutdown handshake into the M4 ELF.
weight: 4
layout: "learningpathall"
---

## Build with the Part 2 toolchain

On the Ubuntu host, reactivate the Part 2 virtual environment and verify the existing checkout:

```bash
source "$HOME/pb2-zephyr-venv/bin/activate"
cd "$HOME/pb2-zephyr-workspace/zephyr"
git describe --tags --exact-match
cat SDK_VERSION
```

Expect `v4.3.0` and `0.17.4`. Use the working Python 3.12 environment from Part 2. If creating a new environment on Ubuntu 22.04, install Python **3.12 and its matching venv package**; Part 2's example package line names Python 3.11 even though its subsequent commands invoke 3.12.

Build the new application from the west workspace:

```bash
cd "$HOME/pb2-zephyr-workspace"
export ZEPHYR_TOOLCHAIN_VARIANT=zephyr
west build -p always -b pocketbeagle_2/am6254/m4 \
  "$HOME/pb2-temperature-part3/firmware" -d build/pb2-external-temperature
file build/pb2-external-temperature/zephyr/zephyr.elf
```

On the ubuntu host, install the `arm-zephyr-eabi-readelf` tool via snap:

```bash
sudo snap install zephyr-crosstool-arm
```

The output must be a 32-bit Arm ELF for the M4. Keep it unstripped. Use your installed SDK's `arm-zephyr-eabi-readelf` to inspect sections and load segments:

```bash
arm-zephyr-eabi-readelf -S -l build/pb2-external-temperature/zephyr/zephyr.elf
```

Output should resemble:

```output
There are 34 section headers, starting at offset 0x6b6b4:

Section Headers:
  [Nr] Name              Type            Addr     Off    Size   ES Flg Lk Inf Al
  [ 0]                   NULL            00000000 000000 000000 00      0   0  0
  [ 1] rom_start         PROGBITS        00000000 000114 000140 00  AX  0   0  4
  [ 2] text              PROGBITS        00000140 000254 002fcc 00  AX  0   0  4
  [ 3] .ARM.exidx        ARM_EXIDX       0000310c 003220 000008 00  AL  2   0  4
  [ 4] initlevel         PROGBITS        00003114 003228 000038 00   A  0   0  4
  [ 5] device_area       PROGBITS        0000314c 003260 000080 00   A  0   0  4
  [ 6] gpio_driver_api_a PROGBITS        000031cc 0032e0 000024 00   A  0   0  4
  [ 7] mbox_driver_api_a PROGBITS        000031f0 003304 000014 00   A  0   0  4
  [ 8] uart_driver_api_a PROGBITS        00003204 003318 000014 00   A  0   0  4
  [ 9] tbss              NOBITS          00003218 00332c 000004 00 WAT  0   0  4
  [10] rodata            PROGBITS        00003218 00332c 000634 00   A  0   0  4
  [11] .ramfunc          PROGBITS        00030000 003c04 000000 00   W  0   0  1
  [12] datas             PROGBITS        00030000 003960 000068 00  WA  0   0  8
  [13] sw_isr_table      PROGBITS        00030068 0039c8 000200 00  WA  0   0  4
  [14] device_states     PROGBITS        00030268 003bc8 000008 00  WA  0   0  1
  [15] k_sem_area        PROGBITS        00030270 003bd0 000010 00  WA  0   0  4
  [16] .resource_table   PROGBITS        9cc00000 003be4 000010 00   A  0   0  4
  [17] .comment          PROGBITS        00000000 003c04 000020 01  MS  0   0  1
  [18] .debug_aranges    PROGBITS        00000000 003c28 000c60 00      0   0  8
  [19] .debug_info       PROGBITS        00000000 004888 02498b 00      0   0  1
  [20] .debug_abbrev     PROGBITS        00000000 029213 007b4c 00      0   0  1
  [21] .debug_line       PROGBITS        00000000 030d5f 014509 00      0   0  1
  [22] .debug_frame      PROGBITS        00000000 045268 001aec 00      0   0  4
  [23] .debug_str        PROGBITS        00000000 046d54 005f20 01  MS  0   0  1
  [24] .debug_loc        PROGBITS        00000000 04cc74 010ced 00      0   0  1
  [25] .debug_ranges     PROGBITS        00000000 05d968 002fa0 00      0   0  8
  [26] .ARM.attributes   ARM_ATTRIBUTES  00000000 060908 000032 00      0   0  1
  [27] .last_section     PROGBITS        00003acc 003be0 000004 00  WA  0   0  4
  [28] bss               NOBITS          00030280 003be8 000289 00  WA  0   0  8
  [29] noinit            NOBITS          00030510 003be8 001140 00  WA  0   0  8
  [30] .resource_table   PROGBITS        9cc00010 003bf4 000010 00  WA  0   0  4
  [31] .symtab           SYMTAB          00000000 06093c 005440 10     32 551  4
  [32] .strtab           STRTAB          00000000 065d7c 0057c9 00      0   0  1
  [33] .shstrtab         STRTAB          00000000 06b545 00016f 00      0   0  1
Key to Flags:
  W (write), A (alloc), X (execute), M (merge), S (strings), I (info),
  L (link order), O (extra OS processing required), G (group), T (TLS),
  C (compressed), x (unknown), o (OS specific), E (exclude),
  y (purecode), p (processor specific)

Elf file type is EXEC (Executable file)
Entry point 0xf49
There are 7 program headers, starting at offset 52

Program Headers:
  Type           Offset   VirtAddr   PhysAddr   FileSiz MemSiz  Flg Align
  EXIDX          0x003220 0x0000310c 0x0000310c 0x00008 0x00008 R   0x4
  LOAD           0x000114 0x00000000 0x00000000 0x0384c 0x0384c RWE 0x4
  LOAD           0x003960 0x00030000 0x0000384c 0x00280 0x00280 RW  0x8
  LOAD           0x003be0 0x00003acc 0x00003acc 0x00004 0x00004 RW  0x4
  LOAD           0x000000 0x00030280 0x00030280 0x00000 0x013d0 RW  0x8
  LOAD           0x003be4 0x9cc00000 0x9cc00000 0x00020 0x00020 RW  0x4
  TLS            0x00332c 0x00003218 0x00003218 0x00000 0x00004 R   0x4

 Section to Segment mapping:
  Segment Sections...
   00     .ARM.exidx 
   01     rom_start text .ARM.exidx initlevel device_area gpio_driver_api_area mbox_driver_api_area uart_driver_api_area rodata 
   02     datas sw_isr_table device_states k_sem_area 
   03     .last_section 
   04     bss noinit 
   05     .resource_table .resource_table 
   06     tbss 
   ```

The SDK tool may require its full path under `zephyr-sdk-0.17.4/arm-zephyr-eabi/bin/`. Confirm a single `.resource_table` at `0x9cc00000`, with size 16 bytes and inclusion in a loadable segment. The app supplies a version-one table with zero entries; UART is the telemetry transport, so no RPMsg device is advertised. Its custom linker fragment uses the board's existing `RSC_TABLE` region and does not enable OpenAMP's resource-table generator. Never deploy `zephyr.bin` in place of the ELF.

## Inspect acquisition and telemetry

First, lets ensure we have a good serial terminal program on our ubuntu host:

```bash
sudo apt install gtkterm
```

Also, using the A 3.3 V logic USB-to-UART adapter from [Part 2](/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-zephyr-part2/), connect the ground (GND - black) to the pocketbeagle2's P2.22 pin. Temporarily unplug the P2.07 pin (should be jumpered to P1.32 as defined previously... we'll return the jumper when done) and temporarily connect the adapter's RX (orange) to P2.07.  Connect the adapter itself to a USB port on your Ubuntu host. 

Bring up gtkterm in the Ubuntu host desktop and connect to /dev/ACM0 (should be your pocketbeagle2) at 115200 baud.

Next, in a SSH terminal on the Ubuntu host, copy over the zephyr.elf file that we built for the temperature sensor reader:

```bash
cd "$HOME/pb2-zephyr-workspace"
scp build/pb2-external-temperature/zephyr/zephyr.elf root@192.168.7.2:/root/pb2-temperature.elf
ssh root@192.168.7.2
```

In the just opened SSH shell into your pocketbeagle2, load the temperature sensor binary to temporarily run it:

```bash
pb2-m4 load /root/pb2-temperature.elf
pb2-m4 status
```

You should see output similar to this:

```output
device=/sys/class/remoteproc/remoteproc0 name=5000000.m4fss state=running firmware=pb2-zephyr-heartbeat.elf
```

This indicates that the temperature sensor zephyr instance is running. On the Ubuntu host gtkterm app, you should also see:

```json
{"type":"pb2.external.temperature","schema":1,"seq":12,"uptime_ms":60320,"temperature_uC":25080000}
```
This indicates that the temperature sensor is properly wired and the Zephyr temperature sensor reader app is working. 

Lets shut down the Zephyr app now:

```bash
echo stop > /sys/class/remoteproc/remoteproc0/state
pb2-m4 status 
```

You should see output similar to:

```output
device=/sys/class/remoteproc/remoteproc0 name=5000000.m4fss state=offline firmware=pb2-zephyr-heartbeat.elf
```

This indicates that the Zephyr temperature sensor app has halted.

Lastly, please disconnect the P2.07 lead from your USB UART adapter and replace the jumper lead out of P1.32 back into P2.07 on your pocketbeagle2.

### What we now have operational

`firmware/app.overlay` enables MCU GPIO0 using the pinned board's P2.09/P2.11 pinctrl groups. `src/main.c` implements software I2C with external pull-ups, bounded waits, acknowledgments, and repeated START. It probes `0x76` and `0x77`, requires exactly one chip ID `0x58`, resets that BMP280, waits for calibration loading, and reads `dig_T1`, `dig_T2`, and `dig_T3` from `0x88`–`0x8d`.

Each sample triggers a forced measurement with temperature oversampling ×1 and pressure skipped (`ctrl_meas=0x21`). After completion, it reads the 20-bit temperature value at `0xfa`–`0xfc`. `src/bmp280_temperature.h` implements the [Bosch integer compensation](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp280-ds001.pdf) with wider intermediates. The 0.01 °C result is scaled into the existing integer `temperature_uC` transport field; that field does not imply microdegree measurement precision. A successful UART frame looks like (this will be jumpered):

```json
{"type":"pb2.external.temperature","schema":1,"seq":12,"uptime_ms":60320,"temperature_uC":25080000}
```

The BMP280 returns to sleep between samples, approximately five seconds apart. An identification, calibration, acquisition, or range failure emits a diagnostic and **no temperature frame**. The app retries configuration on the next interval. Sensor diagnostics and Zephyr's boot banner share the UART; the bridge validates and filters input.

## Implement actual M4 shutdown

The pinned [Linux driver](https://github.com/beagleboard/linux/blob/2eea568f445af33f3280261904bf1027b02512d8/drivers/remoteproc/ti_k3_common.c) sends mailbox `0xffffff14`, waits for acknowledgment `0xffffff15`, checks CPU WFI, and asserts reset. The Part 1 mailbox wiring uses FIFO 1 toward the M4 and FIFO 0 toward Linux. The new app registers directly with Zephyr's mailbox driver; it does not also enable an IPM/OpenAMP consumer of the same channel.

On a shutdown message, the interrupt callback wakes the main thread. The main thread finishes acquisition, requests BMP280 sleep, releases SCL/SDA, sends the acknowledgment, disables interrupts, and enters WFI. It also replies to the driver's echo request. This is the firmware support that Part 2 deliberately omitted.

## Understand the Linux firmware manager

`components/firmware_manager.py` is the first component's foreground process:

1. **Install:** validate the ELF header and stage it under `{work:path}/installed`. The M4 is not started during installation.
2. **Run:** locate exactly one M4 by the `5000000` device name, require `offline`, and hold an exclusive lock. Save an ownership record, copy the ELF to a unique SHA-256-derived filename under `/lib/firmware`, select it, and write `start` to remoteproc.
3. **Supervise:** keep running in the component unit and detect an unexpected remoteproc state.
4. **Terminate:** request `stop`, require `offline`, restore the previous firmware filename, and delete the owned ELF, staged install directory, and ownership record.

Both phases request root privileges because the manager writes remoteproc sysfs and `/lib/firmware`. The firmware is loaded into M4 memory; it does not flash the separate MSPM0. The manager does not overwrite TI's default firmware file or use the Part 2 `pb2-m4 load` helper, which was designed for a one-shot heartbeat.

On a normal restart, the manager stages the immutable artifact again if cleanup removed the installed copy. A stop failure preserves the ownership record and reports an error; it must never be hidden as successful cleanup. The later deployment page makes repeated stop/start a required hardware acceptance test.

## What you have learned

You have learned how to build the M4 ELF, check its resource table, and acquire BMP280 temperature using the sensor's factory calibration. You also understand how UART frames carry the readings and how the firmware manager and mailbox shutdown protocol allow Linux to start and stop the M4 application cleanly.
