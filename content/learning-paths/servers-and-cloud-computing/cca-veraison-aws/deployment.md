---
title: Create the Veraison Deployment
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create the Veraison Deployment
Now that your AWS account, internet domain and certificate are prepared, you are ready to deploy the Veraison services into AWS.

This process is highly automated, but it takes some time, because a number of resources need to be created in AWS. Be prepared for this step to take from 30 to 60 minutes, although there won't be too much for you to do during this time. You will just run a command to kick off the process.

The deployment process is documented in [Veraison's GitHub repository](https://github.com/veraison/services/blob/main/deployments/aws/README.md). 

You can follow the instructions below to deploy the Veraison services into AWS:

Use the [Bootstrap](https://github.com/veraison/services/tree/main/deployments/aws#bootstrap) process first to clone the Veraison source code from GitHub and set up your build environment. This will take care of installing the dependencies that you need on your development machine.

```bash
git clone https://github.com/veraison/services.git
cd services/deployments/aws
make bootstrap
```
Once your build environment is bootstrapped, you will use the [Quickstart](https://github.com/veraison/services/tree/main/deployments/aws#quickstart) procedure to provide some AWS configuration and create the deployment.

You need to provide your AWS account-specific configuration that specifies the IDs of the VPC and subnets that will be used for the deployment as well as the CIDR that will be granted access to the deployment. In this deployment you will use `misc/arm.cfg` file for example. Make sure you update `VERAISON_AWS_REGION` to the same region where you created your AWS Certificate for your new domain.`VERAISON_AWS_DNS_NAME` will need to match the domain name you chose. 

Once the account-specific config file is created, define `AWS_ACCOUNT_CFG` environment variable to point to it and then create the deployment.

```bash
source env/env.bash
export AWS_ACCOUNT_CFG=misc/arm.cfg  # replace with path to your config
make deploy
```

You do not need to use the end-to-end flow as described in the document. Later in this learning path, you will perform some additional steps to prepare and use the Veraison services.

The rest of the document provides additional information about how to manage the deployment, but you don't need this now.

## Check the Deployment Status
In the command shell where you ran the steps above, run the following command:

```bash
veraison status
```
This command will output a status report for the deployment. If successful, it will include information about:-

- The Amazon Machine Images (AMIs) that have been used for the servers.
- The status of the VPC stack, support stack and services stack. All of these should read as `created`.
- Information about RDS, ElastiCache and EC2 resources in the deployment.
- The version of the Veraison software that is running.
- The public part of the key that is used to sign attestation results (known as the EAR Verification Key).
- A list of media types that Veraison will accept as attestation evidence.
- A list of media types that Veraison will accept as endorsements.

Use the following command to test the REST API endpoint of the verification service. Remember to substitute `example-veraison.com` with the domain name that you used in the initial step, but you will need to keep the `services` prefix as shown.

```bash
curl https://services.example-veraison.com:8443/.well-known/veraison/verification
```

If it succeeds, this command produces some JSON output, including the EAR verification key.

Use the following command to test the REST API endpoint of the endorsement provisioning service. Remember to substitute `example-veraison.com` with the domain name that you used in the initial step.

```bash
curl https://services.example-veraison.com:9443/.well-known/veraison/provisioning
```

This command will produce JSON output containing the list of supported media types for endorsement.

Your Veraison services are now deployed and working, and you can proceed to the next step.
