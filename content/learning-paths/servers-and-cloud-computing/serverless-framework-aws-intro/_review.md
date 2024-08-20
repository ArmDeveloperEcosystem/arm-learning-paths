---
review:
    - questions:
        question: >
            Which command do you use to invoke the Lambda function using Serverless Framework?
        answers:
            - serverless invoke <function-name>
            - serverless invoke lambda <function-name>
            - serverless invoke local --function <function-name>
        correct_answer: 3
        explanation: >
            In Serverless Framework you use serverless invoke local --function <function-name> to invoke the Lambda function

    - questions:
        question: >
            What is the serverless.yml file?
        answers:
            - It includes the structure and configuration options for setting up a Serverless service
            - It provides AWS credentials            

        correct_answer: 1
        explanation: >
            The serverless.yml file defines a Serverless service.

    - questions:
        question: >
            Is the Serverless Framework compatible only with AWS?
        answers:
            - No
            - Yes
            
        correct_answer: 1
        explanation: >
            The Serverless Framework supports multiple cloud providers such as AWS, Google Cloud, and Microsoft Azure, providing a versatile and scalable solution for modern application development

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
