---
review:
    - questions:
        question: >
            How does SME2 speedup matrix multiplication ?
        answers:
            - Outer product
            - Quantum physics
        correct_answer: 1
        explanation: >
            The matrix multiplication operation can be expressed as a sum of outer products,
            which allows the SME engine to perform many multiplication/accumulations at once.

    - questions:
        question: >
            Why is the ZA storage so important for SME2 ?
        answers:
            - It's infinite
            - It holds a 2D view of matrices
        correct_answer: 2
        explanation: >
            The ZA storage offers a 2D view of part of a matrix, a.k.a a tile. SME can operate
            on complete tiles, or on horizontal / vertical slices of the tiles, which is a useful
            and often used feature in numerous algorithms. ZA storage is finite and has size SVL x SVL.

    - questions:
        question: >
            What are predicates ?
        answers:
            - Parts of a sentence or clause containing a verb and stating something about the subject
            - They select the active lanes in a vector operation
            - It's just another word for flags from the Processor Status Register (PSR)
        correct_answer: 2
        explanation: >
            SVE is a predicate centric architecture. Predicates allow Vector Length Agnosticism (VLA),
            they support complex nested conditions and loops and reduce vector loop management
            overhead by allowing lane predication in vector operations. Predicates have their own
            dedicated registers.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
