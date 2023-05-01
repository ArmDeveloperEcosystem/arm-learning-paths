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
            Does PaddleOCR use configuration files(.yml) to control network training and evaluation parameters?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1                     
        explanation: >
            PaddleOCR uses configuration files(.yml) to control network training and evaluation parameters. In the configuration file, you can set the parameters for building the model, optimizer, loss function, and model pre- and post-processing. PaddleOCR reads these parameters from the configuration file, and then forms a complete training process to complete the model training.

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
            What happens to operators when you specify --target=cmsis-nn,c ... while using TVMC to compile the model?
        answers:
            - "Operators offload to standard C library"
            - "Operators offload to CMSIS-NN library"
            - "Operators which are supported by Arm’s CMSIS-NN library will be offloaded to a CMSIS–NN kernel and the rest will fall back to standard C library."
        correct_answer: 3                    
        explanation: >
            By specifying --target=cmsis-nn,c, the operators supported by Arm’s CMSIS-NN library will be offloaded to a CMSIS–NN kernel which best makes use of underlying Arm hardware acceleration. All other operators fall back to standard C library implementations.
            
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
