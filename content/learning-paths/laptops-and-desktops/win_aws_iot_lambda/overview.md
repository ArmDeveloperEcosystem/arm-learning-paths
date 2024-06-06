---
# User change
title: "Overview of Learning Path"

weight: 2

layout: "learningpathall"
---

## Overview of Learning Path
In this learning path, you will learn how to use AWS Lambda to process data from an IoT device, and specifically, how to set up AWS Lambda to send an email notification whenever the temperature from a sensor exceeds a predefined threshold. 

This setup involves several steps:

1. Set up the IoT device and AWS IoT Core - connect your IoT device to AWS IoT Core and configure it to send temperature data. 

   Here you will use the same IoT emulator as in [Create IoT applications with Windows on Arm and AWS IoT Core](/learning-paths/laptops-and-desktops/win_aws_iot/) learning path.

2. Create an AWS Lambda Function - develop a Lambda function that processes the incoming temperature data and checks if it exceeds the defined threshold. 

3. Integrate AWS Lambda with AWS IoT Core -  use the AWS IoT Core Rules Engine to trigger the Lambda function whenever new data from the temperature sensor arrives.

4. Configure email notifications - set up Amazon Simple Notification Service (SNS) to send email notifications when the Lambda function detects a temperature reading above the threshold.

By following these steps, you will be able to automatically monitor temperature readings from your IoT device and receive email alerts when critical temperature levels are detected. This process leverages the power of AWS services to create a responsive and scalable solution for IoT data processing and alerting.
