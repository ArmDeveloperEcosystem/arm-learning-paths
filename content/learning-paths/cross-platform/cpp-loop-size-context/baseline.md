---
title: Baseline loop implementation
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand the baseline loop

The following C++ program takes user input as the loop size so that the loop size `max_loop_size` is only known at runtime. This initializes an array of size `max_loop_size` with the value for each element corresponding to the index position. 

The function `foo()` loops through each element to print out the sum of all elements. Without any boundary information provided to the compiler, it must generate conservative code that works for any loop size. 

Use a text editor to copy the code below into a file named `no-context.cpp`. 

```cpp
#include <iostream>
#include <chrono>

void foo(const int* x, int max_loop_size)
{
    int sum = 0;
    for (int k = 0; k < max_loop_size; k++) {
        sum += x[k];
    }
    std::cout << "Sum: " << sum << std::endl;
}

int main() {
    int max_loop_size;
    std::cout << "Enter a value for max_loop_size (must be a multiple of 4): ";
    std::cin >> max_loop_size;

    int x[max_loop_size];
    // Initialise test data
    for(int i = 0; i < max_loop_size; ++i) x[i] = i;
 
    // Start timing
    auto start = std::chrono::high_resolution_clock::now();
    foo(x, max_loop_size);
    // Stop timing
    auto end = std::chrono::high_resolution_clock::now();

    // Calculate and display the elapsed time
    auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count();
    std::cout << "Time taken by foo: " << duration << " nanoseconds" << std::endl;

    return 0;
}
```

Compile the program using the following command: 

```bash
g++ -O3 -march=armv8-a+simd no-context.cpp -o no-context
```

Run the example with 40000 as the input:

```bash
./no-context 
```

You see the output below, your runtime will vary depending on the computer you are using.

```output
Enter a value for max_loop_size (must be a multiple of 4): 40000
Sum: 799980000
Time taken by foo: 138100 nanoseconds
```

Continue to the next section to see how to use developer knowledge of loops to improve performance. 