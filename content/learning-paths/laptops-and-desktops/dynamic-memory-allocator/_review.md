---
review:
    - questions:
        question: >
            What is one difference between static and dynamic memory allocation?
        answers:
            - Dynamic allocation cannot be done on embedded systems, but static
              allocation can.
            - Dynamic allocation takes place while the program is running, rather
              than when it is built.
            - Static allocation can allocate larger amounts of memory than dynamic
              allocation.
        correct_answer: 2
        explanation: >
            Both types of allocation can run on any sort of system, though the
            complexity of the dynamic allocator may change.

            Dynamic allocation is done using runtime calls, so the program can
            react to what's needed at the time. Static alloation is decided ahead
            of time instead.

            Both types of allocation have the same memory constraints as the
            system itself. So in theory at least, they could have access to the
            same amount of memory.

    - questions:
        question: >
            Do C's memory management functions like malloc and free validate the
            addresses passed to them?
        answers:
            - Never
            - Always
            - The implementation may choose to validate them, but does not have to.
        correct_answer: 3
        explanation: >
            An allocator may choose to be strict about the parameters it accepts
            but the C specification at least does not require it to be. Generally
            this strictness can be controlled with debugging or hardening options.

            When writing your own allocators, you get to decide how to handle
            invalid data.

    - questions:
        question: >
            If the allocator presented here was used mainly for very small
            allocations (less than 8 bytes), what concern would you have?
        answers:
            - That memory was being wasted because the details of each allocation
              (which take up 8 bytes) are larger than the useable space in each
              allocation.
            - That the heap walk would take an unacceptably long time due to
              the large amount of ranges.
            - That the time taken to walk the heap would increase as time went
              on, until it was eventually unacceptable.
            - All of the above.
        correct_answer: 4
        explanation: >
            Everything mentioned is a concern here, and is why some allocators
            prefer to use "pools" or "buckets" for very small allocations.

            The allocator can make assumptions about these special areas that
            reduce the time taken to find a free range, and the overhead of
            recording the information about the ranges.

            In our case, the performance of the heap would be ok to begin with.
            As the program continues, more and more small ranges pile up. Leading
            to poorer performance later.

            This is sometimes not a problem, but for real time applications like
            video game, unpredictable heap performance is a problem.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
