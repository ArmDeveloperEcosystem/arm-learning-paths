---
title: Adapt the workflow to other Arm extensions
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Reuse the evidence sequence

The reusable workflow has six stages:

1. Select the final shipped artifact, not an object file or build log.
2. Select the architecture slice and executable sections.
3. Decode the instructions with a decoder that enables the required extension.
4. Apply an operand-aware extension predicate to decoded instruction text.
5. Inspect nearby instructions, symbols, and component context.
6. Record a verdict that states what the evidence proves and what remains unknown.

For the positive fixture, an evidence-bounded verdict is:

```output
Static presence confirmed: strict SME/SME2 instructions decode from executable
code at matching static PCs in two decoder views. Runtime execution, dispatch
selection, and performance impact were not measured.
```

## Design another extension predicate

You can apply the same sequence to SVE and SVE2, Dot Product, Int8 Matrix Multiplication (I8MM), BFloat16 (BF16), Large System Extensions (LSE), cryptographic instructions, and Pointer Authentication. Each extension has different encodings, aliases, and operand constraints.

Don't publish a supposedly complete regular expression based only on mnemonic names. Ground the predicate in the [A64 Instruction Set Architecture](https://developer.arm.com/documentation/ddi0602/latest/) and validate it with these controls:

- A positive artifact containing known extension instructions in executable code.
- A negative artifact containing nearby base-architecture or related-extension instructions.
- A string-only artifact containing feature names and mnemonic-like text but no matching instruction.

For example, a Dot Product predicate must distinguish the intended dot-product encodings and operand types from unrelated multiply-accumulate operations. A Pointer Authentication predicate must account for instruction aliases and whether hints decode differently under the selected architecture features. These are validation requirements, not complete predicates.

## Apply the method to ELF and PE/COFF

The evidence model is independent of the object format, but the artifact and section-selection commands change:

| Artifact format | Common deployment | What changes |
| --- | --- | --- |
| Mach-O | macOS and iOS | Select an arm64 slice and Mach-O executable sections |
| ELF | Arm Linux, Android native libraries, and most Neoverse releases | Select AArch64 ELF executable sections and account for shared objects and stripped symbols |
| PE/COFF | Windows on Arm | Select the ARM64 image and executable PE sections |

Don't use the Mach-O commands in this Learning Path to claim that a separate Neoverse Linux artifact contains the same code. Inspect the actual ELF executable or shared library that you plan to release on the Neoverse target.

## Create a static release gate

A release gate should scan the final artifact, pin the decoder, fail when required code is absent, and retain its inputs and disassembly. Create `verify-static-sme2.sh` with the following CI-neutral script. It uses the `strict-sme2.awk` predicate from the previous section.

```bash { file_name="verify-static-sme2.sh" }
#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
    printf 'Usage: %s <Mach-O artifact> [evidence directory]\n' "$0" >&2
    exit 2
fi

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
artifact=$1
evidence_dir=${2:-static-disassembly-evidence}
decoder=${LLVM_OBJDUMP:-$(xcrun -f llvm-objdump)}

mkdir -p "$evidence_dir"

"$decoder" --version > "$evidence_dir/decoder-version.txt"
decoder_version=$(sed -n '1p' "$evidence_dir/decoder-version.txt")
if [[ -n ${EXPECTED_LLVM_OBJDUMP_VERSION:-} &&
      "$decoder_version" != "$EXPECTED_LLVM_OBJDUMP_VERSION" ]]; then
    printf 'FAIL: decoder version is %s; expected %s\n' \
        "$decoder_version" "$EXPECTED_LLVM_OBJDUMP_VERSION" >&2
    exit 2
fi

"$decoder" -d --macho --arch=arm64 --mattr=+sme,+sme2 "$artifact" \
    > "$evidence_dir/llvm-objdump.txt"

awk -f "$script_dir/strict-sme2.awk" \
    "$evidence_dir/llvm-objdump.txt" \
    > "$evidence_dir/strict-sme2-hits.txt"

if [[ ! -s "$evidence_dir/strict-sme2-hits.txt" ]]; then
    printf 'FAIL: no strict SME/SME2 instruction was decoded from %s\n' "$artifact" >&2
    exit 1
fi

printf 'PASS: strict SME/SME2 instructions were decoded from %s\n' "$artifact"
printf 'Evidence: %s\n' "$evidence_dir"
```

Make the gate executable, pin it to the decoder used in this Learning Path, and test the positive artifact:

```bash
chmod +x verify-static-sme2.sh
EXPECTED_LLVM_OBJDUMP_VERSION='Apple LLVM version 21.0.0' \
  ./verify-static-sme2.sh sme2-positive evidence-positive
```

The expected output is:

```output
PASS: strict SME/SME2 instructions were decoded from sme2-positive
Evidence: evidence-positive
```

Apply the gate to the string-only control to test the failing outcome:

```bash
EXPECTED_LLVM_OBJDUMP_VERSION='Apple LLVM version 21.0.0' \
  ./verify-static-sme2.sh string-only-control evidence-string-only
```

The gate returns status 1 and reports:

```output
FAIL: no strict SME/SME2 instruction was decoded from string-only-control
```

The evidence directory still contains `decoder-version.txt`, `llvm-objdump.txt`, and the empty `strict-sme2-hits.txt`. Configure your CI system to retain that directory even when the gate fails.

The following GitHub Actions fragment selects a named Xcode installation, checks the pinned decoder string, scans a previously built final artifact, and uploads the evidence on both pass and fail:

```yaml
- name: Verify SME2 in the final Mach-O artifact
  env:
    DEVELOPER_DIR: /Applications/Xcode_26.6.app/Contents/Developer
    EXPECTED_LLVM_OBJDUMP_VERSION: Apple LLVM version 21.0.0
  run: |
    ./fixture/verify-static-sme2.sh \
      ./release/MyApp.app/Contents/MacOS/MyApp \
      ./static-disassembly-evidence

- name: Retain static disassembly evidence
  if: always()
  uses: actions/upload-artifact@v4
  with:
    name: static-disassembly-evidence
    path: static-disassembly-evidence/
```

Replace the artifact path and Xcode installation with the pinned versions in your release environment. If the decoder version changes, review the disassembly and predicate results before updating the pin.

This gate verifies static inclusion. It doesn't verify that a runtime dispatcher selected the code, that a target executed it, or that it improved performance.

## What you've learned and what's next

You can now adapt the workflow to another extension or object format and enforce static inclusion in CI. Next, you will choose between exact artifact inspection and Arm Performix runtime performance analysis.
