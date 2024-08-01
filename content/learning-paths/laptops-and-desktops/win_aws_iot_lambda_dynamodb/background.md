---
# User change
title: "Background"

weight: 2

layout: "learningpathall"
---

## Background
AWS Lambda is a serverless compute service that allows you to run code without provisioning or managing servers. It automatically scales your application by running code in response to triggers such as changes in data, system state, or user actions. When integrated with DynamoDB, AWS Lambda can seamlessly process data stored in DynamoDB tables, enabling real-time data processing and analytics. This integration is particularly beneficial for serverless applications, as it eliminates the need to manage infrastructure, handle scaling, or perform maintenance tasks. AWS Lambda and DynamoDB together provide a highly efficient and scalable solution for modern application development, ensuring that resources are used effectively and costs are minimized.

AWS Lambda functions, when published, can be accessed via HTTP calls, making them accessible to any device supporting HTTP. This feature is particularly important for IoT applications which often have limited resources. By leveraging AWS Lambda, IoT devices can easily retrieve data from the cloud without the need for extensive processing power or storage capabilities. Additionally, the same AWS Lambda functions can be accessed by web applications, allowing for a seamless integration between IoT devices and web-based portals or dashboards. This enables real-time data retrieval and display, providing a unified interface for controlling and monitoring IoT devices. As a result, data stored in DynamoDB can be easily accessed and managed by both IoT devices and web applications, enhancing the overall efficiency and functionality of IoT solutions.

In this learning path, you will learn how to create an AWS Lambda function that scans records. These have been added to DynamoDB by an IoT device streaming data containing temperature, humidity, and pressure [in this learning path about creating IoT applications](/learning-paths/laptops-and-desktops/win_aws_iot/). The function will take records from the previous N minutes, average the temperatures, and return them to the caller.
