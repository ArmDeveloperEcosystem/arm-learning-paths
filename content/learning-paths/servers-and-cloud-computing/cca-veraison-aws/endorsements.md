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
cd $HOME/cca_veraison/services/end-to-end
SCHEME=cca ./end-to-end-aws provision
```

This command sends the CCA endorsements to your AWS-hosted Veraison deployment. You should see output similar to the following:

```output
cocli corim submit --config=/tmp/veraison-aws-client-configs/cocli/config.yaml --corim-file=/home/danson/cca_veraison/services/end-to-end/input/cca-endorsements.cbor '--media-type=application/rim+cbor; profile="tag:arm.com,2025:cca_platform#1.0.0"'
cocli corim submit --config=/tmp/veraison-aws-client-configs/cocli/config.yaml --corim-file=/home/danson/cca_veraison/services/end-to-end/input/cca-realm-endorsements.cbor '--media-type=application/rim+cbor; profile="tag:arm.com,2025:cca_realm#1.0.0"'
```

Next, run the following command:

```bash
cd $HOME/cca_veraison/services/deployments/aws
veraison stores
```
This command will query Veraison's database stores. If the CCA endorsements were provisioned successfully, the output should look something like the example below. (You don't need to understand all of the detail here.)

```output
┌────┬────────┬───────────┬────────────────────────────────────────────────┬───────────┬─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ ID │ ACTIVE │   LABEL   │                     SOURCE                     │    TYPE   │                                                               ENVIRONMENT                                                               │
├────┼────────┼───────────┼────────────────────────────────────────────────┼───────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│    │        │           │ manifest: 00000000-0000-0001-cca6-000000000001 │           │ class: 7f454c4602010100000000000000000003003e00010000005058000000000000                                                                 │
│  2 │ true   │ 0/ARM_CCA │ module: ceb50b5a-a61e-4666-8b6b-33cb957b6801   │ attest    │ instance: AQcGBQQDAgEADw4NDAsKCQgXFhUUExIREB8eHRwbGhkY                                                                                  │
│    │        │           │                                                │           │                                                                                                                                         │
│  3 │ true   │ 0/ARM_CCA │ manifest: 00000000-0000-0001-cca6-000000000001 │ reference │ class: 7f454c4602010100000000000000000003003e00010000005058000000000000                                                                 │
│    │        │           │ module: 43bbe37f-2e61-4b33-aed3-53cff1428b16   │           │                                                                                                                                         │
│  4 │ true   │ 0/ARM_CCA │ manifest: 00000000-0000-0001-cca4-000000000001 │ reference │ class: 43434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343434343 │
│    │        │           │ module: 43bbe37f-2e61-4b33-aed3-53cff1428b16   │           │                                                                                                                                         │
└────┴────────┴───────────┴────────────────────────────────────────────────┴───────────┴─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
Your Veraison deployment is now ready to act as an attestation verification service for pre-silicon Arm CCA platforms.