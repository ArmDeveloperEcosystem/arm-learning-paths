---
# User change
title: "Create Lambda Function"

weight: 4

layout: "learningpathall"
---
## Objective
You will now implement the Lambda function to scan records from the DynamoDB. We assume the records are already written to the table as demonstrated in this [learning path](/learning-paths/laptops-and-desktops/win_aws_iot_dynamodb/).

## Create and configure a Lambda function
Go the AWS Lambda console. Then, create the function as shown:
1. Click the *Create function* button:

![fig1](Figures/01.png)

2. This opens a *Create function* wizard, in which you:
* Select **Author from scratch**
* Type **GetAverageTemperature** for the Function name
* Select **Node.js 20.x** as the Runtime
* Select **arm64** under Architecture

At this point your wizard should look as shown:

![fig2](Figures/02.png)

Next, in the *Create function* wizard expand *Change default execution role*, and proceed as follows:
1. Select **Create a new role from AWS policy templates**.
2. Type **role-lambda-to-dynamodb** under the Role name.
3. Under *Policy templates - optional* select **Simple microservice permissions**.

![fig3](Figures/03.png)

This, ensures your Lambda function has necessary permissions to access the items in the DynamoDB table.

Finally, scroll down, and click the **Create function** button. This will take you to the GetAverageTemperature function dashboard: 

![fig4](Figures/04.png)

In the next step, you will use this dashboard to modify the function code.
