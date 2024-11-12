---
review:
    - questions:
        question: >
            What is the purpose of garbage collection?
        answers:
            - To manage memory by automatically reclaiming unused objects
            - To manually manage memory allocation
        correct_answer: 1                    
        explanation: >
            Garbage collection is used to manage memory by automatically reclaiming memory occupied by objects that are no longer in use, thus preventing memory leaks and optimizing memory usage.

    - questions:
        question: >
            Which JVM flag can be used to enable detailed garbage collection logging?
        answers:
            - -XX:+UseG1GC
            - -XX:+PrintGCDetails
        correct_answer: 2                    
        explanation: >
            The flag -XX:+PrintGCDetails enables detailed logging of garbage collection events, which helps in monitoring and tuning the GC performance.

    - questions:
        question: >
            Which garbage collector is best suited for applications requiring very low latency in a heavily multi-threaded application?
        answers:
            - Serial GC
            - ZGC
        correct_answer: 2                    
        explanation: >
            ZGC (Z Garbage Collector) is designed for applications requiring very low latency, as it aims to keep pause times below 10 milliseconds even for large heaps.




# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
