---
title: "Upload S3 artifacts and publish both components"
description: Grant artifact downloads and topic publishing, generate Lite-compatible recipes, and register immutable component versions.
weight: 6
layout: "learningpathall"
---

## Confirm AWS CLI versioning

On your Ubuntu host, lets first confirm that the aws cli version used is new enough:

```bash
aws --version
```

If the version reported is earlier than 2.17.34, please update to the latest version:

```bash
curl -fsSL https://awscli.amazonaws.com/v2/install.sh | bash
export PATH=${HOME}/.local/bin:${PATH}
which aws
aws --version
```

Your aws cli version should now be greater than 2.17.34.

## Reuse the Part 1 AWS identity

Run this page on the Ubuntu administrative workstation, in the source workspace. Retain the actual Region and existing device role alias from Part 1:

```bash
cd "$HOME/pb2-temperature-part3"
export AWS_REGION=us-east-1
export THING_NAME=MyPocketBeagle2
export THING_GROUP=PocketBeagleDevices
export ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
export IOT_ROLE_ALIAS=YOUR_EXISTING_ROLE_ALIAS
export YOUR_UNIQUE_SUFFIX=MySuffix
export ROLE_ARN=$(aws iot describe-role-alias --role-alias "$IOT_ROLE_ALIAS" \
  --query roleAliasDescription.roleArn --output text)
export ROLE_NAME=${ROLE_ARN##*/}
export ARTIFACT_BUCKET="pb2-temperature-${ACCOUNT_ID}-${AWS_REGION}-${YOUR_UNIQUE_SUFFIX}"
export ARTIFACT_PREFIX=pb2-temperature
```

Change `YOUR_EXISTING_ROLE_ALIAS` with your IoTCore Role alias used. Also customize `YOUR_UNIQUE_SUFFIX` as needed.

Replace both uppercase placeholders, including the bucket suffix, before running commands. Use lowercase letters, digits, and hyphens in the bucket name. These commands assume the commercial AWS partition. Keep administrative credentials on the workstation.

## Create a private artifact bucket

Choose a globally unique bucket in the deployment Region:

```bash
if [ "$AWS_REGION" = us-east-1 ]; then
  aws s3api create-bucket --bucket "$ARTIFACT_BUCKET" --region "$AWS_REGION"
else
  aws s3api create-bucket --bucket "$ARTIFACT_BUCKET" --region "$AWS_REGION" \
    --create-bucket-configuration "LocationConstraint=$AWS_REGION"
fi
aws s3api put-public-access-block --bucket "$ARTIFACT_BUCKET" \
  --public-access-block-configuration \
  BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
aws s3api put-bucket-encryption --bucket "$ARTIFACT_BUCKET" \
  --server-side-encryption-configuration \
  '{"Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"AES256"}}]}'
```

The example uses S3-managed encryption and a bucket in the same account. If using an existing bucket with customer-managed KMS encryption, its KMS and bucket policies must also authorize the device role.

## Grant artifact downloads to the existing device role

Part 1's inline Hello World needed no S3 permission. Add the following narrowly scoped policy to its **existing token-exchange IAM role**, following [AWS's artifact-access guidance](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-service-role.html#device-service-role-access-s3-bucket):

```bash
python3 - <<'PYTHON'
import json, os
from pathlib import Path
bucket, prefix = os.environ['ARTIFACT_BUCKET'], os.environ['ARTIFACT_PREFIX']
policy = {'Version': '2012-10-17', 'Statement': [
    {'Effect': 'Allow', 'Action': 's3:GetObject',
     'Resource': f'arn:aws:s3:::{bucket}/{prefix}/*'},
    {'Effect': 'Allow', 'Action': 's3:GetBucketLocation',
     'Resource': f'arn:aws:s3:::{bucket}'}
]}
Path('artifact-access.json').write_text(json.dumps(policy, indent=2) + '\n')
PYTHON
aws iam put-role-policy --role-name "$ROLE_NAME" \
  --policy-name PB2ExternalTemperatureArtifacts \
  --policy-document file://artifact-access.json
```

Use a fresh inline-policy name if that name is already used for another purpose. Preserve the role trust, permissions boundary, role alias, and Part 1 policies. A boundary or explicit deny must also permit these reads. The role does not need S3 write access; the workstation identity performs uploads and component registration.

## Grant the device certificate the exact MQTT topic

There are three separate authorization checks: device-role S3 reads, component IPC publish authorization, and certificate IoT publish authorization. The recipe generator supplies the IPC permission. Add a supplemental certificate policy for the topic:

```bash
python3 - <<'PYTHON'
import json, os
from pathlib import Path
arn = ('arn:aws:iot:' + os.environ['AWS_REGION'] + ':' + os.environ['ACCOUNT_ID']
       + ':topic/ti/pocketbeagle2/temperature/external')
Path('temperature-publish.json').write_text(json.dumps({
    'Version': '2012-10-17', 'Statement': [
        {'Effect': 'Allow', 'Action': 'iot:Publish', 'Resource': arn}
    ]
}, indent=2) + '\n')
PYTHON
aws iot list-thing-principals --thing-name "$THING_NAME"
```

Set `CERT_ARN` to the active certificate actually used by this board, from the returned principals. Then:

```bash
export CERT_ARN=YOUR_DEVICE_CERTIFICATE_ARN
aws iot create-policy --policy-name PB2ExternalTemperaturePublish \
  --policy-document file://temperature-publish.json
aws iot attach-policy --policy-name PB2ExternalTemperaturePublish --target "$CERT_ARN"
```

If that supplemental policy already exists, inspect its default version and reuse it only if its contents match. Leave the original connection-kit policy attached. The device still needs its existing connection, deployment subscription, and role-alias permissions. Adding `iot:Publish` to the IAM role alone does not grant certificate MQTT publishing.

## Generate both complete recipes

```bash
python3 tools/make_recipes.py --bucket "$ARTIFACT_BUCKET" --prefix "$ARTIFACT_PREFIX"
python3 -m json.tool recipes/com.arm.PocketBeagle2.ZephyrExternalTemperature.json
python3 -m json.tool recipes/com.arm.PocketBeagle2.ExternalTemperatureBridge.json
```

The generator enumerates the actual staged files, including both wheel filenames, and creates version `1.0.0` of exactly two generic components. Both manifests select `linux`, `aarch64`, and `aws_nucleus_lite`. Every artifact has an explicit private `s3://` URI. There is no dependency on the Java nucleus, Java CLI component, or a third custom service.

The firmware lifecycle is equivalent to:

```output
{
  "install": {
    "RequiresPrivilege": true,
    "Script": "exec python3 -u \"{artifacts:path}/firmware_manager.py\" install --artifact \"{artifacts:path}/zephyr.elf\" --work \"{work:path}\""
  },
  "run": {
    "RequiresPrivilege": true,
    "Script": "exec python3 -u \"{artifacts:path}/firmware_manager.py\" run --artifact \"{artifacts:path}/zephyr.elf\" --work \"{work:path}\""
  }
}
```

The bridge lifecycle invokes its S3-delivered shell script with `install` or `run`, its artifact/work paths, the configured serial device, and `{iot:thingName}`. Its default configuration grants only `aws.greengrass#PublishToIoTCore` on `ti/pocketbeagle2/temperature/external` under `aws.greengrass.ipc.mqttproxy`. Review the generated full JSON before publishing. These fields follow the [recipe reference](https://docs.aws.amazon.com/greengrass/v2/developerguide/component-recipe-reference.html) and the pinned Lite subset; an unsupported `shutdown` field is intentionally absent.

## Upload first, then register the versions

```bash
python3 tools/upload.py --bucket "$ARTIFACT_BUCKET" --prefix "$ARTIFACT_PREFIX"
aws s3 ls "s3://$ARTIFACT_BUCKET/$ARTIFACT_PREFIX/" --recursive
aws greengrassv2 create-component-version \
  --inline-recipe fileb://recipes/com.arm.PocketBeagle2.ZephyrExternalTemperature.json
aws greengrassv2 create-component-version \
  --inline-recipe fileb://recipes/com.arm.PocketBeagle2.ExternalTemperatureBridge.json
```

Keep the returned version ARNs. The upload script uses [S3 conditional writes](https://docs.aws.amazon.com/cli/latest/reference/s3api/put-object.html) to refuse an existing key. If a partial upload is interrupted, compare existing objects with your staged files and upload only the missing ones; do not delete published artifacts merely to rerun the helper. Use a recent AWS CLI v2 if `--if-none-match` is unavailable.

Never overwrite S3 objects behind a published component version: registration records artifact integrity information, and devices may already cache the old bytes. For an update, change the version in `make_recipes.py` and `stage.sh`, use new versioned S3 keys, restage into a clean staging tree, regenerate, upload, and publish a new component version. The old version and its artifacts remain available for rollback.

## What you have learned

You have learned how to authorize S3 artifact downloads, component IPC publishing, and certificate-based MQTT publishing as separate permissions. You can now generate both Lite-compatible recipes, upload their artifacts, and publish immutable component versions while preserving the board's existing AWS identity.
