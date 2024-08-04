---
title: Objective
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The Serverless Framework is an open-source toolkit that enables developers to build and deploy applications on cloud infrastructure without managing server operations. By abstracting away the underlying server management, it allows for greater focus on writing code and developing features, enhancing productivity and efficiency. The framework supports multiple cloud providers such as AWS, Google Cloud, and Microsoft Azure, providing a versatile and scalable solution for modern application development. With its powerful plugins and community support, the Serverless Framework simplifies complex deployment processes, promotes best practices, and facilitates rapid iteration, making it an essential tool in the DevOps landscape.

In the previous [Learning Path](/learning-paths/servers-and-cloud-computing/serverless-framework-aws-intro/), we learned how to set up Serverless Framework for AWS, and deploy a simple AWS Lambda function. On the other hand in the series of learning paths about IoT on AWS we demonstrated how to manually create various AWS resources:
1. [Use Amazon DynamoDB for your IoT applications running on Arm64](learning-paths/laptops-and-desktops/win_aws_iot_dynamodb).
2. [Use AWS Lambda for IoT applications running on Arm64](learning-paths/laptops-and-desktops/win_aws_iot_lambda).
3. [Integrate AWS Lambda with DynamoDB for IoT applications running on Windows on Arm](learning-paths/laptops-and-desktops/win_aws_iot_lambda_dynamodb).

While manual resource provisioning has its benefits, it can become increasingly problematic as you start deploying your applications to the cloud. As your solutions grow and become more complex, the challenges associated with manual provisioning escalate. This is where the Serverless Framework comes into play, offering a streamlined and efficient way to manage your cloud resources.

In this guide, I will demonstrate how to automatically deploy a multi-resource serverless solution to AWS. By leveraging the Serverless Framework, you can simplify the deployment process, enhance scalability, and reduce the operational overhead associated with managing cloud infrastructure manually. Specifically, we will create a solution composed of the DynamoDB table and the AWS Lambda function. The latter will consume the data from the table. The function will calculate the average of numerical values in the selected column. Similarly to what we achieved in this [Learning Path](learning-paths/laptops-and-desktops/win_aws_iot_lambda_dynamodb).