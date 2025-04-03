---
title: Add CCA Platform Endorsements to Veraison
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction to Endorsements
Now that your Veraison services are deployed into AWS, the next step is to provide the endorsements for the CCA platform. This will allow the Veraison services to act as a verifier for CCA attestation tokens.

## Get the Linaro Endorsement Tool
The endorsement tool is available on Linaro's Git server. Run the following command to clone the repository into a suitable directory on your machine:

```bash
cd $HOME
git clone https://git.codelinaro.org/linaro/dcap/cca-demos/poc-endorser
```
## Configure the Endorsement Tool for AWS
By default, the endorsement tool assumes that your Veraison services are deployed locally on your machine. This is not the case here, because your Veraison services have been deployed into AWS instead. Therefore, you will need to provide some configuration to the tool, in order to point it at the correct API endpoints with the required authentication.

In the command shell where you created the AWS deployment of Veraison, run the following command:

```bash
cd $HOME/services/deployments/aws
veraison create-client-config -o /tmp/vconfig
```

The output should look like:
```output
2025-04-03 19:12:21,442 create-client-config INFO: creating Veraison client config(s)...
2025-04-03 19:12:21,446 create-client-config INFO: generating cocli config...
2025-04-03 19:12:21,447 create-client-config INFO: done.
2025-04-03 19:12:21,447 create-client-config INFO: generating evcli config...
2025-04-03 19:12:21,448 create-client-config INFO: done.
2025-04-03 19:12:21,448 create-client-config INFO: generating pocli config...
2025-04-03 19:12:21,449 create-client-config INFO: done.
```
Next, change back to the directory where you cloned the endorsement tool.

```bash
cd $HOME/poc-endorser/
```
 Use your preferred text editor to edit the file `endorse.sh` in the endorsement tool. Locate these lines in the script:

```code
api_server: https://provisioning-service:8888/endorsement-provisioning/v1/submit
auth: oauth2
username: veraison-provisioner
password: veraison
client_id: veraison-client
client_secret: YifmabB4cVSPPtFLAmHfq7wKaEHQn10Z
token_url: https://keycloak-service:11111/realms/veraison/protocol/openid-connect/token
```
Delete these lines, and replace them with the contents of `/tmp/vconfig/cocli/config.yaml`. You should notice that the URL endpoints now refer to your AWS domain, while some of the other details may remain the same. Exit the text editor, making sure to save your changes.

## Provision the Endorsements to Veraison
The provisioning tool runs inside a Docker container. 
First, make sure you have [installed Docker](/install-guides/docker) on your machine.
In the command shell where you have cloned the endorsement tool, run the following command:

```bash
make build
```
This command will build the Docker image locally on your machine.

Now run the following command to provision the endorsements:

```bash
make endorse
```
This command will run the Docker container and send the CCA endorsements to Veraison. You should see output similar to the following:

```output
docker run --network=host "cca-demo/endorser"
+ GOLDEN=cca-token.cbor
+ CPAK=cpak-pub.json
+ CORIM=cca-endorsements.cbor
+ gen-corim cca cca-token.cbor cpak-pub.json --template-dir corim-templates --corim-file cca-endorsements.cbor
>> generated "cca-endorsements.cbor" using "cca-token.cbor"
+ cat
+ cocli corim submit '--ca-cert=/app/rootCA.crt' '--corim-file=cca-endorsements.cbor' '--media-type=application/corim-unsigned+cbor; profile="http://arm.com/cca/ssd/1"' '--config=cocli.yaml'
+ '[' 0 '=' 0 ]
```
Next, return to the command shell where you created the Veraison AWS deployment, and run the following command:

```bash
cd $HOME/services/deployments/aws
veraison stores
```
This command will query Veraison's database stores. If the CCA endorsements were provisioned successfully, the output should look something like the example below. (You don't need to be concerned with understanding all of the detail here.)

```output
TRUST ANCHORS:
--------------
ARM_CCA://0/f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=/AQcGBQQDAgEADw4NDAsKCQgXFhUUExIREB8eHRwbGhkY
{
    "attributes": {
        "iak-pub": "-----BEGIN PUBLIC KEY-----\nMHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEIShnxS4rlQiwpCCpBWDzlNLfqiG911FP\n8akBr+fh94uxHU5m+Kijivp2r2oxxN6MhM4tr8mWQli1P61xh3T0ViDREbF26DGO\nEYfbAjWjGNN7pZf+6A4OTHYqEryz6m7U\n-----END PUBLIC KEY-----\n",
        "impl-id": "f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=",
        "inst-id": "AQcGBQQDAgEADw4NDAsKCQgXFhUUExIREB8eHRwbGhkY"
    },
    "scheme": "ARM_CCA",
    "subType": "",
    "type": "trust anchor"
}

ENDORSEMENTS:
-------------
ARM_CCA://0/f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=
{
    "attributes": {
        "impl-id": "f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=",
        "measurement-desc": "sha-256",
        "measurement-type": "RSE_BL1_2",
        "measurement-value": "micfKpFrC27mzsskJvCzIG7wdFeL5V2byU9vP+Orhqo=",
        "signer-id": "U3h5YwdTXfPsjYsVouLcVkFBnD0wYM/jIjjA+pc/eqM="
    },
    "scheme": "ARM_CCA",
    "subType": "platform.sw-component",
    "type": "reference value"
}

ARM_CCA://0/f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=
{
    "attributes": {
        "impl-id": "f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=",
        "measurement-desc": "sha-256",
        "measurement-type": "RSE_BL2",
        "measurement-value": "U8I05ehHK2rFHBrhyrP+BvrQU7646/2Jd7AQZVv908M=",
        "signer-id": "U3h5YwdTXfPsjYsVouLcVkFBnD0wYM/jIjjA+pc/eqM="
    },
    "scheme": "ARM_CCA",
    "subType": "platform.sw-component",
    "type": "reference value"
}

ARM_CCA://0/f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=
{
    "attributes": {
        "impl-id": "f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=",
        "measurement-desc": "sha-256",
        "measurement-type": "RSE_S",
        "measurement-value": "ESHPzNWRPwpj/sQKb/1E6mT53BNcZmNLoAHRC89DAqI=",
        "signer-id": "U3h5YwdTXfPsjYsVouLcVkFBnD0wYM/jIjjA+pc/eqM="
    },
    "scheme": "ARM_CCA",
    "subType": "platform.sw-component",
    "type": "reference value"
}

ARM_CCA://0/f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=
{
    "attributes": {
        "impl-id": "f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=",
        "measurement-desc": "sha-256",
        "measurement-type": "AP_BL1",
        "measurement-value": "FXG17Hi9aFEr94MLtqKkSyBHx99XvOeeuKHA5b6gpQE=",
        "signer-id": "U3h5YwdTXfPsjYsVouLcVkFBnD0wYM/jIjjA+pc/eqM="
    },
    "scheme": "ARM_CCA",
    "subType": "platform.sw-component",
    "type": "reference value"
}

ARM_CCA://0/f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=
{
    "attributes": {
        "impl-id": "f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=",
        "measurement-desc": "sha-256",
        "measurement-type": "AP_BL2",
        "measurement-value": "EBWbryYrQ6ktldtZ2uH3LGRRJzAWYeCjzk44spWpfFg=",
        "signer-id": "U3h5YwdTXfPsjYsVouLcVkFBnD0wYM/jIjjA+pc/eqM="
    },
    "scheme": "ARM_CCA",
    "subType": "platform.sw-component",
    "type": "reference value"
}

ARM_CCA://0/f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=
{
    "attributes": {
        "impl-id": "f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=",
        "measurement-desc": "sha-256",
        "measurement-type": "SCP_BL1",
        "measurement-value": "EBIuhWs/zUnwY2NjF0dhSctzChqhz6rYGFUrcvVtb2g=",
        "signer-id": "U3h5YwdTXfPsjYsVouLcVkFBnD0wYM/jIjjA+pc/eqM="
    },
    "scheme": "ARM_CCA",
    "subType": "platform.sw-component",
    "type": "reference value"
}

ARM_CCA://0/f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=
{
    "attributes": {
        "impl-id": "f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=",
        "measurement-desc": "sha-256",
        "measurement-type": "SCP_BL2",
        "measurement-value": "qmehabC7oheqCqiKZTRpIMhMQkR8NrpffqZfQiwf5dg=",
        "signer-id": "8UtJh5BLy1gU5EWaBX7U0g9YpjMVIoinYSFNzSh4C1Y="
    },
    "scheme": "ARM_CCA",
    "subType": "platform.sw-component",
    "type": "reference value"
}

ARM_CCA://0/f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=
{
    "attributes": {
        "impl-id": "f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=",
        "measurement-desc": "sha-256",
        "measurement-type": "AP_BL31",
        "measurement-value": "Lm0xpZg6kSUb+uWu+hwKGdi6PPYB0OinBrTPqWYaa4o=",
        "signer-id": "U3h5YwdTXfPsjYsVouLcVkFBnD0wYM/jIjjA+pc/eqM="
    },
    "scheme": "ARM_CCA",
    "subType": "platform.sw-component",
    "type": "reference value"
}

ARM_CCA://0/f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=
{
    "attributes": {
        "impl-id": "f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=",
        "measurement-desc": "sha-256",
        "measurement-type": "RMM",
        "measurement-value": "oftQ5shvrhZ57zNRKW/WcTQRoIz43ReQpP0F+uhogWQ=",
        "signer-id": "U3h5YwdTXfPsjYsVouLcVkFBnD0wYM/jIjjA+pc/eqM="
    },
    "scheme": "ARM_CCA",
    "subType": "platform.sw-component",
    "type": "reference value"
}

ARM_CCA://0/f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=
{
    "attributes": {
        "impl-id": "f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=",
        "measurement-desc": "sha-256",
        "measurement-type": "HW_CONFIG",
        "measurement-value": "GiUkApcvYFf6U8wXK1K5/8ppjhgxH6zQ87Buyq73nhc=",
        "signer-id": "U3h5YwdTXfPsjYsVouLcVkFBnD0wYM/jIjjA+pc/eqM="
    },
    "scheme": "ARM_CCA",
    "subType": "platform.sw-component",
    "type": "reference value"
}

ARM_CCA://0/f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=
{
    "attributes": {
        "impl-id": "f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=",
        "measurement-desc": "sha-256",
        "measurement-type": "FW_CONFIG",
        "measurement-value": "mpKtvAzuOO9ljHHOGxv4xlZo8Wa/shNkTIlcyxrQeiU=",
        "signer-id": "U3h5YwdTXfPsjYsVouLcVkFBnD0wYM/jIjjA+pc/eqM="
    },
    "scheme": "ARM_CCA",
    "subType": "platform.sw-component",
    "type": "reference value"
}

ARM_CCA://0/f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=
{
    "attributes": {
        "impl-id": "f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=",
        "measurement-desc": "sha-256",
        "measurement-type": "TB_FW_CONFIG",
        "measurement-value": "I4kDGAzBBOwsXYs/IMW8YbOJ7AqWffjMIIzcfNRUF08=",
        "signer-id": "U3h5YwdTXfPsjYsVouLcVkFBnD0wYM/jIjjA+pc/eqM="
    },
    "scheme": "ARM_CCA",
    "subType": "platform.sw-component",
    "type": "reference value"
}

ARM_CCA://0/f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=
{
    "attributes": {
        "impl-id": "f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=",
        "measurement-desc": "sha-256",
        "measurement-type": "SOC_FW_CONFIG",
        "measurement-value": "5sIejSYP5xiC3r2zOdJAKiynZIUpvCMD9IZJvOA4ABc=",
        "signer-id": "U3h5YwdTXfPsjYsVouLcVkFBnD0wYM/jIjjA+pc/eqM="
    },
    "scheme": "ARM_CCA",
    "subType": "platform.sw-component",
    "type": "reference value"
}

ARM_CCA://0/f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=
{
    "attributes": {
        "impl-id": "f0VMRgIBAQAAAAAAAAAAAAMAPgABAAAAUFgAAAAAAAA=",
        "platform-config-id": "z8/Pzw==",
        "platform-config-label": "cfg v1.0.0"
    },
    "scheme": "ARM_CCA",
    "subType": "platform.config",
    "type": "reference value"
}

POLICIES:
---------
```
Your Veraison deployment is now complete and ready to act as an attestation verification service for pre-silicon Arm CCA platforms.
