---

title: KleidiAI

weight: 7

### FIXED, DO NOT MODIFY

layout: learningpathall

---

The Voice Assistant application combines local LLM inference and speech recognition - both computationally demanding tasks that have been optimized for Arm platforms using efficient libraries like [Llama.cpp](https://github.com/ggml-org/llama.cpp) and KleidiAI.

Speech recognition is also a computation-intensive task and has been optimized for Arm processors as well.

## KleidiAI

This application uses the [KleidiAI library](https://gitlab.arm.com/kleidi/kleidiai) by default for optimized performance on Arm processors.

[KleidiAI](https://gitlab.arm.com/kleidi/kleidiai) is an open-source library of highly tuned micro-kernels for AI workloads on Arm CPUs. These routines are optimized to exploit specific Arm hardware features for maximum performance.

The KleidiAI library has been designed for easy adoption into C or C++ machine learning (ML) and AI frameworks. Developers looking to incorporate specific micro-kernels into their projects can simply include the corresponding `.c` and `.h` files associated with those micro-kernels and a common header file.

### Compare the performance without KleidiAI

By default, the Voice Assistant is built with KleidiAI support on Arm platforms, but this can be disabled if you want to compare the performance to a raw implementation.

To disable KleidiAI during build:

* Add `-PkleidiAI=false` to your Gradle command:`./gradlew build -PkleidiAI=false`.
* Or, add this to your top-level `gradle.properties` file: kleidiAI=false.  

### Why use KleidiAI?

A significant benefit of using KleidiAI is that it enables the developer to work at a relatively high level, leaving the KleidiAI library to select the best implementation at runtime to perform the computation in the most efficient way on the current target. This is a great advantage because a significant amount of work has gone into optimizing those micro-kernels.

It becomes even more powerful when newer versions of the architecture become available: a simple update of the KleidiAI library used by the Voice Assistant will automatically give it access to newer hardware features as they become available. An example of such a feature deployment is happening with SME2, which means in the near future, the Voice Assistant will be able to benefit from improved performance — on devices that have implemented SME2 — with no further effort required from the developer.