---
review:
    - questions:
        question: >
            Which of the following is a key benefit of Snort3's multithreading support?
        answers:
            - It allows Snort to detect encrypted traffic.
            - It improves packet processing performance 
            - It enables Snort to be run on legacy hardware
            - It support multiple rule sets at the same time.
        correct_answer: 2                    
        explanation: >
            It improves packet processing performance by parallelizing tasks.

    - questions:
        question: >
            Which parameter is used to enable multithreading in Snort3?
        answers:
            - --max-packet-threads
            - --enable-threads
            - --enable-multithreading
            - --packet-loop
        correct_answer: 1                   
        explanation: >
            --max-packet-threads parameter is used to enable and configure multithreading.
               
    - questions:
        question: >
            In Snort 3, which DAQ (Data Acquisition) module is used to read capture files for packet processing?
        answers:
            - afpacket
            - vpp
            - dump
            - pcap
        correct_answer: 3          
        explanation: >
            The dump module in Snort3 is used to read capture files (such as .pcap or .pcapng files) for offline packet analysis. 



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
