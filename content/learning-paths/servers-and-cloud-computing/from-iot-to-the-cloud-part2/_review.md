---
review:
    - questions:
        question: >
            1.	Which command do you use to create a Docker image?
        answers:
            - docker create 
            - docker build
            - docker image create
            - docker image build

        correct_answer: 2                    
        explanation: >
            The docker build command enables you to build the Docker image, e.g. docker build -t people.webapp:v1 .

    - questions:
        question: >
            2.	What do you need to push the image to the remote registry?
        answers:
            - tag the image with the fully qualified registry name
            - tag the image with the subscription identifier
            - dotnet run (correct)
            - dotnet start

        correct_answer: 1
        explanation: >
            Docker uses tags for routing. So, the tag needs to include the fully qualified registry name (login server)



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
