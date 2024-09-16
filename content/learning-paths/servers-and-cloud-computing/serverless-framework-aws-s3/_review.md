---
review:
    - questions:
        question: >
            What is the primary purpose of using the Serverless Framework in your project?
        answers:
            - To create a manual deployment process for AWS resources.
            - To automate the deployment and management of AWS resources using infrastructure as code.
            - To manage server operations on local servers.
            - To replace AWS services with third-party alternatives.
        correct_answer: 2
        explanation: >
            Serverless Framework automates the deployment and management of AWS resources using infrastructure as code.

    - questions:
        question: >
            What is the role of the serverless-s3-sync plugin in the deployment process?
        answers:
            - It synchronizes local files with an S3 bucket during deployment.
            - It compiles JavaScript files before deployment.
            - It creates new S3 buckets for each deployment stage.
            - It compresses files before uploading them to S3.

        correct_answer: 1
        explanation: >
            Serverless-s3-sync plugin synchronizes local files with an S3 bucket during deployment.

    - questions:
        question: >
            What was the purpose of using the prepare script in your serverless project?
        answers:
            - To compile all source files before deploying them to AWS.
            - To dynamically update the index.js file with actual API endpoint URLs before deployment.
            - To create a backup of all project files before starting the deployment process.
            - To validate the serverless.yml file for syntax errors..

        correct_answer: 2                    
        explanation: >
            We used custom prepare.js file to implement the script, which dynamically updated the index.js file with actual API endpoint URLs before deployment.


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
