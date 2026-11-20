---
title: "NXP FRDM i.MX 8M Plus: Publish the Hello World component"
description: "Publish and deploy the NXP FRDM i.MX 8M Plus Hello World component."
weight: 6
layout: "learningpathall"
---

## Prepare the component workspace

Run this page's commands on the Ubuntu host, keeping the AWS account, Region, and variables from the provisioning page. Create a workspace outside the device-credential directory:

```bash
mkdir -p "$HOME/nxp-imx8uplus-hello-world"
cd "$HOME/nxp-imx8uplus-hello-world"
```

## Create the component recipe

Save the following JSON as `recipe.json` in the workspace. The component defines its application directly in the manifest's `run` lifecycle. It prints `Hello from Greengrass Lite on NXP FRDM i.MX 8M Plus!` every 60 seconds. The empty `Artifacts` list means you do not need an S3 bucket, a separate shell script, or artifact download permissions.

```json
{
  "RecipeFormatVersion": "2020-01-25",
  "ComponentName": "com.arm.NXPIMX8MPlus.HelloGreengrassLiteWorld",
  "ComponentVersion": "1.0.1",
  "ComponentType": "aws.greengrass.generic",
  "ComponentDescription": "A simple test component for Greengrass Lite",
  "ComponentPublisher": "Arm",
  "Manifests": [
    {
      "Platform": {
        "os": "linux",
        "runtime": "aws_nucleus_lite",
        "architecture": "aarch64"
      },
      "Lifecycle": {
        "run": "while true; do echo 'Hello from Greengrass Lite on NXP FRDM i.MX 8M Plus!'; sleep 60; done"
      },
      "Artifacts": []
    }
  ],
  "Lifecycle": {}
}
```

The platform selector targets Linux on `aarch64` with the `aws_nucleus_lite` runtime. The recipe has no dependency on the Java nucleus or its CLI component.

Validate the JSON before publishing:

```bash
python3 -m json.tool recipe.json
```

The command displays the formatted recipe. If it reports a parsing error, correct the JSON before continuing.

## Publish the component

Register version `1.0.1` as a private component in your account, then list its published versions:

```bash
aws greengrassv2 create-component-version \
  --inline-recipe fileb://recipe.json
aws greengrassv2 list-component-versions \
  --arn "arn:aws:greengrass:$AWS_REGION:$(aws sts get-caller-identity --query Account --output text):components:com.arm.NXPIMX8MPlus.HelloGreengrassLiteWorld"
```

Confirm, back at the AWS Console, that version `1.0.1` appears under **Greengrass devices > Components > My components** for `com.arm.NXPIMX8MPlus.HelloGreengrassLiteWorld`. Component versions are immutable: publish a new version when you change the recipe. If this version already exists, use the existing version only if its recipe matches this example.

## What you have learned

You can create and publish the trivial `Hello World` Greengrass component. The component utilizes JSON structure to define its content and lifecycle. In the next section, we'll deploy the component down to our device via Greengrass deployments. 
