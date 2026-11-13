---
title: Add CCA Platform Endorsements to Veraison
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction to Endorsements
Now that your Veraison services are deployed into AWS, the next step is to provide the endorsements for the CCA platform. This will allow the Veraison services to act as a verifier for CCA attestation tokens.

## Provision the Endorsements to Veraison

Return to the command shell where you created the Veraison AWS deployment, and run the following command:

```bash
cd $HOME/services/end-to-end
SCHEME=cca ./end-to-end-aws provision
```

This command sends the CCA endorsements to your AWS-hosted Veraison deployment. You should see output similar to the following:

```output
TO-DO
```

Next, run the following command:

```bash
cd $HOME/services/deployments/aws
veraison stores
```
This command will query Veraison's database stores. If the CCA endorsements were provisioned successfully, the output should look something like the example below. (You don't need to understand all of the detail here.)

```output
TO-DO
```
Your Veraison deployment is now ready to act as an attestation verification service for pre-silicon Arm CCA platforms.