---
title: Run dependency discovery before migration
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Audit application ependencies

Run dependency discovery before migration changes so you understand direct references, transitive risk, and hidden native payloads. By doing so, you'll avoid late surprises when deploying to Arm.

### Map direct references

Start from the `nopCommerce` repository root. Project-level references show what the app explicitly depends on before NuGet expands the graph. The command searches project files under `src` and prints file names and line numbers so you can jump directly to the owning project.

```bash
rg -n "<PackageReference|<ProjectReference" src
```

### List transitive dependencies

Enumerate the full dependency graph for the web entry point. Transitive packages often carry architecture-sensitive constraints, so review the output for runtime-specific package names, native library packages, image processing libraries, database providers, and platform-specific assets.

```bash
dotnet list src/Presentation/Nop.Web/Nop.Web.csproj package --include-transitive
```

### Generate an SBOM

Generate an SBOM so you can track all components, versions, and exposure surface as a first-class migration artifact. While not strictly necessary for migration purposes, this is a best practice that will save your team time down the road. You can also give this SBOM to an LLM to extract insights about your codebase for you.

The CycloneDX tool is installed as a .NET global tool. Add `~/.dotnet/tools` to `PATH` in the current shell so the `dotnet-CycloneDX` command is available immediately after installation.

```bash
dotnet tool install --global CycloneDX
export PATH="$PATH:$HOME/.dotnet/tools"
dotnet-CycloneDX src/Presentation/Nop.Web/Nop.Web.csproj -o sbom/ -rs -F Json
```

The `-rs` option includes project references, and `-F Json` writes JSON output that is easier to diff in CI. If tool installation is blocked, treat `dotnet list --include-transitive` plus `*.deps.json` evidence as a temporary fallback, not the final state.

### Inspect package internals for native payloads

Inspect package contents directly when a dependency looks architecture-sensitive. NuGet package folders are usually lower case on Linux, so set `PACKAGE_ID` to the folder name under `~/.nuget/packages` and `PACKAGE_VERSION` to the version you want to inspect.

```bash
PACKAGE_ID="replace-with-package-id"
PACKAGE_VERSION="replace-with-version"
NUPKG="$HOME/.nuget/packages/$PACKAGE_ID/$PACKAGE_VERSION/$PACKAGE_ID.$PACKAGE_VERSION.nupkg"

mkdir -p /tmp/nupkg-audit
cp "$NUPKG" /tmp/nupkg-audit/
cd /tmp/nupkg-audit
unzip -l "$(basename "$NUPKG")" | rg "runtimes/|native/"
```

If the command prints `runtimes/linux-arm64`, the package already carries an Arm Linux asset. If it prints only `linux-x64`, `win-x64`, or another non-Arm runtime, trace whether that asset is used by nopCommerce before you treat the dependency as portable. If there is no output, the package does not advertise runtime or native payload directories in the `.nupkg`.

### Dependency cascade rule

Treat dependencies as a chain, not isolated items:

- App depends on library A
- Library A depends on library B
- Library B is architecture-sensitive

You must resolve B first, then validate A, then validate the app.

## What you've accomplished and what's next

You've reviewed application dependencies to understand what can change when you migrate to Arm.

Next, you'll explore options to containerize the application. 