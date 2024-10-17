---
# User change
title: "Automate build and validation example"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
Your AWS account is now [ready](/learning-paths/cross-platform/avh_cicd2/prep_aws/) to be integrated into the CI/CD flow.

## Define AWS settings to repository

Return to your (forked) project repository in your browser. Navigate to `Settings` > `Secrets` > `Actions`.

Click `New repository secret` to create the below secrets. The secret names must be exactly as specified.

### Region and subnet ID

To find the value for `AWS_SUBNET_ID`, in your AWS console, navigate to `VPC` > `Subnets`, and select any valid `Subnet ID`.

| Secret name          | Notes |
| -------------------- | ----- |
| `AWS_DEFAULT_REGION` | Must be same region as `CloudFormation Stack` was created in (e.g. `us-east-1`) |
| `AWS_SUBNET_ID`      | Format `subnet-xxxxxxxxxxxxxxxxx` |

### Access Keys

Navigate to your AWS `Security credentials` settings from the pull down menu of your account (Click on your name in the upper-right corner of the AWS console).

Click `Access keys` then `Create New Access Key`.

Create these secrets in your project repository with the appropriate key values.

| Secret name             |
| ----------------------- |
| `AWS_ACCESS_KEY_ID`     |
| `AWS_SECRET_ACCESS_KEY` |

For security reasons, it is recommended to set these key pairs as `inactive` when not in use.

### CloudFormation stack

In your AWS console, return to `CloudFormation` > `Stacks`, select the stack created previously, and navigate to the `Outputs` tab.

Create these secrets from the following `Stack Key` values:

| Secret name             | Stack Key               | Notes         |
| ----------------------- | ----------------------- | ------------- |
| `AWS_SECURITY_GROUP_ID` | `AVHEC2SecurityGroupId` | Format `sg-xxxxxxxxxxxxxxxxx` |
| `AWS_IAM_PROFILE`       | `AVHIAMProfile`         | Use only the profile name (e.g `Proj-AVHInstanceRole`)  |
| `AWS_AVHROLE`           | `AVHRole`               | Use entire string (e.g. `arn:aws:iam::111111111111:role/Proj-AVHRole`)  |
| `AWS_S3_BUCKET_NAME`    | `AVHS3BucketName`       | As specified when stack was created |

## Set up GitHub Actions

The example project contains two different CI/CD workflows. For convenience, disable the `blinky` workflow.

Navigate to the `Actions` tab of your project repository, and select the `Arm Virtual Hardware Blinky example` action. Click the `menu` (three dots) button, and select `Disable workflow`.

Next, navigate to the `./github/workflows/basic.yml` file, which defines the workflow that you intend to run. Observe that the above `secrets` are used by the workflow:
```yaml
# TO DO - PUSH THESE CHANGES TO THE MAIN REPO
# FOR NOW, OVERWRITE basic.yml WITH THESE CODE SNIPPETS
env:
  AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
  AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
  AWS_DEFAULT_REGION: ${{ secrets.AWS_DEFAULT_REGION }}
  AWS_S3_BUCKET_NAME: ${{ secrets.AWS_S3_BUCKET_NAME }}
  AWS_IAM_PROFILE: ${{ secrets.AWS_IAM_PROFILE }}
  AWS_SECURITY_GROUP_ID: ${{ secrets.AWS_SECURITY_GROUP_ID }}
  AWS_SUBNET_ID: ${{ secrets.AWS_SUBNET_ID }}
  AWS_AVHROLE: ${{ secrets.AWS_AVHROLE }}
  AWS_INSTANCE_TYPE: t2.micro
# ...
    - name: Configure AWS Credentials
      uses: aws-actions/configure-aws-credentials@v1
      with:
        role-to-assume: ${{ env.AWS_AVHROLE }}
        aws-region: ${{ env.AWS_DEFAULT_REGION }}
```
An additional `AWS_INSTANCE_TYPE` variable is also defined. Use this if you wish to specify the type of AWS instance that will be used for your Arm Virtual Hardware AMI. If not specified, the default type for the AMI (`c5.large`) will be used.

## Run the workflow

Return to the `Actions` tab. If any changes were made to the above `basic.yml`, then a workflow run would have been automatically triggered. If not, select the `Arm Virtual Hardware basic example` action, and click `Run workflow` to manually trigger.

Click on the workflow run, and the `ci_test` job therein to follow progress. In the `Run tests` step, you will observe an AWS instance is started, using the Arm Virtual Hardware AMI. In your AWS console, navigate to `EC2` > `Instances`, and you will see this instance listed.

The workflow takes a few minutes to complete. Observe that one of the tests fails by default.

### Issues running workflow

You may encounter minor issues running the workflow to completion. The `Publish test results` step of the `ci_test` fails to write the results, and so the subsequent `badge` job fails.

This is due to restricted `GITHUB_TOKEN` permissions on forked repositories.

For more information, see the GitHub Actions [documentation](https://docs.github.com/en/actions/security-guides/automatic-token-authentication#permissions-for-the-github_token).

For the purposes of this example, this can be ignored.

## Fix the failing test

The example intentionally contains a failing test. To fix this locate the failing test in `/basic/main.c`:
```C
static void test_my_sum_fail(void) {
  const int sum = my_sum(1, -1);
  TEST_ASSERT_EQUAL_INT(2, sum);
}
```
and fix the `TEST_ASSERT_EQUAL_INT` parameter:
```C
static void test_my_sum_fail(void) {
  const int sum = my_sum(1, -1);
  TEST_ASSERT_EQUAL_INT(0, sum);
}
```
Push the fixed code to your repository and the workflow will run automatically.

Congratulations, you now have a fully automated CI/CD workflow using Arm Virtual Hardware, running on AWS, controlled by GitHub Actions.
