---
title: When can we use restrict
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## So, when can we use restrict?

This is all very good, but when can we use it? Or put differently, how to recognize we need `restrict` in our code?

`restrict` as a pointer attribute is rather easy to test. As a rule of thumb, if our function includes one or more pointers to memory objects as arguments, we can use `restrict` if we are certain that the memory pointed by those pointer arguments does not overlap and there is no other way to access it in the body of the function, except by the use of those pointers -eg. there is no other global pointer, or some other indirect way to access these elements.

Let's show a coutner-example:

```
int A[10];

int f(int *B, size_t n) {
    int sum = 0;
    for (int i=0; i < n; i++) {
        sum += A[i] * B[i];    // B is used in conjunction with A
    }
}

int main() {
    int s = f(A, 10);       // A is passed to f, so f will be calculating sum of A[i] * A[i] elements
    printf("sum = %d", s);
}
```

This example does not not benefit from `restrict` at all in both gcc and clang.

However, there are plenty of cases that are candidates for the `restrict` optimization. And it's safe and easy to try. Nevertheless, even if it looks like a good candidate, it is still possible that the compiler will not detect a pattern that is suited for optimization and we might not see any reduction in the code or speed gain. It is up to the compiler, some cases clang handles better or differently than gcc, and vice versa, and that even depends on the version. If you have a particular piece of code that falls in the above criteria that you would care to optimize, before you attempt to refactor it completely, or rewrite it in assembly or use any SIMD instructions, it might be worth a shot to try `restrict`. Even saving a couple of instructions in a critical loop function is worth having to add just one keyword!