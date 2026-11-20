---
title: "NXP FRDM i.MX 8M Plus: Build the Yocto development image"
description: "Use the NXP manifest and board-specific kernel and runtime layer."
weight: 3
layout: "learningpathall"
---

## Prepare the Linux build host

Use Ubuntu 22.04 or 24.04 (or a compatible Ubuntu-based distribution) on
**x86_64/amd64 or arm64/aarch64**, with a native Linux filesystem. The Yocto build script
detects the CPU architecture, installs native apt dependencies and selects the
matching SDKMACHINE for the optional Linux SDK. BitBake selects its native build
tools; MACHINE continues to select the FRDM board. 

Lets get started by setting up the build scripts on our Ubuntu host:

```bash
mkdir -p "$HOME/nxp-imx8uplus-yocto-bundle"
unzip yocto-build.zip -d "$HOME/nxp-imx8uplus-yocto-bundle"
cd "$HOME/nxp-imx8uplus-yocto-bundle"
bash build-yocto.sh --help
```

Read NXP's EULA from the BSP before setting `ACCEPT_FSL_EULA=1`. Set that variable only if you accept the terms. It is required for NXP's firmware packages.

```bash
export ACCEPT_FSL_EULA=1
WORKDIR="$HOME/yocto-nxp-imx8uplus" JOBS=4   bash build-yocto.sh --install-deps --configure-only --no-sdk
```

The script selects machine `imx8mp-lpddr4-frdm` explicitly in its configuration block, uses the dedicated `build-frdm` directory, sources NXP's `imx-setup-release.sh`, and adds the supplied `meta-nxp-lp` layer and pinned `meta-aws`. It preserves configuration outside its own marked block. Existing `build/` configurations are left untouched; the same `WORKDIR` and downloaded sources can be reused. `LP_BUILD_DIR` can select another single directory name when needed.

NXP's first-time setup removes `imx95-19x19-verdin.conf` and `include/imx95-evk.inc` from `sources/meta-freescale`, because it supplies replacements in `meta-imx`. This happens for all three board builds. The script recognizes only these unstaged deletions at the pinned release, verifies that the replacements are unchanged, and preserves the removals if sync restores the files. Other edits, staged deletions, and untracked files still stop the build before sync. Keep `bsp-checkouts.py` beside `build-yocto.sh` when updating an extracted bundle.

Configure-only runs parsing and image dependency-graph generation. It does not compile yocto. Inspect the recorded manifest and graphs:

```bash
cat "$HOME/yocto-nxp-imx8uplus/meta-aws.lock"
ls "$HOME/yocto-nxp-imx8uplus/validation/image"
```

We are now ready to build yocto.

## Build the Yocto image and optional SDK

Initiate the build on the Ubuntu host. You can adjust the JOBS parameter to suit how many CPUs you have on your build host:

```bash
WORKDIR="$HOME/yocto-nxp-imx8uplus" JOBS=4   bash build-yocto.sh --no-sdk
ls -lh "$HOME/yocto-nxp-imx8uplus/build-frdm/tmp/deploy/images/imx8mp-lpddr4-frdm/"*.wic*
```

## Additional build script details: Included AWS Greengrass Lite runtime details

The image installs `packagegroup-nxp-lp-greengrass`, which requires
`greengrass-lite`, `libcgroup`, `sudo` and CA certificates. The pinned
`greengrass-lite_2.3.0.bb` recipe builds every core daemon, CLI, recipe runner
and token-exchange service; its library dependencies are resolved through the
recipe and package manager. No separate `ggtesd` recipe is required.

The learning-path append explicitly enables systemd unit installation. Before
compilation, `verify-greengrass.py` checks the selected recipe/version/source,
all core units and required build/runtime dependencies. The completed-image
hook then checks the actual rootfs: all 12 Greengrass executables, 19 core units,
version marker, support files and service/component accounts. It also checks
the deployed package manifest. Missing files fail the image build.

The build script publishes build reports in WORKDIR:

```text
validation/greengrass-config.json
validation/greengrass-image.json
```

The image audit is deployed beside the WIC as
`nxp-lp-dev-image-MACHINE.greengrass.json` and is tied to the package manifest's
SHA256. Keep these reports with the image. `--configure-only` checks metadata
and dependency graphs; its result does not prove that binaries were installed.
See `bundle/GREENGRASS-RUNTIME.md` for the audited component list.

## Additional build script details: Understanding the board integration

The kernel append uses NXP's `DELTA_KERNEL_DEFCONFIG` step, which runs after its recipe replaces `.config`. It checks remoteproc and RPMsg options after configuration. A board-specific patch updates the machine's original DTB, so the stock boot flow selects the modified board tree using the FRDM board DTB.

For M7 use, obtain the updated bundle whose reserved-memory node names are
`vdev0vring0@55000000`, `vdev0vring1@55008000`, and `vdev0buffer@55400000`.
The original `vring@...` names were not matched by Linux remoteproc. Rebuild and
boot the corrected `imx8mp-frdm.dtb`; rebuilding Zephyr alone is insufficient.
The corrected U-Boot defaults select `imx8mp-frdm.dtb` and run `prepare_mcore`
before the BSP boot path. Verify the actual Linux model and command line after boot. See Part 2's `HANG-FIX.md`
and run its read-only `check-linux.py` before starting M7.

The image includes `nxp-mcore`, `nxp-provision-greengrass`, `/etc/nxp-lp/board.json`, and stable RPMsg aliases. Greengrass services remain disabled until the first provisioning step, preventing an empty configuration database from being seeded before credentials exist.

If packaging fails with `got *at() syscall for unknown directory, fd 4` and `tar: ... Cannot mkdir: Bad address`, update the complete bundle at its existing location and rerun the build command with the same `WORKDIR`. Newer host `tar` security updates use `openat2`, which the BSP's pinned `pseudo` cannot track. The bundled layer backports the [upstream syscall fix](https://git.yoctoproject.org/pseudo/commit/?id=472c8977e0238e5a1ed4d29d7c41de699646ceff) and its header follow-up. The script builds the patched `pseudo-native` before building the image. BitBake tracks the patch changes and rebuilds affected tasks; keep your BSP edits, downloads, and shared-state cache.

If BitBake fails, fix the first reported error and reuse the same work directory. A namespace denial is a build-host policy issue; configure it with the administrator instead of running BitBake as root.

## What you have learned

You have learned how to select the imx8mp-lpddr4-frdm NXP BSP, generate its dependency graph, and build an image with Greengrass and MCU support. You can locate the actual WIC/SDK artifacts and distinguish source/configuration checks from a completed build.
