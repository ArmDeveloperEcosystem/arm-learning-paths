---
title: Data type demotions and possible problems
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Demotions in C/C++

You previously saw that demotions are not detected in C and only in a few cases in C++, let's explain that in more detail, consider the small C++ program:

```
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

    int16_t d1 = c*2;
    int16_t d2{c*2};
    printf("a = %d, b = %d, c = %ld, d1 = %d, d2 = %d\n", a, b, c, d1, d2);

    int32_t e1 =w;
    int32_t e2{w};
    printf("e1 = %d, e2 = %d\n", e1, e2);
}
```

Save this file under `demotiontest.c` and compile it:

```
$ g++ demotiontest.cpp -o demotiontest
```

You will most likely get the following warnings, but the program will compile successfully:

```
demotiontest.cpp: In function ‘int main()’:
demotiontest.cpp:15:17: warning: narrowing conversion of ‘w’ from ‘double’ to ‘float’ [-Wnarrowing]
   15 |         float z{w};
      |                 ^
demotiontest.cpp:24:21: warning: narrowing conversion of ‘(c * 2)’ from ‘int64_t’ {aka ‘long int’} to ‘int16_t’ {aka ‘short int’} [-Wnarrowing]
   24 |         int16_t d2{c*2};
      |                    ~^~
demotiontest.cpp:28:20: warning: narrowing conversion of ‘w’ from ‘double’ to ‘int32_t’ {aka ‘int’} [-Wnarrowing]
   28 |         int32_t e2{w};
```

Now let's run it:

```
$ ./demotiontest 
w = 100000000000000007629769841091887003294964970946560.000000
y = inf
z = inf
a = -16380, b = -16380000, c = 799869184, d1 = 4608, d2 = 4608
e1 = 2147483647, e2 = 2147483647
```

So, obviously `w` is a huge value and it cannot fit in a `float` (remember largest positive float is `3.4e+38`), but the compiler only complains about `z` which uses bracket initialization and not `y` which uses assignment. 
Similarly, `d1` an `int16_t` uses assignment and doesn't cause a warning, but `d2`, also an `int16_t`, uses bracket initialization which does trigger a warning in the compiler.

The same happens with the demotion/conversion of the the `double w` to the `int32_t` variables `e1`, `e2`.

This means that some demotions/conversions that happen through assignment can pass the compiler without a warning, leading to wrong values and difficult to track bugs in your code.

In general demotions can be risky, you should always take a second look when a demotion takes place. If using C++, try to use bracket initialization to trigger compiler warnings!