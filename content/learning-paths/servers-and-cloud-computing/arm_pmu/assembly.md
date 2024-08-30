---
title: "Use a system counter"
weight: 3
layout: "learningpathall"
---

There are two Arm instructions that allow access to system registers. These are [MSR](https://developer.arm.com/documentation/dui0489/i/arm-and-thumb-instructions/msr--arm-register-to-system-coprocessor-register-) to write a system register and [MRS](https://developer.arm.com/documentation/dui0489/i/arm-and-thumb-instructions/mrs--system-coprocessor-register-to-arm-register-) to read a system register. These are the only two instructions required for counting.

## Using assembly for system counter access

If you only need to count time/cycles, then the [system counter](https://developer.arm.com/documentation/102379/0102/System-Counter?lang=en) can be used. You can do this from user space. An example of measuring system counter ticks across a function is shown below:

Use a text editor to create a file named `syscnt.c` with the code below:

```C
#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

// The function we are interested in counting through (see main)
void code_to_measure(){
  int sum = 0;
  for(int i = 0; i < 1000000000; ++i){
    sum += 1;
  }
}

int main() {
  uint64_t syscnt_freq = 0;
  uint64_t syscnt_before, syscnt_after;

  // Get frequency of the system counter
  asm volatile("mrs %0, cntfrq_el0" : "=r" (syscnt_freq));

  // Read system counter
  asm volatile("mrs %0, cntvct_el0" : "=r" (syscnt_before));

  // This is what we are counting through
  code_to_measure();

  // Read system counter
  asm volatile("mrs %0, cntvct_el0" : "=r" (syscnt_after));

  // Calculate results and print to stdout
  uint64_t syscnt_ticks = syscnt_after - syscnt_before;
  printf("System counter ticks: %"PRIu64"\n", syscnt_ticks);
  printf("System counter freq (Hz): %"PRIu64"\n", syscnt_freq);

  return 0;
}
```
This method only requires access to two registers, [`cntfrq_el0`](https://developer.arm.com/documentation/ddi0595/2020-12/AArch64-Registers/CNTFRQ-EL0--Counter-timer-Frequency-register?lang=en) and [`cntvct_el0`](https://developer.arm.com/documentation/ddi0595/2020-12/AArch64-Registers/CNTVCT-EL0--Counter-timer-Virtual-Count-register?lang=en). `cntfrq_el0` contains the frequency at which the system counter increments in Hz. `cntvct_el0` contains the counter value. These registers can be used to measure real time because they are not affected by power management mechanisms like frequency scaling and are always on, even when the cores are put to sleep.

Compile the example using the GNU compiler:

``` bash
gcc syscnt.c -o syscnt
```

Run the application:

``` console
 ./syscnt
 ```

The output will be similar to:

 ```output
System counter ticks: 280201338
System counter freq (Hz): 121875000
```

Your counter values may be different from the output above.
