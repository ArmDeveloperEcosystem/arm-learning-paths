---
# User change
title: Run confidentail containers with encrypted images using Arm CCA and Trustee

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Overview
In this section you will

- run the **Trustee services** (AS, KBS, RVPS) and a local docker image registry.
- publish an encrypted docker image.
- on **Arm FVP** you will start a confidential container using the encrypted image and confirm that it runs in a **CCA realm**.

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

Clone the **kata** branch of the **cca-trustee** repository:
``` bash
git clone -b kata https://github.com/ArmDeveloperEcosystem/cca-trustee.git
```

This repository contains configuration to run Trustee services (KBS, AS, RVPS, keyprovider) with CCA attestation support as a simple cluster. The configuration is based on the recommended settings from [KBS Cluster](https://github.com/confidential-containers/trustee/blob/main/kbs/docs/cluster.md).

Additional Learning Path–specific changes include:

- External Linaro CCA verifier in the AS configuration

- Attestation policy with CCA rules

- An **affirming** resource policy

- Docker registry service

- A shared Docker network for all containers in this demo

Go into the **cca-trustee** directory and generate a self-signed certificate for the docker registry service:
``` bash
cd cca-trustee

openssl req -x509 -days 365 -config config/registry.cnf -keyout config/registry.key -out config/registry.crt
```

Start the Trustee services Docker containers (as detached services):
``` bash { output_lines = "2-9" }
docker compose up -d
 ✔ Network cca-trustee                                                                         Created
 ✔ Container cca-trustee-rvps-1                                                                Created
 ✔ Container cca-trustee-setup-1                                                               Exited
 ✔ Container cca-trustee-registry-1                                                            Created
 ✔ Container cca-trustee-as-1                                                                  Created
 ✔ Container cca-trustee-kbs-1                                                                 Created
 ✔ Container cca-trustee-keyprovider-1                                                         Created
 ✔ Container cca-trustee-kbs-client-1                                                          Created
```

While running the demo you can also check logs of the Trustee services in this terminal:
``` bash
docker compose logs <service>
```
Where **service** is either **as**, **kbs** or **rvps**.

## Publish an encrypted docker image

Generate an image encryption key:
``` bash
head -c 32 /dev/urandom | openssl enc >image.key
```

Publish the encryption key as a KBS secret resourse. This resource can be obtained only with an attestation token with **affirming** status.

Learn more about how the attestation result is used to evaluate the trustworthiness of a CCA realm and how attestation policy gates secrets release in
["Run an end-to-end Attestation with Arm CCA and Trustee"](/learning-paths/servers-and-cloud-computing/cca-trustee)
``` bash
./publish-key.sh
```

Encrypt a **busybox** docker image with the published key and push it into the local docker registry with **busybox_encrypted** name:
``` bash { output_lines = "2-9" }
./encrypt_image.sh
Encrypting docker://busybox image with busybox_encrypted name
Getting image source signatures
Copying blob 5bc51b87d4ec done   |
Copying config eade5be814 done   |
Writing manifest to image destination

Inspecting MIMEType of docker://registry:5000/busybox_encrypted image
            "MIMEType": "application/vnd.oci.image.layer.v1.tar+gzip+encrypted",
```
By inspecting MIMEType of the published image you can see that it is encrypted.

{{% notice Encryption key note %}}
Annotations data for an encrypted image contains a path to the key which Confidential Containers workload needs to obtain to decrypt the image.

You can check it with this command
``` bash { output_lines = "4" }
docker compose exec keyprovider skopeo inspect docker://registry:5000/busybox_encrypted \
 | jq -r '.LayersData[0].Annotations."org.opencontainers.image.enc.keys.provider.attestation-agent"' \
 |base64 -d | jq .kid
"kbs:///cca-trustee/demo-key/encrypt.key"
```
{{% /notice %}}

{{% notice Docker image note %}}
**encrypt_image.sh** uses [skopeo](https://github.com/containers/skopeo) in the Trustee **keyprovider** container to pull, encrypt and push docker images.
Without parameters it encrypts **busybox** docker image which will be used in this Learning Path.
You can use this script to encrypt other docker images as well. For example with this command it will encrypt
**alpine** docker image and push it into the local docker registry with **alpine_encrypted** name.

``` bash
./encrypt_image.sh alpine
```
{{% /notice %}}

You have prepared infrastructure and ready to start Confidential Containers in CCA realm.

## Launch an FVP

With the Trustee Services running in one terminal, open up a new terminal in which you will run Confidential Containers.

Pull the Docker image with the pre-built FVP, and then run the container connected to the same Docker network:

```bash
docker pull armswdev/cca-learning-path:cca-simulation-with-kata-v3
```
```bash
docker run --rm -it --network cca-trustee armswdev/cca-learning-path:cca-simulation-with-kata-v3
```

Within your running container, launch the **run-cca-fvp.sh** script to run the Arm CCA pre-built binaries on the FVP:

```bash
./run-cca-fvp.sh
```

The **run-cca-fvp.sh** script uses the **screen** command to connect to the different UARTs in the FVP.

When the host Linux boots, уnter root as the username:
```output

Welcome to the CCA host
host login: root
(host) #
```

## Inject the local docker registry self-signed certificate

The local docker registry service was deployed with a self-signed certificate.
To trust this certicate it needs to be added into the CA certificates list in the guest VM image.

Inject the local docker repository certificate into the image:
``` bash { output_lines = "2-6" }
inject_registry_cert.sh

### Injecting the ceritficate into guest file system image
[ 2250.576395] loop0: detected capacity change from 0 to 518144
[ 2250.588006] EXT4-fs (loop0): mounted filesystem ae947b26-4cdd-4e7c-8018-52b3e1594c9e r/w with ordered data mode. Quota mode: none.
[ 2250.862743] EXT4-fs (loop0): unmounting filesystem ae947b26-4cdd-4e7c-8018-52b3e1594c9e.
```

## Calculate Realm Initial Measurement (RIM)

For a successful attestation of your CCA realm you need to provide the Trustee Reference Values Provider Service (RVPS) with a known good reference value.

In a production environment, the known good reference value is generated using a deployment-specific process.
This Learning Path includes **rim_calc.sh** script which:
- Runs qemu-system-aarch64-cca-experimental (used by Kata containers to run a guest VM in Arm CCA realm) to dump Device Tree into a file.
- Checks Kata shim configuration file for guest VM delpoyment parameters.
- Uses ["cca-realm-measurements"](https://github.com/veraison/cca-realm-measurements) to calculate the realm initial measurement (RIM).

Run the script:
``` bash { output_lines = "2-8" }
(host) # rim_calc.sh
Running /opt/kata/bin/qemu-system-aarch64-cca-experimental with dumpdtb=/tmp/kata-qemu.dtb parameter
Running /usr/bin/realm-measurements
RIM: rBD3xqcqqYHrjZ1Tu9aMWqFmwBgwT+NvLxg9jsozZm9rMDhjcaEM5LOQ+qJs+SLdG1jyco33EDuJ8+1/oMdFIQ==
REM0: KSzpB3Vo+rW1bSAJtAbxhN+dvTv6e6SqSwQSKqXFR8vX1mYHlKDA7SJBiHUBx/4UgZ/PLMmrxHrIuGzHaUi6aQ==
REM1: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==
REM2: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==
REM3: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==
```
Realm Extensible Measurements (REMs) are not used for attesation in this Learning Path and can be ignored.


## Endorse Realm Initial Measurement (RIM)

In the terminal where you started Trustee services, run **endorse-rim.sh** script with the RIM as a parameter:

```bash { output_lines = "2-3" }
./endorse-rim.sh "rBD3xqcqqYHrjZ1Tu9aMWqFmwBgwT+NvLxg9jsozZm9rMDhjcaEM5LOQ+qJs+SLdG1jyco33EDuJ8+1/oMdFIQ=="

Reference Values Updated
```

## Launch a Confidentail container in CCA realm

Reduce amount of kernel messages printed to console:
``` bash
dmesg -n 4
```

Run a confidential container from the **busybox_encrypted** image and check its kernel version and RME kernel messages.
Because the container is run in CCA realm on emulated environment (Fixed Virtual Platform (FVP)), it will take some time to launch, be patient.
Depending on the machine you run this Learning Path on it might take between 8 and 15 minutes to run a container.

``` bash { output_lines = "5-9" }
nerdctl --snapshotter nydus run --runtime io.containerd.kata.v2 \
  --annotation io.kubernetes.cri.image-name=registry:5000/busybox_encrypted \
  --rm -it registry:5000/busybox_encrypted \
  sh -c 'echo; echo "Kernel version:"; uname -a; echo "RME kernel message:"; dmesg | grep RME; echo'

Kernel version:
Linux 4ce958e5e51f 6.15.0-rc1+ #1 SMP Thu Dec  4 12:55:41 UTC 2025 aarch64 GNU/Linux
RME kernel message:
[    0.000000] RME: Using RSI version 1.0
```

Verify that the FVP kernel version is different to the Confidential Container version:
``` bash { output_lines = "2" }
uname -a
Linux host 6.15.0-rc1-g916aeec68dd4 #1 SMP PREEMPT @1764597323 aarch64 GNU/Linux
```

{{% notice Nydus snapshotter messages note %}}
When you run a confidential container you will see messages from Nydus snapshotter when it loads container snapshot.
```
registry:5000/busybox_encrypted:latest: resolving      |--------------------------------------|
elapsed: 0.1 s                          total:   0.0 B (0.0 B/s)
registry:5000/busybox_encrypted:latest: resolving      |--------------------------------------|
elapsed: 0.2 s                          total:   0.0 B (0.0 B/s)
registry:5000/busybox_encrypted:latest:                                           resolving      |--------------------------------------|
manifest-sha256:8b72055942ded7b1f7f31959ab8ccbee4fbc6355423580275593e5ffeb578f33: waiting        |--------------------------------------|
elapsed: 1.1 s                                                                    total:   0.0 B (0.0 B/s)
registry:5000/busybox_encrypted:latest:                                           resolved       |++++++++++++++++++++++++++++++++++++++|
manifest-sha256:8b72055942ded7b1f7f31959ab8ccbee4fbc6355423580275593e5ffeb578f33: downloading    |--------------------------------------|    0.0 B/1.3 KiB
elapsed: 1.2 s                                                                    total:   0.0 B (0.0 B/s)
```
These messages can be ignored. The docker image will be downloaded by **image-rs** in the guest VM as described previously.
{{% /notice %}}

{{% notice Failed attestation note %}}
If you forget to endorse RIM for your environment or make a mistake doing that, then CCA realm attesation would fail.
In this case you will see an image decryption error when starting a confidential container with an encrypted image.
```
FATA[0189] failed to create shim task: rpc status: Status { code: INTERNAL, message: "[CDH] [ERROR]: Image Pull error: Failed to pull image registry:5000/busybox_encrypted from all mirror/mapping locations or original location: image: registry:5000/busybox_encrypted:latest, error: Errors happened when pulling image: Failed to decrypt layer: Failed to decrypt the image layer, please ensure that the decryption key is placed and correct", details: [], special_fields: SpecialFields { unknown_fields: UnknownFields { fields: None }, cached_size: CachedSize { size: 0 } } }
```

By checking KBS logs (in the termial where you run Trustee services)  you could see that the ecnryption key couldn't be obtained because of an AS policy:
``` bash { output_lines = "2-5" }
docker compose logs kbs

kbs-1  | [2025-12-08T12:25:39Z INFO  actix_web::middleware::logger] 172.18.0.7 "POST /kbs/v0/auth HTTP/1.1" 200 74 "-" "attestation-agent-kbs-client/0.1.0" 0.001568
kbs-1  | [2025-12-08T12:25:40Z INFO  actix_web::middleware::logger] 172.18.0.7 "POST /kbs/v0/attest HTTP/1.1" 200 2952 "-" "attestation-agent-kbs-client/0.1.0" 0.420476
kbs-1  | [2025-12-08T12:25:40Z ERROR kbs::error] PolicyDeny
```
{{% /notice %}}

You have successfully run a confidentail container with Arm CCA using an encrypted image.

{{% notice Unencrypted docker images note %}}
In this Learnig Path environment you can also run confidential containers in Arm CCA realm from any unencrypted docker images.
Please notice that you need to define the **annotation** parameter so **image-rs** knows where to pull the image from.
For example:
```
nerdctl run --runtime io.containerd.kata.v2 --rm -it --annotation io.kubernetes.cri.image-name=alpine:latest alpine sh
```
{{% /notice %}}

You can stop all Trustee containers with:
```bash
docker compose down
```
