---
title: Containerize the application
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Containerize the application

Containerization should preserve reproducibility across architectures. This page shows practical paths for Dockerfile-based builds and .NET SDK container publish, with guardrails for multi-architecture delivery.

### 1. Dockerfile path

Run a Dockerfile build with buildx:

```bash
# Create or reuse a buildx builder that supports multi-architecture builds.
docker buildx create --use --name nopx

# Build and publish a manifest list that includes multiple architectures.
docker buildx build --platform linux/amd64,linux/arm64 -t [your repo:tag name] --push .
```

### 2. .NET SDK publish path (single architecture)

Use SDK publish when you want tighter integration with .NET build settings and fewer custom Docker steps.

```bash
dotnet publish src/Presentation/Nop.Web/Nop.Web.csproj \
  -c Release \
  /t:PublishContainer \
  -p:ContainerImageTag=publish-test
```

### 3. .NET SDK multi-arch path

Define runtime identifiers and multi-arch container runtime identifiers in the project file, then publish once.

```xml
<PropertyGroup>
  <RuntimeIdentifiers>linux-x64;linux-arm64</RuntimeIdentifiers>
  <ContainerRuntimeIdentifiers>linux-x64;linux-arm64</ContainerRuntimeIdentifiers>
</PropertyGroup>
```

```bash
# Publish all configured runtime identifiers from one project definition.
dotnet publish src/Presentation/Nop.Web/Nop.Web.csproj -c Release /t:PublishContainer
```

This is the scalable path for one image definition across both architectures.

## SDK version guardrail

Before choosing the SDK publish path for multi-architecture images, check the SDK version used by CI and by developer workstations:

```bash
dotnet --version
```

If you cannot use a .NET SDK version that supports multi-RID container publishing, or if SDK publish does not produce the multi-architecture image index you need, use the `docker buildx build --platform linux/amd64,linux/arm64` workflow instead. Multi-RID container publishing starts with .NET SDK versions 8.0.405, 9.0.102, and 9.0.2xx.

## Recommendation

Use SDK publish as the default migration path. Use a Dockerfile workflow for advanced layer control or custom build logic.
