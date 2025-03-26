---
title: Adding Inside Knowledge
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Adding Inside Knowledge

To make the compiler aware that the input will be a multiple of 4 we will rewrite our loop size as the following. 

```output
((max_loop_size/4)*4)
```

Mathematically this may seem redundant. However since `(max_loop_size/4)` will be truncated to an integer this guarantees `(max_loop_size/4)*4` is a multiple of 4. 

As slightly easier to read method that avoids confusion when arguments are passed in is dividing the variable before passing it in. For example.

```output
(max_loop_size_div_4 * 4)
```

## Adding Insider Knowledge

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
g++ -O3 -march=armv8-a+simd  -o context
```

```output
./context 
Enter a value for max_loop_size (must be a multiple of 4): 40000
Sum: 799980000
Time taken by foo: 24650 nanoseconds
```

## Comparison

To compare we will use compiler explorer to see the assembly. 

First, looking at the example without context [here](https://godbolt.org/z/qPaW5Kjxa).
Second, looking at the example with context [here](https://godbolt.org/z/rhj65Pe4v).


[Here](https://godbolt.org/z/nvx4j1vTK). 

As the assembly shows we have fewer lines of assembly corresponding to the function `foo` as there is less setup code to account given the insider knowledge. 


