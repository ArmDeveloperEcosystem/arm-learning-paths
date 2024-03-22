---
title: Summary
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Burst, Neon and Auto-vectorization
In this learning path you have followed an iteration of measuring, optimizing, and comparing changes using the Burst compiler and Neon intrinsics.

The Burst compiler does a great job of auto-vectorization and leveraging Neon but hand-written Neon can give an extra boost. It is worthwhile investigating your application to see what solution suits you best.

In some situations you may find it optimal to switch between implementations depending on the context of your application. In the collision sample the Burst and Neon performance gains were maximized when the character count was high, so an alternative method could have been used while the character count was low.

Always consider best practice for auto-vectorization, keep your code simple and loops small as the compiler will find it much easier to vectorize.
