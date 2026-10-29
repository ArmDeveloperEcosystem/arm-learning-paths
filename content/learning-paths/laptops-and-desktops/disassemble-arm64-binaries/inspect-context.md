---
title: Inspect binary context
description: Inspect strings and symbols in arm64 Mach-O fixtures to distinguish supporting SME2 hints from instruction evidence.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Inspect supporting strings

A string is printable data stored in the binary. It can reveal a feature check, diagnostic message, or component name without interpreting executable machine code.

Set the positive fixture as the artifact to inspect, then search its arm64 slice for SME2-related text:

```bash
BIN=sme2-positive
strings -arch arm64 "$BIN" | grep -Ei 'FEAT_SME|FEAT_SME2|sme2|matrix|kernel'
```

The output includes the feature-name string. The output is similar to:

```output
hw.optional.arm.FEAT_SME2
```

This text supports the interpretation that the program is SME2-aware. It could remain in a binary after extension-specific code was removed, so it isn't instruction proof.

## Inspect symbols

The `nm` tool reads structured symbol-table metadata. A code symbol can associate a name with a static address, which helps you attribute nearby instructions.

Search the positive fixture for relevant symbols:

```bash
nm -arch arm64 "$BIN" | grep -Ei 'sme|sme2|mopa|matrix|kernel'
```

The output is similar to:

```output
0000000100004000 D _keep_sme2_kernel
0000000100000424 T _sme2_fixture_kernel
```

The `T` identifies `_sme2_fixture_kernel` as a defined code symbol. Its address is the start of the function in this build. The leading underscore is the Mach-O naming convention for a C-compatible symbol.

Symbols improve attribution, but they can be removed by stripping or use a misleading name. Executable instructions remain the primary evidence.

## Check the string-only control

Apply the same supporting-evidence searches to the string-only control:

```bash
strings -arch arm64 string-only-control | grep -Ei 'FEAT_SME|FEAT_SME2|sme2|matrix|kernel'
nm -arch arm64 string-only-control | grep -Ei 'sme|sme2|mopa|matrix|kernel'
```

The output is similar to:

```output
hw.optional.arm.FEAT_SME2
0000000100000378 T _sme2_string_only_marker
```

The control produces convincing-looking hints despite containing no SME2 instruction. This is why source names, compiler options, strings, symbols, and arm64 slice metadata must remain supporting evidence.

You can see how SME2 presence can be detected methodically:

| Finding | What it supports | What it doesn't prove |
| --- | --- | --- |
| Source or `-march` option | Build intent | Inclusion in the final artifact |
| arm64 slice | Base architecture | Optional extension instructions |
| String or symbol | Feature awareness and attribution | Extension instruction presence or execution |
| Decoded strict instruction in executable code | Static presence | Runtime execution, dispatch, or performance |

## What you've accomplished and what's next

You inspected strings and symbols to collect attribution hints without treating them as instruction proof. Next, you'll disassemble the binary to check for SME2 instructions.
