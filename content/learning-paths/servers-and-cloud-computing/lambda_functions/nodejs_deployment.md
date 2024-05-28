---
# User change
title: "Deploy Node.js Lambda functions on Graviton processors with Terraform"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

[AWS Lambda](https://aws.amazon.com/lambda/) is a serverless, event-driven compute service that lets you run code without managing servers. 

Lambda runs your code on high-availability compute infrastructure and frees you from spending time administering servers.

You can configure Lambda functions to run on Graviton processors. 

This Learning Path shows you how to deploy AWS Lambda functions using Terraform and select "arm64" as the architecture.

## Before you begin

You should have the prerequisite tools installed before starting the Learning Path. 

Any computer which has the required tools installed can be used for this section. The computer can be your desktop or laptop computer or a virtual machine with the required tools. 

You will need an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) to complete this Learning Path. Create an account if you don't have one.

Before you begin you will also need:
- An AWS access key ID and secret access key. 

The instructions to create the keys are below.

### Acquire AWS Access Credentials

The installation of Terraform on your desktop or laptop needs to communicate with AWS. Thus, Terraform needs to be able to authenticate with AWS.

To generate and configure the Access key ID and Secret access key, follow this [guide](/install-guides/aws_access_keys).

Before you begin, confirm you have an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) and you can login to the AWS console.

## Deploy a Lambda function using Terraform

1. Using a text editor, save the code below in a file called `index.js`

This is the source code for the Lambda function. 

```console
exports.handler = function (event, context) {
        console.log(event);
        context.succeed('hello ' + event.name + ', are you using ' + event.type);
};
```

The Lambda function will simply print a message. The message adds the `event.name` and `event.type` inputs to the output string. 

2. Copy the `index.js` to a subdirectory named `nodejs`

```console
mkdir nodejs ; cp index.js nodejs
```

Terraform will zip the Lambda source code so the source needs to be separated from the rest of the project files in a subdirectory.

3. Using a text editor, save the code below in a file called `main.tf`

```console
provider "aws" {
  region = "us-east-1"
}

provider "archive" {}

data "archive_file" "lambda_zip_dir" {
  type        = "zip"
  output_path = "nodejs.zip"
  source_dir  = "nodejs"
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
  assume_role_policy = data.aws_iam_policy_document.policy.json
}

resource "aws_lambda_function" "lambda" {
  function_name    = "indexjs"
  filename         = data.archive_file.lambda_zip_dir.output_path
  source_code_hash = data.archive_file.lambda_zip_dir.output_base64sha256
  role             = aws_iam_role.iam_for_lambda.arn
  handler          = "index.handler"
  runtime          = "nodejs18.x"
  architectures    = ["arm64"]
}

data "aws_lambda_invocation" "example" {
  function_name = aws_lambda_function.lambda.function_name

  input = <<JSON
{
  "name": "Arm_user",
  "type": "Testing"
}
JSON
}

output "result" {
  value = data.aws_lambda_invocation.example.result
}
```

4. Using a text editor, save the code below in a file called `output.tf`

```console
output "lambda" {
  value = aws_lambda_function.lambda.qualified_arn
}
```

You should have three files ready to deploy the Lambda function using Terraform. You have `main.tf` and `output.tf` in the current directory, and `index.js` in a subdirectory named `nodejs`

Running the Lambda function displays the **ARN** (Amazon Resource Names) of the Lambda resource and the output message from the code.

## Terraform Commands

Use Terraform to deploy the `main.tf` file.

### Initialize Terraform

Run `terraform init` to initialize the Terraform deployment. This command downloads the dependencies required for AWS.

```console
terraform init
```
    
The output should be similar to:

```output
Initializing the backend...

Initializing provider plugins...
- Finding latest version of hashicorp/aws...
- Finding latest version of hashicorp/archive...
- Installing hashicorp/aws v4.58.0...
- Installed hashicorp/aws v4.58.0 (signed by HashiCorp)
- Installing hashicorp/archive v2.3.0...
- Installed hashicorp/archive v2.3.0 (signed by HashiCorp)

Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

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
Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

lambda = "arn:aws:lambda:us-east-1:200211127965:function:indexjs:$LATEST"
result = "\"hello Arm_user, are you using Testing\""
```

You have successfully created and executed the Lambda function on AWS.

### Verify the Lambda function

To verify the creation of the Lambda function to to the AWS console and select AWS Lambda. Click on Functions and verify the Lambda function `indexjs` is displayed.

![nodejs1 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/40816837/006f990d-191b-42d3-b90d-1bd8956af574)

Click on the function `indexjs` and scroll down to the `Runtime settings`

You will see the Architecture listed as arm64

![nodejs2 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/40816837/81c09af4-f209-4d7c-9fc5-4c4cb1f556e5)

You can use the Test tab of the Lambda console to run the function again.

Enter the text below in the `Event JSON` input area.

```json
{
  "name": "Arm_user",
  "type": "Testing"
}
```

Click the `Test` button to run the function. 

You should see the same output as running the function with Terraform.

```output
"hello Arm_user, are you using Testing"
```

You have successfully deployed a Lambda function using Node.js on an AWS Graviton2 processor.

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```

After you run `terraform destroy` the Lambda function is gone from the AWS console.

Continue the Learning Path to create a Lambda function in Python.

