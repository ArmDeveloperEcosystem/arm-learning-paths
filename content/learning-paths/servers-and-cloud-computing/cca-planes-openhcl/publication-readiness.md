---
# User change
title: "Prepare the Learning Path for publication"

weight: 6

# Do not modify these elements
layout: "learningpathall"
---

## Publication readiness

This Learning Path is a draft. Complete the following tasks before publication:

- Publish a planes-enabled `CCA-dev-platform` workflow or replace the source-build steps with a public prebuilt Docker image.
- Publish `cca-planes-lp.yaml` or update the CCA development platform so the `config/lkvm.patch` prebuild step from `kvmtool.yaml` is skipped for the planes-enabled `kvmtool` branch.
- Publish the `planes.yaml` Shrinkwrap overlay used by the demo.
- Run `shrinkwrap build ... --dry-run` with the published overlay and fix any Shrinkwrap macro escaping issues.
- Run a real Shrinkwrap build through the `kvmtool` phase and confirm that `config/lkvm.patch` is not applied to the planes-enabled branch.
- Publish or identify the public OpenHCL Linux branch used for the plane 0 kernel.
- Publish or identify the public OpenVMM/OpenHCL branch used for `simple_tmk` and `tmk_vmm`.
- Confirm that the OpenVMM/OpenHCL branch is reachable from a clean host. The public upstream OpenVMM repository does not currently expose an obvious CCA planes branch for this draft.
- Replace placeholder repository URLs and branch names with public URLs.
- Capture and add the exact successful `tmk_vmm` output.
- Test the full flow on a clean Ubuntu 24.04 LTS host.
- Remove `draft: true` from `_index.md` after the content is runnable from public inputs.

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
