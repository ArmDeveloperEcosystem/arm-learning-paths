---
title: Read power from the Raspberry Pi 5 PMIC
description: Read Raspberry Pi 5 PMIC current and voltage with vcgencmd pmic_read_adc to estimate rail power and understand what the rail sum includes and excludes.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Confirm `hwmon` has no power files

Before you can measure energy per token on a Raspberry Pi board, you need a reliable way to read the power consumption. On a general-purpose Arm Linux system, such as a server or cloud instance, the standard approach is the `hwmon` interface.

The Raspberry Pi 5 doesn't expose power or current data through `hwmon`. Instead, use the onboard power management integrated circuit (PMIC). You can query it with the `vcgencmd` tool included in Raspberry Pi OS.

List the hardware monitoring sensors exposed by `hwmon` on your board to confirm that there are no power or current files:

```bash
for d in /sys/class/hwmon/hwmon*; do echo "$d $(cat $d/name): $(ls $d | grep -E '^(power|curr|in|temp|fan)[0-9]' | tr '\n' ' ')"; done
```

The output is similar to:

```output
/sys/class/hwmon/hwmon0 cpu_thermal: temp1_input
/sys/class/hwmon/hwmon1 rp1_adc: in1_input in1_raw in2_input in2_raw in3_input in3_raw in4_input in4_raw temp1_input temp1_raw
/sys/class/hwmon/hwmon2 pwmfan: fan1_input
/sys/class/hwmon/hwmon3 rpi_volt: in0_lcrit_alarm
```

The output shows a temperature sensor and an analog-to-digital converter (ADC) with voltage inputs. It also includes the fan and a voltage monitor. There are no power or current files.

## Read the PMIC ADC

Read all power rails:

```bash
vcgencmd pmic_read_adc
```

The output lists a current reading (`_A`) and a voltage reading (`_V`) for each rail.

On an idle Raspberry Pi 5, the output is similar to:

```output
 3V7_WL_SW_A current(0)=0.09271335A
   3V3_SYS_A current(1)=0.05953173A
   1V8_SYS_A current(2)=0.16102850A
  DDR_VDD2_A current(3)=0.00000000A
  DDR_VDDQ_A current(4)=0.00000000A
   1V1_SYS_A current(5)=0.17371550A
    0V8_SW_A current(6)=0.26740480A
  VDD_CORE_A current(7)=0.66082000A
   3V3_DAC_A current(17)=0.00000000A
   3V3_ADC_A current(18)=0.00042735A
   0V8_AON_A current(16)=0.00311355A
      HDMI_A current(22)=0.02588520A
 3V7_WL_SW_V volt(8)=3.70441600V
   3V3_SYS_V volt(9)=3.31096100V
   1V8_SYS_V volt(10)=1.80317300V
  DDR_VDD2_V volt(11)=1.11318600V
  DDR_VDDQ_V volt(12)=0.60732540V
   1V1_SYS_V volt(13)=1.11062200V
    0V8_SW_V volt(14)=0.80292960V
  VDD_CORE_V volt(15)=0.80693450V
   3V3_DAC_V volt(20)=3.31318300V
   3V3_ADC_V volt(21)=3.30768900V
   0V8_AON_V volt(19)=0.80117140V
      HDMI_V volt(23)=5.07056000V
     EXT5V_V volt(24)=5.06654000V
      BATT_V volt(25)=0.00085470V
```

12 rails, such as `VDD_CORE`, `0V8_SW` and `1V1_SYS`, have both a current and a voltage reading. The power of each of these rails is the current multiplied by the voltage. In the example output, `VDD_CORE` draws 0.661 A at 0.807 V, which is 0.53 W.

`VDD_CORE` is the largest rail at idle. It's the rail that changes the most when the Arm cores are busy.

## Know what the sum of the rails measures

Consider the sum of current times voltage over the rails that report both values. This value is a useful measure of how much power the system on chip and its supplies draw. It isn't the power at the wall or at the USB-C input:

- `EXT5V_V` reports only the 5 V input voltage. There's no input current reading, so the total input power isn't available.
- The losses in the PMIC regulators, the fan, and USB devices powered from the 5 V input aren't included.
- On the example 2 GB board, `DDR_VDD2_A` and `DDR_VDDQ_A` read 0 A at idle. During token generation, `DDR_VDD2` reports up to about 0.3 W, and `DDR_VDDQ` stays below 0.06 W. The idle reading of 0 A is therefore likely less than what these channels can resolve. Treat the two DDR rails as a lower bound for memory power. Check them on your own board before drawing conclusions about memory power.

Use the rail sum to compare settings on the same board, for example two thread counts or two clock frequencies. If you need the absolute input power, measure it with a USB-C power meter.

## Check how fast you can sample

Each call to `vcgencmd pmic_read_adc` takes time. Measure the read rate on your board by running 20 consecutive reads for all rails, then for a single named channel:

```bash
time (for i in $(seq 20); do vcgencmd pmic_read_adc > /dev/null; done)
time (for i in $(seq 20); do vcgencmd pmic_read_adc VDD_CORE_A > /dev/null; done)
```

The output is similar to:

```output
real	0m0.493s
user	0m0.015s
sys	0m0.001s

real	0m0.078s
user	0m0.014s
sys	0m0.001s
```

A full read of every rail takes about 25 ms, so you can sample all rails about 40 times per second. Reading one named channel is several times faster. A token-generation run of a few seconds therefore produces a few hundred samples. This is enough for a stable average.

## What you've accomplished and what's next

You can now read PMIC current and voltage on a Raspberry Pi 5, and estimate the power of each rail.

Next, you'll log the power to a file with a timestamp on every sample.
