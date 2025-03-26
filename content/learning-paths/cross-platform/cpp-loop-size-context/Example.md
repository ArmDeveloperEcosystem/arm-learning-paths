---
title: Example
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Example

The following `C++` snippet takes user input as the loop size so that the loop size, `max_loop_size`, is only known at runtime. This initialises an array of size, , `max_loop_size` with the value for each element corresponding to the index position. The function, `foo`, loops through each element to print out the sum of all elements. 

Copy the snippet below into a file named, `no-context.cpp`. 

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

Compiling using the following command. 

```bash
g++ -O3 -march=armv8-a+simd no_context.cpp -o no_context
```

Running the example with the number 4000 leads to the following results. You will see runtime variability depending on which platform you run this on. 

```output
./no_context 
Enter a value for max_loop_size (must be a multiple of 4): 40000
Sum: 799980000
Time taken by foo: 138100 nanoseconds
```

