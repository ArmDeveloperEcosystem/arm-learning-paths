---
title: Automate and adapt the inspection workflow
description: Automate the SME and SME2 instruction check for Mach-O binaries and adapt the inspection method to other instruction groups and binary formats.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Automate the SME and SME2 instruction check

You inspected the example binary with two disassemblers and checked both comparison binaries. You can now combine the `llvm-objdump` and AWK steps in a reusable script.

Continue in the `arm64-extension-inspection` working directory, alongside `strict-sme2.awk` and the compiled binaries. Run the following block to create `verify-static-sme2.sh` and make it executable:

```bash
cat > verify-static-sme2.sh <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
    printf 'Usage: %s <Mach-O binary> [output directory]\n' "$0" >&2
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
    printf 'FAIL: no matching SME or SME2 instructions found in %s\n' "$artifact" >&2
    exit 1
fi

printf 'PASS: matching SME or SME2 instructions found in %s\n' "$artifact"
printf 'Results saved to: %s\n' "$evidence_dir"
EOF
chmod +x verify-static-sme2.sh
```

Run the script on the example binary:

```bash
./verify-static-sme2.sh sme2-positive evidence-positive
```

The script returns exit status 0 to indicate that it found matching instructions. The expected output is:

```output
PASS: matching SME or SME2 instructions found in sme2-positive
Results saved to: evidence-positive
```

Now run the same check on the string-only comparison binary:

```bash
./verify-static-sme2.sh string-only-control evidence-string-only
```

The script returns exit status 1. The expected output is:

```output
FAIL: no matching SME or SME2 instructions found in string-only-control
```

This `FAIL` result is expected because the comparison binary contains no matching instructions. Exit status 1 indicates that the filter found no matches. The output directory still contains the disassembler version in `decoder-version.txt`, the disassembly in `llvm-objdump.txt`, and an empty `strict-sme2-hits.txt` file.

This check confirms that matching instructions are present in the binary. It doesn't show whether the application runs them or whether they improve performance.

## Check another binary

To inspect another binary, follow these steps:

1. Select the executable or library you plan to distribute.
2. Select the architecture slice and sections containing executable code.
3. Decode the instructions with a disassembler configured to recognize the instruction group you want to check.
4. Filter the decoded instructions by checking both their names and operands.
5. Inspect the surrounding function and its symbols.
6. Summarize which instructions you found and what the checks don't establish.

For the example binary, you can summarize the manual checks and script results as follows:

Both disassemblers found SME and SME2 instructions at matching addresses. These checks don't show whether the application runs those instructions or whether they improve performance.

## Check for other instruction groups

You can apply the same method to other instruction groups, such as Scalable Vector Extension (SVE), SVE2, and Dot Product instructions.

To check another instruction group, update the filter to recognize its instruction names and operands. Check the documentation for those instructions rather than relying on names alone. Test the filter with these comparison binaries:

- A binary containing instructions you want to detect
- A binary containing similar instructions that shouldn't match
- A binary containing related strings and symbol names, but no matching instructions

## Adapt the commands for Linux or Windows

The inspection method also applies to Linux and Windows binaries, but the commands must match the binary format:

| Binary format | Common platforms | What to inspect |
| --- | --- | --- |
| Mach-O | macOS and iOS | The arm64 slice and sections containing executable code |
| ELF | Linux and Android | The AArch64 executable or shared library and its executable code sections |
| PE/COFF | Windows on Arm | The ARM64 executable or library and its executable code sections |

Inspect the actual executable or library you plan to distribute. Checking the macOS binary doesn't establish what a separately built Linux or Windows binary contains.

## What you've accomplished

You can now inspect a macOS binary for SME and SME2 instructions using two disassemblers and automate the check with a reusable script. You also know why strings, symbols, and compiler options alone don't prove those instructions are present.

Apply this workflow to your own executable or library. Remember that finding instructions in a binary doesn't establish whether your application runs them or whether they improve performance.
