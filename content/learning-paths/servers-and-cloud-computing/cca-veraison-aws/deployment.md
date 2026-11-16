---
title: Create the Veraison Deployment
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare your build environment

Lets first establish what AWS region will be used. On your Ubuntu host:

```bash
# Set this to the AWS region to be used
export AWS_REGION=us-east-1
```

Now, still in your Ubuntu host, run the following:

```bash
# Leave any previous python venv...
deactivate
hash -r

# Install virtual-environment support for Ubuntu's Python 3.12.
sudo apt update
sudo apt install python3.12-venv

# Use a fresh directory, preserving the existing ~/venv/aws environment.
export VERAISON_AWS_VENV="$HOME/venv/veraison-aws-py312"

/usr/bin/python3.12 -m venv "$VERAISON_AWS_VENV"
source "$VERAISON_AWS_VENV/bin/activate"

# Set this to fix issues with the make deploy scripts
export VERAISON_DEB="/tmp/veraison_0.0.261100+ebadb73_amd64.deb"

# Fixes and requirements for make deploy
sudo apt install gettext-base

# Follows AWS_REGION
export AWS_DEFAULT_REGION=${AWS_REGION}

# Verify what bootstrap will use.
python --version
python -m pip --version

# make sure we have cocli
mkdir -p "$HOME/.local/bin"

GOBIN="$HOME/.local/bin" go install github.com/veraison/cocli@v0.1.0
GOBIN="$HOME/.local/bin" go install github.com/veraison/evcli/v2@0e253e8

export PATH="$HOME/.local/bin:$PATH"
hash -r

command -v cocli
command -v evcli
```

You should see output similar to:

```output
Python 3.12.3
pip 24.0 from /usr/lib/python3/dist-packages/pip (python 3.12)
go: github.com/veraison/cocli@v0.1.0 requires go >= 1.25.0; switching to go1.26.11
go: github.com/veraison/evcli/v2@v2.2.1-0.20261013091050-0e253e803cfb requires go >= 1.25.0; switching to go1.26.11
/home/danson/.local/bin/cocli
/home/danson/.local/bin/evcli
```

Your Ubuntu environment is now ready for creating the Veraison deployment

## Create the Veraison Deployment
Now that your AWS account, internet domain and certificate are prepared, you are ready to deploy the Veraison services into AWS.

This process is highly automated, but will take between 30 to 60 minutes, as several resources need to be created in AWS.

The deployment process is documented in [Veraison's GitHub repository](https://github.com/veraison/services/blob/ebadb733d44ba2f8ffefdae49a0f0d3c1bfc9800/deployments/aws/README.md).

You can follow the instructions below to deploy the Veraison services into AWS:

Use the [Bootstrap](https://github.com/veraison/services/blob/ebadb733d44ba2f8ffefdae49a0f0d3c1bfc9800/deployments/aws/README.md#bootstrap) process first to clone the Veraison source code from GitHub and set up your build environment. This will take care of installing the dependencies that you need on your development machine.

The pinned services revision uses CoRIM-store commit `a2a60b6a11ad`, as specified in its [dependency file](https://github.com/veraison/services/blob/ebadb733d44ba2f8ffefdae49a0f0d3c1bfc9800/go.mod#L44). Its AWS deployment script still selects an older CoRIM-store tool for the sentinel image. Update that tool's pin before creating the image so database initialization includes the migrations required by the services, including the `tokens` table.

Download the [Veraison services repo patch scripts](../cca-veraison-aws-upstream-fixes.tar.gz) to your HOME directory on the Ubuntu host and unzip:

```bash
cd $HOME
tar xzpf $HOME/cca-veraison-aws-upstream-fixes.tar.gz
```

Then:

```bash
mkdir $HOME/cca_veraison
cd $HOME/cca_veraison
git clone https://github.com/veraison/services.git
git -C services checkout ebadb733d44ba2f8ffefdae49a0f0d3c1bfc9800

# patch the veraison repo to fix several issues with it so the build steps complete.
$HOME/cca-veraison-aws-upstream-fixes/apply.sh --check $HOME/cca_veraison/services
$HOME/cca-veraison-aws-upstream-fixes/apply.sh --apply $HOME/cca_veraison/services
```

Patching output should resemble:

```outputHEAD is now at ebadb73 Add details for psa-iot and arm-cca evidence apraisal (#509)
Target: /home/danson/cca_veraison/services
HEAD: ebadb733d44ba2f8ffefdae49a0f0d3c1bfc9800
  patches/0001-bootstrap-and-environment.patch: pending
  patches/0002-cli-and-package-build.patch: pending
  patches/0003-aws-templates-and-store-compatibility.patch: pending
  patches/0004-end-to-end-failure-handling.patch: pending
  patches/0005-deployment-regression-tests.patch: pending
  patches/0006-aws-quickstart-documentation.patch: pending
Dry run passed. Run again with --apply to update the clone.
Target: /home/danson/cca_veraison/services
HEAD: ebadb733d44ba2f8ffefdae49a0f0d3c1bfc9800
  patches/0001-bootstrap-and-environment.patch: pending
  patches/0002-cli-and-package-build.patch: pending
  patches/0003-aws-templates-and-store-compatibility.patch: pending
  patches/0004-end-to-end-failure-handling.patch: pending
  patches/0005-deployment-regression-tests.patch: pending
  patches/0006-aws-quickstart-documentation.patch: pending
Applied 6 patch groups.
Review with: git -C /home/danson/cca_veraison/services diff
```

If the patching succeeds, then we can bootstrap everything:

```bash
cd services/deployments/aws
make bootstrap
```

The `grep` command should show the `--rev` argument with `default='a2a60b6a11ad'`. Keep the sentinel tool's revision aligned with `services/go.mod` when changing the services revision.

Once your build environment is bootstrapped, you will use the [Quickstart](https://github.com/veraison/services/blob/ebadb733d44ba2f8ffefdae49a0f0d3c1bfc9800/deployments/aws/README.md#quickstart) procedure to provide some AWS configuration and create the deployment.

Next lets confirm that we have some additional requirements setup for the deployment to succeed:

```bash
source env/env.bash

# Ensure that we have the packages needed
"$VERAISON_AWS_VENV/bin/python" -m pip install --force-reinstall "envsubst==0.1.5"

# Replace the venv's command wrapper with GNU envsubst.
ln -sf /usr/bin/envsubst "$VIRTUAL_ENV/bin/envsubst"
hash -r

envsubst --version
"$VERAISON_AWS_VENV/bin/python" -c \
  'from envsubst import envsubst; print("Python envsubst import OK")'
```

Your output should resemble:

```output
envsubst (GNU gettext-runtime) 0.21
Copyright (C) 2003-2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Written by Bruno Haible.
Python envsubst import OK
```

You'll provide AWS-specific settings, including the IDs for your VPC and subnets, and the CIDR block allowed access to the deployment. In this deployment, you will use `misc/arm.cfg` file for example. Make sure you update `VERAISON_AWS_REGION` to the same region where you created your AWS certificate for your new domain.`VERAISON_AWS_DNS_NAME` needs to match the domain name you chose.

Please add the following to your `misc/arm.cfg` as well below `VERAISON_AWS_REGION`:

```bash
AWS_DEFAULT_REGION="$VERAISON_AWS_REGION"
AWS_REGION="$VERAISON_AWS_REGION"
```

An example of a configured `misc/arm.cfg` looks something like this (your AWS region and DNS name may/will likely be different though):

```output
##############################################################################
# Veraison Deployment Account-specific settings.
# These settings are specific to the Arm account used by the core development
# team. Users without access to this account must provide their own version of
# this file (or configure these settings inside deployment.cfg).
##############################################################################
VERAISON_AWS_REGION=us-east-1
AWS_DEFAULT_REGION="$VERAISON_AWS_REGION"
AWS_REGION="$VERAISON_AWS_REGION"
VERAISON_AWS_ADMIN_CIDR=217.140.96.0/20
VERAISON_AWS_VPC_CIDR=10.1.0.0/16
VERAISON_AWS_DNS_NAME=veraison-example.com
IAM_LOGGER_ROLE_NAME=
IAM_INSTANCE_PROFILE_NAME=
IAM_PERMISSION_BOUNDARY_ARN=
```

{{% notice Note %}}
Some AWS accounts may have permissions boundaries enabled (such as assumed role accounts). In this case you will need to create the logger and instance profile roles and specify the permissions boundary arn specifically. Most standard AWS accounts do not require this though so you can just leave them empty. 
{{% /notice %}}

Once the account-specific config file is created, define `AWS_ACCOUNT_CFG` environment variable to point to it and then create the deployment:

```bash
export AWS_ACCOUNT_CFG=misc/arm.cfg  # replace with path to your config
make deploy
```

You do not need to use the end-to-end flow as described in the document. Later in this Learning Path, you will perform some additional steps to prepare and use the Veraison services.

The rest of the document provides additional information about how to manage the deployment, but you don't need this now.

## Check the Deployment Status
In the command shell where you ran the steps above, run the following command:

```bash
veraison status
```
This command outputs a status report for the deployment. If successful, it includes information about:

- The Amazon Machine Images (AMIs) that have been used for the servers.
- The status of the VPC stack, support stack and services stack. All of these should read as `created`.
- Information about RDS, ElastiCache and EC2 resources in the deployment.
- The version of the Veraison software that is running.
- The public part of the key that is used to sign attestation results (known as the EAR Verification Key).
- A list of media types that Veraison accepts as attestation evidence.
- A list of media types that Veraison accepts as endorsements.

Use the following command to test the REST API endpoint of the verification service. Remember to substitute `example-veraison.com` with the domain name that you used in the initial step, but you will need to keep the `services` prefix as shown.

```bash
curl https://services.example-veraison.com:8443/.well-known/veraison/verification
```

If it succeeds, this command produces some JSON output, including the EAR verification key.

Use the following command to test the REST API endpoint of the endorsement provisioning service. Remember to substitute `example-veraison.com` with the domain name that you used in the initial step.

```bash
curl https://services.example-veraison.com:9443/.well-known/veraison/provisioning
```

This command produces JSON output containing the list of supported media types for endorsement.

Your Veraison services are now successfully deployed - you're ready for the next step.
