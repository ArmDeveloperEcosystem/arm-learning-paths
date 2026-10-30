---
title: Inspect strings and symbols in a binary
description: Search a macOS binary for SME2-related strings and symbols, and understand why these don't prove SME2 instructions are present.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Inspect supporting strings

A string is printable data stored in the binary. It can reveal a feature check, diagnostic message, or component name without interpreting executable machine code.

Select the example binary, then search its arm64 slice for SME2-related text:

```bash
BIN=sme2-positive
strings -arch arm64 "$BIN" | grep -Ei 'FEAT_SME|FEAT_SME2|sme2|matrix|kernel'
```

The output includes the feature-name string:

```output
hw.optional.arm.FEAT_SME2
```

This text suggests that the program includes code related to SME2. It could remain in a binary after SME and SME2 instructions were removed, so it doesn't prove those instructions are present.

## Inspect symbols

The `nm` tool lists symbols in a binary. Symbols associate names with addresses, helping you locate functions and data.

Search the example binary for SME2-related symbols:

```bash
nm -arch arm64 "$BIN" | grep -Ei 'sme|sme2|mopa|matrix|kernel'
```

The output is similar to:

```output
0000000100004000 D _keep_sme2_kernel
0000000100000424 T _sme2_fixture_kernel
```

The `T` identifies `_sme2_fixture_kernel` as a defined code symbol. Its address is the start of the function in this build. The leading underscore is the Mach-O naming convention for a C-compatible symbol.

Symbol names can be misleading, and symbols can be removed from a binary. Disassembly is needed to check which instructions are present.

## Check the string-only control

Run the same searches on the string-only comparison binary:

```bash
strings -arch arm64 string-only-control | grep -Ei 'FEAT_SME|FEAT_SME2|sme2|matrix|kernel'
nm -arch arm64 string-only-control | grep -Ei 'sme|sme2|mopa|matrix|kernel'
```

The output is similar to:

```output
hw.optional.arm.FEAT_SME2
0000000100000378 T _sme2_string_only_marker
```

The comparison binary contains an SME2-related string and symbol, but no SME2 instructions. Finding these names doesn't prove the instructions are present. Compiler options and the arm64 architecture label don't prove this either.

Each check tells you something different about the binary:

| Finding | What it supports | What it doesn't prove |
| --- | --- | --- |
| `-march` option | Requested compiler features | Presence of SME or SME2 instructions in the compiled binary |
| arm64 slice | Code compiled for arm64 | Presence of SME or SME2 instructions |
| String or symbol | Names associated with SME2 | Presence or runtime execution of SME or SME2 instructions |
| Decoded SME or SME2 instruction in executable code | Instructions present in the binary | Whether those instructions run or improve performance |

## What you've accomplished and what's next

You found SME2-related strings and symbols in both the example and comparison binaries. Next, you'll disassemble the binaries to check which ones contain SME2 instructions.
