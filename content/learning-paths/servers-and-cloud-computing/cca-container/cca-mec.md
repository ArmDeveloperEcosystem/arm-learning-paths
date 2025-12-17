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

Memory Encryption Contexts (MEC) is an extension of the Arm Realm Management Extension (RME). MEC extends the existing support for memory encryption, allowing multiple encryption contexts in the Realm Physical Address Space. In an RME system with MEC, each access to a physical address is tagged with a Memory Encryption Context Identifier (MECID), which associates the access with a specific memory encryption context. The Arm Confidential Compute Architecture (CCA) requires that the Realm, Secure, and Root PASes are encrypted. Without MEC, the encryption context used within each PAS is global to that PAS. For example, all Realm memory would use the same encryption context.

With MEC, this model is extended. Non-secure, Secure, and Root PAS accesses use a default MECID value (0), while the Realm PAS supports multiple MECIDs. This allows each Realm to use a distinct memory encryption context, providing additional defense in depth beyond the isolation already provided by RME. The Realm Management Monitor (RMM) itself can also use a separate encryption context.


## Run the FVP without FEAT_MEC

When the FVP starts, it can advertise support for MEC by exposing the `FEAT_MEC` CPU feature. The CCA software stack detects whether `FEAT_MEC` is available and enables MEC support accordingly.

First, start the docker container:

```console
docker run --rm -it armswdev/cca-learning-path:cca-simulation-v3
```

Then start a CCA host in the FVP without enabling MEC:

```console
./run-cca-fvp.sh
```

This boots the 3 worlds. Switch to the second `screen` console by pressing `ctrl+a 2`, which corresponds to the RMM output console. The output on the console should look similar to:

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

The messages indicate that the RMM has detected that FEAT_MEC is not available.

You can now bring down the FVP simulation. Switch back to the main `screen` console with `ctrl+a 1`, log in as `root` (no password) and `poweroff` to exit.

## Run the FVP with FEAT_MEC enabled

Next, start the CCA host in the FVP with `FEAT_MEC` enabled:

```console
./run-cca-fvp.sh --enable-mec
```

This again boots the three worlds. Switch to the RMM output console (ctrl+a 2). It should look similar to:

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

With FEAT_MEC enabled, the RMM detects MEC support and no longer reports it as missing. The RMM will now make use of multiple memory encryption contexts, assigning distinct MECIDs to Realms that you create using the lkvm command in the previous sections of this learning path.

You can now shut down the FVP simulation. Switch back to the main screen console with ctrl+a 1, log in as root (no password), and run poweroff to exit. You can then exit the docker container with exit.

You have learned how to enable Memory Encryption Contexts (MEC) on the FVP and verified that the RMM detects and uses this capability.
