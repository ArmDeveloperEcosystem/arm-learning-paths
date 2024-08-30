---
title: Data type demotions
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Data type demotions in C/C++

You previously saw that demotions are not detected in C and only in a few cases in C++. 

To learn more about demotions, consider the small C++ program below.

Use a text editor to copy the code to a text file named `demotiontest.cpp`:

```C++
#include <cmath>
#include <cstdio>
#include <cstdint>

int main() {
    double w = 1.0e50;
    printf("w = %f\n", w);
    float y = w;
    float z{w};
    printf("y = %f\n", y);
    printf("z = %f\n", z);

    int16_t a = -16380;
    int32_t b = a*1000;
    int64_t c = b*1000;

    int16_t d1 = c*2;
    int16_t d2{c*2};
    printf("a = %d, b = %d, c = %ld, d1 = %d, d2 = %d\n", a, b, c, d1, d2);

    int32_t e1 =w;
    int32_t e2{w};
    printf("e1 = %d, e2 = %d\n", e1, e2);
}
```

Compile the example:

```bash
g++ demotiontest.cpp -o demotiontest
```

You will most likely get the following warnings but the program will compile successfully:

```bash
demotiontest.cpp: In function ‘int main()’:
demotiontest.cpp:9:13: warning: narrowing conversion of ‘w’ from ‘double’ to ‘float’ [-Wnarrowing]
    9 |     float z{w};
      |             ^
demotiontest.cpp:18:17: warning: narrowing conversion of ‘(c * 2)’ from ‘int64_t’ {aka ‘long int’} to ‘int16_t’ {aka ‘short int’} [-Wnarrowing]
   18 |     int16_t d2{c*2};
      |                ~^~
demotiontest.cpp:22:16: warning: narrowing conversion of ‘w’ from ‘double’ to ‘int32_t’ {aka ‘int’} [-Wnarrowing]
   22 |     int32_t e2{w};
      |
```

Now run the program:

```bash
./demotiontest 
```

The output is:

```output
w = 100000000000000007629769841091887003294964970946560.000000
y = inf
z = inf
a = -16380, b = -16380000, c = 799869184, d1 = 4608, d2 = 4608
e1 = 2147483647, e2 = 2147483647
```

Obviously `w` is a huge value and it does not fit in a `float` (remember that the largest positive float is `3.4e+38`), but the compiler only complains about `z` which uses bracket initialization and not `y` which uses assignment. 

Similarly `d1`, with type `int16_t`, uses assignment and does not generate a warning but `d2`, also an `int16_t`, uses bracket initialization and triggers a compiler warning.

The same happens with the demotion/conversion of the `double w` to the `int32_t` variables `e1`, `e2`.

This means that some demotions/conversions that happen through assignment can pass the compiler without a warning, leading to wrong values and difficult to track bugs.

In general, demotions are risky and you should always take a second look when a demotion takes place. When using C++, try to use bracket initialization to trigger compiler warnings.
