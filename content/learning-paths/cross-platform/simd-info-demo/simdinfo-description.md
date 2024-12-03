---
title: SIMD.info Features
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

#### SIMD.info categories of information
**[SIMD.info](https://simd.info/)** offers a variety of powerful tools to enable developers to work more efficiently with SIMD code across different architectures. 

With a database of over 10,000 intrinsics, it provides valuable detailed information to support effective SIMD development.

For each intrinsic, SIMD.info provides information in the following categories:

* **Purpose**: a brief description of what the intrinsic does and the primary use case.

* **Result**: an explanation of the output or result of the intrinsic.

* **Example**: a code snippet demonstrating how to use the intrinsic.

* **Prototypes**: function prototypes for different programming languages (currently C/C++).

* **Assembly Instruction**: the corresponding assembly instruction that the intrinsic uses.

* **Notes**: any further information about the intrinsic, such as caveats.

* **Architecture**: a list of architecture that supports the intrinsic.

* **Links to official documentation**.

This information ensures that you have all the necessary resources to effectively use and port SIMD instructions across different platforms. Each feature is designed to simplify navigation, improve the search for equivalent instructions, and foster a collaborative environment for knowledge-sharing.

#### Tree-based navigation
SIMD.info uses a clear, hierarchical layout to present the instructions. It categorizes instructions into high-level groups such as **Arithmetic**, which are then further divided into specific subcategories such as **Vector Add**, and **Vector Subtract**. 

This organized structure enables you to browse through SIMD instruction sets across various platforms, allowing you to efficiently find and access the instructions that you need. Below is an example of the tree structure:
  
     - Arithmetic 
     - Arithmetic (Complex Numbers) 
       - Boolean Logic & Bit Manipulation 
       - Boolean AND 
       - Boolean AND NOT 
            - Boolean AND NOT 128-bit vector 
            - Boolean AND NOT 16-bit signed integers 
            - Boolean AND NOT 16-bit unsigned integers 
            - Boolean AND NOT 256-bit vector
            - Boolean AND NOT 32-bit float 
            - Boolean AND NOT 32-bit signed integers 
                - AVX512: mm512_andnot_epi32 
                - NEON: vbic_s32
                - NEON: vbicq_s32 
                - VSX: vec_andc 
        - Bit Clear 
        - XOR

#### Advanced search functionality
With its robust search engine, SIMD.info allows you to either search for a specific intrinsic, for example `vaddq_f64`, or enter more general terms, for example "How to add 2 vectors," and it returns a list of the corresponding intrinsics. 

You can also filter results based on the specific engine you're working with, such as NEON, SSE4.2, AVX, AVX512, or VSX. This functionality streamlines the process of finding the right commands tailored to your needs.

#### Comparison tools
This feature lets you directly compare SIMD instructions from different, or the same, platforms side by side, offering a clear view of the similarities and differences. It’s a helpful tool for porting code across architectures, as it ensures accuracy and efficiency.

#### Discussion forum 
The integrated discussion forum, powered by **[Disqus](https://disqus.com/)**, allows users to ask questions, share insights, and troubleshoot problems together. This community-driven space ensures that you’re never stuck on a complex issue without support. It fosters collaboration and knowledge-sharing among SIMD developers. Imagine something like **[StackOverflow](https://stackoverflow.com/)** but specific to SIMD intrinsics.

Now let's look at these features in the context of a real example.
