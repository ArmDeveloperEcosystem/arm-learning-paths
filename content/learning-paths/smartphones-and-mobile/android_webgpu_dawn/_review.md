---
review:
    - questions:
        question: >
            What is WebGPU?
        answers:
            - A highly customized API for specific GPUs.
            - APIs designed to provide unified access to GPUs whichever the GPU vendor and operating system the application runs with.
            - APIs designed for cloud-based applications.
        correct_answer: 2                    
        explanation: >
            WebGPU is a Render Hardware Interface built on top of the various APIs provided by the driver/OS depending on your platform. This duplicated development effort is made once by the web browsers and made available to us through the webgpu.h header they provide

    - questions:
        question: >
            What is Dawn?
        answers:
            - An open-source WebGPU implementation lead by Google.
            - A community-driven WebGPU implementation.
            - A new programming language to program GPUs.
        correct_answer: 1                   
        explanation: >
            Dawn is an open-source and cross-platform implementation of the WebGPU standard, lead by Google. More precisely it implements webgpu.h that is a one-to-one mapping with the WebGPU IDL. 
               
    - questions:
        question: >
            What is Arm Streamline?
        answers:
            - A profiling tool to profile CPUs.
            - A profiling tool to profile GPUs.
            - A a comprehensive profiling software to profile both CPUs and GPUs.
        correct_answer: 3          
        explanation: >
            Streamline is an application profiler that can capture data from multiple sources, including Program Counters (PC), Samples from the hardware Performance Monitoring Unit (PMU) counters in the Arm CPU, Arm® Mali™ GPUs, and Arm Immortalis™ GPUs.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---