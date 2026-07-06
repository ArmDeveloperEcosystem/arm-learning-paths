---
title: Choose a containerization path for the nopCommerce application
description: Compare Dockerfile and .NET SDK container publish workflows so you can choose a reproducible arm64 container path for nopCommerce.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Containerize and migrate the application

Containerization should preserve reproducibility across architectures. The following are practical paths for Dockerfile-based builds, and .NET SDK container publish with multi-architecture delivery guardrails.

Use the Dockerfile workflow as the default migration path for nopCommerce until your SDK-published image has the same Linux runtime dependencies and smoke-test results. Use SDK publish when you want MSBuild-owned image metadata and have a repeatable plan for the native packages that the Dockerfile previously installed.

### Dockerfile path

Run a Dockerfile build with `buildx` from the repository root when you want to preserve the upstream nopCommerce Dockerfile behavior. This is the safest first containerization path because the Dockerfile installs runtime packages used by nopCommerce on Linux, including globalization and image-processing dependencies.

Before you push a multi-architecture image, make sure `buildx` is available, you're logged in to your registry, and your builder can build both requested platforms. If `docker buildx version` fails, install the Docker Buildx plugin for your Docker package before continuing. On an Arm-only VM, the `linux/amd64` build requires emulation or an additional x64 builder node.

```bash
docker buildx version

IMAGE="registry.example.com/team/nopcommerce:4.90.3-cobalt"

# Create or reuse a buildx builder and initialize its platform support.
docker buildx create --use --name nopx || docker buildx use nopx
docker buildx inspect --bootstrap

# Build and publish a manifest list that includes multiple architectures.
docker buildx build --platform linux/amd64,linux/arm64 -t "$IMAGE" --push .

# Confirm that the pushed image contains both platform entries.
docker buildx imagetools inspect "$IMAGE"
```

### Single architecture .NET SDK publish path

Use SDK publish when you want tighter integration with .NET build settings and fewer custom Docker steps. For nopCommerce, treat this as a validation path until you've confirmed that the generated image includes the Linux native packages your store needs. SDK publish creates the container image, but it doesn't run `apk add` or `apt-get install` steps the way a Dockerfile does.

This command publishes an arm64 image into the local Docker daemon with an explicit repository, tag, and container runtime identifier:

```bash
dotnet publish src/Presentation/Nop.Web/Nop.Web.csproj \
  -c Release \
  /t:PublishContainer \
  -p:ContainerRuntimeIdentifier=linux-arm64 \
  -p:ContainerRepository=nopcommerce \
  -p:ContainerImageTag=arm64-test
```

Verify the local image architecture before you test it:

```bash
docker image inspect nopcommerce:arm64-test --format '{{.Architecture}}'
```

The expected output is `arm64`.

### Multi-arch .NET SDK publish path

Define runtime identifiers and multi-arch container runtime identifiers in the project file, then publish once. Add this metadata only after you've decided where nopCommerce's Linux runtime dependencies will live. If you use SDK publish for production, move those dependencies into a custom base image or another repeatable image-build step before replacing the Dockerfile workflow.

```xml
<PropertyGroup>
  <RuntimeIdentifiers>linux-x64;linux-arm64</RuntimeIdentifiers>
  <ContainerRuntimeIdentifiers>linux-x64;linux-arm64</ContainerRuntimeIdentifiers>
  <ContainerRepository>nopcommerce</ContainerRepository>
</PropertyGroup>

<ItemGroup>
  <ContainerPort Include="80" Type="tcp" />
</ItemGroup>
```

```bash
# Publish all configured runtime identifiers from one project definition.
dotnet publish src/Presentation/Nop.Web/Nop.Web.csproj -c Release /t:PublishContainer
```

This is the scalable path for one image definition across both architectures, but the generated image still needs the same smoke test as the Dockerfile image: start the container, connect it to PostgreSQL, and verify storefront routes before you promote it.

#### SDK version guardrail

Before choosing the SDK publish path for multi-architecture images, check the SDK version used by CI and by developer workstations:

```bash
dotnet --version
```

If you can't use a .NET SDK version that supports multi-RID container publishing, or if SDK publish doesn't produce the multi-architecture image index you need, use the `docker buildx build --platform linux/amd64,linux/arm64` workflow instead. 

Multi-RID container publishing starts with .NET SDK versions `8.0.405`, `9.0.102`, and `9.0.2xx`. The nopCommerce `release-4.90.3` source pins SDK `9.0.100` in `global.json` with feature-band roll-forward, so confirm the actual SDK selected by CI is new enough before relying on SDK multi-arch publish.


## What you've accomplished and what's next

You've learned about different containerization paths for the .NET application. 

Next, you'll tune application performance. 
