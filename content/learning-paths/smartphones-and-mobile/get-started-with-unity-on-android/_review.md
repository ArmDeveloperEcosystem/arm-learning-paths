---
review:
    - questions:
        question: >
            What is the benefit of using Unity Hub?
        answers:
            - It provides Android support
            - It provides version control for your project
            - It provides convenient installation and maintenance of Unity versions
        correct_answer: 3
        explanation: >
            The Unity Hub also allows you to add build support for additional platforms and maintains a list of recently opened projects.

    - questions:
        question: >
            Which Unity modules are required for Android development?
        answers:
            - Android Studio
            - OpenJDK, Android SDK & Android NDK
            - Visual Studio
        correct_answer: 2
        explanation: >
            When installing Unity, we recommend you tick "Android Build Support" which installs the required modules; OpenJDK, Android SDK and Android NDK
               
    - questions:
        question: >
            What is the purpose of the Unity Profiler?
        answers:
            - Checks that your code compiles successfully
            - Measures the performance of your application and helps identify performance issues
            - Checks that your application adheres to platform guidelines
        correct_answer: 2
        explanation: >
            While the Unity Editor is a convenient way to develop your game and make sure everything is working, it is a good idea to run your project regularly on a real target device. Bottlenecks, if any, will not necessarily be the same across all devices and development platforms.

    - questions:
        question: >
            What areas of an application can be profiled using the Unity Profiler?
        answers:
            - CPU & Memory
            - CPU & Graphics
            - CPU, Memory, Graphics, Audio, UI and more!
        correct_answer: 3
        explanation: >
            The Profiler window provides information about many areas of your app, not just CPU and graphics. Developers of applications with complex user interfaces will likely find the UI section useful, particularly batch counts as they can affect rendering performance. If your application has heavy memory requirements or makes frequent smaller allocations, you may find the garbage collection statistics useful in the Memory area.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
