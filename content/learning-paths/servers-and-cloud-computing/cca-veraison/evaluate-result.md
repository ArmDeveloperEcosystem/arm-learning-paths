---
title: Evaluate results
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build the arc tool

You are already familiar with the evcli tool, which you can use to process attestation tokens. There is a very similar tool called `arc`, which you can use to process attestation results. The `arc` tool is also part of the Veraison project. 

Clone its repository as follows:

```bash
cd $HOME
git clone https://github.com/veraison/ear.git
```

The arc tool is in a subdirectory of this repo, so change directory as follows:

```bash
cd ear/arc
go build
```

You are now ready to proceed to the final step in this Learning Path, where you will use the arc tool to inspect the attestation result.

## Evaluate the Attestation Result
You have now submitted the example CCA attestation token to the Veraison verification service hosted by Linaro and saved the result to the file `attestation_result.jwt`. In this step, you will examine the result and see how it can be used to evaluate the trustworthiness of a CCA realm.

The attestation result is a JWT file, which stands for JSON Web Token. This means that the result has been cryptographically-signed by the Veraison verification service. In a previous step, you saved the public key that will be used to verify the signature.

The following command will use the `arc` tool, which you built in the previous step, to verify the cryptographic signature on the attestation result, and display the result in a human-readable format:

```bash
./arc verify --pkey $HOME/pkey.json --color $HOME/attestation_result.jwt
```

This command produces quite a lot of output. However, you will notice that a large amount of the output simply reflects the contents of the CCA attestation token that you inspected earlier with the evcli tool. The most interesting part of the output is towards the bottom, and should look like this:

```output
[trustworthiness vectors]
submod(CCA_REALM):
Instance Identity [affirming]: recognized and not compromised
Configuration [none]: no claim being made
Executables [warning]: unrecognized run-time
File System [none]: no claim being made
Hardware [none]: no claim being made
Runtime Opaque [none]: no claim being made
Storage Opaque [none]: no claim being made
Sourced Data [none]: no claim being made

submod(CCA_SSD_PLATFORM):
Instance Identity [affirming]: recognized and not compromised
Configuration [affirming]: all recognized and approved
Executables [affirming]: recognized and approved boot- and run-time
File System [none]: no claim being made
Hardware [affirming]: genuine
Runtime Opaque [affirming]: memory encryption
Storage Opaque [affirming]: encrypted secrets with HW-backed keys
Sourced Data [none]: no claim being made
```

This part of the output shows how the verification service has compared the attestation token against its expectations of a trustworthy system. It also shows the conclusions that were drawn from that comparison.

It is important to understand that an attestation result is not a simple "yes" or "no" answer to the question of whether the system is trustworthy. Instead, it is a set of data points, known as _trustworthiness vectors_. Each data point shows how a particular aspect of the system compares against the expectations set by the verification service. Each point of comparison can lead to one of the following results:

- __Affirming__. This is the most favorable result. It is given when the evidence in the attestation token shows a good match against the expectations of a trustworthy system.
- __Warning__. This is a less favorable result. It is given when the attestation token does not show a good match against the expectations of a trustworthy system.
- __None__. This is an unfavorable result, meaning that no comparison was possible, either because data was missing from the evidence in the attestation token, or because the verification service does not have any expectations to compare the evidence against, and is therefore unable to draw any conclusion.
- __Contraindicated__. This is the least favorable result. It is given when the evidence in the attestation token specifically contradicts the expectations of a trustworthy system.

You will also notice that the result is grouped into two sections known as submodules, and indicated with the `submod()` notation. Recall from the earlier steps that the CCA attestation token is grouped into two parts: the _realm_ token and the _platform_ token. This same grouping is therefore also reflected in the attestation result. There are separate results for each.

How is all this data used to make a single "yes" or "no" decision about whether this realm is trustworthy for a confidential computation to take place? After all, making such a decision is the whole purpose of the attestation process.

The next Learning Path in this series on Arm CCA answers this question by taking you through the steps needed to deploy an example workload that depends on attestation to release some secret data into a running realm. 

You will learn how to use policies to govern the strictness of the attestation process. You will also see how the workflow steps and data that you have just been using can be orchestrated together to form the common programming patterns of confidential computing.