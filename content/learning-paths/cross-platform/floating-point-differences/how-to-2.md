---
title: Differences between x86 and Arm
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Differences in behaviour between x86 and Arm. 

The C++ code snippet below type casts floating point numbers to various data types. Copy and paste into a new file called `converting-float.cpp`. 

```cpp
#include <iostream>
#include <cmath>
#include <limits>
#include <cstdint>

void convertFloatToInt(float value) {
    // Convert to unsigned 32-bit integer
    uint32_t u32 = static_cast<uint32_t>(value);

    // Convert to signed 32-bit integer
    int32_t s32 = static_cast<int32_t>(value);

    // Convert to unsigned 16-bit integer (truncation happens)
    uint16_t u16 = static_cast<uint16_t>(u32); 
    uint8_t u8 = static_cast<uint8_t>(value); 

    // Convert to signed 16-bit integer (truncation happens)
    int16_t s16 = static_cast<int16_t>(s32);

    std::cout << "Floating-Point Value: " << value << "\n";
    std::cout << "  → uint32_t:  " << u32 << " (0x" << std::hex << u32 << std::dec << ")\n";
    std::cout << "  → int32_t:   " << s32 << " (0x" << std::hex << s32 << std::dec << ")\n";
    std::cout << "  → uint16_t (truncated):  " << u16 << " (0x" << std::hex << u16 << std::dec << ")\n";
    std::cout << "  → int16_t (truncated):   " << s16 << " (0x" << std::hex << s16 << std::dec << ")\n";
    std::cout << "  → uint8_t (truncated):   " << static_cast<int>(u8) << std::endl;

    std::cout << "----------------------------------\n";
}

int main() {
    std::cout << "Demonstrating Floating-Point to Integer Conversion\n\n";

    // Test cases
    convertFloatToInt(42.7f);                   // Normal case
    convertFloatToInt(-15.3f);                  // Negative value -> wraps on unsigned
    convertFloatToInt(4294967296.0f);           // Overflow: 2^32 (UINT32_MAX + 1)
    convertFloatToInt(3.4e+38f);                // Large float exceeding UINT32_MAX
    convertFloatToInt(-3.4e+38f);               // Large negative float
    convertFloatToInt(NAN);                     // NaN behavior on different platforms
    return 0;
}
```

To demonstrate we will compile `converting-float.cpp` on an Arm64 and x86 machine. For this example I am using a `t2.2xlarge`, x86-based instance on AWS but other x86 machines can be used. Run the command below on both an Arm-based and x86-based system

```g++ -g converting-float.cpp -o converting-float ```

For easy visualisation, the image below shows the x86 output (left) and Arm output (right). The  highlighted lines show the difference in output. 

![differences](./differences.png)