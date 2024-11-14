---
review:
    - questions:
        question: >
            Streamline Profiling lets you profile:
        answers:
            - Arm CPU activity
            - Arm GPU activity
            - when your Neural Network is running
            - All of the above
        correct_answer: 4                    
        explanation: >
            Streamline will show you CPU and GPU activity (and a lot more counters!), and if Custom Activity Maps are used, you can see when your Neural Network and other parts of your application are running.

    - questions:
        question: >
            Does Android Studio have a profiler?
        answers:
            - "Yes"
            - "No"
        correct_answer: 1                   
        explanation: >
            Yes, Android Studio has a built-in profiler that can be used to monitor the memory usage of your app among other things
               
    - questions:
        question: >
            Is there a way to profile what is happening inside your Neural Network?
        answers:
            - Yes, Streamline just shows you out of the box
            - No.
            - Yes, ArmNN's ExecuteNetwork can do this
            - Yes, Android Studio Profiler can do this
        correct_answer: 3          
        explanation: >
            Standard profilers don't have an easy way to see what is happening inside an ML framework to see a model running inside it. ArmNN's ExecuteNetwork can do this for TensorFlow Lite models, and ExecuTorch has tools that can do this for PyTorch models.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
