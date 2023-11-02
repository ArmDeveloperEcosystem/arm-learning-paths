---
title: When can we use restrict
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

When can we use `restrict` or, put differently, how do we recognize that we need `restrict` in our code?

`restrict` as a pointer attribute is rather easy to test. As a rule of thumb, if the function includes one or more pointers to memory objects as arguments, we can use `restrict` if we are certain that the memory pointed to by these pointer arguments does not overlap and there is no other way to access them in the body of the function, except by the use of those pointers, i.e., there is no other global pointer or some other indirect way to access these elements.

Let's show a counter example:

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

This example does not not benefit from `restrict` in either gcc and clang.

However, there are plenty of cases that are candidates for the `restrict` optimization. It's safe and easy to try but, even if it looks like a good candidate, it is still possible that the compiler will not detect a pattern that is suited for optimization and we might not see any reduction in the code or speed gain. It is up to the compiler; in some cases clang handles this better or differently from gcc, and vice versa, and this will also depend on the version. If you have a particular piece of code that you would like to optimize, before you attempt to refactor it completely, rewrite it in assembly or use any SIMD instructions, it might be worth trying `restrict`. Even saving a couple of instructions in a critical loop function is worth having by just adding one keyword.
