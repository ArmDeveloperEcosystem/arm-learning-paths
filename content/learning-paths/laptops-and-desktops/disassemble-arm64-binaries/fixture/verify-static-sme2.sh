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
