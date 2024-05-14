---
title: Using Process Watch
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Using Process Watch
Process Watch can be used to prove the presence (or absence) of certain instructions. For example consider the following simple workload
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

With no optimisation applied, I can see that the workload is not making use of NEON of SVE instructions.

```output
aarch64-linux-gnu-gcc workload.c -o workload_none -O0
./workload_none &
[1] 126958

sudo ./processwatch -p 126958 -f HasNEON -f HasSVEorSME

PID      NAME             NEON     SVEorSME %TOTAL   TOTAL
ALL      ALL              0.00     0.00     100.00   24726
126958   workload_none    0.00     0.00     100.00   24726

PID      NAME             NEON     SVEorSME %TOTAL   TOTAL
ALL      ALL              0.00     0.00     100.00   26006
126958   workload_none    0.00     0.00     100.00   26006
^C
```

However, recompiling to make use of NEON instructions, I can now see my workload is retiring NEON instructions

```output
aarch64-linux-gnu-gcc workload.c -o workload_neon  -O2 -ftree-vectorize -march=armv8.6-a
./workload_neon &
[1] 126987

sudo ./processwatch -p 126987 -f HasNEON -f HasSVEorSME

PID      NAME             NEON     SVEorSME %TOTAL   TOTAL
ALL      ALL              31.75    0.00     100.00   24828
126987   workload_neon    31.75    0.00     100.00   24828

PID      NAME             NEON     SVEorSME %TOTAL   TOTAL
ALL      ALL              32.45    0.00     100.00   26143
126987   workload_neon    32.45    0.00     100.00   26143
^C
```
And by running objdump on the binary, I can see those instructions

```output
 788:   4ee18400        add     v0.2d, v0.2d, v1.2d
 78c:   3ca06860        str     q0, [x3, x0]
 790:   91004000        add     x0, x0, #0x10
 794:   f140081f        cmp     x0, #0x2, lsl #12
 798:   54ffff41        b.ne    780 <doLoop+0x20>  // b.any
 ```

 Similarly by recompiling for SVE, I can now see my workload is retiring SVE instructions

```output
aarch64-linux-gnu-gcc workload.c -o workload_sve  -O2 -ftree-vectorize -march=armv8.5-a+sve
./workload_sve &
[1] 126997

sudo ./processwatch -p 126997 -f HasNEON -f HasSVEorSME

PID      NAME             NEON     SVEorSME %TOTAL   TOTAL
ALL      ALL              0.00     96.68    100.00   24914
126997   workload_sve     0.00     96.68    100.00   24914

PID      NAME             NEON     SVEorSME %TOTAL   TOTAL
ALL      ALL              0.00     96.74    100.00   26137
126997   workload_sve     0.00     96.74    100.00   26137
^C
```

Again, by objdumping the binary I see 
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

