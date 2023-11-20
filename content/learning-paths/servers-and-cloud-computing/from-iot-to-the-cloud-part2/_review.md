---
review:
    - questions:
        question: >
            1.	Which tab do you use to configure port mapping in the Azure Container Instance?
        answers:
            - networking
            - port configuration
            - port mapping
            - network configuration

        correct_answer: 1                    
        explanation: >
            To configure port mapping you use the Networking tab of the wizard, which you use to provision the Azure Container Instance.

    - questions:
        question: >
            2.	What do you need to deploy a container from the Azure Container Registry to the Azure Container instance?
        answers:
            - provide Docker credentials
            - enable Admin account (correct) in Azure Container Registry
            - use dotnet run command
            - use the docker run command

        correct_answer: 2
        explanation: >
            Azure Container Instance requires Admin account to be enabled, when deploying images from the Azure Container Registry



# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
