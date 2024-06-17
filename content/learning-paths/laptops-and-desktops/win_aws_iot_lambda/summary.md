---
# User change
title: "Summary"

weight: 6

layout: "learningpathall"
---
## Summary
You have learned how to create a Lambda function that is triggered by a message received on an AWS IoT Core topic. Specifically, you learned how to:

1. **Create a Lambda Function** - you started by setting up a Lambda function that listens for temperature data sent to a specific topic on AWS IoT Core. This function processes the data and takes necessary actions based on predefined conditions.

2. **Implement the Lambda Function** - you saw how to implement the Lambda function to handle the incoming data, check if the temperature exceeds a specified threshold, and prepare to send notifications if necessary. You wrote the function using modern JavaScript with ES modules and utilized the AWS SDK for JavaScript (v3).

3. **Create Test Events** -  to ensure our Lambda function works as expected, you created test events in the Lambda console. These test events simulate the messages that would be received from the IoT Core, allowing us to validate the function's behavior without needing actual IoT devices.

4. **Use SNS to Send Emails** - you integrated Amazon Simple Notification Service (SNS) to send email notifications when the temperature exceeds the threshold. This involved creating an SNS topic, subscribing an email address to the topic, and publishing messages to the topic from within the Lambda function.

5. **Incorporate Environment Variables** - finally, you enhanced our Lambda function by using environment variables for configurable parameters such as the email address and temperature threshold. This approach makes the function more flexible and easier to manage, as you can change these settings without modifying the code.

By following these steps, you have built a complete solution that:

* Processes IoT data in real-time using AWS Lambda.
* Sends alerts via email when specific conditions are met.
* Utilizes best practices for configuration management using environment variables.

This setup can be further expanded and customized to fit various IoT applications, providing a robust foundation for building event-driven architectures with AWS services.
