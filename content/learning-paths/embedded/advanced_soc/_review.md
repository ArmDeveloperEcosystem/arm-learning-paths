---
# ================================================================================
#       Edit
# ================================================================================

# Always 3 questions. Should try to test the reader's knowledge, and reinforce the key points you want them to remember.
    # question:         A one sentence question
    # answers:          The correct answers (from 2-4 answer options only). Should be surrounded by quotes.
    # correct_answer:   An integer indicating what answer is correct (index starts from 0)
    # explanation:      A short (1-3 sentence) explanation of why the correct answer is correct. Can add aditional context if desired


review:
    - questions:
        question: >
            Which of the following lines of Verilog would create an input wire named 'switch'?
        answers:
            - "switch = input wire [3:0]"
            - "input wire [3:0] switch"
            - "wire input [3:0] switch"
        correct_answer: 2
        explanation: >
            This option uses the correct Verilog syntax for adding a port for an input switch. The first operation is incorrect as it in improper Verilog syntax to creating an input wire using the '=' operator. The last option is incorrect as the ordering of the keywords is not correct.

    - questions:
        question: >
            In the lab, you wired the switch and the LED to which of the following blocks?
        answers:
            - "ZYNQ7_Processing_System"
            - "axi_gpio_asoc"
            - "Processor System Reset"
        correct_answer: 2
        explanation: >
            We connected the switch and LED to our custom AXI GPIO peripheral. For the other two options, we did not connect the switch or LED ports to their corresponding blocks.
               
    - questions:
        question: >
            In order to program the device with the design, you must complete several steps in a certain order, choose the correct option.
        answers:
            - "Generate Bitstream > Synthesis > Implementation"
            - "Implementation > Synthesis > Generate Bitstream"
            - "Synthesis > Implementation > Generate Bitstream"
        correct_answer: 3
        explanation: >
            Once the design has gone through synthesis, implementation and then had a bitstream generated, it can be deployed to an FPGA device. The others are in the wrong order - if you followed them, the generated bitstream would not be correct and the program deployed to the device may not act as expected.




# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
