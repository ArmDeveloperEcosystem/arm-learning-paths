---
review:
    - questions:
        question: >
            What do you use to specify which ports are open in the Virtual Machine?
        answers:
            - Network Security Group 
            - Azure Firewall
            - Microsoft Firewall
        correct_answer: 1                    
        explanation: >
            Network Security Group is the Azure resource you can use to filter network traffic. 

    - questions:
        question: >
            Which command is used to build and start the .NET app from the command line?
        answers:
            - .net run
            - .net start
            - dotnet run
            - dotnet start

        correct_answer: 3
        explanation: >
            .NET CLI is the command-line tool you use to build and run applications. The tool is accessed by dotnet command. To run the application you use the run subcommand. 

    - questions:
        question: >
            Which command do you use to create a Docker image?
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
            What do you need to push the image to the remote registry?
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
