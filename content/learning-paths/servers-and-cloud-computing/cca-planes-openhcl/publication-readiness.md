---
# User change
title: "Prepare the Learning Path for publication"

weight: 6

# Do not modify these elements
layout: "learningpathall"
---

## Publication readiness

This Learning Path is a draft. Complete the following tasks before publication:

- Publish `https://github.com/EllieRoe/CCA-dev-platform.git` with unauthenticated HTTPS clone access, or replace the source-build steps with a public prebuilt Docker image.
- Push the CCA-dev-platform `planes` branch through commit
  `edfca45414f8ea0a90f08ff9d9cee99b85c8e3e0`, or an equivalent commit that
  provides `config/cca-planes-lp.yaml` and `config/planes.yaml`, including the
  MEC FVP run parameters required by `ENABLE_FEAT_MEC=1` and
  `RMM_V1_COMPAT=1` for the pinned TF-RMM revision.
- Run `shrinkwrap build ... --dry-run` with the published overlay and fix any Shrinkwrap macro escaping issues.
- Run a real Shrinkwrap build through the `kvmtool` phase and confirm that `config/lkvm.patch` is not applied to the planes-enabled branch.
- Publish or identify the public OpenHCL Linux branch used for the plane 0 kernel. The current prototype uses the internal `openhcl-linux` `planes` branch.
- Publish or identify the public OpenVMM/OpenHCL branch used for `simple_tmk` and `tmk_vmm`. The current prototype uses the internal `openhcl` `cca-support` branch.
- Confirm that the OpenVMM/OpenHCL branch is reachable from a clean host. The public upstream OpenVMM repository does not currently expose an obvious CCA planes branch for this draft.
- Replace internal prototype repository URLs and branch names with public URLs.
- Replace the captured internal `tmk_vmm` output with the final public demo
  output, or remove the post-test CCA register-read panic from the prototype.
- Test the full flow on a clean Ubuntu 24.04 LTS host.
- Remove `draft: true` from `_index.md` after the content is runnable from public inputs.

## Tested state

Testing on 29 June 2026 used Ubuntu 24.04.4 LTS and the `planes` branch of `CCA-dev-platform`.

The HTTPS clone command prompted for GitHub credentials:

```console
git clone --branch planes https://github.com/EllieRoe/CCA-dev-platform.git CCA-dev-platform
```

SSH access to the same repository initially reached commit `a7c5ec548bbf148ace0bea889cba92ef33c33f76` on the `planes` branch.

The required planes overlays were absent at that commit. CCA-dev-platform commit
`401dfd13882e994df38fa741266b14ccda2d407c` adds the overlays, commit
`70c5e946294e81da8fbe4d9a4bc079526e31925e` adds the MEC FVP run parameters
required to boot the TF-A build, and commit
`edfca45414f8ea0a90f08ff9d9cee99b85c8e3e0` enables `RMM_V1_COMPAT=1` for the
pinned TF-RMM revision:

```console
test -f config/cca-planes-lp.yaml
test -f config/planes.yaml
```

With those overlays available, the documented Shrinkwrap dry run generated a build script:

```console
shrinkwrap build cca-3world.yaml --overlay cca-planes-lp.yaml --overlay planes.yaml \
    --btvar GUEST_ROOTFS='${artifact:BUILDROOT}' --dry-run
```

The generated script selected `linux-cca` branch `cca/planes/rfc-v1`, `kvmtool-cca` branch `cca/planes/rfc-v1`, TF-RMM commit `9a98e8fcb1645b9917b2abd79212e6e3062e09fd`, and TF-A
parameter `GIC_ENABLE_V4_EXTN=1`. The generated script did not contain `config/lkvm.patch`.

The full Shrinkwrap build completed successfully with the generated overlays:

```console
shrinkwrap build cca-3world.yaml --overlay cca-planes-lp.yaml --overlay planes.yaml \
    --btvar GUEST_ROOTFS='${artifact:BUILDROOT}'
```

The build completed the `buildroot` and `guest-disk` artifact stages.

The internal OpenHCL Linux source resolved branch `planes` to commit `b407f1ab33b2092f054cf3d5087ee6933a80d5f4`. The plane 0 kernel build completed and produced
`arch/arm64/boot/Image`.

The internal OpenVMM/OpenHCL source resolved branch `cca-support` to commit `e09ae82bb0b9ea55ec52c490e000539088dad8ab`. The `simple_tmk` and `tmk_vmm` builds completed with Rust 1.85.0,
`rust-src`, `aarch64-unknown-linux-gnu`, and `aarch64-unknown-none`.

The root filesystem resize completed from 256 MiB to 1 GiB. The copy step completed with `debugfs`, and `e2fsck -fn rootfs.ext2` passed after copying the plane 0 files into `/cca`. The `tp-desktop`
test host did not have passwordless `sudo`, so the Learning Path uses `debugfs` instead of mounting the root filesystem image.

The FVP boot test used FVP `FVP_Base_RevC_AEMvA_11.31_28` from the existing `armlimited/cca-learning-path:cca-simulation-kitten-1-x86_64` Docker image because the model was not installed in the
`tp-desktop` host `PATH`. The first boot attempt failed in BL31 with `feat_mec not supported by the PE`. After adding the MEC FVP run parameters to `cca-planes-lp.yaml` and running
`shrinkwrap run` with both overlays, the FVP reached the Linux login prompt.

The first Realm start attempt failed before the Realm launched because BL31
logged `RMM init failed: -2`, and the host kernel did not report an RMI ABI.
After enabling `RMM_V1_COMPAT=1`, the host kernel reported
`RMI ABI version 1.1` and kvmtool started the Realm.

The Realm command was tested with `--disk /cca/guest-disk.img`. Without the
disk, plane 0 Linux mounted the 9P share as the root filesystem and panicked
while running `/virt/init`. With the disk argument present, plane 0 Linux
detected `vda1` and `vda2`, mounted `/dev/vda2` as ext4, ran `/sbin/init`, and
reached the login prompt.

Plane 0 login as `root` was tested. The documented 9P mount command mounted
`cca_mount` on `/root/mount`, the hugetlbfs command mounted `none` on
`/root/huge` with `pagesize=32M`, and `simple_tmk` and `tmk_vmm` were visible
through the 9P mount.

The `tmk_vmm` command was tested from `/root/mount` with the CCA backend and
`simple_tmk`. The log showed the plane 1 memory permission setup, multiple
`rsi_plane_enter` calls, `tmk: hello world`, and `tmk_vmm::run: test complete`.
The shell reported exit code 0. The internal `cca-support` branch also emitted
a post-test Rust panic from `openhcl/virt_mshv_vtl/src/processor/cca/mod.rs`
line 386, where the CCA `registers()` accessor is still implemented as
`todo!()`.

## Optional Docker flow

If the final demo is packaged as a Docker image, replace the build page with a shorter setup flow:

```console
docker pull armswdev/cca-learning-path:cca-planes-openhcl-<version>
docker run --rm -it armswdev/cca-learning-path:cca-planes-openhcl-<version>
```

The image should contain:

- A planes-enabled FVP launch script.
- A planes-enabled CCA host root filesystem.
- `Image_ohcl` for plane 0 Linux.
- `simple_tmk` and `tmk_vmm`.
- Any helper scripts needed to mount 9P and hugetlbfs in plane 0.

## Source handling

Use public sources in the final Learning Path. Do not copy private links, private branch names, or restricted diagrams into the public Learning Paths repository.
