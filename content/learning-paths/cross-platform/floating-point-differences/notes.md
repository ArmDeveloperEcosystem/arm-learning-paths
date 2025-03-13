## Floating Point Numbers 

Essentially scientific notation that you learnt in Maths. Where large numbers are represented with significant and exponent. For example, the speed of light, 2.97 x 10^8. Of course, there are other ways to represent this number such as 29.7 x 10^7 and so forth. Naturally with scientific notation we have rounded the number the actual value for the speed of light is 297282828 != 2.97x10^8. 

Recursion in binary and decimal. 1/3 = 0.33333 recurring in decimal. Likewise, in binary 0.2 = 0.0001100110011 recurring.  

```python
>>> 0.1 + 0.2
0.30000000000000004
>>> 
```

IEEE 754, Significand is a positive number between 1<= and <10, and matissa is fractional fit, and exponent is 2^x?


Out of scope for this learning path is decimal datatype.


## Commutative

(a+b)+c != a+(b+c)


## Unit in Last Place

## Use Integers

2^64 – 1 = 18446744073709551615, a 20-digit number. However scientific notation (floating point) is far easier to calculate multiplication and division since we can add the exponent. 

in C, a `int` is 32 bits. Hence 2^32 - 1 = 2,

## Language data widths

Usually specify the minimum, e.g., a short is at least 16 bits.

Float is unspecified but most adhere to IEEE 754 standard.

E.g., C99 specifies minimum size and relative size.

## ABI compliance and Compilers

Undefined behaviour, unspecified behaviour.
Subtle difference for Arm compliant systems, e.g., Apple. 

## Conversions

Between different widths doesn't happen directly, but instead in 2 steps

## Obvious corrections

Use the standard functions to check, e.g., `sizeof(int)` for a runtime check. `CHAR_BIT` = size of a byte, but any system that doesn't consider a byte to be a bit will likely be found in a computer museum.

## Calculations 

If we take, 0.4 + 0.1. We can cleanly represent the value 0.5 in binary. 0.1 and 0.4 may be stored in different floating point represenations.


`-fno-unsafe-math-optimizations` [documentation](https://gcc.gnu.org/onlinedocs/gcc-14.2.0/gcc/Optimize-Options.html).



## Minimising error propagations

`-ffloat-store`. Taken from [g++-13.3 documentation](https://gcc.gnu.org/onlinedocs/gcc-13.3.0/gcc/Optimize-Options.html)

```output
-ffloat-store
Do not store floating-point variables in registers, and inhibit other options that might change whether a floating-point value is taken from a register or memory.

This option prevents undesirable excess precision on machines such as the 68000 where the floating registers (of the 68881) keep more precision than a double is supposed to have. Similarly for the x86 architecture. For most programs, the excess precision does only good, but a few programs rely on the precise definition of IEEE floating point. Use -ffloat-store for such programs, after modifying them to store all pertinent intermediate computations into variables.
```

`-frounding-math`.
```output
-frounding-math
Disable transformations and optimizations that assume default floating-point rounding behavior. This is round-to-zero for all floating point to integer conversions, and round-to-nearest for all other arithmetic truncations. This option should be specified for programs that change the FP rounding mode dynamically, or that may be executed with a non-default rounding mode. This option disables constant folding of floating-point expressions at compile time (which may be affected by rounding mode) and arithmetic transformations that are unsafe in the presence of sign-dependent rounding modes.

The default is -fno-rounding-math.

This option is experimental and does not currently guarantee to disable all GCC optimizations that are affected by rounding mode. Future versions of GCC may provide finer control of this setting using C99’s FENV_ACCESS pragma. This command-line option will be used along with -ftrapping-math to specify the default state for FENV_ACCESS.
```

`-fexcess-precision=standard`
```output
-fexcess-precision=style
This option allows further control over excess precision on machines where floating-point operations occur in a format with more precision or range than the IEEE standard and interchange floating-point types. By default, -fexcess-precision=fast is in effect; this means that operations may be carried out in a wider precision than the types specified in the source if that would result in faster code, and it is unpredictable when rounding to the types specified in the source code takes place. When compiling C or C++, if -fexcess-precision=standard is specified then excess precision follows the rules specified in ISO C99 or C++; in particular, both casts and assignments cause values to be rounded to their semantic types (whereas -ffloat-store only affects assignments). This option is enabled by default for C or C++ if a strict conformance option such as -std=c99 or -std=c++17 is used. -ffast-math enables -fexcess-precision=fast by default regardless of whether a strict conformance option is used.

-fexcess-precision=standard is not implemented for languages other than C or C++. On the x86, it has no effect if -mfpmath=sse or -mfpmath=sse+387 is specified; in the former case, IEEE semantics apply without excess precision, and in the latter, rounding is unpredictable.
```