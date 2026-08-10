#!/usr/bin/env bash
set -euo pipefail

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
build_dir="${1:-$script_dir/build}"

mkdir -p "$build_dir"

xcrun clang -arch arm64 -O2 -march=armv9-a+sme2 \
    "$script_dir/sme2-main.c" \
    "$script_dir/sme2-kernel.S" \
    -o "$build_dir/sme2-positive"

xcrun clang -arch arm64 -O2 \
    "$script_dir/string-only-control.c" \
    -o "$build_dir/string-only-control"

xcrun clang -arch arm64 -O2 \
    "$script_dir/plain-arm64-control.c" \
    -o "$build_dir/plain-arm64-control"

printf 'Built static-inspection fixtures in %s\n' "$build_dir"
