---
title: Use the verification service
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Attestation Verification Service for Pre-Silicon CCA Platforms
[Linaro](https://www.linaro.org/) provides an attestation verifier service for pre-silicon CCA platforms, such as the Fixed Virtual Platform (FVP). This service is available publicly and is hosted on Linaro infrastructure. This verification service can be used to verify CCA attestation tokens that come from emulated Arm platforms, including the example token that you have been using in this exercise.

Linaro’s verification service is implemented using components from the open source [Veraison](https://github.com/veraison) project.

The URL for reaching this experimental verifier service is https://veraison.test.linaro.org:8443.

To check that you can reach the Linaro attestation verifier service, run the following command:

```bash
curl https://veraison.test.linaro.org:8443/.well-known/veraison/verification
```

This is a simple call to query the well-known characteristics of the verification service. If it succeeds, it will return a JSON response that looks something like this:

```output
{
  "ear-verification-key": {
    "alg": "ES256",
    "crv": "P-256",
    "kty": "EC",
    "x": "usWxHK2PmfnHKwXPS54m0kTcGJ90UiglWiGahtagnv8",
    "y": "IBOL-C3BttVivg-lSreASjpkttcsz-1rb7btKLv8EX4"
  },
  "media-types": [
    "application/vnd.parallaxsecond.key-attestation.tpm",
    "application/eat-cwt; profile=\http://arm.com/psa/2.0.0\",
    "application/eat+cwt; eat_profile=\"tag:psacertified.org,2023:psa#tfm\"",
    "application/eat-collection; profile=\http://arm.com/CCA-SSD/1.0.0\",
    "application/eat+cwt; eat_profile=\"tag:psacertified.org,2019:psa#legacy\"",
    "application/vnd.enacttrust.tpm-evidence",
    "application/vnd.parallaxsecond.key-attestation.cca",
    "application/psa-attestation-token",
    "application/pem-certificate-chain"
  ],
  "version": "commit-2063e7e",
  "service-state": "READY",
  "api-endpoints": {
    "newChallengeResponseSession": "/challenge-response/v1/newSession"
  }
}
```

This JSON response contains all the information that you need to use the verification service. Review the different JSON properties.

- The `ear-verification-key` is the cryptographic key that you will use later to verify the results that are returned by the service.

- The `media-types` entry provides the list of the different attestation data formats that the verification service supports. If you look down this list, you will find an entry for the CCA profile of the EAT format. It is the fourth entry in the list. This tells us that the service is capable of processing Arm CCA attestation tokens.

- The `api-endpoints` entry describes the set of RESTful APIs that are supported by the service. When verifying an attestation token, you will use the challenge-response API.

If you can reach the verification service, you are now ready to use it to evaluate the CCA example token.

## Save the Public Key of the Verification Service

One of the properties that was returned in the previous step was the public key of the verification service. This key will be needed later to check the signature on the attestation results. All that is needed in this step is to copy the contents of the `ear-verification-key` field from the previous step and save it to a separate JSON file.

The easiest way to do this is to use the `jq` utility. 
You can save the public key by repeating the curl command from the previous step and use `jq` to filter the response down to just the public key part. Save it into a file called `pkey.json`:

```bash
curl -s -N https://veraison.test.linaro.org:8443/.well-known/veraison/verification | jq '."ear-verification-key"' > $HOME/pkey.json
```
You have now saved the public key of the verification service. You are now ready to submit the CCA example attestation token to the service and get an attestation result.

## Submit the CCA Example Token to the Verification Service
To submit the example CCA attestation token to the verification service, you will need to use the `evcli` tool once again. First, configure the correct API endpoint for the Linaro verifier service:

```bash
export API_SERVER=https://veraison.test.linaro.org:8443/challenge-response/v1/newSession
```

Now submit the token using the following command. The output of this command is an attestation result, which will be saved in a file called `attestation_result.jwt`:

```bash
./evcli cca verify-as relying-party --token $HOME/cca_example_token.cbor | tr -d \" > $HOME/attestation_result.jwt
```

{{% notice Note%}}
The `| tr -d \"` is used to remove the double quotes in capturing the output from the `evcli` command.
{{% /notice %}}

The verification service has now evaluated the token and returned a result, which you have saved.
The last two steps in this Learning Path are about understanding the resultant data that came back from the verification service.
