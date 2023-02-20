---
# User change
title: "Deploy Python Lambda functions on Graviton processors with Terraform"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Before you begin

Before you begin, confirm you have an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) and you can login to the AWS console.

You will also need a computer with [Terraform](/install-tools/terraform/) and the [AWS CLI](/install-tools/aws-cli/) installed. This can be any operating system as long as these tools installed. 

## Deploy Lambda function via Terraform

To generate an **access key** and **secret key**, follow the [instructions in the previous section](/learning-paths/server-and-cloud/lambda_functions/nodejs_deployment/).

To deploy AWS Lambda functions, create the **main.tf**, **output.tf** and **lambda_function (python_lambda.py)** files below using a text editor.

Here is the **python_lambda.py** file

```console

def lambda_handler(event, context):
    message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])
    return {
        'message' : message
    }

```
The above Lambda function will simply print `event.name` value as an output.

Here is the complete **main.tf** file

```console
provider "aws" {
  region = "us-east-2"
  access_key  = "Axxxxxxxxxxxxxxxxxxxx"
  secret_key   = "Rxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}

provider "archive" {}

data "archive_file" "lambda_zip_dir" {
  type        = "zip"
  output_path = "hello_lambda.zip"
  source_file  = "hello_lambda.py"
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
  handler = "hello_lambda.lambda_handler"
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

{{% notice Note %}}
Replace `access_key` and `secret_key` with your values.
{{% /notice %}}

In the **main.tf** file mentioned above, a Lambda function is being created. Additionally, you are creating a Lambda function specific IAM role.

Lambda functions use the **ZIP** file of code for uploading, so you are using the resource `Archive` for this purpose.

Use the `lambda invoke` resource in the **main.tf** file for invoking the Lambda function.

Here is the **output.tf** file

```console
output "lambda" {
  value = "${aws_lambda_function.lambda.qualified_arn}"
}

```
The output displays the **ARN** (Amazon Resource Names) of the Lambda resource in the above **output.tf** file.

Now, use the Terraform commands below to deploy **main.tf** file.


### Terraform Commands

**Initialize Terraform**

Run `terraform init` to initialize the Terraform deployment. This command is responsible for downloading all dependencies which are required for the AWS provider.

```console
terraform init
```
    
![Screenshot (255)](https://user-images.githubusercontent.com/92315883/209255228-8c8b1b17-ce55-4c7d-9916-6c15918fc82e.png)

**Create a Terraform execution plan**

Run `terraform plan` to create an execution plan.

```console
terraform plan
```

{{% notice Note %}}
The **terraform plan** command is optional. You can directly run **terraform apply** command. But it is always better to check the resources about to be created.
{{% /notice %}}

**Apply a Terraform execution plan**

Run `terraform apply` to apply the execution plan to your cloud infrastructure. The below command creates all required infrastructure.

```console
terraform apply
```      
![Screenshot (351)](https://user-images.githubusercontent.com/92315883/216279981-a46e3cd0-50a0-4c93-b9e5-2c77ea84f865.png)

### Verify the Lambda function

To verify the deployment of Lambda functions on AWS console, go to **Lambda » Functions**. Verify the Lambda function is displayed.

![Screenshot (354)](https://user-images.githubusercontent.com/92315883/216284315-dec9b16c-bc34-4752-8408-e5af819ea030.png)

![Screenshot (357)](https://user-images.githubusercontent.com/92315883/216515003-78546861-9d21-4d79-995c-0c2b5073feec.png)

{{% notice Note %}}
To execute Lambda functions on the Graviton processor, set architectures = ["arm64"].
{{% /notice %}}