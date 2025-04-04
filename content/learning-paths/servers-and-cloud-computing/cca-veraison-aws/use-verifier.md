---
title: Use Veraison Service for CCA Attestation
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Use Your AWS Deployment to Verify a CCA Attestation Token
Now that your Veraison services are deployed into AWS and initialized with endorsements for the CCA reference platform, you are ready to make use of the verification service to verify a CCA attestation token.

To do this, you should follow the steps set out in the learning path [Get Started with CCA Attestation and Veraison](https://learn.arm.com/learning-paths/servers-and-cloud-computing/cca-veraison/). However, you should follow this learning path in such a way that it uses your AWS deployment of Veraison, instead of the service provided by Linaro.

The URL for the Veraison server provided by Linaro is `https://veraison.test.linaro.org:8443`.

Instead if using this URL, you should use the URL for your Veraison service, which will be of the form ` https://services.example-veraison.com:8443`, although you will need to replace `example-veraison.com` with your own registered AWS domain.

Apart from this URL change, all other steps in the learning path remain the same.
