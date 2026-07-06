---
title: Audit dependencies
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Audit dependencies

Run dependency discovery before migration changes so you understand direct references, transitive risk, and hidden native payloads. This avoids late surprises when deploying to Arm.

### 1. Map direct references

Start with project-level references to see what your app explicitly depends on.

```bash
rg -n "<PackageReference|<ProjectReference" src
```

### 2. List transitive dependencies

Enumerate the full dependency graph; transitive packages often carry architecture-sensitive constraints.

```bash
dotnet list src/Presentation/Nop.Web/Nop.Web.csproj package --include-transitive
```

### 3. Generate an SBOM

Generate an SBOM so you can track all components, versions, and exposure surface as a first-class migration artifact. While not strictly necessary for migration purposes, this is a best practice that will save your team time down the road. You can also give this SBOM to an LLM to extract insights about your codebase for you.

```bash
dotnet tool install --global CycloneDX
dotnet CycloneDX src/Presentation/Nop.Web/Nop.Web.csproj -o sbom/
```

If tool installation is blocked, treat `dotnet list --include-transitive` plus `*.deps.json` evidence as a temporary fallback, not the final state.

### 4. Inspect package internals for native payloads

Inspect package contents directly to find architecture-specific native binaries.

```bash
mkdir -p /tmp/nupkg-audit
cp ~/.nuget/packages/<package>/<version>/<package>.<version>.nupkg /tmp/nupkg-audit/
cd /tmp/nupkg-audit
unzip -l <package>.<version>.nupkg | rg "runtimes/|native/"
```

This is how you catch hidden architecture-specific binaries.

## Dependency cascade rule

Treat dependencies as a chain, not isolated items:

- App depends on library A
- Library A depends on library B
- Library B is architecture-sensitive

You must resolve B first, then validate A, then validate the app.
