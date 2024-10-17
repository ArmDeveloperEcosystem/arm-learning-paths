---
review:
    - questions:
        question: >
            How does the serverless.yml file facilitate the deployment and management of serverless applications and what are its key components?
        answers:
            - The serverless.yml file is used only for defining environment variables for AWS Lambda functions and it does not impact resource deployment.
            - The serverless.yml file defines the service configuration, including functions, events, and resources, enabling the Serverless Framework to automate deployment and manage cloud infrastructure.
            - The serverless.yml file serves as a configuration template for the AWS CloudFormation stack and is primarily used for setting user permissions for the serverless application.
        correct_answer: 2
        explanation: >
            serverless.yml file is used to define services, functions, and resources, and its role in automating the deployment process

    - questions:
        question: >
            What steps are involved in using the serverless deploy command and how does it ensure that all resources and functions are correctly provisioned and configured in AWS?
        answers:
            - The serverless deploy command only packages the application code into a ZIP file and uploads it to an S3 bucket without provisioning any infrastructure.
            - The serverless deploy command packages the application, generates an infrastructure template, uploads the artifacts, and executes the deployment, provisioning all defined resources and functions automatically.
            - The serverless deploy command executes the application locally and prints logs to the console but does not interact with AWS services.

        correct_answer: 2
        explanation: >
            Serverless Framework packages code, uploads it, and provisions infrastructure automatically.

    - questions:
        question: >
            How can you configure an AWS Lambda function to interact with a DynamoDB table and what are the benefits of using ES Modules and IAM roles in this context?
        answers:
            - AWS Lambda functions cannot directly interact with DynamoDB tables; they must use an intermediate service like S3 to access data.
            - You configure an AWS Lambda function to interact with a DynamoDB table by using the AWS SDK to perform read/write operations and defining IAM roles to manage permissions, while ES Modules provide a modern syntax for importing dependencies and organizing code.
            - AWS Lambda functions require a direct connection string to the DynamoDB table and ES Modules are not supported in AWS environments, making CommonJS the only viable module system.

        correct_answer: 2                    
        explanation: >
            AWS SDK is used to perform read/write operations and defining IAM roles to manage permissions, while ES Modules provide a modern syntax for importing dependencies and organizing code.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
