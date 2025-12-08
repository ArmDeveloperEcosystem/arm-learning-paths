---
# User change
title: "Use memory encryption"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Before you begin

Download the [`armswdev/cca-learning-path:cca-simulation-v3`](https://hub.docker.com/r/armswdev/cca-learning-path:cca-simulation-v3) docker container.

## About Memory Encryption Context (MEC)

Memory Encryption Contexts (MEC) are configurations of encryption that are associated with areas of memory, assigned by the MMU.

MEC is an extension to the Arm Realm Management Extension (RME). The RME system architecture requires that the Realm, Secure, and Root PASes are encrypted. The encryption key or tweak, or encryption context, used with each of these PASes is global within that PAS. So, for example, for the Realm PAS, all Realm memory uses the same encryption context.

With MEC this concept is broadened, and for the Realm PAS specifically, this allow each Realm to have a unique encryption context. This provides additional defense in depth to the isolation already provided in RME. Realms and RMM itself can all have separate encryption. MECIDs are identifying tags that are associated with different Memory Encryption Contexts. MECIDs are assigned to different software entities in the system, for example, Realms or the RMM.

## RMM without FEAT_MEC

When the FVP starts, it can be configured to advertize that it has MEC support by setting `FEAT_MEC` in the system configuration registers. The CCA software stack will detect that MEC is available, and as configured in the CCA stack built for the `armswdev/cca-learning-path:cca-simulation-v3` will make use of it.

First, fire up a container:

```console
docker run --rm -it armswdev/cca-learning-path:cca-simulation-v3
```

Then start a CCA host in the FVP (without MEC):

```console
./run-cca-fvp.sh
```

This boots the 3 worlds. Switch to the second screen of `screen` by pressing `ctrl+a 2`, which corresponds to the output console of the RMM. It should look like:

```output
Trying ::1...
Connection failed: Connection refused
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
RMM_MEM_SCRUB_METHOD 2 is selected.
RMM_MEM_SCRUB_METHOD=2 is set but FEAT_MEC is not present.
Booting RMM v.0.8.0(release) tf-rmm-v0.8.0 Built: Dec  4 2025 13:47:33 with GCC 14.3.1
RMM-EL3 Interface v.0.6
Boot Manifest Interface v.0.5
RMI ABI revision v1.1
RSI ABI revision v1.1
RMM_MEM_SCRUB_METHOD 2 is selected.
RMM_MEM_SCRUB_METHOD=2 is set but FEAT_MEC is not present.
RMM_MEM_SCRUB_METHOD 2 is selected.
RMM_MEM_SCRUB_METHOD=2 is set but FEAT_MEC is not present.
RMM_MEM_SCRUB_METHOD 2 is selected.
RMM_MEM_SCRUB_METHOD=2 is set but FEAT_MEC is not present.
RMM_MEM_SCRUB_METHOD 2 is selected.
RMM_MEM_SCRUB_METHOD=2 is set but FEAT_MEC is not present.
RMM_MEM_SCRUB_METHOD 2 is selected.
RMM_MEM_SCRUB_METHOD=2 is set but FEAT_MEC is not present.
RMM_MEM_SCRUB_METHOD 2 is selected.
RMM_MEM_SCRUB_METHOD=2 is set but FEAT_MEC is not present.
RMM_MEM_SCRUB_METHOD 2 is selected.
RMM_MEM_SCRUB_METHOD=2 is set but FEAT_MEC is not present.
SMC_RMI_VERSION                   10000 > RMI_SUCCESS 10000 10001
```

Note how the RMM has detected `FEAT_MEC`is not available --- and complains about it.

You can now bring down the FVP simulation. Switch back to the main `screen` console with `ctrl+a 1`, log in as `root` (no password) and `poweroff` to exit.

## RMM with FEAT_MEC enabled

Now, start the CCA host in the FVP with `FEAT_MEC` enabled:

```console
./run-cca-fvp.sh --enable-mec
```

This boots the 3 worlds again. Switch to the RMM output console (second screen of `screen` with `ctrl+a 2`). It should look like:

```output
Trying ::1...
Connection failed: Connection refused
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
RMM_MEM_SCRUB_METHOD 2 is selected.
Booting RMM v.0.8.0(release) tf-rmm-v0.8.0 Built: Dec  4 2025 13:47:33 with GCC 14.3.1
RMM-EL3 Interface v.0.6
Boot Manifest Interface v.0.5
RMI ABI revision v1.1
RSI ABI revision v1.1
RMM_MEM_SCRUB_METHOD 2 is selected.
RMM_MEM_SCRUB_METHOD 2 is selected.
RMM_MEM_SCRUB_METHOD 2 is selected.
RMM_MEM_SCRUB_METHOD 2 is selected.
RMM_MEM_SCRUB_METHOD 2 is selected.
RMM_MEM_SCRUB_METHOD 2 is selected.
RMM_MEM_SCRUB_METHOD 2 is selected.
SMC_RMI_VERSION                   10000 > RMI_SUCCESS 10000 10001
```

With `FEAT_MEC` enabled, the RMM detects it and no longer complain about it missing. The RMM will now use different memory encryption contexts for each of the realms that you would start with the `lkvm` command from the previous pages.

You can now bring down the FVP simulation. Switch back to the main `screen` console with `ctrl+a 1`, log in as `root` (no password) and `poweroff` to exit. You can also exit the docker container with `exit`.
