---

title: KleidiAI

weight: 7

### FIXED, DO NOT MODIFY

layout: learningpathall

---

## KleidiAI

The Voice Assistant application combines local LLM inference and speech recognition - both computationally demanding tasks that have been optimized for Arm platforms using the efficient libraries [Llama.cpp](https://github.com/ggml-org/llama.cpp) and [KleidiAI library](https://gitlab.arm.com/kleidi/kleidiai).

KleidiAI is an open-source library of highly tuned micro-kernels for AI workloads on Arm CPUs. These routines are optimized to exploit specific Arm hardware features for maximum performance.

The KleidiAI library is designed for easy integration into C or C++ machine learning (ML) and AI frameworks. Developers looking to incorporate specific micro-kernels into their projects can include the corresponding `.c` and `.h` files associated with those micro-kernels and a common header file.

### Compare the performance without KleidiAI

By default, the Voice Assistant is built with KleidiAI support on Arm platforms, but this can be disabled if you want to compare the performance to a raw implementation.

To disable KleidiAI during build:

* Add `-PkleidiAI=false` to your Gradle command:`./gradlew build -PkleidiAI=false`.
* Or, add this to your top-level `gradle.properties` file: `kleidiAI=false`.  

### Why use KleidiAI?

KleidiAI simplifies development by abstracting away low-level optimization: developers can write high-level code while the KleidiAI library selects the most efficient implementation at runtime based on the target hardware. This is possible thanks to its deeply optimized micro-kernels tailored for Arm architectures.

As newer versions of the architecture become available, KleidiAI becomes even more powerful: simply updating the library allows applications like the multimodal Voice Assistant to take advantage of the latest architectural improvements such as SME2, without requiring any code changes. This means better performance on newer devices with no additional effort from developers.

Now that you can build the Voice Assistant with and without KleidiAI, you can test out the benchmarking functionality it provides.
