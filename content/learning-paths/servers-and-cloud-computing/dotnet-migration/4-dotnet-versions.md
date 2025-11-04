---
title: Evaluate .NET performance across versions on Arm
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Version-by-version feature and throughput improvements

Understanding which versions perform best and the features they offer can help you make informed decisions when developing applications for Arm-based systems.

.NET has evolved significantly over the years, with each version introducing new features and performance improvements. Here, you will learn about key versions that have notable performance implications for Arm architecture.

{{% notice Support status summary %}}

- .NET 8 – Current LTS (support until Nov 2026)
- .NET 9 – STS (support until Nov 2026)
- .NET 10 – Next LTS (preview; expected GA Nov 2025)
- .NET 3.1, 5, 6, 7 – End of life
{{% /notice %}}


## .NET Core 3.1 (end-of-life 2022)

.NET Core 3.1 was the first LTS with meaningful Arm64 support. 

Highlights were:

- Initial JIT (Just-In-Time) optimizations for Arm64 (but the bulk of Arm throughput work arrived in .NET 5).
- Faster garbage collection thanks to refinements to the background GC mode.
- Initial set of Arm64 hardware intrinsics (AdvSIMD, AES, CRC32) exposed in `System.Runtime.Intrinsics`.

## .NET 5 (end-of-life 2022)

With .NET 5 Microsoft started the “one .NET” unification. Even though it had only 18 months of support, it delivered notable Arm gains:

- Cross-gen2 shipped, delivering better Arm64 code quality (but only became the default in .NET 6).
- Single-file application publishing (with optional IL-trimming) simplified deployment to Arm edge devices.
- Major ASP.NET Core throughput wins on Arm64 (Kestrel & gRPC) compared with .NET Core 3.1.

## .NET 6 (end-of-life 2024)

.NET 6 laid the foundation for the modern performance story on Arm64:

- Tiered PGO entered preview, combining tiered compilation with profile-guided optimization.
- Better scalability on many-core Arm servers thanks to the new ThreadPool implementation.
- First-class support for Apple M1, enabling full .NET development on Arm-based macOS, as well as for Windows Arm64.


## .NET 7 (end-of-life 2024)

.NET 7 was an STS (Standard-Term Support) release which is now out of support, but it pushed the performance envelope and is therefore interesting from a historical perspective. 

Key highlights were:

- General-availability of Native AOT publishing for console applications, producing self-contained, very small binaries with fast start-up on Arm64.
- Dynamic PGO (Profile-Guided Optimization) and On-Stack Replacement became the default, letting the JIT optimize the hottest code paths based on real run-time data.
- New Arm64 hardware intrinsics (e.g. SHA-1/SHA-256, AES, CRC-32) exposed through System.Runtime.Intrinsics, enabling high-performance crypto workloads.

## .NET 8 (current LTS – support until November 2026)

.NET 8 is the current Long-Term Support release and should be your baseline for new production workloads. 

Important Arm-related improvements include:

- Native AOT support for ASP.NET Core, trimming enhancements and even smaller self-contained binaries, translating into faster cold-start for containerized Arm services.
- Further JIT tuning for Arm64 delivering single-digit to low double-digit throughput gains in real-world benchmarks.
- Smaller base container images (`mcr.microsoft.com/dotnet/aspnet:8.0` and `…/runtime:8.0`) thanks to a redesigned layering strategy, particularly beneficial on Arm where network bandwidth is often at a premium.
- Garbage-collector refinements that reduce pause times on highly-threaded, many-core servers.

## .NET 9 (current STS - support until November 2026)

.NET 9 is still in preview, so features may change, but public builds already show promising Arm-centric updates:

- PGO is now enabled for release builds by default and its heuristics have been retuned for Arm workloads, yielding notable throughput improvements with zero developer effort.
- The JIT has started to exploit Arm v9 instructions such as SVE2 where hardware is available, opening the door to even wider SIMD operations.
- C# 13 and F# 8 previews ship with the SDK, bringing useful productivity improvements fully supported on Arm devices.

Although .NET 9 will receive only 18 months of support, it is an excellent choice when you need the very latest performance improvements or want to trial new language/runtime capabilities ahead of the next LTS.

## .NET 10 (preview – next LTS)

.NET 10 is still in preview and will likely evolve prior to its GA release, but it will be the next LTS version of .NET, with the following benefits:

- [Extended SVE2 intrinsics](https://github.com/dotnet/runtime/issues/109652) to unlock efficient implementation of large-scale numerical algorithms and on-device AI inference on Arm v9.
- C# 14 is expected to ship alongside .NET 10, bringing additional compile-time metaprogramming features that can reduce boilerplate on resource-constrained Arm edge devices.

Developers targeting Arm-based systems should track preview builds and roadmap updates closely to validate feature availability and compatibility with their target platforms.

