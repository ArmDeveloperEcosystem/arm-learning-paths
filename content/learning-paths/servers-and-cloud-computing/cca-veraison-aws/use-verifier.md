---
title: Use Veraison Service for CCA Attestation
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Use Your AWS Deployment to Verify a CCA Attestation Token
Now that your Veraison services are deployed into AWS and initialized with endorsements for the CCA reference platform, you are ready to make use of the verification service to verify a CCA attestation token.

To do this, you should follow the steps set out in the Learning Path [Get Started with CCA Attestation and Veraison](/learning-paths/servers-and-cloud-computing/cca-veraison/). Follow the steps in this Learning Path exactly, except you'll use your AWS-hosted Veraison deployment instead of Linaro's service.

The URL for the Veraison server provided by Linaro is `https://veraison.test.linaro.org:8443`.

Instead of this URL, use the one for your own Veraison service, which will be of the form `https://services.example-veraison.com:8443`, although you need to replace `example-veraison.com` with your AWS domain.

Apart from this URL change, all other steps in the Learning Path remain the same.
