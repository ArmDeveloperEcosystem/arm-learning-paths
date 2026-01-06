---
# User change
title: Run confidential containers with encrypted images using Arm CCA and Trustee

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Overview
In this section you will:

   * Start the Trustee services (AS, KBS, RVPS) along with a local Docker registry.
   * Publish an encrypted container image to the local registry.
   * Launch a Confidential Container on the Arm FVP using the encrypted image and verify it runs inside an Arm CCA Realm.

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

Add your user name to the Docker group (open a new shell afterwards so the change takes effect):
``` bash
sudo usermod -aG docker $USER
newgrp docker
```

## Start Trustee services containers

Clone the **kata** branch of the **cca-trustee** repository:
``` bash
git clone -b kata https://github.com/ArmDeveloperEcosystem/cca-trustee.git
```

This repository includes a Docker Compose configuration that starts Trustee services (KBS, AS, RVPS, and a key provider) with Arm CCA attestation support as a simple local cluster. The configuration follows the recommended approach described in the Trustee documentation for running a [KBS Cluster](https://github.com/confidential-containers/trustee/blob/main/kbs/docs/cluster.md).

This Learning Path also applies a few environment-specific changes, including:

- An external Linaro CCA verifier configured in the Attestation Service (AS)

- An attestation policy containing CCA rules

- An affirming resource policy

- A local Docker registry service

- A shared Docker network used by all services in this demo

Change into the cca-trustee directory and generate a self-signed certificate for the local docker registry:
``` bash
cd cca-trustee

openssl req -x509 -days 365 -config config/registry.cnf -keyout config/registry.key -out config/registry.crt
```

Start the Trustee services as detached containers:
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

To view logs while running the demo:
``` bash
docker compose logs <service>
```
Where <service> is one of as, kbs or rvps.

## Publish an encrypted container image

Generate a 32-byte image encryption key:
``` bash
head -c 32 /dev/urandom | openssl enc >image.key
```
Learn more about how the attestation result is used to evaluate the trustworthiness of a CCA realm and how attestation policy gates secrets release in the ["Run an end-to-end Attestation with Arm CCA and Trustee"](/learning-paths/servers-and-cloud-computing/cca-trustee) Learning Path.

Publish the encryption key as a KBS secret resource. This resource is only released when the requester presents an attestation token with affirming status.
``` bash
./publish-key.sh
```

Encrypt the **busybox** image using the published key, then push it to the local registry as **busybox_encrypted**:
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
The published image layers use an encrypted OCI layer media type, confirming that the image has been encrypted.

{{% notice Encryption key note %}}
Encrypted images include annotations that describe where the guest should retrieve the key required for decryption.

You can inspect the key identifier (kid) with:
``` bash { output_lines = "4" }
docker compose exec keyprovider skopeo inspect docker://registry:5000/busybox_encrypted \
 | jq -r '.LayersData[0].Annotations."org.opencontainers.image.enc.keys.provider.attestation-agent"' \
 |base64 -d | jq .kid
"kbs:///cca-trustee/demo-key/encrypt.key"
```
{{% /notice %}}

{{% notice Docker image note %}}
**encrypt_image.sh** uses [skopeo](https://github.com/containers/skopeo) inside the Trustee keyprovider container to pull, encrypt, and push images.
By default it encrypts busybox, which is used throughout this Learning Path. You can also encrypt other images. For example, this command encrypts **alpine** and pushes it as **alpine_encrypted**:

``` bash
./encrypt_image.sh alpine
```
{{% /notice %}}

At this point, the host-side infrastructure is running and the encrypted image is available from the local registry.

## Launch an FVP

With the Trustee services running in one terminal, open a second terminal for the Confidential Containers environment.

Pull the pre-built FVP container image and run it on the same Docker network:

```bash
docker pull armswdev/cca-learning-path:cca-simulation-with-kata-v3
```
```bash
docker run --rm -it --network cca-trustee armswdev/cca-learning-path:cca-simulation-with-kata-v3
```

Inside your running container, launch the `run-cca-fvp.sh` script to run the Arm CCA pre-built binaries on the FVP:

```bash
./run-cca-fvp.sh
```

The `run-cca-fvp.sh` script uses the `screen` command to connect to the different UARTs in the FVP.

When the host Linux boots, enter root as the username:
```output

Welcome to the CCA host
host login: root
(host) #
```

## Inject the local Docker registry certificate

The local registry is configured with a self-signed TLS certificate. To allow the guest VM to trust the registry, add this certificate to the guest image’s CA certificate store.

Inject the registry certificate into the guest filesystem image:
``` bash { output_lines = "2-6" }
inject_registry_cert.sh

### Injecting the certificate into guest file system image
[ 2250.576395] loop0: detected capacity change from 0 to 518144
[ 2250.588006] EXT4-fs (loop0): mounted filesystem ae947b26-4cdd-4e7c-8018-52b3e1594c9e r/w with ordered data mode. Quota mode: none.
[ 2250.862743] EXT4-fs (loop0): unmounting filesystem ae947b26-4cdd-4e7c-8018-52b3e1594c9e.
```

## Calculate Realm Initial Measurement (RIM)

To validate the guest during attestation, the Trustee Reference Values Provider Service (RVPS) must be configured with a known-good reference value for the Realm.

In production, reference values are generated as part of a deployment-specific build and release process. This Learning Path includes a helper script, `rim_calc.sh`, which:
- Runs qemu-system-aarch64-cca-experimental (used by Kata containers to launch a guest VM inside an Arm CCA realm) to dump the guest Device Tree into a file.
- Reads the Kata shim configuration to capture guest deployment parameters
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
Realm Extensible Measurements (REMs) are not used for attestation in this Learning Path and can be ignored.


## Endorse Realm Initial Measurement (RIM)

In the terminal where you started Trustee services, run `endorse-rim.sh` and pass the RIM value:

```bash { output_lines = "2-3" }
./endorse-rim.sh "rBD3xqcqqYHrjZ1Tu9aMWqFmwBgwT+NvLxg9jsozZm9rMDhjcaEM5LOQ+qJs+SLdG1jyco33EDuJ8+1/oMdFIQ=="

Reference Values Updated
```

## Launch a Confidential Container in an Arm CCA realm

Reduce the verbosity of kernel messages printed to the console:
``` bash
dmesg -n 4
```

Run a Confidential Container from the **busybox_encrypted** image and verify both the kernel version and Arm RME-related kernel messages.
Because this runs on an emulated platform (Arm FVP), container startup can take several minutes depending on the host machine.

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

Verify that the host kernel version differs from the Confidential Container guest kernel:
``` bash { output_lines = "2" }
uname -a
Linux host 6.15.0-rc1-g916aeec68dd4 #1 SMP PREEMPT @1764597323 aarch64 GNU/Linux
```

{{% notice Nydus snapshotter messages note %}}
When launching a Confidential Container, you may see progress output from the Nydus snapshotter while it prepares the snapshot. For example:
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
If the RIM is not endorsed (or the wrong value is configured), attestation will fail and the guest will be unable to retrieve the decryption key. In this case, container startup fails with an image decryption error:
```
FATA[0189] failed to create shim task: rpc status: Status { code: INTERNAL, message: "[CDH] [ERROR]: Image Pull error: Failed to pull image registry:5000/busybox_encrypted from all mirror/mapping locations or original location: image: registry:5000/busybox_encrypted:latest, error: Errors happened when pulling image: Failed to decrypt layer: Failed to decrypt the image layer, please ensure that the decryption key is placed and correct", details: [], special_fields: SpecialFields { unknown_fields: UnknownFields { fields: None }, cached_size: CachedSize { size: 0 } } }
```

Checking the KBS logs (in the terminal running Trustee services) shows the request was denied by policy:
``` bash { output_lines = "2-5" }
docker compose logs kbs

kbs-1  | [2025-12-08T12:25:39Z INFO  actix_web::middleware::logger] 172.18.0.7 "POST /kbs/v0/auth HTTP/1.1" 200 74 "-" "attestation-agent-kbs-client/0.1.0" 0.001568
kbs-1  | [2025-12-08T12:25:40Z INFO  actix_web::middleware::logger] 172.18.0.7 "POST /kbs/v0/attest HTTP/1.1" 200 2952 "-" "attestation-agent-kbs-client/0.1.0" 0.420476
kbs-1  | [2025-12-08T12:25:40Z ERROR kbs::error] PolicyDeny
```
{{% /notice %}}

You have now successfully launched a Confidential Container in an Arm CCA Realm using an encrypted container image.

{{% notice Unencrypted docker images note %}}
In this Learning Path environment, you can also run Confidential Containers from unencrypted images. You still need to set the `io.kubernetes.cri.image-name` annotation so **image-rs** knows where to pull the image from. For example:
```
nerdctl run --runtime io.containerd.kata.v2 --rm -it --annotation io.kubernetes.cri.image-name=alpine:latest alpine sh
```
{{% /notice %}}

Stop all Trustee service containers with:
```bash
docker compose down
```
In this section, you brought up the Trustee services (AS, KBS, and RVPS) along with a local Docker registry, published an encrypted container image, and configured the environment so a guest running in an Arm CCA Realm could trust and pull from that registry. You then calculated and endorsed a Realm Initial Measurement (RIM), enabling successful attestation and allowing the guest to retrieve the decryption key from KBS. Finally, you launched a Confidential Container from the encrypted image and verified it was running inside a Realm by checking RME-related kernel messages.
