#!/usr/bin/env bash
set -euo pipefail

fail() { printf 'Prerequisite check failed: %s\n' "$*" >&2; exit 1; }
[[ $(uname -s) == Linux && $(uname -m) == aarch64 ]] || fail "Run this on the Spark over SSH, not on your Mac."
export PATH="/usr/local/cuda/bin:$PATH"
for command in curl git python3 docker cmake make c++ nvcc nvidia-smi; do
  command -v "$command" >/dev/null || fail "$command is missing. Install it before continuing."
done
# This recipe targets the tested stock Ubuntu/Python/CUDA combination.
source /etc/os-release
[[ "$ID" == ubuntu && "$VERSION_ID" == 24.04 ]] || fail "This recipe was tested on Ubuntu 24.04-based DGX OS."
python3 -c 'import sys; assert sys.version_info[:2] == (3, 12)' || fail "Use Python 3.12 for the ExecuTorch environment."
python3 -m venv --help >/dev/null || fail "Python venv support is missing. Install python3.12-venv."
nvcc --version | grep -q 'release 13.0,' || fail "Use the CUDA 13.0 development toolkit tested by this recipe."
nvidia-smi --query-gpu=name --format=csv,noheader | grep -q 'GB10' || fail "No GB10 GPU is visible. Check the NVIDIA driver."
docker info >/dev/null 2>&1 || fail "Docker is unavailable to this account. Fix access and reconnect before continuing."
driver=$(nvidia-smi --query-gpu=driver_version --format=csv,noheader | head -n 1)
[[ ${driver%%.*} -ge 580 ]] || fail "CUDA 13 requires NVIDIA driver 580 or newer."
docker_arch=$(docker info --format '{{.Architecture}}')
[[ "$docker_arch" == aarch64 || "$docker_arch" == arm64 ]] || fail "Docker must use an Arm64 daemon."
[[ $(docker info --format '{{.OSType}}') == linux ]] || fail "Docker must run Linux containers."

python3 - "${1:-$HOME}" <<'PY'
from pathlib import Path
import re, shutil, subprocess, sys, tempfile, venv
path = Path(sys.argv[1]).expanduser().resolve()
while not path.exists():
    path = path.parent
if shutil.disk_usage(path).free < 100 * 1024**3:
    sys.exit('Prerequisite check failed: allow 100 GiB free before downloading/building the model stack.')
memory = Path('/proc/meminfo').read_text()
available = int(re.search(r'^MemAvailable:\s+(\d+)', memory, re.M).group(1)) * 1024
if available < 80 * 1024**3:
    sys.exit('Prerequisite check failed: free at least 80 GiB for export. Coordinate with owners of other model services before stopping them.')
version = subprocess.check_output(['cmake', '--version'], text=True).splitlines()[0].split()[-1]
if tuple(map(int, version.split('.')[:2])) < (3, 26):
    sys.exit('Prerequisite check failed: CMake 3.26 or newer is required.')
with tempfile.TemporaryDirectory(prefix='muse-venv-check-') as directory:
    venv.EnvBuilder(with_pip=True).create(directory)
    source = Path(directory) / 'check.cpp'
    source.write_text('#include <optional>\nint main() { std::optional<int> n = 0; return *n; }\n')
    binary = str(Path(directory) / 'check')
    subprocess.run(['c++', '-std=c++17', str(source), '-o', binary], check=True)
    subprocess.run([binary], check=True)
print('PASS: host architecture, OS, Python/venv/pip, compiler, CUDA, GPU, Docker, disk and export memory checks')
PY
