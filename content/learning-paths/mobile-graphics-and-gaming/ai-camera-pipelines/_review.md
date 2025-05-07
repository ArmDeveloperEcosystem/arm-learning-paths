---
review:
    - questions:
        question: >
            What is KleidiAI?
        answers:
            - An anime about a little AI lost in a giant world.
            - A software library
        correct_answer: 2
        explanation: >
            KleidiAI is an open-source software library that provides optimized,
            performance-critical micro-kernels for artificial intelligence (AI)
            workloads tailored for Arm processors.

    - questions:
        question: >
            How does KleidiAI optimize performance?
        answers:
            - Lots of magic, and let's be honest, a bit of hard work.
            - It takes advantage of various available Arm processor architectural features.
        correct_answer: 2
        explanation: >
            Processor architectural features, e.g., ``FEAT_DotProd``, when implemented, enable
            the software to use specific instructions dedicated to efficiently performing some
            tasks or computations. For example, ``FEAT_DotProd`` adds the
            ``UDOT`` and ``SDOT`` 8-bit dot product instructions, which are critical for
            improving the performance of dot product computations.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---