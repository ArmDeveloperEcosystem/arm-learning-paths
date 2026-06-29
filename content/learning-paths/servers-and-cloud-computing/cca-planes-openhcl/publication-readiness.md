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
- Push CCA-dev-platform commit `401dfd13882e994df38fa741266b14ccda2d407c` or an equivalent commit that provides `config/cca-planes-lp.yaml` and `config/planes.yaml` on the `planes` branch.
- Run `shrinkwrap build ... --dry-run` with the published overlay and fix any Shrinkwrap macro escaping issues.
- Run a real Shrinkwrap build through the `kvmtool` phase and confirm that `config/lkvm.patch` is not applied to the planes-enabled branch.
- Publish or identify the public OpenHCL Linux branch used for the plane 0 kernel. The current prototype uses the internal `openhcl-linux` `planes` branch.
- Publish or identify the public OpenVMM/OpenHCL branch used for `simple_tmk` and `tmk_vmm`. The current prototype uses the internal `openhcl` `cca-support` branch.
- Confirm that the OpenVMM/OpenHCL branch is reachable from a clean host. The public upstream OpenVMM repository does not currently expose an obvious CCA planes branch for this draft.
- Replace internal prototype repository URLs and branch names with public URLs.
- Capture and add the exact successful `tmk_vmm` output.
- Test the full flow on a clean Ubuntu 24.04 LTS host.
- Remove `draft: true` from `_index.md` after the content is runnable from public inputs.

## Tested state

Testing on 29 June 2026 used Ubuntu 24.04.4 LTS and the `planes` branch of `CCA-dev-platform`.

The HTTPS clone command prompted for GitHub credentials:

```console
git clone --branch planes https://github.com/EllieRoe/CCA-dev-platform.git CCA-dev-platform
```

SSH access to the same repository initially reached commit `a7c5ec548bbf148ace0bea889cba92ef33c33f76` on the `planes` branch.

The required planes overlays were absent at that commit. CCA-dev-platform commit `401dfd13882e994df38fa741266b14ccda2d407c` adds the overlays:

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

The internal OpenHCL Linux source resolved branch `planes` to commit `b407f1ab33b2092f054cf3d5087ee6933a80d5f4`. The internal OpenVMM/OpenHCL source resolved branch `cca-support` to
commit `e09ae82bb0b9ea55ec52c490e000539088dad8ab`.

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
