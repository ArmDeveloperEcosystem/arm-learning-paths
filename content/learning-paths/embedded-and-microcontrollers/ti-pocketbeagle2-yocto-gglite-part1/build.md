---
title: "Build the PocketBeagle 2 Yocto image"
description: Build a PocketBeagle 2 Yocto image with the supplied script and locate the image and optional SDK artifacts.
weight: 3
layout: "learningpathall"
---

## Prepare the Linux build host

Run this page's commands as a normal user on an x86_64 Linux host. On macOS, use a remote Linux host or x86_64 Linux VM with files stored on its Linux filesystem. Do not build in a macOS shared folder.

Copy the downloaded archive to the Linux host. Extract it to a fixed location without spaces, then inspect the script's options:

```bash
mkdir -p "$HOME/ti"
unzip pocketbeagle2-scarthgap-build.zip -d "$HOME/ti"
cd "$HOME/ti/pocketbeagle2"
chmod +x build-pocketbeagle2.sh
./build-pocketbeagle2.sh --help
```

The script requires its bundled layer. Copying only the shell script causes the layer check to fail.

## Configure and validate dependencies

Install host dependencies and generate the image and SDK task graphs before compiling:

```bash
WORKDIR="$HOME/yocto-pocketbeagle2" JOBS=4 \
  ./build-pocketbeagle2.sh --install-deps --configure-only
```

`--install-deps` uses `sudo apt-get` and enables `en_US.UTF-8`; BitBake runs as your normal user. `WORKDIR` selects a dedicated build tree and `JOBS` controls parallel tasks and make jobs. The default is four jobs. Use the same `WORKDIR` on subsequent runs to reuse downloads and shared state.

The script checks user and network namespaces before fetching sources. If Ubuntu 24.04 blocks them, read the bundled `ubuntu24-usernamespaces.txt` and have the build-host administrator apply a suitable configuration. Do not run BitBake as root to bypass this check.

A successful configure-only run reports that parsing and requested task graphs passed. It does not prove compilation, image assembly, or boot. Inspect the generated revisions and graphs:

```bash
cat "$HOME/yocto-pocketbeagle2/sources.lock"
ls "$HOME/yocto-pocketbeagle2/validation/image"
ls "$HOME/yocto-pocketbeagle2/validation/sdk"
```

## Build the image

For this Hello World exercise, skip the optional cross-compilation SDK:

```bash
WORKDIR="$HOME/yocto-pocketbeagle2" JOBS=4 \
  ./build-pocketbeagle2.sh --no-sdk
```

The script packages the board integration recipes, builds LTTng modules and Weston, and builds `pocketbeagle2-dev-image`. The image includes Nucleus Lite, Python, development tools, SSH, and USB Ethernet support. Weston is included but is not needed for Hello World.

For Part 2, the image also includes `pb2-m4`, the M4 remoteproc driver, and the AM6254 reserved-memory settings.

Omit `--no-sdk` to build both image and SDK. The script regenerates `local.conf` and `bblayers.conf`. Store persistent overrides in `$WORKDIR/build/conf/pocketbeagle2-extra.conf`; keep the bundle at its original location because `bblayers.conf` references it.

Locate the compressed image and matching block map:

```bash
ls -lh "$HOME/yocto-pocketbeagle2/build/deploy-ti/images/pocketbeagle2/"*.wic*
```

Select `pocketbeagle2-dev-image-pocketbeagle2*.wic.xz` and its matching `.wic.bmap` from the same build. SDK installers, when requested, are under `$WORKDIR/build/deploy-ti/sdk/`. These are TI deployment paths rather than the usual `tmp/deploy` paths.

If a build fails, fix the reported error and rerun with the same work directory. The script refuses to overwrite edits in upstream layer checkouts and rejects concurrent builds in one work directory.

## What you have accomplished

You have a built microSD image and a record of its upstream layer revisions. Next, write the image to a card and verify the board's network connection.
