---
title: "Build the PocketBeagle 2 Yocto image"
description: Build a PocketBeagle 2 Yocto image with the supplied script and locate the image and block map to write to a microSD card.
weight: 3
layout: "learningpathall"
---

## Unpack the build scripts

Extract the zip file you downloaded to a fixed location without spaces, then inspect the script's options:

```bash
mkdir -p "$HOME/ti"
unzip pocketbeagle2-scarthgap-build.zip -d "$HOME/ti"
cd "$HOME/ti/pocketbeagle2"
chmod +x build-pocketbeagle2.sh
./build-pocketbeagle2.sh --help
```

The `pocketbeagle2` directory contains three main items:

- `build-pocketbeagle2.sh`: the script that downloads the Yocto sources, configures the build, and builds the image
- `meta-pocketbeagle2-dev`: a Yocto layer with the board-specific changes, including the image definition, USB networking, kernel settings, and the Greengrass provisioning helper
- `README.md`: reference notes on the build and the board's configuration

Keep these together, because the script finds the layer relative to its own location.

## Configure and validate dependencies

Install host dependencies and generate the image task graph before compiling:

```bash
WORKDIR="$HOME/yocto-pocketbeagle2" \
  ./build-pocketbeagle2.sh --install-deps --configure-only
```

`--install-deps` uses `sudo apt-get` and enables `en_US.UTF-8`. `WORKDIR` selects a dedicated build tree. Use the same `WORKDIR` on subsequent runs to reuse downloads and shared state.

The script checks that BitBake can create the sandboxes it needs. Ubuntu 24.04 can restrict these by default. If the check fails, relax the restriction until the next reboot, then run the script again:

```bash
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0
```

Do not run BitBake as root to get around this check.

A successful configure-only run reports that parsing and requested task graphs passed. It does not prove compilation, image assembly, or boot. Inspect the generated revisions and graphs:

```bash
cat "$HOME/yocto-pocketbeagle2/sources.lock"
ls "$HOME/yocto-pocketbeagle2/validation/image"
```

## Build the image

The first build takes several hours. Builds that reuse the same `WORKDIR` are faster, because they reuse downloads and shared state.

Set the number of parallel jobs from your CPU cores and available memory. Memory is usually the limit, so the calculation allows 3 GB of RAM per job:

```bash
CORES=$(nproc)
MEM_GB=$(awk '/MemAvailable/ {print int($2/1024/1024)}' /proc/meminfo)
JOBS=$(( MEM_GB / 3 < CORES ? MEM_GB / 3 : CORES ))
(( JOBS >= 1 )) || JOBS=1
echo "Building with $JOBS jobs"
```

Skip the SDK, a cross-compiler toolchain for building your own C and C++ applications for the board. The Hello World component is a shell script and doesn't need it:

```bash
WORKDIR="$HOME/yocto-pocketbeagle2" JOBS=$JOBS \
  ./build-pocketbeagle2.sh --no-sdk
```

The script packages the board integration recipes, builds LTTng modules and Weston, and builds `pocketbeagle2-dev-image`. The image includes Greengrass nucleus lite, Python, development tools, SSH, and USB Ethernet support. Weston is included but is not needed for Hello World.

The image also includes M4 core support: the `pb2-m4` tool, the M4 remoteproc driver, and the AM6254 reserved-memory settings. The steps that follow don't use them.

The script regenerates `local.conf` and `bblayers.conf`. Store persistent overrides in `$WORKDIR/build/conf/pocketbeagle2-extra.conf`; keep the build scripts at their original location because `bblayers.conf` references it.

## Monitor the build

The build runs in several stages, and the task count BitBake reports grows from one stage to the next. For example, the total can rise from 964 to 10,460 tasks. This is expected. Each stage ends with a line that says all of its tasks succeeded.

A successful build ends with a `Summary` line and the paths to the results. Your task counts differ:

```output
NOTE: Tasks Summary: Attempted 10460 tasks of which 4312 didn't need to be rerun and all succeeded.

Summary: There were 5 WARNING messages.
Image: /home/user/yocto-pocketbeagle2/build/deploy-ti/images/pocketbeagle2/
Layer revisions: /home/user/yocto-pocketbeagle2/sources.lock
Dependency graphs: /home/user/yocto-pocketbeagle2/validation/
```

Warnings that a source download failed and fell back to a mirror are normal. A real failure appears as a line that starts with `ERROR`.

If a build fails, fix the reported error and rerun with the same work directory. The script refuses to overwrite edits in upstream layer checkouts and rejects concurrent builds in one work directory.

## Locate the image

When the build is complete, locate the compressed image and matching block map:

```bash
ls -lh "$HOME/yocto-pocketbeagle2/build/deploy-ti/images/pocketbeagle2/"*.wic*
```

The folder contains the disk image, `pocketbeagle2-dev-image-pocketbeagle2.rootfs.wic.xz`, and its block map, `pocketbeagle2-dev-image-pocketbeagle2.rootfs.wic.bmap`. You write both to the microSD card on the next page. The names without a timestamp are links to the latest build. The image is about 2 GB compressed.

## What you have accomplished

You have a built microSD image and a record of its upstream layer revisions. Next, write the image to a card and verify the board's network connection.
