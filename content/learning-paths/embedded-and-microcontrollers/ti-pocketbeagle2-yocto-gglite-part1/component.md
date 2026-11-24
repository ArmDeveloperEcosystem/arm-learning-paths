---
title: "Create and publish the Hello World component"
description: Create a Hello World component recipe and publish it as a private component version that you can deploy to PocketBeagle 2 with AWS IoT Greengrass nucleus lite.
weight: 6
layout: "learningpathall"
---

## Prepare the component workspace

Run these commands on the host computer, in the same terminal session you used for provisioning, so the AWS account, Region, and variables stay set. If you opened a new terminal, set `AWS_REGION` again, as in [Set variables on the host computer](/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-gglite-part1/provision/#set-variables-on-the-host-computer).

Create a workspace directory that is separate from the folder holding your device credentials:

```bash
mkdir -p "$HOME/pb2-hello-world"
cd "$HOME/pb2-hello-world"
```

## Create the component recipe

Save the following JSON as `recipe.json` in the workspace. The component defines its application directly in the manifest's `run` lifecycle step. It prints `Hello from Greengrass nucleus lite on PocketBeagle 2!` every 60 seconds. The empty `Artifacts` list means you don't need an Amazon S3 bucket, a separate shell script, or artifact download permissions.

```json
{
  "RecipeFormatVersion": "2020-01-25",
  "ComponentName": "com.arm.HelloGreengrassLiteWorld",
  "ComponentVersion": "1.0.1",
  "ComponentType": "aws.greengrass.generic",
  "ComponentDescription": "A simple test component for Greengrass nucleus lite",
  "ComponentPublisher": "Arm",
  "Manifests": [
    {
      "Platform": {
        "os": "linux",
        "runtime": "aws_nucleus_lite",
        "architecture": "aarch64"
      },
      "Lifecycle": {
        "run": "while true; do echo 'Hello from Greengrass nucleus lite on PocketBeagle 2!'; sleep 60; done"
      },
      "Artifacts": []
    }
  ],
  "Lifecycle": {}
}
```

The platform selector targets Linux on `aarch64` with the `aws_nucleus_lite` runtime, which is the runtime value AWS documents for Greengrass nucleus lite. The recipe has no dependency on the Java nucleus or its CLI component.

Validate the JSON before publishing:

```bash
python3 -m json.tool recipe.json
```

The command prints the formatted recipe. If it reports a parsing error, correct the JSON before you continue.

## Publish the component

Register version `1.0.1` as a private component in your account. Then save your account ID and list the component's published versions:

```bash
aws greengrassv2 create-component-version \
  --inline-recipe fileb://recipe.json
export ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
aws greengrassv2 list-component-versions \
  --arn "arn:aws:greengrass:$AWS_REGION:$ACCOUNT_ID:components:com.arm.HelloGreengrassLiteWorld"
```

Version `1.0.1` is listed for `com.arm.HelloGreengrassLiteWorld`. You can also find it in the console under **Greengrass devices > Components > My components**.

AWS validates a new component version before you can deploy it. Check that its state is `DEPLOYABLE`. The state is `REQUESTED` or `INITIATED` until validation finishes, and `FAILED` if validation fails:

```bash
aws greengrassv2 describe-component \
  --arn "arn:aws:greengrass:$AWS_REGION:$ACCOUNT_ID:components:com.arm.HelloGreengrassLiteWorld:versions:1.0.1" \
  --query status
```

The output is similar to:

```output
{
    "componentState": "DEPLOYABLE",
    "message": "NONE",
    "errors": {}
}
```

Component versions are immutable, so publish a new version when you change the recipe. If version `1.0.1` already exists, use it only if its recipe matches this example.

## What you have accomplished

Your AWS account contains a versioned Hello World component that runs its application from the recipe. Next, deploy it to the dedicated thing group and verify its output on the board.
