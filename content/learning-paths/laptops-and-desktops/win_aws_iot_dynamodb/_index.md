---
title: Use Amazon DynamoDB for your IoT applications running on Arm64

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for developers who are interested in using Amazon DynamoDB as a database for storing data.

learning_objectives:
   - Gain familiarity with Amazon DynamoDB.
   - Be able to run the IoT application that streams data to AWS IoT Core.
   - Be able to create the rule that parses messages from AWS IoT Core and writes them to DynamoDB.

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).   
    - Any code editor. [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user) is suitable.
    - Completion of the [Create IoT applications with Windows on Arm and AWS IoT Core](/learning-paths/laptops-and-desktops/win_aws_iot/) Learning Path.

author: Dawid Borycki

### Tags
skilllevels: Advanced
subjects: Migration to Arm
armips:
    - Cortex-A
operatingsystems:
    - Windows
tools_software_languages:
    - .NET    
    - Visual Studio Code

further_reading:
    - resource:
        title: DynamoDB
        link: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html
        type: documentation
    - resource:
        title: Using DynamoDB with other AWS services
        link: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/OtherServices.html
        type: documentation
    - resource:
        title: Rules for AWS IoT 
        link: https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
