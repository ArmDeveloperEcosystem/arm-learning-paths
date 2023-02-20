---
# User change
title: "Deploy Node.js Lambda functions on Graviton processors with Terraform"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Before you begin

Before you begin, confirm you have an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) and you can login to the AWS console.

You will also need a computer with [Terraform](/install-tools/terraform/) and the [AWS CLI](/install-tools/aws-cli/) installed. This can be any operating system as long as these tools installed. 


## Generate Access keys (access key ID and secret access key)

The installation of Terraform on your desktop or laptop needs to communicate with AWS. Thus, Terraform needs to be able to authenticate with AWS. For authentication, generate access keys (access key ID and secret access key). These access keys are used by Terraform for making programmatic calls to AWS via the AWS CLI.
  
Go to **Security Credentials**
   
![190137370-87b8ca2a-0b38-4732-80fc-3ea70c72e431](https://user-images.githubusercontent.com/92315883/217728054-4259add4-5c40-4b69-9329-4252037a5afd.png)


On Your **Security Credentials** page, click on **Create access key** (access key ID and secret access key)
   
![image](https://user-images.githubusercontent.com/87687468/190137925-c725359a-cdab-468f-8195-8cce9c1be0ae.png)
   
Copy the **Access key ID** and **Secret access key**

![image](https://user-images.githubusercontent.com/87687468/190138349-7cc0007c-def1-48b7-ad1e-4ee5b97f4b90.png)

## Deploy Lambda function via Terraform

AWS Lambda is a compute service that lets you run code without provisioning or managing servers.
Lambda runs your code on a high-availability compute infrastructure and performs all of the administration of the compute resources, including server and operating system maintenance, capacity provisioning, automatic scaling and logging.
To deploy AWS Lambda functions, create the **main.tf**, **output.tf** and **lambda_function (index.js)** files below using a text editor.

Here is the **index.js** file

```console

exports.handler = function (event, context) {
        console.log(event);
        context.succeed('hello ' + event.name + ', are you using ' + event.type);
};

```

The above Lambda function will simply print `event.name` value as an output.

Here is the complete **main.tf** file

```console
provider "aws" {
  region = "us-east-2"
  access_key  = "Axxxxxxxxxxxxxxxxxxxxxxxxx"
  secret_key   = "Rxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
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
  assume_role_policy = "${data.aws_iam_policy_document.policy.json}"
}

resource "aws_lambda_function" "lambda" {
  function_name = "indexjs"
  filename         = "${data.archive_file.lambda_zip_dir.output_path}"
  source_code_hash = "${data.archive_file.lambda_zip_dir.output_base64sha256}"
  role    = "${aws_iam_role.iam_for_lambda.arn}"
  handler = "index.handler"
  runtime = "nodejs18.x"
  architectures = ["arm64"]
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

![Screenshot (360)](https://user-images.githubusercontent.com/92315883/216524630-0e24329d-5278-4dd2-9bfc-3e314842d4b6.png)


### Verify the Lambda function

To verify the deployment of Lambda functions on AWS console, go to **Lambda » Functions**. Verify the Lambda function is displayed.

![Screenshot (348)](https://user-images.githubusercontent.com/92315883/216253082-792bc564-dbb1-46ec-a3ba-e3220f31dd2d.jpg)

![Screenshot (358)](https://user-images.githubusercontent.com/92315883/216524063-a3d36a0a-9b42-44c5-a5b6-a0c90a3725d3.png)

{{% notice Note %}}
To execute Lambda functions on the Graviton processor, set architectures = ["arm64"].
{{% /notice %}}

