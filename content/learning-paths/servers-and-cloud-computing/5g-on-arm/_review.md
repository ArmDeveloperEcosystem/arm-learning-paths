---
# ================================================================================
#       Edit
# ================================================================================

# Always 3 questions. Should try to test the reader's knowledge, and reinforce the key points you want them to remember.
    # question:         A one sentence question
    # answers:          The correct answers (from 2-4 answer options only). Should be surrounded by quotes.
    # correct_answer:   An integer indicating what answer is correct (index starts from 0)
    # explanation:      A short (1-3 sentence) explanation of why the correct answer is correct. Can add additional context if desired

review:
    - questions:
        question: >
            Which server has better support of Nvidia A100X?
        answers:
            - "HPE"
            - "Foxconn"
            - "Gigabyte"
            - "WIWYNN"
            - "Supermicro"
            - "All the above"
        correct_answer: 5
        explanation: >
            The Supermicro server is designed to support A100X with correct orientation for its ethernet ports
    - questions:
        question: >
            Which statement is correct?
        answers:
            - "Regular Linux kernel is sufficient for supporting the 5G stack"
            - "Low latency Linux kernel is required for supporting 5G stack"
        correct_answer: 2                    
        explanation: >
            Low Latency Kernel minimizes the time it takes for the operating system to respond to events and processes, it is essential for the latency sensitive processes in the 5G stack.
    - questions:
        question: >
            What is the potential issue with a 2P server?        
        answers:
            - "PCIe devices sit on different node from the CPU"
            - "Cross socket communication overhead"
            - "Sometimes you can't put the PCIe device and CPU on same node"
            - "All the above"
        correct_answer: 4                    
        explanation: >
            These are all potential issues related to multiple socket servers.
    - questions:
        question: >
            What is isolcpus?
        answers:
            - "Remove the core off access"
            - "Isolate the core off limit"
            - "Reserved for real-time or other special purpose tasks"
        correct_answer: 3                    
        explanation: >
            The isolcpus setting is important for dedicated tasks that are not interfered by the kernel
    - questions:
        question: >
            How do you affinitize your program to cores?
        answers:
            - "taskset"
            - "numactl"
            - "pthread_setaffinity_np"
            - "All the above"
        correct_answer: 4                    
        explanation: >
            These are all the ways you can assign your program to cpu/cores




# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
