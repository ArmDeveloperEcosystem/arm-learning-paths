---
# User change
title: "How do I measure RPi Pico Application Performance?"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

Measure application performance using SysTick, the 24-bit system timer.

A common requirement is to measure the number of cycles it takes to execute a section of code. For the Cortex-M0+ included in the Raspberry Pi Pico, this can be done using SysTick. 

The application below shows how to use SysTick to count cycles.

The code computes the Fibonacci series in two different ways and counts the number of cycles required to make the computation.

## How do I build the RPi Pico application?

Save the C code bellow to a file named `fib.c`

```C
#include <stdio.h>
#include "pico/stdlib.h"
#include "systick.h"

int fib1(int count)
{
    int first_term = 0, second_term = 1, next_term;

    printf("First Fibonacci series\n");

    (void) start_systick();

    for (int i = 0; i < count ; i++ )
    {
        if ( i <= 1 )
           next_term = i;
        else
        {
            next_term = first_term + second_term;
            first_term = second_term;
            second_term = next_term;
        }
        printf("%d\n",next_term);
    }

    printf("First Fibonacci series complete: %d cycles\n",stop_systick());

    return 0;
}

int fibonacci_series(int num)
{
    if (num == 0)
        return 0;
    else if (num == 1)
        return 1;
    else
        return (fibonacci_series(num-1) + fibonacci_series(num-2));
}

int fib2(int count)
{
    int c = 0;

    printf("Second Fibonacci series\n");

    (void) start_systick();

    for (int i = 1; i <= count ; i++ )
    {
        fibonacci_series(c);
        printf("%d\n", fibonacci_series(c));
        c++;
    }

    printf("Second Fibonacci series complete: %d cycles\n",stop_systick());
}

int main()
{
    int count = 25;
    int st;

    const uint LED_PIN = PICO_DEFAULT_LED_PIN;

    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);

    stdio_init_all();

    printf("Hello, Pi Pico!\n");

    while (true)
    {
        st = fib1(count);
        gpio_put(LED_PIN, 1);
        sleep_ms(500);
        st = fib2(count);
        gpio_put(LED_PIN, 0);
        sleep_ms(500);
    }

    return 0;
}
```

Save the information below as `CMakeLists.txt`

```cmake
cmake_minimum_required(VERSION 3.18)

include($ENV{PICO_SDK_PATH}/external/pico_sdk_import.cmake)

project(fib C CXX ASM)
set(CMAKE_C_STANDARD 11)

pico_sdk_init()

add_executable(${PROJECT_NAME}
            ${PROJECT_NAME}.c systick.c
        )

# pull in common dependencies
target_link_libraries(${PROJECT_NAME} pico_stdlib)

# enable usb or uart output
pico_enable_stdio_usb(${PROJECT_NAME} 1)
pico_enable_stdio_uart(${PROJECT_NAME} 1)

# create map/bin/hex/uf2 file etc.
pico_add_extra_outputs(${PROJECT_NAME})
```

Two more files are needed for SysTick. 

Save the code below as `systick.h`

```c
#include <stdint.h>

void start_systick(void);
uint32_t stop_systick(void);

/* SysTick variables */
#define SysTick_BASE          (0xE000E000UL +  0x0010UL)
#define SysTick_START         0xFFFFFF

#define SysTick_CSR           (*((volatile uint32_t*)(SysTick_BASE + 0x0UL)))
#define SysTick_RVR           (*((volatile uint32_t*)(SysTick_BASE + 0x4UL)))
#define SysTick_CVR           (*((volatile uint32_t*)(SysTick_BASE + 0x8UL)))

#define SysTick_Enable        0x1
#define SysTick_ClockSource   0x4
```

Finally, the fourth file is `systick.c`

```c
#include <stdio.h>
#include "systick.h"

void start_systick()
{
    SysTick_RVR = SysTick_START;
    SysTick_CVR = 0;
    SysTick_CSR |=  (SysTick_Enable | SysTick_ClockSource);
}

uint32_t stop_systick()
{
    SysTick_CSR &= ~SysTick_Enable;

    uint32_t cycles = (SysTick_START - SysTick_CVR);

    if (SysTick_CSR & 0x10000)
        printf("WARNING: counter has overflowed, more than 16,777,215 cycles");

    return(cycles);
}
```

Build the application:

```bash
mkdir build ; cd build
cmake ..
make
```

The fib application is now ready to run.

## How do I run fib?

To run, hold down the BOOTSEL button on the Raspberry Pi Pico and plugin the USB cable between the Pico and your development computer. 

The Pico will appear as a USB storage device on your computer. 

When developing on a Raspberry Pi OS or Ubuntu, the Pico appears in `/media/$HOME/RPI-RP2`

Copy the executable (in uf2 format) to the Pico.

```bash
cp fib.uf2 /media/$USER/RPI-RP2/
```

After copying the file the Pico disappears as a storage device and the fib program starts running. 

The LED on the Pico will start blinking as specified in fib.c. 

The cycle counts will be printed to the USB serial.

Connect to USB serial using minicom. 

For a Raspberry Pi or Ubuntu development computer the USB device to connect to is `/dev/ttyACM0`

```bash
sudo minicom -b 115200 -o -D /dev/ttyACM0
```

The terminal will show the output of the hello string along with the cycle counts for each implementation.

```console
First Fibonacci series
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
10946
17711
28657
46368
First Fibonacci series complete: 1181868 cycles
Second Fibonacci series
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
10946
17711
28657
46368
Second Fibonacci series complete: 12225226 cycles
```

## Summary 

SysTick can be used as a cycle counter for Cortex-M0+.

There are two things to learn from this example. 

First, the SysTick code may be rearranged by the compiler. It doesn't have any dependencies on the code around it and the compiler may reorder the calls to start and stop the cycle count. If this happens it will not wrap around the intended code and the cycle counts will be very small. Look at the disassembly output in fib.dis to review the code.

Second, counting cycles for print statements is not advised. Printing to the UART takes a long time and cycle counts may be dominated by time spent in in print statements. 

