---
title: More on implicit conversions
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## A closer look at implicit conversions

The example below explains more about implicit conversions. 

The code is meant to calculate the *golden ratio* number 1.618033988749894... using 2 consecutive Fibonacci numbers, as `φ[N] = F[N]/F[N-1]` and `Φ = Φ[Ν]` as `N -> inf`.

Use a text editor to save the C program in a file named `golden_ratio.c`:

```C
#include <math.h>
#include <stdio.h>
#include <stdint.h>

#define MAX 50

static int fibonacci[MAX];

void calculate_fibonacci(size_t N) {
    fibonacci[0] = 0;
    fibonacci[1] = 1;

    for (int i = 2; i < N; ++i) {
        fibonacci[i] = fibonacci[i-2] + fibonacci[i-1];
    }
}

void print_fibonacci(size_t N) {
    for (int i = 0; i < N; ++i) {
        printf("%d ", fibonacci[i]);
    }
    printf("\n");
}

float golden_ratio(int N) {
    float golden_ratio = fibonacci[N]/fibonacci[N-1];
    return golden_ratio;
}

int main() {
    calculate_fibonacci(50);
    print_fibonacci(50);

    for (int i = 2; i < MAX; i++) {
        float result = golden_ratio(i);
        printf("Golden ratio using N: %d Fibonacci numbers: %f\n", i, result);
    }

    return 0;
}
```

Compile and run the program:

```bash
gcc -O3 golden_ratio.c -o golden_ratio
./golden_ratio
```

The output is:

```output
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 5702887 9227465 14930352 24157817 39088169 63245986 102334155 165580141 267914296 433494437 701408733 1134903170 1836311903 -1323752223 512559680 -811192543
Golden ratio using N: 2 Fibonacci numbers: 1.000000
Golden ratio using N: 3 Fibonacci numbers: 2.000000
Golden ratio using N: 4 Fibonacci numbers: 1.000000
Golden ratio using N: 5 Fibonacci numbers: 1.000000
Golden ratio using N: 6 Fibonacci numbers: 1.000000
Golden ratio using N: 7 Fibonacci numbers: 1.000000
Golden ratio using N: 8 Fibonacci numbers: 1.000000
Golden ratio using N: 9 Fibonacci numbers: 1.000000
Golden ratio using N: 10 Fibonacci numbers: 1.000000
...
Golden ratio using N: 40 Fibonacci numbers: 1.000000
Golden ratio using N: 41 Fibonacci numbers: 1.000000
Golden ratio using N: 42 Fibonacci numbers: 1.000000
Golden ratio using N: 43 Fibonacci numbers: 1.000000
Golden ratio using N: 44 Fibonacci numbers: 1.000000
Golden ratio using N: 45 Fibonacci numbers: 1.000000
...
```

You will immediately notice the results are unexpected because the `golden_ratio()` function is incorrect.

```C
static int fibonacci[MAX];
...
float golden_ratio(int N) {
    float golden_ratio = fibonacci[N]/fibonacci[N-1];
    return golden_ratio;
}
```

All results will be either 1.0 or 2.0. This is because the division is done between the integers and then converted to floating-point. This is a frequent problem which is usually easy to find and fix. However, there are cases where it's part of complex arithmetic expressions and easy to miss. Unfortunately, the compiler does not generate a warning.

You can fix the problem and demonstrate a different problem. Split the calculation to avoid the previous integer division:

```C
float golden_ratio(int N) {
	float golden_ratio = fibonacci[N];
    golden_ratio /= fibonacci[N-1];
    return golden_ratio;
}
```

Compile and run the program again:

```bash
gcc -O3 golden_ratio.c -o golden_ratio
./golden_ratio
```

The output is:

```output
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368
75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 5702887 9227465 14930352
24157817 39088169 63245986 102334155 165580141 267914296 433494437 701408733 1134903170
1836311903 -1323752223 512559680 -811192543 
Golden ratio using N: 2 Fibonacci numbers: 1.00000000000000
Golden ratio using N: 3 Fibonacci numbers: 2.00000000000000
Golden ratio using N: 4 Fibonacci numbers: 1.50000000000000
Golden ratio using N: 5 Fibonacci numbers: 1.66666662693024
Golden ratio using N: 6 Fibonacci numbers: 1.60000002384186
Golden ratio using N: 7 Fibonacci numbers: 1.62500000000000
...
Golden ratio using N: 44 Fibonacci numbers: 1.61803388595581
Golden ratio using N: 45 Fibonacci numbers: 1.61803400516510
Golden ratio using N: 46 Fibonacci numbers: 1.61803400516510
Golden ratio using N: 47 Fibonacci numbers: -0.72087544202805
Golden ratio using N: 48 Fibonacci numbers: -0.38720214366913
Golden ratio using N: 49 Fibonacci numbers: -1.58263039588928
```

You will notice two things. 

First, the 32-bit int is not large enough to hold Fibonacci numbers for N >= 47. This is easily fixed by changing to `int64_t`. 

Next, you can also change `float` to `double`. This will also give increased precision in the calculations. 

However, this is not the actual problem. 

Look at the assembly code of `golden_ratio()`:

```as
golden_ratio:
        sub     w2, w0, #1
        adrp    x1, .LANCHOR0
        add     x1, x1, :lo12:.LANCHOR0
        ldr     s2, [x1, w0, sxtw 2]
        ldr     s1, [x1, w2, sxtw 2]
        scvtf   s2, s2
        scvtf   s0, s1
        fdiv    s0, s2, s0
        ret
```

You now see that `scvtf` instruction is executed twice, which converts from integer to floating point, so that the quantities can be divided using floating point with the `fdiv` instruction. The `scvtf` instruction has up to 6 CPU cycles latency on the Neoverse N1 processor and 3 cycles on the Neoverse N2. Imagine a complicated expression many similar implicit conversions, executed millions or billions of times, it would definitely under perform.

This example is easy to fix, if you just convert the `fibonacci` array to `float` or `double`:

```C
static float fibonacci[MAX];
```

and rewrite the `golden_ratio()` function as single line division:

```C
float golden_ratio(int N) {
    float golden_ratio = fibonacci[N] / fibonacci[N-1];
    return golden_ratio;
}
```

The assembly output does not contain any `scvtf` instructions:

```as
golden_ratio:
        sub     w2, w0, #1
        adrp    x1, .LANCHOR0
        add     x1, x1, :lo12:.LANCHOR0
        ldr     s1, [x1, w0, sxtw 2]
        ldr     s0, [x1, w2, sxtw 2]
        fdiv    s0, s1, s0
        ret
```

Compile the updated program and run it: 

```bash
gcc -O3 golden_ratio.c -o golden_ratio
./golden_ratio
```

The output is now:

```output
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368
75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 5702887 9227465 14930352 
24157817 39088169 63245986 102334155 165580141 267914296 433494437 701408733 1134903170
1836311903 2971215073 4807526976 7778742049
Golden ratio using N: 2 Fibonacci numbers: 1.00000000000000
Golden ratio using N: 3 Fibonacci numbers: 2.00000000000000
Golden ratio using N: 4 Fibonacci numbers: 1.50000000000000
Golden ratio using N: 5 Fibonacci numbers: 1.66666662693024
Golden ratio using N: 6 Fibonacci numbers: 1.60000002384186
Golden ratio using N: 7 Fibonacci numbers: 1.62500000000000
...
Golden ratio using N: 43 Fibonacci numbers: 1.61803400516510
Golden ratio using N: 44 Fibonacci numbers: 1.61803400516510
Golden ratio using N: 45 Fibonacci numbers: 1.61803400516510
Golden ratio using N: 46 Fibonacci numbers: 1.61803400516510
Golden ratio using N: 47 Fibonacci numbers: 1.61803400516510
Golden ratio using N: 48 Fibonacci numbers: 1.61803400516510
Golden ratio using N: 49 Fibonacci numbers: 1.61803400516510
```

Not all problems are as easy to fix. If your use case involves numbers too big to fit in `int64_t` or even in `double` incorrect results will occur. 

You can change `MAX` to 100 and see incorrect results as the loop approaches 100. 

In such cases another method would have to be used, possibly an arbitrary precision data type in a library created to handle large numbers. 

Implicit conversions can have a significant impact in performance, especially in loops involving complex mathematical expressions.