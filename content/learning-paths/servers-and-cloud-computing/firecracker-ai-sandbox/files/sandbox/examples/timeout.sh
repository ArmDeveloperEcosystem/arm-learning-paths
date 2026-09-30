#!/usr/bin/env bash
set -euo pipefail

echo "Starting work that should exceed the job timeout."
sleep 30
echo "Unexpected: the job completed without timing out."

