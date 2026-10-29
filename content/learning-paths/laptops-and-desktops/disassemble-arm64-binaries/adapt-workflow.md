---
title: Automate and adapt the inspection workflow
description: Automate the static SME/SME2 check for Mach-O binaries and identify how to adapt the evidence sequence to other Arm extensions and binary formats.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Automate the SME/SME2 check

In the previous section, you inspected the fixture with two disassemblers and checked both negative controls. You can now combine the `llvm-objdump` and AWK steps in a reusable script.

Continue in the `arm64-extension-inspection` working directory, alongside `strict-sme2.awk` and the compiled fixtures. Run the following block to create `verify-static-sme2.sh` and make it executable:

```bash
cat > verify-static-sme2.sh <<'EOF'
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
EOF
chmod +x verify-static-sme2.sh
```

Run the script against the positive fixture:

```bash
./verify-static-sme2.sh sme2-positive evidence-positive
```

The script returns status 0. The expected output is:

```output
PASS: strict SME/SME2 instructions were decoded from sme2-positive
Evidence: evidence-positive
```

Now run the same check against the string-only control:

```bash
./verify-static-sme2.sh string-only-control evidence-string-only
```

The script returns status 1. The expected output is:

```output
FAIL: no strict SME/SME2 instruction was decoded from string-only-control
```

This `FAIL` result is expected for a negative control: status 1 means that no matching instruction was found. The evidence directory still contains `decoder-version.txt`, `llvm-objdump.txt`, and the empty `strict-sme2-hits.txt`, so you can inspect how the result was obtained.

This check verifies static inclusion. It doesn't verify that a runtime dispatcher selected the code, that a target executed it, or that it improved performance.

## Reuse the evidence sequence

To apply the same approach beyond the fixture, use this sequence:

1. Select the final shipped artifact, not an object file or build log.
2. Select the architecture slice and executable sections.
3. Decode the instructions with a decoder that enables the required extension.
4. Apply an operand-aware extension predicate to decoded instruction text.
5. Inspect nearby instructions, symbols, and component context.
6. Record a verdict that states what the evidence proves and what remains unknown.

For the positive fixture, combining the manual checks from the previous section with the script results supports this verdict:

```output
Static presence confirmed: strict SME/SME2 instructions decode from executable
code at matching static PCs in two decoder views. Runtime execution, dispatch
selection, and performance impact were not measured.
```

## Design another extension predicate

You can apply the same sequence to SVE and SVE2, Dot Product, Int8 Matrix Multiplication (I8MM), BFloat16 (BF16), Large System Extensions (LSE), cryptographic instructions, and Pointer Authentication. Each extension has different encodings, aliases, and operand constraints.

Don't publish a supposedly complete regular expression based only on mnemonic names. Ground the predicate in the [A64 Instruction Set Architecture](https://developer.arm.com/documentation/ddi0602/latest/) and validate it with these controls:

- A positive artifact containing known extension instructions in executable code
- A negative artifact containing nearby base-architecture or related-extension instructions
- A string-only artifact containing feature names and mnemonic-like text but no matching instruction

For example, a Dot Product predicate must distinguish the intended dot-product encodings and operand types from unrelated multiply-accumulate operations. A Pointer Authentication predicate must account for instruction aliases and whether hints decode differently under the selected architecture features. These are validation requirements, not complete predicates.

## Apply the method to ELF and PE/COFF

The evidence model is independent of the object format, but the artifact and section-selection commands change:

| Artifact format | Common deployment | What changes |
| --- | --- | --- |
| Mach-O | macOS and iOS | Select an arm64 slice and Mach-O executable sections |
| ELF | Arm Linux, Android native libraries, and most Neoverse releases | Select AArch64 ELF executable sections and account for shared objects and stripped symbols |
| PE/COFF | Windows on Arm | Select the ARM64 image and executable PE sections |

Don't use the Mach-O commands in this Learning Path to claim that a separate Neoverse Linux artifact contains the same code. Inspect the actual ELF executable or shared library that you plan to release on the Neoverse target.

## What you've accomplished and what's next

You can now automate the static instruction check and adapt the inspection method to other Arm extensions and binary formats. Next, you'll learn when to use static inspection and when to use Arm Performix to investigate runtime performance.
