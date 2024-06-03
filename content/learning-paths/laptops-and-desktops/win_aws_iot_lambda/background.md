---
# User change
title: "Background"

weight: 2

layout: "learningpathall"
---

## Background
AWS Lambda is a serverless compute service provided by Amazon Web Services (AWS) that allows you to run code without provisioning or managing servers. With AWS Lambda, you can execute your code in response to various events, such as changes to data in an Amazon S3 bucket, updates to a DynamoDB table, or HTTP requests via Amazon API Gateway. This event-driven compute service automatically scales your application by running code in response to each trigger, handling the necessary infrastructure management.

Lambda supports a variety of programming languages, including Python, Java, Node.js, C#, and Go, giving developers flexibility in their choice of technology stack. It is designed to be cost-effective, as you are only billed for the compute time your code consumes, measured in milliseconds, rather than for idle server time.

By leveraging AWS Lambda, developers can focus on writing business logic without worrying about the underlying infrastructure. This makes it an ideal solution for building microservices, automating operational tasks, and creating back-end services for web and mobile applications. Additionally, AWS Lambda can be seamlessly integrated with AWS IoT Core through the Rules Engine, enabling you to process and respond to data from IoT devices in real-time, enhancing the capabilities of IoT applications.

In this learning path, you will learn how to use AWS Lambda to process data from an IoT device. Specifically, you will learn how to set up AWS Lambda to send an email notification whenever the temperature from a sensor exceeds a predefined threshold. This setup involves several steps:
1. Set Up the IoT Device and AWS IoT Core: Connect your IoT device to AWS IoT Core and configure it to send temperature data. Here you will use the same IoT emulator as in [Create IoT applications with Windows on Arm and AWS IoT Core](/learning-paths/laptops-and-desktops/win_aws_iot/) learning path.

2. Create an AWS Lambda Function: Develop a Lambda function that will process the incoming temperature data and check if it exceeds the defined threshold. 

3. Integrate AWS Lambda with AWS IoT Core: Use the AWS IoT Core Rules Engine to trigger the Lambda function whenever new data from the temperature sensor arrives.

4. Configure Email Notifications: Set up Amazon Simple Notification Service (SNS) to send email notifications when the Lambda function detects a temperature reading above the threshold.

By following these steps, you will be able to automatically monitor temperature readings from your IoT device and receive email alerts when critical temperature levels are detected. This process leverages the power of AWS services to create a responsive and scalable solution for IoT data processing and alerting.
