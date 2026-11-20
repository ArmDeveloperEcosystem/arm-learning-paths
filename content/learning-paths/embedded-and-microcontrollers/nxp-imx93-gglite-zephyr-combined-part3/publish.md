---
title: "NXP FRDM i.MX93: Publish both S3-backed custom components"  
description: "Grant artifact and MQTT permissions and register immutable component versions."
weight: 6
layout: "learningpathall"
---

## Confirm the environment

Run this page on the Ubuntu host, in the source workspace. Retain the actual AWS Region and existing device role alias from Part 1:

```bash
cd "$HOME/nxp-imx93-temperature-part3"
export AWS_REGION=us-east-1
export AWS_DEFAULT_REGION="$AWS_REGION"
export THING_NAME=MyNXPIMX93
export THING_GROUP=NXPIMX93Devices
export ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
export IOT_ROLE_ALIAS=YOUR_EXISTING_ROLE_ALIAS
export ROLE_ARN=$(aws iot describe-role-alias --role-alias "$IOT_ROLE_ALIAS" \
  --query roleAliasDescription.roleArn --output text)
export ROLE_NAME=${ROLE_ARN##*/}
export ARTIFACT_BUCKET="nxp-imx93-temperature-${ACCOUNT_ID}-${AWS_REGION}-YOUR_UNIQUE_SUFFIX"
export ARTIFACT_PREFIX=nxp-imx93-temperature
```

Update/customize the IOT_ROLE_ALIAS (`YOUR_EXISTING_ROLE_ALIAS`) and the bucket suffix (`YOUR_UNIQUE_SUFFIX`), before running commands. Use lowercase letters, digits, and hyphens in the bucket name. 

## Create a S3 artifact bucket

Lets create our S3 bucket for our component artifacts:

```bash
aws s3api create-bucket --bucket "$ARTIFACT_BUCKET" --region "$AWS_REGION"
aws s3api put-public-access-block --bucket "$ARTIFACT_BUCKET" \
  --public-access-block-configuration \
  BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
aws s3api put-bucket-encryption --bucket "$ARTIFACT_BUCKET" \
  --server-side-encryption-configuration \
  '{"Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"AES256"}}]}'
```

## Generate both complete recipes

Lets build our component recipe JSON files:

```bash
python3 tools/make_recipes.py --bucket "$ARTIFACT_BUCKET" --prefix "$ARTIFACT_PREFIX" --region "$AWS_REGION"
python3 -m json.tool recipes/com.arm.NXPIMX93.ZephyrExternalTemperature.json
python3 -m json.tool recipes/com.arm.NXPIMX93.ExternalTemperatureBridge.json
```

The generator enumerates the actual staged files, including both wheel filenames, and creates the version in `release.json` (currently `1.0.0`) of exactly two generic components. Both manifests select `linux`, `aarch64`, and `aws_nucleus_lite`. Every artifact has an explicit private `s3://` URI. There is no dependency on the Java nucleus, Java CLI component, or a third custom service.

## Grant artifact downloads to the existing device role

Part 1's inline Hello World needed no S3 permission. Add the following narrowly scoped policy to its **existing token-exchange IAM role**, following [AWS's artifact-access guidance](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-service-role.html#device-service-role-access-s3-bucket):

```bash
python3 -m json.tool artifact-access.json
aws iam put-role-policy --role-name "$ROLE_NAME" \
  --policy-name NXPIMX93ExternalTemperatureArtifacts \
  --policy-document file://artifact-access.json
```

Use a fresh inline-policy name if that name is already used for another purpose. Preserve the role trust, permissions boundary, role alias, and Part 1 policies. A boundary or explicit deny must also permit these reads. The role does not need S3 write access; the workstation identity performs uploads and component registration.

## Grant the device certificate access to the exact MQTT topic to be used

There are three separate authorization checks: device-role S3 reads, component IPC publish authorization, and certificate IoT publish authorization. The recipe generator supplies the IPC permission. Add a supplemental certificate policy for the topic:

```bash
python3 - <<'PYTHON'
import json, os
from pathlib import Path
arn = ('arn:aws:iot:' + os.environ['AWS_REGION'] + ':' + os.environ['ACCOUNT_ID']
       + ':topic/nxp/imx93/temperature/external')
Path('temperature-publish.json').write_text(json.dumps({
    'Version': '2012-10-17', 'Statement': [
        {'Effect': 'Allow', 'Action': 'iot:Publish', 'Resource': arn}
    ]
}, indent=2) + '\n')
PYTHON
aws iot list-thing-principals --thing-name "$THING_NAME"
```

Set `CERT_ARN` to the active certificate actually used by this board, from the returned principals (replace `YOUR_DEVICE_CERTIFICATE_ARN` with the devices certificate's ARN. You can find that in the AWS Console when examining our device `thing` within AWS IoT Core portion of the dashboard). With the ARN set for `CERT_ARN`, lets type:

```bash
export CERT_ARN=YOUR_DEVICE_CERTIFICATE_ARN
aws iot create-policy --policy-name NXPIMX93ExternalTemperaturePublish \
  --policy-document file://temperature-publish.json
aws iot attach-policy --policy-name NXPIMX93ExternalTemperaturePublish --target "$CERT_ARN"
```

If that supplemental policy already exists, inspect its default version and reuse it only if its contents match. Leave the original connection-kit policy attached. The device still needs its existing connection, deployment subscription, and role-alias permissions. Adding `iot:Publish` to the IAM role alone does not grant certificate MQTT publishing.

## Upload the artifacts into S3, then create the components

```bash
python3 tools/upload.py --plan artifact-plan.json
aws s3 ls "s3://$ARTIFACT_BUCKET/$ARTIFACT_PREFIX/" --recursive
python3 tools/check_artifact_access.py --plan artifact-plan.json \
  --role-alias "$IOT_ROLE_ALIAS" &&
aws greengrassv2 create-component-version \
  --inline-recipe fileb://recipes/com.arm.NXPIMX93.ZephyrExternalTemperature.json &&
aws greengrassv2 create-component-version \
  --inline-recipe fileb://recipes/com.arm.NXPIMX93.ExternalTemperatureBridge.json
```

Keep the returned version ARNs.

{{% notice NOTE %}}
Never overwrite S3 objects behind a published component version: registration records artifact integrity information, and devices may already cache the old bytes. For an update, change only `release.json` to an unused version, use new versioned S3 keys, restage into a clean staging tree, regenerate, upload, and publish a new component version. The old version and its artifacts remain available for rollback.
{{% /notice %}}

## Additional details: Diagnosing an artifact 403 before changing lifecycle scripts

Artifacts download before install/run scripts execute. The pinned Lite runtime
signs S3 requests using its configured awsRegion, so the bucket must be in that
Region. Copy the exact iotRoleAlias from this board's effective configuration;
a workstation IAM user or a similarly named role is not the device identity.
The generated policy grants reads for these two component prefixes across
versions, retaining rollback access. It does not make the bucket public.

The read-only preflight requires the workstation to call GetBucketLocation,
HeadObject, DescribeRoleAlias and SimulatePrincipalPolicy. It checks all seven
objects, server SHA256, Region and simulated role reads. This is not an on-device
credential/signing test and does not rule out bucket/SCP/VPC explicit denies,
KMS policy issues or a wrong board clock. SSE-KMS requires separate verification.

For an already published version, inspect its actual S3 URIs first. If the URIs
are correct, repair the existing token-exchange role's read policy and retry
the deployment; that alone does not require a new component version. If the
URIs/bytes are wrong, publish an unused version with fresh keys. Do not replace
objects behind 1.0.0 or delete the working Hello World deployment.

If these workstation checks pass but the board still gets 403, use the
read-only `tools/diagnose_s3.py` procedure in ARTIFACT-DELIVERY.md. It uses the
board certificate and fresh credentials, reports the caller ARN and S3 error
code, and excludes credentials from output. It is a comparison against the
supplied configuration, not a dump of the daemon's cached credentials.

## What you have learned

You can create S3 buckets, generate both AWS Greengrass component recipes, upload our built component artifacts, and create the components.
