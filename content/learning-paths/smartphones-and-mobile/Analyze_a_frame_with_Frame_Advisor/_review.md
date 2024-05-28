---
review:
    - questions:
        question: >
            Which graphics APIs are supported by Frame Advisor when capturing data from an Android application?
        answers:
            - OpenGL ES
            - Vulkan
            - Both
        correct_answer: 3                    
        explanation: >
            Frame Advisor can collect data from applications using either OpenGL ES or Vulkan. You must select which API to use on the connection screen.

    - questions:
        question: >
            Which Frame Advisor views can you use to step through draw calls to see how the frame is built?
        answers:
            - Render Graph and Framebuffers views
            - Frame Hierarchy and Framebuffers views
            - Content Metrics and Detailed Metrics views
        correct_answer: 2                  
        explanation: >
            You can see all the render passes that make up the frame in the Frame Hierarchy view. Expand a render pass to see the draw calls within it. Step through the draw calls to see the scene being built up in the Framebuffers view.
               
    - questions:
        question: >
            The Render Graph is used to:
        answers:
            - Find render passes that are not used in the final output
            - Find output attachments that are not used in a future render pass
            - See how data flows between render passes
            - All of the above
        correct_answer: 4          
        explanation: >
            The Render Graph in Frame Advisor shows a visualization of the rendering operations that make up the frame. It shows how data flows between render passes, and how resources such as textures are produced and consumed.

    - questions:
        question: >
            How can you reduce processing cost and memory bandwidth?
        answers:
            - Reduce the number of primitives used by complex objects
            - Use software culling techniques to remove draw calls that don’t render visible changes to the framebuffer
            - Batch multiple identical draws into a single mesh or use instanced draw calls
            - Remove duplicate vertices
            - All of the above
        correct_answer: 5          
        explanation: >
            There are many ways to reduce processing cost and memory bandwidth. Frame Advisor can help you find expensive objects so that you can optimize them.



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
