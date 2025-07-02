---
title: Accuracy modes in Libamath
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Accuracy modes

Libamath provides multiple accuracy modes for the same vectorized mathematical function, allowing developers to choose between speed and precision depending on workload requirements.

Some functions offer selectable modes with tradeoffs between:
- **High accuracy** (≤ 1 ULP)
- **Default accuracy** (≤ 3.5 ULP)
- **Low accuracy / max performance** (approx. ≤ 4096 ULP)


### How accuracy modes are encoded 

You can recognize the accuracy mode of a function by the **suffix** in the function symbol:

- **`_u10`** → High accuracy  
  Example: `armpl_vcosq_f32_u10`  
  Ensures results within **1 Unit in the Last Place (ULP)**.

- *(no suffix)* → Default accuracy  
  Example: `armpl_vcosq_f32`  
  Keeps errors within **3.5 ULP** - balancing precision and performance.

- **`_umax`** → Low accuracy/max performance  
  Example: `armpl_vcosq_f32_umax`  
  Prioritizes speed, tolerating errors up to **4096 ULP**, or roughly **11 correct bits** in single-precision.


## When to use each mode

Selecting an appropriate accuracy level helps avoid unnecessary compute cost while preserving output quality where it matters.


### High accuracy (≤ 1 ULP)

Use when bit-level correctness matters. These routines employ advanced algorithms (such as high-degree polynomials, tight range reduction, or FMA usage) and are ideal for:

- **Scientific computing**
  such as simulations or finite element analysis
- **Signal processing pipelines** [1,2]
  particularly recursive filters or transform 
- **Validation and reference implementations**

While slower, these functions provide **near-bitwise reproducibility** — critical for validation and scientific fidelity.

### Default accuracy (≤ 3.5 ULP)

The default mode strikes a **practical balance** between performance and numerical fidelity. It’s optimized for:

- **General-purpose math libraries**
- **Analytics workloads** [3]
  such as log or sqrt during feature extraction 
- **Inference pipelines** [4]
  especially on edge devices where latency is critical

Also suitable for many **scientific workloads** that can tolerate modest error in exchange for **faster throughput**.


### Low accuracy / max performance (≤ 4096 ULP)

This mode trades precision for speed — aggressively. It's designed for:

- **Games, graphics, and shaders** [5]
  such as approximating sin or cos for animation curves
- **Monte Carlo simulations**  
  where statistical convergence outweighs per-sample accuracy [6]
- **Genetic algorithms, audio processing, and embedded DSP**

Avoid in control-flow-critical code or where errors might compound or affect control flow.


## Summary

| Accuracy Mode | Libamath example          | Approx. Error   | Performance | Typical Applications                                      |
|---------------|------------------------|------------------|-------------|-----------------------------------------------------------|
| `_u10`        | _ZGVnN4v_cosf_u10       | ≤1.0 ULP         | Low         | Scientific computing, backpropagation, validation |
| *(default)*   | _ZGVnN4v_cosf           | ≤3.5 ULP         | Medium      | General compute, analytics, inference              |
| `_umax`       | _ZGVnN4v_cosf_umax      | ≤4096 ULP      | High        | Real-time graphics, DSP, approximations, simulations |



{{% notice  Tip %}}
If your workload has mixed precision needs, you can *selectively call different accuracy modes* for different parts of your pipeline. Libamath lets you tailor precision where it matters — and boost performance where it doesn’t.
{{% /notice %}}


## References
1. Higham, N. J. (2002). *Accuracy and Stability of Numerical Algorithms* (2nd ed.). SIAM.

2. Texas Instruments. *Overflow Avoidance Techniques in Cascaded IIR Filter Implementations on the TMS320 DSPs*. Application Report SPRA509, 1999.
https://www.ti.com/lit/pdf/spra509

3. Ma, S., & Huai, J. (2019). *Approximate Computation for Big Data Analytics*. arXiv:1901.00232.
https://arxiv.org/pdf/1901.00232

4. Gupta, S., Agrawal, A., Gopalakrishnan, K., & Narayanan, P. (2015). *Deep Learning with Limited Numerical Precision*. In Proceedings of the 32nd International Conference on Machine Learning (ICML), PMLR 37.
https://proceedings.mlr.press/v37/gupta15.html

5. Unity Technologies. *Precision Modes*. Unity Shader Graph Documentation.  
[https://docs.unity3d.com/Packages/com.unity.shadergraph@17.1/manual/Precision-Modes.html](https://docs.unity3d.com/Packages/com.unity.shadergraph@17.1/manual/Precision-Modes.html)

6. Croci, M., Gorman, G. J., & Giles, M. B. (2021). *Rounding Error using Low Precision Approximate Random Variables*. arXiv:2012.09739.
https://arxiv.org/abs/2012.09739

