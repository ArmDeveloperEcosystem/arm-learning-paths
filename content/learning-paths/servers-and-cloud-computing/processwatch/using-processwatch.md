---
title: Using Process Watch
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Using Process Watch
You can use Process Watch to determine the presence or absence of certain instructions. In this section, you will use Process Watch to detect the use of NEON and SVE instructions by this example workload. Start by saving the simple workload shown below in a file name `workload.c`:
```C
#include <stdint.h>
#define LEN 1024
uint64_t a[LEN];
uint64_t b[LEN];
uint64_t c[LEN]; 
void doLoop() {
  for (int i = 0; i < LEN; i++)
    c[i] = a[i] + b[i];
}
void main() {
  while (1)
    doLoop();
}
```
## Case 1: No optimization
Compile the workload without applying any optimizations:

```bash
aarch64-linux-gnu-gcc workload.c -o workload_none -O0
```
Now, run the workload in the background and launch `processwatch` on the workload to detect the use of NEON and SVE instructions:
```bash
./workload_none &
[1] 126958

sudo ./processwatch -p 126958 -f HasNEON -f HasSVEorSME
```
You will need to change the PID in the `processwatch` command with the PID of the workload running in the background.

The output should look like:
```output
PID      NAME             NEON     SVEorSME %TOTAL   TOTAL
ALL      ALL              0.00     0.00     100.00   24726
126958   workload_none    0.00     0.00     100.00   24726

PID      NAME             NEON     SVEorSME %TOTAL   TOTAL
ALL      ALL              0.00     0.00     100.00   26006
126958   workload_none    0.00     0.00     100.00   26006
^C
```

You can see that in this case, the workload is not making use of NEON or SVE instructions.

## Case 2: Use NEON instructions
Now recompile the same workload to make use of NEON instructions:

```bash
aarch64-linux-gnu-gcc workload.c -o workload_neon  -O2 -ftree-vectorize -march=armv8.6-a
```
Run the workload in the background and launch `processwatch` on the workload to detect the use of NEON and SVE instructions:
```bash
./workload_neon &
[1] 126987

sudo ./processwatch -p 126987 -f HasNEON -f HasSVEorSME
```
You will need to change the PID in the `processwatch` command with the PID of the workload running in the background.

The output should look like:
```output
PID      NAME             NEON     SVEorSME %TOTAL   TOTAL
ALL      ALL              31.75    0.00     100.00   24828
126987   workload_neon    31.75    0.00     100.00   24828

PID      NAME             NEON     SVEorSME %TOTAL   TOTAL
ALL      ALL              32.45    0.00     100.00   26143
126987   workload_neon    32.45    0.00     100.00   26143
^C
```
You can now see the workload is retiring NEON instructions as you would expect.

You can run `objdump` on the binary to view the disassembled NEON instructions:

```bash
objdump -S workload_neon
```
The output should look like:
```output
 788:   4ee18400        add     v0.2d, v0.2d, v1.2d
 78c:   3ca06860        str     q0, [x3, x0]
 790:   91004000        add     x0, x0, #0x10
 794:   f140081f        cmp     x0, #0x2, lsl #12
 798:   54ffff41        b.ne    780 <doLoop+0x20>  // b.any
 ```

### Case 3: Use SVE instructions
Before you run this part, make sure the Arm machine you are running on has support for SVE.

To check which features are available on your platform, use:
```bash
cat /proc/cpuinfo
```
Look at the flags values and check for presence of sve.

Recompile the workload again. This time include support for SVE instructions:

```bash
aarch64-linux-gnu-gcc workload.c -o workload_sve  -O2 -ftree-vectorize -march=armv8.5-a+sve
```
Run the workload in the background and launch `processwatch` on the workload to detect the use of NEON and SVE instructions:
```bash
./workload_sve &
[1] 126997

sudo ./processwatch -p 126997 -f HasNEON -f HasSVEorSME
```
You will need to change the PID in the `processwatch` command with the PID of the workload running in the background.

The output should look like:
```output
PID      NAME             NEON     SVEorSME %TOTAL   TOTAL
ALL      ALL              0.00     96.68    100.00   24914
126997   workload_sve     0.00     96.68    100.00   24914

PID      NAME             NEON     SVEorSME %TOTAL   TOTAL
ALL      ALL              0.00     96.74    100.00   26137
126997   workload_sve     0.00     96.74    100.00   26137
^C
```

You can see the retired SVE instructions from running this workload.

Verify the SVE instructions by using `objdump` on the binary:

```bash
objdump -S workload_sve
```
The output should look similar to:
```output
 7c4:   25e20fe0        whilelo p0.d, wzr, w2
 7c8:   a5e04080        ld1d    {z0.d}, p0/z, [x4, x0, lsl #3]
 7cc:   a5e04061        ld1d    {z1.d}, p0/z, [x3, x0, lsl #3]
 7d0:   04e10000        add     z0.d, z0.d, z1.d
 7d4:   e5e04020        st1d    {z0.d}, p0, [x1, x0, lsl #3]
 7d8:   8b050000        add     x0, x0, x5
 7dc:   25e20c00        whilelo p0.d, w0, w2
 7e0:   54ffff41        b.ne    7c8 <doLoop+0x28>  // b.any
 ```

As you can see, the Process Watch tool gives a good indication of what instructions or groups/features of the Arm architecture your workload is compiled for.
