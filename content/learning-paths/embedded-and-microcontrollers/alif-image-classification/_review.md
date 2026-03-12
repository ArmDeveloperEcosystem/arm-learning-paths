---
title: Knowledge check
weight: 20

layout: "learningpathall"

review:
    - questions:
        question: "Which NPU peripheral on the Alif Ensemble E8 is used for the Ethos-U85?"
        explanation: "NPU_HG (High-Grade) at base address 0x49042000 is the Ethos-U85. NPU_HP is an Ethos-U55 at a different address. Using the wrong base address causes a product mismatch error."
        correct_answer: 2
        answers:
            - "NPU_HP"
            - "NPU_HG"
            - "NPU_HE"
    - questions:
        question: "Why do some ExecuTorch libraries need to be linked with --whole-archive?"
        explanation: "Libraries like libexecutorch and libcortex_m_ops_lib contain static registration constructors that register operators and PAL symbols at startup. Without --whole-archive, the linker sees these constructors as unused and discards them, causing missing operator errors at runtime."
        correct_answer: 3
        answers:
            - "Because they are too large for normal linking"
            - "Because the linker requires it for all C++ libraries"
            - "Because they contain static registration constructors that would otherwise be discarded"
    - questions:
        question: "What does the GOT (Global Offset Table) fix in the linker script address?"
        explanation: "The precompiled ExecuTorch libraries use position-independent code (PIC) that relies on the GOT for indirect function calls and vtable lookups. If the GOT isn't copied from flash to RAM at startup, these lookups resolve to address zero, causing BusFaults."
        correct_answer: 1
        answers:
            - "BusFaults caused by uninitialized indirect function call tables"
            - "Stack overflow errors during inference"
            - "Incorrect NPU command stream alignment"
    - questions:
        question: "What input data type does the MobileNetV2 model expect?"
        explanation: "The model's first operator is cortex_m::quantize_per_tensor, which converts float32 input to int8 for the NPU. The image is stored as int8 in the header to save flash space, but the application code converts it to float32 before passing it to the model."
        correct_answer: 2
        answers:
            - "int8"
            - "float32"
            - "uint8"
---
