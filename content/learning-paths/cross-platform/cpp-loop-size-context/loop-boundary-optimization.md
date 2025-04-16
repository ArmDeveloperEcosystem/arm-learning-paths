---
title: Optimize loops using boundary information
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How can I add developer knowledge to optimize performance? 

To ensure the loop size is always a multiple of 4 and communicate this boundary information to the compiler, you can rewrite the loop size calculation as follows:

```output
((max_loop_size/4)*4)
```

At first glance, this calculation looks mathematically redundant. However, since the expression `(max_loop_size/4)` is an integer division, it truncates the result, effectively guaranteeing that `(max_loop_size/4)*4` will always yield a number divisible by 4. This pattern allows the compiler to recognize and optimize for this specific constraint.

This optimization is particularly effective because it enables the compiler to use SIMD (Single Instruction, Multiple Data) vectorization. When the compiler knows the loop count is a multiple of 4, it can process four elements at once using vector registers, significantly improving performance on Arm processors.

A slightly easier to read method that avoids confusion when passing arguments is to divide the variable and rename before it is passed in. 

For example:

```output
(max_loop_size_div_4 * 4)
```

## Try an improved example

Use a text editor to copy the code below and paste it into a file named `context.cpp`.

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

Compile the new program with the same flags:

```bash
g++ -O3 -march=armv8-a+simd context.cpp -o context
```

Run the new example with the same 40000 as input:

```bash
./context 
```

You see the new output:

```output
Enter a value for max_loop_size (must be a multiple of 4): 40000
Sum: 799980000
Time taken by foo: 24650 nanoseconds
```

The time taken has significantly reduced compared to the previous version. This performance improvement is a direct result of providing boundary information to the compiler. 

## Performance considerations

While this optimization technique provides significant performance benefits, it's important to note that it assumes the input is a multiple of 4. In a real-world application, you would need to validate user input or handle cases where the input isn't a multiple of 4. 

For example:

```cpp
// Validate input
if (max_loop_size % 4 != 0) {
    std::cerr << "Error: Input must be a multiple of 4" << std::endl;
    return 1;
}
```

Alternatively, you could pad the array to ensure its size is always a multiple of 4, or handle the remainder elements separately after processing the vectorized portion of the array. The approach you choose depends on your specific application requirements and constraints.

## Comparison

You can compare the differences in [Compiler Explorer](https://godbolt.org/z/nvx4j1vTK). 

The assembly code shows there are fewer lines of assembly corresponding to the function `foo()` when context is added. This is because the compiler can optimize the conditional checking and any clean up code given the context.

When examining the assembly output in Compiler Explorer, look for these key differences:

1. **Vector instructions**: In the optimized version, look for instructions like `ld1` (load to vector register) and `addv` (add across vector) which indicate SIMD operations.

2. **Loop structure**: The optimized version will likely have fewer instructions inside the main loop body as multiple elements are processed at once.

3. **Unrolling factor**: Notice how the compiler might unroll the loop to process multiple elements in each iteration, reducing branch overhead.

4. **Register usage**: The optimized version will make more efficient use of vector registers (v0-v31) rather than just scalar registers.

These assembly-level differences directly translate to the performance improvements you observed in the execution time. 

