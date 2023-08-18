---
review:
    - questions:
        question: >
            Terraform is an infrastructure as Code (IaC) solution created by OCI?
        answers:
            - True
            - False
        correct_answer: 2                    
        explanation: >
            Terraform is not specific to OCI and was created by HashiCorp.

    - questions:
        question: >
            If I accidentally delete my instance, I can retrieve it?
        answers:
            - True
            - False
        correct_answer: 2                  
        explanation: >
            Instances that have been deleted cannot be retrieved. However, if an instance is simply stopped, you can start it again.
            
    - questions:
        question: >
            Is the Ampere (always Free) compute instance in OCI a static instance with only 2 OCPUs and 8GB of RAM ?
        answers:
            - True
            - False
        correct_answer: 2
        explanation: >
            In OCI the always Free Tier for an Ampere Compute instance is 3,000 OCPU hours and 18,000 GB hours per month for free for VM instances using 
            VM.Standard.A1.Flex shape. This is the equivalent of 4 OCPUs and 24GB of memory that can be shared between multiple instances. 
    - questions:
        question: >
            If I forgot to print the some output such as the IP address of my compute instance, do I need to destroy it and deploy (apply) it again ?
        answers:
            - No after having added the output code, just run -> terraform output
            - No after having added the output code, just run -> terraform refresh
            - Yes after having added the output code, you need to run -> terraform destroy && terraform apply
        correct_answer: 2
        explanation: >
            Once you have added the output code, you just need to run terraform refresh.
            You have also the possibilty to always display the last output (if any) using terraform output.
    - questions:
        question: >
            If I want to be able to connect from my laptop to my compute instance in OCI, in which subnet should I create it:
        answers:
            - public (default)
            - private
        correct_answer: 1
        explanation: >
            To be able to connect to a compute instance, the instance must be located
            in a public subnet where a public ip could be assigned to it. 

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
