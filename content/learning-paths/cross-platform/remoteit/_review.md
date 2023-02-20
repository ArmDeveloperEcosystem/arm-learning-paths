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
        Enabling Remote.It on devices allows anyone on the public Internet to access the device.
      answers:
        - "True"
        - "False"
      correct_answer: 2
      explanation: >
        Remote.It provides connectivity to devices without a public IP address or open ports or port forwarding. Remote.It connections are private between the target and the connecting client.

  - questions:
      question: >
        Remote.It provides simple, secure connectors between computers, as long as both computers run the same operating system.
      answers:
        - "True"
        - "False"
      correct_answer: 2
      explanation: >
        Remote.it runs on a variety of operating systems and Arm hardware. Any operating systems supported by Remote.It can be used and the initiator and target devices do not need to have the same operating system.
  - questions:
      question: >
        Remote.It connects users to remote devices regardless of the location or network configuration.
      answers:
        - "True"
        - "False"
      correct_answer: 1
      explanation: >
        Remote.it works on all types of network backhauls such as traditional cable/DSL, cellular and satellite connections because Remote.It doesn't need a unique public IP address which are often not available on cellular or satellite networks which use CGNAT.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review" # Always the same title
weight: 20 # Set to always be larger than the content in this path
layout: "learningpathall" # All files under learning paths have this same wrapper
---
