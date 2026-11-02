#!/usr/bin/env bash
set -euo pipefail

echo "Hello from an ephemeral AI code-execution sandbox"
echo "architecture=$(uname -m)"
echo "kernel=$(uname -r)"
echo "cpus=$(nproc)"
echo "memory_limit:"
free -h
echo "pid_1=$(ps -p 1 -o comm=)"

