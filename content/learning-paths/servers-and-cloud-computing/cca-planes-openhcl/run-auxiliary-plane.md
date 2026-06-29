---
# User change
title: "Run the auxiliary plane test"

weight: 5

# Do not modify these elements
layout: "learningpathall"
---

## Start the test microkernel

Run `tmk_vmm` from plane 0:

```console
cd /root/mount
export RUST_BACKTRACE=1
./tmk_vmm --hv cca --tmk ./simple_tmk
```

The VMM prepares memory for the auxiliary plane, asks the plane 0 kernel to set the required permissions, and enters the test microkernel.

The output is similar to:

```output
mshv_rsi_set_mem_perm: plane=1, base_addr=0x9a000000, top_addr=0x9c000000
rsi_plane_enter: plane=1
INFO tmk: hello world
rsi_plane_enter: plane=1
INFO tmk_vmm::run: test complete
```

## Validate the result

Confirm these conditions before treating the run as successful:

- The OpenHCL CCA backend selects the `cca` hypervisor path.
- The test microkernel reaches its success path.
- `tmk_vmm` prints `test complete`.
- Control returns to plane 0 after the auxiliary plane exits.

{{% notice Note %}}
The internal WIP branch tested for this draft printed `test complete` and
returned exit code 0, then an unnamed thread emitted a Rust panic from an
unimplemented CCA register-read path. Replace this note with the final expected
output before publication.
{{% /notice %}}

If the command fails before entering the auxiliary plane, check that `/root/huge` is mounted with 32 MB pages and that the `hugepagesz=32M hugepages=1` kernel parameters were passed to plane 0 Linux.

If the command reports that CCA support is unavailable, check that the stack was built with planes-enabled RMM, host kernel, and `kvmtool` components.

## Shut down

Shut down plane 0 Linux:

```console
poweroff
```

When you return to the CCA host prompt, shut down the host:

```console
poweroff
```

## What you've accomplished

You have run the test VMM in plane 0 and used it to start a test microkernel in an auxiliary plane.
