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
            Lower IPC indicates a program will complete in less time.
        answers:
            - "True"
            - "False"
        correct_answer: 2
        explanation: >
            Lower IPC indicates a stalled pipeline. The Neoverse N1 is capable of up to 4 instructions per cycle and higher IPC means it is retiring more instructions in each cycle.

    - questions:
        question: >
            High backend stall rate is a signal to look at data cache metrics and the memory system. 
        answers:
            - "True"
            - "False"
        correct_answer: 1                  
        explanation: >
            If you see a high backend stall rate you should investigate L1 data cache and unified L2 and last level caches, instruction mix, and data TLB.
               
    - questions:
        question: >
            Which tool is provided by the Arm Telemetry Solution?
        answers:
            - "perf"
            - "topdown-tool"
            - "topdown-perf"
            - "strace"
        correct_answer: 2                    
        explanation: >
            Telemetry Solution provides topdown-tool.




# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
