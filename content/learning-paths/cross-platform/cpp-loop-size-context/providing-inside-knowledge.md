---
title: Adding Inside Knowledge
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Adding Inside Knowledge

To explicitly inform the compiler that our input will always be a multiple of 4, we can rewrite the loop size calculation as follows:

```output
((max_loop_size/4)*4)
```

At first glance, this calculation might seem mathematically redundant. However, since the expression `(max_loop_size/4)` is an integer division, it truncates the result, effectively guaranteeing that `(max_loop_size/4)*4` will always yield a number divisible by 4. The compiler can pick up on this information and optimise accordingly. 

As slightly easier to read method that avoids confusion when passing arguments is to divide the variable and rename before it is passed in. For example.

```output
(max_loop_size_div_4 * 4)
```

## Improved Example

Copy the snippet below and paste into a file named `context.cpp`.

```cpp
#include <iostream>
#include <chrono>

void foo(const int* x, int max_loop_size_div_4)
{
    int sum = 0;
    for (int k = 0; k < max_loop_size_div_4 * 4; k++) {
        sum += x[k];
    }
    std::cout << "Sum: " << sum << std::endl;
}

int main() {
    int max_loop_size;
    std::cout << "Enter a value for max_loop_size (must be a multiple of 4): ";
    std::cin >> max_loop_size;

    int max_loop_size_div_4 = max_loop_size / 4;
    int x[max_loop_size];
    // Initialise test data
    for(int i = 0; i < max_loop_size; ++i) x[i] = i;
 
    // Start timing
    auto start = std::chrono::high_resolution_clock::now();
    foo(x, max_loop_size_div_4);
    // Stop timing
    auto end = std::chrono::high_resolution_clock::now();

    // Calculate and display the elapsed time
    auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count();
    std::cout << "Time taken by foo: " << duration << " nanoseconds" << std::endl;

    return 0;
}
```

Again compile with the same compiler flags. 

```bash
g++ -O3 -march=armv8-a+simd context.cpp -o context
```

```output
./context 
Enter a value for max_loop_size (must be a multiple of 4): 40000
Sum: 799980000
Time taken by foo: 24650 nanoseconds
```
In this particular run, the time taken has significantly reduced compared to our previous example. 

## Comparison

To compare we will use compiler explorer to see the assembly [here](https://godbolt.org/z/nvx4j1vTK). 

As the assembly shows we have fewer lines of assembly corresponding to the function `foo` when context is added. This is because the compiler can optimise the conditional checking and any clean up code given the context. 

