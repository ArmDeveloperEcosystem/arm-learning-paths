---
# User change
title: "Deploy Python Lambda functions on Graviton processors with Terraform"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

You can also write Lambda functions using Python. 

## Before you begin

You can reuse everything your learned from the previous topic and replace the Node.js code with a Lambda function written in Python.

## Deploy Lambda function via Terraform

1. Using a text editor, save the code below to in a file called `python_lambda.py`

This is the source code for the Lambda function. 

```Python
def lambda_handler(event, context):
  message = 'Hello {}{}!'.format(event['first_name'], event['last_name'])
  return {
    'message' : message
  }
```

The Lambda function will simply print a message. The message adds the `first_name` and `last_name` inputs to the output string. 

This example doesn't place the Python source code in a subdirectory, leave it in the current directory.

2. Using a text editor, save the code below to in a file called `main.tf`

Change the `main.tf` `provider` section and update all 3 values to use your preferred AWS region and your AWS access key ID and secret access key.

After editing the `provider` section, save the file.

```console
provider "aws" {
  region = "us-east-1"
  access_key  = "Axxxxxxxxxxxxxxxxxxxx"
  secret_key   = "Rxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}

provider "archive" {}

data "archive_file" "lambda_zip_dir" {
  type        = "zip"
  output_path = "python_lambda.zip"
  source_file  = "python_lambda.py"
}
data "aws_iam_policy_document" "policy" {
  statement {
    sid    = ""
    effect = "Allow"

    principals {
      identifiers = ["lambda.amazonaws.com"]
      type        = "Service"
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "iam_for_lambda" {
  name               = "iam_for_lambda"
  assume_role_policy = "${data.aws_iam_policy_document.policy.json}"
}

resource "aws_lambda_function" "lambda" {
  function_name = "python_lambda"
  filename         = "${data.archive_file.lambda_zip_dir.output_path}"
  source_code_hash = "${data.archive_file.lambda_zip_dir.output_base64sha256}"
  role    = "${aws_iam_role.iam_for_lambda.arn}"
  handler = "python_lambda.lambda_handler"
  runtime = "python3.8"
  architectures = ["arm64"]
}

data "aws_lambda_invocation" "example" {
  function_name = aws_lambda_function.lambda.function_name

  input = <<JSON
{
  "first_name": "Arm-",
  "last_name": "user"
}
JSON
}

output "result" {
  value = "${data.aws_lambda_invocation.example.result}"
}
```

3. Using a text editor, save the code below to in a file called `output.tf`

```console
output "lambda" {
  value = "${aws_lambda_function.lambda.qualified_arn}"
}
```

You should have three files ready to deploy the Lambda function using Terraform. You have `main.tf`, `output.tf`, and `python_lambda.py` in the current directory.

Running the Lambda function displays the **ARN** (Amazon Resource Names) of the Lambda resource and the output message from the code.

## Terraform Commands

Use Terraform to deploy the `main.tf` file.

### Create a Terraform execution plan

Run `terraform plan` to create an execution plan.

```console
terraform plan
```

A long output of resources to be created will be printed.

Any errors in the Terraform setup are usually identified by `terraform plan`.

### Apply a Terraform execution plan

Run `terraform apply` to apply the execution plan and create all AWS resources:

```console
terraform apply
```      

Answer yes to the prompt to confirm you want to create AWS resources.

The result should print output similar to:

```output
Apply complete! Resources: 0 added, 1 changed, 0 destroyed.

Outputs:

lambda = "arn:aws:lambda:us-east-1:200211127965:function:python_lambda:$LATEST"
result = "{\"message\": \"Hello Arm-user!\"}"
```
You have successfully created and executed the Python Lambda function on AWS.

### Verify the Lambda function

To verify the creation of the Lambda function to to the AWS console and select AWS Lambda. Click on Functions and verify the Lambda function `python_lambda` is displayed.

![Screenshot (354)](https://user-images.githubusercontent.com/92315883/216284315-dec9b16c-bc34-4752-8408-e5af819ea030.png)

You can use the Test tab of the Lambda console to run the function again.

Enter the text below in the `Event JSON` input area.

```json
{
  "first_name": "Arm-",
  "last_name": "user"
}
```

Click the `Test` button to run the function. 

You should see the same output as running the function with Terraform.

```output
"hello Arm_user, are you using Testing"
```
You have successfully deployed a Lambda function using Python on an AWS Graviton2 processor.

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```
After you run `terraform destroy` the Lambda function is gone from the AWS console.

