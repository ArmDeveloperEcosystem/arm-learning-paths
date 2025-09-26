---
title: Migrating SIMD code to the Arm architecture
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Vectorization on x86 vs. Arm

Migrating SIMD (Single Instruction, Multiple Data) code from x86 extensions to Arm extensions is an important task for software developers aiming to optimize performance on Arm platforms. 

Understanding the mapping between x86 instruction sets like SSE, AVX, and AMX to Arm's NEON, SVE, and SME extensions is essential for ensuring portability and high performance. This Learning Path provides an overview to help you design a migration plan, leveraging Arm features such as scalable vector lengths and advanced matrix operations, to effectively adapt your code.

Vectorization lets one instruction process multiple data elements simultaneously. It drives performance in HPC, AI/ML, signal processing, and data analytics.

Both x86 and Arm processors offer rich SIMD capabilities, but they differ in philosophy and design. The x86 architecture provides fixed-width vector units of 128, 256, and 512 bits. The Arm architecture offers a mix of fixed-width, for NEON,  and scalable vectors for SVE and SME ranging from 128 to 2048 bits.  

If you are interested in migrating SIMD software to Arm, understanding these differences ensures portable, high-performance code.

## Arm vector and matrix extensions

### NEON

NEON is a 128-bit SIMD extension available across all Armv8 cores, including both mobile and Neoverse platforms. It is particularly well-suited for multimedia processing, digital signal processing (DSP), and packet processing workloads. Conceptually, NEON is equivalent to x86 SSE or AVX-128, making it the primary target for migrating SSE workloads. Compiler support for auto-vectorization to NEON is mature, simplifying the migration process for developers.

### Scalable Vector Extension (SVE)

SVE introduces a revolutionary approach to SIMD with its vector-length agnostic (VLA) design. Registers in SVE can range from 128 to 2048 bits, with the exact width determined by the hardware implementation in multiples of 128 bits. This flexibility allows the same binary to run efficiently across different hardware generations. SVE also features advanced capabilities like per-element predication, which eliminates branch divergence, and native support for gather/scatter operations, enabling efficient handling of irregular memory accesses. While SVE is ideal for high-performance computing (HPC) and future-proof portability, developers must adapt to its unique programming model, which differs significantly from fixed-width SIMD paradigms. SVE is most similar to AVX-512 on x86, offering greater portability and scalability.

### Scalable Matrix Extension (SME)

SME is designed to accelerate matrix multiplication and is similar to AMX. Unlike AMX, which relies on dot-product-based operations, SME employs outer-product-based operations, providing greater flexibility for custom AI and HPC kernels. SME integrates seamlessly with SVE, utilizing scalable tiles and a streaming mode to optimize performance. It is particularly well-suited for AI training and inference workloads, as well as dense linear algebra in HPC applications. 

## x86 vector and matrix extensions

### Streaming SIMD Extensions (SSE)

The SSE instruction set provides 128-bit XMM registers and supports both integer and floating-point SIMD operations. Despite being an older technology, SSE remains a baseline for many libraries due to its widespread adoption. 

However, its fixed-width design and limited throughput make it less competitive compared to more modern extensions like AVX. When migrating code from SSE to Arm, developers will find that SSE maps well to Arm NEON, enabling a relatively straightforward transition.

### Advanced Vector Extensions (AVX)

The AVX extensions introduce 256-bit YMM registers with AVX and 512-bit ZMM registers with AVX-512, offering significant performance improvements over SSE. Key features include Fused Multiply-Add (FMA) operations, masked operations in AVX-512, and VEX/EVEX encodings that allow for more operands and flexibility. 

Migrating AVX code to Arm requires careful consideration, as AVX maps to NEON for up to 128-bit operations or to SVE for scalable-width operations. Since SVE is vector-length agnostic, porting AVX code often involves refactoring to accommodate this new paradigm.

### Advanced Matrix Extensions (AMX)

AMX is a specialized instruction set designed for accelerating matrix operations using dedicated matrix-tile registers, effectively treating 2D arrays as first-class citizens. It is particularly well-suited for AI workloads, such as convolutions and General Matrix Multiplications (GEMMs). 

When migrating AMX workloads to Arm, you can leverage Arm SME, which conceptually aligns with AMX but employs a different programming model based on outer products rather than dot products. This difference requires you to adapt their code to fully exploit SME's capabilities.

## Comparison tables

## SSE vs. NEON

| Feature               | SSE                                                      | NEON                                                      |
|-----------------------|---------------------------------------------------------------|----------------------------------------------------------------|
| **Register width**     | 128-bit (XMM registers)                                       | 128-bit (Q registers)                                           |
| **Vector length model**| Fixed 128 bits                                                | Fixed 128 bits                                                 |
| **Predication / masking**| Minimal predication; SSE lacks full mask registers           | Conditional select instructions; no hardware mask registers   |
| **Gather / Scatter**   | No native gather/scatter (introduced in AVX2 and later)       | No native gather/scatter; requires software emulation         |
| **Instruction set scope**| Arithmetic, logical, shuffle, blend, conversion, basic SIMD  | Arithmetic, logical, shuffle, saturating ops, multimedia, crypto extensions (AES, SHA)|
| **Floating-point support**| Single and double precision floating-point SIMD operations   | Single and double precision floating-point SIMD operations     |
| **Typical applications**| Legacy SIMD workloads; general-purpose vector arithmetic      | Multimedia processing, DSP, cryptography, embedded compute    |
| **Extensibility**      | Extended by AVX/AVX2/AVX-512 for wider vectors and advanced features| NEON fixed at 128-bit vectors; ARM SVE offers scalable vectors but is separate |
| **Programming model**  | Intrinsics supported in C/C++; assembly used for optimization | Intrinsics widely used; inline assembly less common            |


## AVX vs. SVE (SVE2)

| Feature               | x86: AVX / AVX-512                                      | ARM: SVE / SVE2                                               |
|-----------------------|---------------------------------------------------------|---------------------------------------------------------------|
| **Register width**     | Fixed: 256-bit (YMM), 512-bit (ZMM)                     | Scalable: 128 to 2048 bits (in multiples of 128 bits)         |
| **Vector length model**| Fixed vector length; requires multiple code paths or compiler dispatch for different widths | Vector-length agnostic; same binary runs on any hardware vector width |
| **Predication / masking**| Mask registers for per-element operations (AVX-512)    | Rich predication with per-element predicate registers          |
| **Gather/Scatter**    | Native gather/scatter support (AVX2 and AVX-512)         | Native gather/scatter with efficient implementation across vector widths |
| **Key operations**    | Wide SIMD, fused multiply-add (FMA), conflict detection, advanced masking | Wide SIMD, fused multiply-add (FMA), predicated operations, gather/scatter, reduction operations, bit manipulation |
| **Best suited for**   | HPC, AI workloads, scientific computing, data analytics  | HPC, AI, scientific compute, cloud and scalable workloads     |
| **Limitations**       | Power and thermal throttling on heavy 512-bit usage; complex software ecosystem | Requires vector-length agnostic programming style; ecosystem and hardware adoption still maturing |

## AMX vs. SME

| Feature               | x86: AMX                                                | ARM: SME                                                   |
|-----------------------|---------------------------------------------------------|------------------------------------------------------------|
| **Register width**     | Tile registers with fixed dimensions: 16×16 for BF16, 64×16 for INT8 (about 1 KB total) | Scalable matrix tiles integrated with SVE, implementation-dependent tile dimensions |
| **Vector length model**| Fixed tile dimensions based on data type                    | Implementation-dependent tile dimensions, scales with SVE vector length |
| **Predication / masking**| No dedicated predication or masking in AMX tiles      | Predication integrated through SVE predicate registers      |
| **Gather/Scatter**    | Not supported within AMX; handled by other instructions | Supported via integration with SVE’s gather/scatter features |
| **Key operations**    | Focused on dot-product based matrix multiplication, optimized for GEMM and convolutions | Focus on outer-product matrix multiplication with streaming mode for dense linear algebra |
| **Best suited for**   | AI/ML workloads such as training and inference, specifically GEMM and convolution kernels | AI/ML training and inference, scientific computing, dense linear algebra workloads |
| **Limitations**       | Hardware and software ecosystem currently limited (primarily Intel Xeon platforms) | Emerging hardware support; compiler and library ecosystem in development |


## Key Differences for Developers  

When migrating from x86 SIMD extensions to Arm SIMD, there are several important architectural and programming differences for you to consider.

### Vector Length Model

x86 SIMD extensions such as SSE, AVX, and AVX-512 operate on fixed vector widths, 128, 256, or 512 bits. This often necessitates multiple code paths or compiler dispatch techniques to efficiently exploit available hardware SIMD capabilities. Arm NEON, similar to SSE, uses a fixed 128-bit vector width, making it a familiar, fixed-size SIMD baseline. 

In contrast, Arm’s Scalable Vector Extension (SVE) and Scalable Matrix Extension (SME) introduce a vector-length agnostic model. This allows vectors to scale from 128 bits up to 2048 bits depending on the hardware, enabling the same binary to run efficiently across different implementations without modification.

### Programming and Intrinsics

x86 offers a comprehensive and mature set of SIMD intrinsics that increase in complexity especially with AVX-512 due to advanced masking and lane-crossing operations. Arm NEON intrinsics resemble SSE intrinsics and are relatively straightforward for porting existing SIMD code. However, Arm SVE and SME intrinsics are designed for a more predicated and vector-length agnostic style of programming. 

When migrating to SVE/SME you are encouraged to leverage compiler auto-vectorization with predication support, moving away from heavy reliance on low-level intrinsics to achieve scalable, portable performance.

### Matrix Acceleration

For matrix computation, AMX provides fixed-size tile registers optimized for dot-product operations such as GEMM and convolutions. In comparison, Arm SME extends the scalable vector compute model with scalable matrix tiles designed around outer-product matrix multiplication and novel streaming modes. 

SME’s flexible, hardware-adaptable tile sizes and tight integration with SVE’s predication model provide a highly adaptable platform for AI training, inference, and scientific computing. 

Both AMX and SME are currently available on limited set of platforms. 

### Overall Summary

Migrating from x86 SIMD to Arm SIMD entails embracing Arm’s scalable and predicated SIMD programming model embodied by SVE and SME, which supports future-proof, portable code across a wide range of hardware. 

NEON remains important for fixed-width SIMD similar to SSE but may be less suited for emerging HPC and AI workloads that demand scale and flexibility. 

You need to adapt to Arm’s newer vector-length agnostic programming and tooling to fully leverage scalable SIMD and matrix architectures. 

Understanding these key differences in vector models, programming paradigms, and matrix acceleration capabilities helps you migrate and achieve good performance on Arm. 

## Migration tools

There are tools and libraries that help translate SSE intrinsics to NEON intrinsics, which can shorten the migration effort and produce efficient Arm code. These libraries enable many SSE operations to be mapped to NEON equivalents, but some SSE features have no direct NEON counterparts and require workarounds or redesign. 

Overall, NEON is the standard for SIMD on Arm much like SSE for x86, making it the closest analogue for porting SIMD-optimized software from x86 to ARM.

[sse2neon](https://github.com/DLTcollab/sse2neon) is an open-source header library that provides a translation layer from Intel SSE2 intrinsics to Arm NEON intrinsics. It enables many SSE2-optimized codebases to be ported to Arm platforms with minimal code modification by mapping familiar SSE2 instructions to their NEON equivalents. 


[SIMD Everywhere (SIMDe)](https://github.com/simd-everywhere/simde) is a comprehensive, header-only library designed to ease the transition of SIMD code between different architectures. It provides unified implementations of SIMD intrinsics across x86 SSE/AVX, Arm NEON, and other SIMD instruction sets, facilitating portable and maintainable SIMD code. SIMDe supports a wide range of SIMD extensions and includes implementations that fall back to scalar code when SIMD is unavailable, maximizing compatibility. 


[Google Highway](https://github.com/google/highway) is a high-performance SIMD optimized vector hashing and data processing library designed by Google. It leverages platform-specific SIMD instructions, including Arm NEON and x86 AVX, to deliver fast, portable, and scalable hashing functions and vector operations. Highway is particularly well-suited for large-scale data processing, machine learning, and performance-critical applications requiring efficient SIMD usage across architectures. 

You can also review [Porting architecture specific intrinsics](/learning-paths/cross-platform/intrinsics/) for more information.