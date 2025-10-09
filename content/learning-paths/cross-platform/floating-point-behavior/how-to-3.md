---
title: Precision and floating-point instruction considerations
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

When moving from x86 to Arm you may see differences in floating-point behavior. Understanding these differences may require digging deeper into the details, including the precision and the floating-point instructions.

This section explores an example with minor differences in floating-point results, particularly focused on Fused Multiply-Add (FMAC) operations. You can run the example to learn more about how the same C code can produce different results on different platforms.

## Single precision and FMAC differences

Consider two mathematically equivalent functions, `f1()` and `f2()`. While they should theoretically produce the same result, small differences can arise due to the limited precision of floating-point arithmetic and the instructions used. 

When these small differences are amplified, you can observe how Arm and x86 architectures handle floating-point operations differently, particularly with respect to FMAC (Fused Multiply-Add) operations. The example shows the Clang compiler on Arm using FMAC instructions by default, which can lead to slightly different results compared to x86, which is not using FMAC instructions.

Functions `f1()` and `f2()` are mathematically equivalent. You would expect them to return the same value given the same input. 
 
Use an editor to copy and paste the C code below into a file named `example.c` 

```c
#include <stdio.h>
#include <math.h>

// Function 1: Computes sqrt(1 + x) - 1 using the naive approach
float f1(float x) {
    return sqrtf(1 + x) - 1;
}

// Function 2: Computes the same value using an algebraically equivalent transformation
// This version is numerically more stable
float f2(float x) {
    return x / (sqrtf(1 + x) + 1);
}

int main() {
    float x = 1e-8;  // A small value that causes floating-point precision issues
    float result1 = f1(x);
    float result2 = f2(x);

    // Theoretically, result1 and result2 should be the same
    float difference = result1 - result2;
    
    // Multiply by a large number to amplify the error - using single precision (float)
    // This is where architecture differences occur due to FMAC instructions
    float final_result = 100000000.0f * difference + 0.0001f;
    
    // Using double precision for the calculation makes results consistent across platforms
    double final_result_double = 100000000.0 * difference + 0.0001;

    // Print the results
    printf("f1(%e) = %.10f\n", x, result1);
    printf("f2(%e) = %.10f\n", x, result2);
    printf("Difference (f1 - f2) = %.10e\n", difference);
    printf("Final result after magnification (float): %.10f\n", final_result);
    printf("Final result after magnification (double): %.10f\n", final_result_double);

    return 0;
}
```

You need access to an Arm and x86 Linux computer to compare the results. The output below is from Ubuntu 24.04 using Clang. The Clang version is 18.1.3.

Compile and run the code on both x86 and Arm with the following command:

```bash
clang -g example.c -o example -lm
./example
```

The output running on x86:

```output
f1(1.000000e-08) = 0.0000000000
f2(1.000000e-08) = 0.0000000050
Difference (f1 - f2) = -4.9999999696e-09
Final result after magnification (float): -0.4999000132
Final result after magnification (double): -0.4998999970
```

The output running on Arm:

```output
f1(1.000000e-08) = 0.0000000000
f2(1.000000e-08) = 0.0000000050
Difference (f1 - f2) = -4.9999999696e-09
Final result after magnification (float): -0.4998999834
Final result after magnification (double): -0.4998999970
```

Notice that the double precision results are identical across platforms, while the single precision results differ.

You can disable the fused multiply-add on Arm with a compiler flag:

```bash
clang -g -ffp-contract=off example.c -o example2 -lm
./example2
```

Now the output of `example2` on Arm matches the x86 output. 

You can use `objdump` to look at the assembly instructions to confirm the use of FMAC instructions.

Page through the `objdump` output to find the difference shown below in the `main()` function.

```bash
llvm-objdump -d ./example  | more
```

The Arm output includes `fmadd`:

```output
8c8: 1f010800     	fmadd	s0, s0, s1, s2
```

The x86 uses separate multiply and add instructions:

```output
125c: f2 0f 59 c1                  	mulsd	%xmm1, %xmm0
1260: f2 0f 10 0d b8 0d 00 00      	movsd	0xdb8(%rip), %xmm1      # 0x2020 <_IO_stdin_used+0x20>
1268: f2 0f 58 c1                  	addsd	%xmm1, %xmm0
```

{{% notice Note %}}
On Ubuntu 24.04 the GNU Compiler, `gcc`, produces the same result as x86 and does not use the `fmadd` instruction. Be aware that corner case examples like this may change in future compiler versions.
{{% /notice %}}

## Techniques for consistent results

You can make the results consistent across platforms in several ways:

- Use double precision for critical calculations by changing `100000000.0f` to `100000000.0` (double precision).

- Disable fused multiply-add operations using the `-ffp-contract=off` compiler flag. 

- Use the compiler flag `-ffp-contract=fast` to enable fused multiply-add on x86.

## Key takeaways

- Different floating-point behavior between architectures can often be traced to specific hardware features or instructions such as Fused Multiply-Add (FMAC) operations.
- FMAC performs multiplication and addition with a single rounding step, which can lead to different results compared to separate multiply and add operations.
- Compilers may use FMAC instructions on Arm by default, but not on x86. 
- To ensure consistent results across platforms, consider using double precision for critical calculations and controlling compiler optimizations with flags like `-ffp-contract=off` and `-ffp-contract=fast`.
- Understanding [numerical stability](https://en.wikipedia.org/wiki/Numerical_stability) remains important for writing portable code.

If you see differences in floating-point results, it typically means you need to look a little deeper to find the causes.

These situations are not common, but it is good to be aware of them as a software developer migrating to the Arm architecture. You can be confident that floating-point on Arm behaves predictably and that you can get consistent results across multiple architectures.
