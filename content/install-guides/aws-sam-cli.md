---
title: AWS SAM CLI

author_primary: Jason Andrews
minutes_to_complete: 15

official_docs: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html

additional_search_terms:
- AWS
- Lambda

layout: installtoolsall
multi_install: false
multitool_install_part: false
test_maintenance: false
tool_install: true
weight: 1
---

The Amazon Web Services (AWS) Serverless Application Model (SAM) CLI is an open-source command-line tool that you can use to build, test, and deploy serverless applications. The SAM CLI provides a Lambda-like execution environment that lets you locally build, test and debug applications defined by AWS SAM templates. It is available for a variety of operating systems and Linux distributions, and supports the Arm architecture. 

## Before you begin

Follow the instructions below to install and try the latest version of the AWS SAM CLI for Ubuntu on Arm.

Confirm you are using an Arm machine by running:

```bash { target="ubuntu:latest" }
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm-based computer running 64-bit Linux.

Running the AWS SAM CLI requires Docker. Refer to the [Docker](/install-guides/docker/) Install Guide for installation instructions. Confirm Docker is running before installing the SAM CLI.

Python and Python pip are also required to run the SAM CLI example.

To install, run the following command:

```console
sudo apt install python-is-python3 python3-pip -y
```

## Download and install the AWS SAM CLI

There are two options to install the SAM CLI, you can select your preferred method:

* From a zip file.
* Using the Python `pip` command.

### Download and install from zip file

Use `wget`:

```bash
wget https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-arm64.zip
unzip aws-sam-cli-linux-arm64.zip -d sam-install
sudo ./sam-install/install
```

### Install the SAM CLI using Python pip

```
sudo apt install python3-venv -y
python -m venv .venv
source .venv/bin/activate
pip install aws-sam-cli
```

### Confirm that the SAM CLI has been installed

```bash
sam --version
```

The version should be printed on screen:

```output
SAM CLI, version 1.125.0
```

## Example application

You can use the AWS SAM CLI to build and deploy a simple "Hello World" serverless application that includes the line `uname -m` to check the platform it is running on, by following these steps.

1. Create the project 

Use the code below, adjusting the runtime argument if you have a different version of Python:

```console
sam init --runtime python3.12 --architecture arm64 --dependency-manager pip --app-template hello-world --name uname-app --no-interactive
```

2. Change to the new directory:

```console
cd uname-app
```

3. Modify the `hello_world/app.py` file to include the command `uname -m`

Use a text editor to replace the contents of the `hello_world/app.py` file with the code below:

```python
import json
import os

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    ret = os.popen('uname -m').read()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": ret,
            # "location": ip.text.replace("\n", "")
        }),
    }
```

4. Build the application:

```console
sam build
```

5. Test the deployed application:

```console
sam local invoke "HelloWorldFunction" -e events/event.json
```

The output below shows the results from the command `uname -m` and the value of `aarch64` confirms an Arm Linux computer: 

```output
Invoking app.lambda_handler (python3.12)                                                                                                                             
Local image was not found.                                                                                                                                           
Removing rapid images for repo public.ecr.aws/sam/emulation-python3.12                                                                                               
Building image........................................................................................................................
Using local image: public.ecr.aws/lambda/python:3.12-rapid-arm64.                                                                                                    
                                                                                                                                                                     
Mounting /home/ubuntu/uname-app/.aws-sam/build/HelloWorldFunction as /var/task:ro,delegated, inside runtime container                                                
START RequestId: 7221da4d-346d-4e2e-831e-dcde1cb47b5b Version: $LATEST
END RequestId: 513dbd6f-7fc0-4212-ae13-a9a4ce2f21f4
REPORT RequestId: 513dbd6f-7fc0-4212-ae13-a9a4ce2f21f4	Init Duration: 0.26 ms	Duration: 84.22 ms	Billed Duration: 85 ms	Memory Size: 128 MB	Max Memory Used: 128 MB	
{"statusCode": 200, "body": "{\"message\": \"aarch64\\n\"}"}
```

You are ready to use the AWS SAM CLI to build more complex functions and deploy them into AWS. Make sure to select `arm64` as the architecture for your Lambda functions. 

