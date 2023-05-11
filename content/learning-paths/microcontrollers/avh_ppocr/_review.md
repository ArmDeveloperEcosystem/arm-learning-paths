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
            Does the TVM compiler compile trained PaddlePaddle models directly?
        answers:
            - "Yes"
            - "No"
        correct_answer: 2                     
        explanation: >
            You need to export the trained PaddlePaddle model to a Paddle inference model that TVM can compile to generate code which is suitable to run on a Cortex-M processor. 
               
    - questions:
        question: >
            Which is a component of Arm Virtual Hardware Corstone-300 platform?
        answers:
            - "Cortex-M55"
            - "Cortex-M85"
            - "Cortex-M33"
        correct_answer: 1                    
        explanation: >
            Corstone-300 combines an example subsystem, complementary System IP, and software and tools to streamline SoC development. Corstone-300 leverages Cortex-M55, Arm's most AI capable Cortex-M CPU, and allows for straightforward integration of the Ethos-U55 NPU.




# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
