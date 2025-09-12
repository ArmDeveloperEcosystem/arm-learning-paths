---
# User change
title: "Run an end-to-end Attestation with Arm CCA and Trustee"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Overview
In this section you’ll run the **Trustee services** (AS, KBS, RVPS), launch a **CCA realm** on **Arm FVP**, generate attestation evidence, and request a secret. You’ll intentionally fail the first request to see how **attestation policy** gates secret release, then **endorse the realm initial measurement (RIM)**, re-attest, and successfully retrieve the secret.

## Install dependencies

Start by installing Docker. On Ubuntu 24.04 LTS, set up Docker’s APT repository:

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to APT sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

Install Git and Docker packages:
```
sudo apt-get install -y git docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Add your user name to the Docker group (open a new shell after this so the change takes effect):
``` bash
sudo usermod -aG docker $USER
newgrp docker
```

## Start Trustee services containers

Clone the `cca-trustee` repository:
``` bash
git clone https://github.com/ArmDeveloperEcosystem/cca-trustee.git
```

This repository contains configuration to run Trustee services (KBS, AS, RVPS) with CCA attestation support as a simple cluster. The configuration is based on the recommended settings from [KBS Cluster](https://github.com/confidential-containers/trustee/blob/main/kbs/docs/cluster.md).

Additional Learning Path–specific changes include:

- External Linaro CCA verifier in the AS configuration

- Attestation policy with CCA rules

- An *affirming* resource policy

- A demo secret message

- A shared Docker network for all containers in this demo

Go into the `cca-trustee` directory and start the Trustee services Docker containers (as detached services):
``` bash { output_lines = "3-9" }
cd cca-trustee
docker compose up -d
[+] Running 6/6
 ✔ Network cca-trustee                 Created
 ✔ Container cca-trustee-setup-1       Exited
 ✔ Container cca-trustee-rvps-1        Started
 ✔ Container cca-trustee-as-1          Started
 ✔ Container cca-trustee-kbs-1         Started
 ✔ Container cca-trustee-kbs-client-1  Started
```

While running the demo you can also check logs of the Trustee services in this terminal:
``` bash
docker compose logs <service>
```
Where `service` is either `as`,`kbs` or `rvps`.

## Launch a CCA Realm with FVP

With the Trustee Services running in one terminal, open up a new terminal in which you will run CCA attestations.

Pull the Docker image with the pre-built FVP, and then run the container connected to the same Docker network:

```bash
docker pull armswdev/cca-learning-path:cca-simulation-v2
```
```bash
docker run --rm -it --network cca-trustee armswdev/cca-learning-path:cca-simulation-v2
```

Within your running container, launch the `run-cca-fvp.sh` script to run the Arm CCA pre-built binaries on the FVP:

```bash
./run-cca-fvp.sh
```

The `run-cca-fvp.sh` script uses the `screen` command to connect to the different UARTs in the FVP.

When the host Linux boots, log in:

Enter root as the username:
```output

Welcome to the CCA host
host login: root
(host) #
```

Change directory to `/cca` and use `lkvm` to launch a guest Linux in a Realm:
```bash
cd /cca
./lkvm run --realm --disable-sve --irqchip=gicv3-its \
  --firmware KVMTOOL_EFI.fd -c 1 -m 512 --no-pvtime --pmu \
  --disk guest-disk.img --restricted_mem --virtio-transport pci
```

You should see the realm boot.

After the realm boots, log in, using the root again as the username:

```output

Welcome to the CCA realm
realm login: root
(realm) #
```

## Request a secret using attestation

This first attempt intentionally fails so you can see why and how attestation policy gates secret release.

Change directory to `/cca` and use `openssl` to create a realm RSA key:
```bash
cd /cca
openssl genrsa -traditional -out realm.key
```

Run the attestation command and save the EAT Attestation Result (EAR) message in JWT (JSON Web Token) format in a file named `ear.jwt`:
```bash
./kbs-client --url http://kbs:8080 attest --tee-key-file realm.key > ear.jwt
```

Request the demo secret with that EAR:

```bash
  ./kbs-client --url http://kbs:8080 get-resource \
  --tee-key-file realm.key --attestation-token ear.jwt \
  --path "cca-trustee/demo-message/message.txt"
```  


The request will fail with `Access denied by policy` and `Token Verifier` errors:
```output
[2025-07-23T14:42:55Z WARN  kbs_protocol::client::token_client] Authenticating with KBS failed. Get a new token from the token provider: ErrorInformation {
        error_type: "https://github.com/confidential-containers/kbs/errors/PolicyDeny",
        detail: "Access denied by policy",
    }
[2025-07-23T14:42:55Z WARN  kbs_protocol::client::token_client] Authenticating with KBS failed. Get a new token from the token provider: ErrorInformation {
        error_type: "https://github.com/confidential-containers/kbs/errors/TokenVerifierError",
        detail: "Token Verifier error",
    }
[2025-07-23T14:42:55Z WARN  kbs_protocol::client::token_client] Authenticating with KBS failed. Get a new token from the token provider: ErrorInformation {
        error_type: "https://github.com/confidential-containers/kbs/errors/TokenVerifierError",
        detail: "Token Verifier error",
    }
Error: request unauthorized
```

## Evaluate the Attestation result

In the previous step, the KBS failed to provide the requested secret. To understand why this happened, you need to learn more about how the attestation result is used to evaluate the trustworthiness of a CCA realm.
In this step, you will examine the attestation result more closely.

The following command will use the `arc` tool to verify the cryptographic signature on the attestation result and display the result in a human-readable format:

```bash
./arc verify ear.jwt
```

{{% notice EAR expiry note %}}
The EAR is valid for 30 minutes. If it expires, re-run the attestation command to generate a fresh token.
If you spend more time on analyzing the message you will start seeing errors from `arc verify` command:

``` output
Using JWK key from JWT header
Error: verifying signed EAR from "ear.jwt" using "JWK header" key: failed verifying JWT message: jwt.Parse: failed to parse token: jwt.Validate: validation failed: "exp" not satisfied: token is expired
```
{{% /notice %}}


The `arc verify` command produces quite a lot of output.

However, the main part is the CCA attestation token that is similar to the one you inspected in
[Get Started with CCA Attestation and Veraison](/learning-paths/servers-and-cloud-computing/cca-veraison) Learning Path.

Check the trustworthiness vectors near the end of the output:

```output
[trustworthiness vectors]
submod(cpu0):
Instance Identity [none]: no claim being made
Configuration [none]: no claim being made
Executables [warning]: unrecognized run-time
File System [none]: no claim being made
Hardware [affirming]: genuine
Runtime Opaque [none]: no claim being made
Storage Opaque [none]: no claim being made
Sourced Data [none]: no claim being made
```

This part of the output shows how the attestation service has compared the attestation token against its expectations of a trustworthy system. These comparisons are known as *trustworthiness vectors*. It also shows the conclusions that were drawn from that comparison.

Note these two trustworthiness vectors in the result:
- __Hardware [affirming]__. Evidence in the attestation token shows a good match against the expectations of CCA platform.
- __Executables [warning]__. Attestation token does not show a good match against the expectations of a recognized genuine set of approved executables have been loaded during the boot process.

You can also check the status of the EAR:
```bash { output_lines = "2" }
./arc verify ear.jwt |grep ear.status
            "ear.status": "warning",
```

The warning status is the reason why the KBS does not grant access
to the secret that you requested in the earlier step.
It has not concluded that the realm is trustworthy.
But this is simply because you have not supplied an expected reference measurement
for the realm. You will do this in the next step.

## Endorse Realm Initial Measurement (RIM)

For a successful attestation of your CCA real you need to provide
the Trustee Reference Values Provider Service (RVPS) with a known good reference value.

In a production environment, the known good reference value is generated using a deployment-specific process,
but for demonstration purposes and simplification, you will use the value which was calculated by `kbs-client`
in the realm and included into the EAT.

Get the RIM from the attestation token:
```bash { output_lines = "2" }
./arc verify ear.jwt |grep "cca-realm-initial-measurement"
                        "cca-realm-initial-measurement": "Nfpl4Y32d2hCpeYsarnnGv9xcbTMTBX90x0ZjnAMjLk=",
```

In the terminal where you started Trustee services, run `endorse-rim.sh` script with the RIM you copied from EAT as a parameter:

```bash { output_lines = "2-9" }
./endorse-rim.sh "Nfpl4Y32d2hCpeYsarnnGv9xcbTMTBX90x0ZjnAMjLk="
[+] Creating 4/4
 ✔ Container cca-trustee-setup-1  Created
 ✔ Container cca-trustee-rvps-1   Running
 ✔ Container cca-trustee-as-1     Running
 ✔ Container cca-trustee-kbs-1    Running
[+] Running 1/1
 ✔ Container cca-trustee-setup-1  Exited
Reference Values Updated
```

## Re-run attestation and request a secret

In the realm terminal re-run the attestation command:
```bash
./kbs-client --url http://kbs:8080 attest --tee-key-file realm.key >ear.jwt
```

Verify that the new EAR now contains `affirming` status:

```bash { output_lines = "2" }
./arc verify ear.jwt |grep "ear.status"
            "ear.status": "affirming",
```

and `affirming` result for the `Executables` trustworthiness vector:
```bash { output_lines = "2-11" }
./arc verify ear.jwt |grep -A10 "trustworthiness vectors"
[trustworthiness vectors]
submod(cpu0):
Instance Identity [none]: no claim being made
Configuration [none]: no claim being made
Executables [affirming]: recognized and approved boot-time
File System [none]: no claim being made
Hardware [affirming]: genuine
Runtime Opaque [none]: no claim being made
Storage Opaque [none]: no claim being made
Sourced Data [none]: no claim being made
```

Request a secret demo message using the new attestation result:
```bash { output_lines = "4" }
./kbs-client --url http://kbs:8080 get-resource \
  --tee-key-file realm.key --attestation-token ear.jwt \
  --path "cca-trustee/demo-message/message.txt" |base64 -d
This is a CCA demo message obtained by using a valid EAR token
```

You have successfully run an end-to-end attestation flow with Arm CCA and obtained a secret.

You can stop all Trustee containers with:
```bash
docker compose down
```
