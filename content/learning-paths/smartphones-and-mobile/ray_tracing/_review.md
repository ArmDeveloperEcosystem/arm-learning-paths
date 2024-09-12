---
review:
    - questions:
        question: >
            Which is the recommended way to do ray traversal on Arm GPUs?
        answers:
            - Ray query
            - Ray tracing pipeline
        correct_answer: 1
        explanation: >
            Ray query is the most efficient way to implement ray traversal on Arm GPUs.

    - questions:
        question: >
            Select the correct statement:
        answers:
            - A TLAS contains the model geometry
            - A BLAS uses instances to group other TLASes
            - A BLAS contains the model geometry
        correct_answer: 3
        explanation: >
            BLASes (Bottom-Level Acceleration Structures) contain the geometry data, usually as triangles. TLASes (Top-Level Accelerations Structures) contain other BLASes and use instances to group and link them with other properties.

    - questions:
        question: >
            How should we design the acceleration structure?
        answers:
            - Empty space does not matter, reduce BLAS overlap.
            - Minimize empty space and minimize overlap.
            - BLAS overlap does not matter, reduce empty space.
            - On Arm GPUs, neither empty space nor BLAS overlap matters.
        correct_answer: 2
        explanation: >
            On ray tracing, the quality of your acceleration structure can have a huge performance impact. Try to reduce overlap across BLASes and reduce empty space inside a BLAS as much as possible.

    - questions:
        question: >
            Is bindless necessary for ray tracing?
        answers:
            - You do not need it for shadows, but it is needed for reflections and refractions.
            - Technically no, but you need it to implement our effects.
            - It is not needed, but it makes implementing our effects a lot easier.
        correct_answer: 3
        explanation: >
            Bindless or descriptor indexing is independent of ray tracing. It is possible to implement our ray tracing effects without using it, however it will make it very easy and simple to access the data of the intercepted objects. This helps a lot when implementing reflections and refractions.

    - questions:
        question: >
            Can reflections handle objects outside the screen?
        answers:
            - Ray tracing reflections can reflect objects not on the screen but Screen Space Reflections can only reflect objects on the screen.
            - Both Screen Space Reflections and ray tracing reflections can reflect objects not on the screen.
            - Neither Screen Space Reflections or ray tracing reflections can reflect objects on the screen.
            - Ray tracing reflections can only reflect objects on the screen but Screen Space Reflections can reflect objects not on the screen.
        correct_answer: 1
        explanation: >
             Screen Space Reflections obtains the information from the G-buffer so it can only reflect object currently on the screen. Ray tracing reflections offer better quality since they can handle any object in the acceleration structure, including objects not on the screen.

    - questions:
        question: >
            Which sentence is true for our ray tracing effects?
        answers:
            - In ray tracing shadows and reflections, you use bindless to retrieve the material of the intercepted object and illuminate it.
            - In ray tracing shadows, you do not care about which objects you hit, only whether you hit an object or not.
            - In ray tracing reflections, you can use the flag gl_RayFlagsTerminateOnFirstHitEXT.
        correct_answer: 2
        explanation: >
            In ray tracing reflections, you need to know which object you are hitting to retrieve its material and illuminate it. In ray tracing shadows, you do not care which exact object you hit, just whether you hit an object at all. This allows us to enable the gl_RayFlagsTerminateOnFirstHitEXT optimization for shadows but not for reflections.


    - questions:
        question: >
            What is the difference between transparency and refraction?
        answers:
            - Light goes through a transparent object in a straight line, but refractions bend the light.
            - None, refractions are how transparency is implemented in ray tracing.
            - Refractions are a faster way to implement transparency.
        correct_answer: 1
        explanation: >
            In a transparent material, light goes through in a straight line, so light rays enter and exit the material in the same direction. Refractions bend the light inside the object, so the ray exits the object in a different direction. We can use refractions to simulate ray tracing transparency, however there are simpler, more efficient ways.

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
