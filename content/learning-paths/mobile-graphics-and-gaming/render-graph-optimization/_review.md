---
review:
    - questions:
        question: >
            Suppose you are developing a game. You notice that the frame rate dips when the player performs certain actions. You suspect the cause is that the GPU has been given more complex geometry than it is able to render in the time budget for each frame. Can you use Frame Advisor's render graphs to find places where you can simplify your geometry?
        answers:
            - Yes, you can use render graphs to identify this issue
            - No, you can't use render graphs to identify this issue
        correct_answer: 2
        explanation: >
            Render graphs summarize and group information about the order of drawing operations. This summary excludes most details of the data being processed (an exception is the resolution of processed images). The Mesh view and Detailed Metrics view are better choices if you wish to identify places where your application is processing too much geometry data.

    - questions:
        question: >
            “Render graphs show all resources used while rendering a frame.” Is this statement correct?
        answers:
            - Yes, the statement is correct
            - No, the statement is incorrect
        correct_answer: 2
        explanation: >
            Render graphs show many resources (as resource nodes). However, they do not show all resources. For example, they do not show read-only resources such as read-only textures.

    - questions:
        question: >
            “Render graphs can only be generated on Arm hardware.” Is this statement correct?
        answers:
            - Yes, the statement is correct
            - No, the statement is incorrect
        correct_answer: 2
        explanation: >
            Render graphs will be generated for any data which can be captured in Frame Advisor. They are not specific to Arm hardware.

    - questions:
        question: >
            “Render graphs can be used to navigate through your API calls.” Is this statement correct?
        answers:
            - Yes, the statement is correct
            - No, the statement is incorrect
        correct_answer: 1
        explanation: >
            Frame Advisor's Render Graph view can be used as a clickable “map” of the data processed by the GPU while generating a frame. Clicking an execution node will take you to the API call relating to that node.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
