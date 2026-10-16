#!/usr/bin/env bash
set -euo pipefail

# Install the tested upstream release and configure this isolated Learning Path.
revision=0e427d788d253630d38a3a51cd76849e73cd6925
sandbox_image=python:3.11-slim@sha256:e88e9763f943ec1834f992a4b51e0f24500486803e8bc534e5767af9ea65f6ce
work_dir=${1:-"$HOME/muse-agent"}

fail() { printf 'Setup prerequisite failed: %s\n' "$*" >&2; exit 1; }
[[ $(uname -s) == Linux && $(uname -m) == aarch64 ]] || fail "Run on the Spark's Linux Arm64 host."
for command in curl git python3 docker; do
  command -v "$command" >/dev/null || fail "$command is missing. Install it before running setup."
done
python3 -c 'import sys; assert sys.version_info >= (3, 12)' || fail "Python 3.12 or newer is required for this helper."
docker info >/dev/null 2>&1 || fail "Docker is unavailable. Start Docker and grant this account Docker access, then reconnect."
docker_arch=$(docker info --format '{{.Architecture}}')
[[ "$docker_arch" == aarch64 || "$docker_arch" == arm64 ]] || fail "Docker must use an Arm64 daemon."
if [[ -e "$work_dir" && ! -d "$work_dir" ]]; then
  fail "$work_dir is not a directory. Choose another work directory."
fi
python3 - "$work_dir" <<'PY'
from pathlib import Path
import shutil, sys
path = Path(sys.argv[1]).expanduser().resolve()
while not path.exists():
    path = path.parent
if shutil.disk_usage(path).free < 10 * 1024**3:
    sys.exit('Setup prerequisite failed: allow at least 10 GiB free for the Hermes installation.')
PY
mkdir -p "$work_dir"
work_dir=$(cd "$work_dir" && pwd)
export HERMES_HOME="$work_dir/hermes-home"
# Hermes uses its own upstream locks, independent of the model environment.
unset PIP_CONSTRAINT PIP_BUILD_CONSTRAINT
checkout="$work_dir/hermes-agent"
installer="$work_dir/install-hermes-cli.sh"

curl --fail --location --connect-timeout 20 --retry 3 \
  "https://raw.githubusercontent.com/NousResearch/hermes-agent/$revision/scripts/install.sh" \
  -o "$installer"

if [[ -d "$checkout/.git" ]] && [[ $(git -C "$checkout" rev-parse HEAD) != "$revision" ]]; then
  echo "Existing checkout differs from the pinned revision. Choose another work directory." >&2
  exit 1
fi
if [[ -d "$checkout/.git" ]] && [[ -n $(git -C "$checkout" status --porcelain) ]]; then
  fail "Existing Hermes checkout has edits. Choose another work directory to preserve them."
fi

docker pull --platform linux/arm64 "$sandbox_image"

bash "$installer" --dir "$checkout" --hermes-home "$HERMES_HOME" \
  --commit "$revision" --non-interactive --skip-browser --skip-computer-use
test -x "$checkout/.hermes/bin/hermes"

mkdir -p "$work_dir/bin"
mkdir -p "$work_dir/demo/input" "$work_dir/demo/output"
python3 - "$work_dir" "$sandbox_image" <<'PY'
import json, shlex, sys
from pathlib import Path
root = Path(sys.argv[1])
sandbox_image = sys.argv[2]
launcher = root / 'bin/hermes'
launcher.write_text(
    '#!/usr/bin/env bash\n'
    f'export HERMES_HOME={shlex.quote(str(root / "hermes-home"))}\n'
    f'export TERMINAL_DOCKER_IMAGE={shlex.quote(sandbox_image)}\n'
    f'exec {shlex.quote(str(root / "hermes-agent/.hermes/bin/hermes"))} "$@"\n'
)
launcher.chmod(0o755)
marker = root / 'hermes-home/.lp-configured'
if not marker.exists():
    config = {
        'model': {'provider': 'spark-local', 'default': 'muse-glimmer-30B',
                  'base_url': 'http://127.0.0.1:8000/v1', 'context_length': 65536,
                  'streaming': False},
        'providers': {'spark-local': {
            'api': 'http://127.0.0.1:8000/v1', 'transport': 'chat_completions',
            'default_model': 'muse-glimmer-30B', 'context_length': 65536,
            'extra_body': {'temperature': 1.0, 'top_p': 0.95, 'top_k': 64,
                           'reasoning_effort': None}}},
        'agent': {'reasoning_effort': None, 'max_turns': 40,
                  'image_input_mode': 'native'},
        'approvals': {'mode': 'manual'},
        'terminal': {'backend': 'docker', 'docker_image': sandbox_image,
                     'docker_network': False, 'docker_forward_env': [],
                     'docker_mount_cwd_to_workspace': False,
                     'docker_volumes': [str(root / 'demo/input') + ':/demo/input:ro',
                                        str(root / 'demo/output') + ':/demo/output'],
                     'container_cpu': 2, 'container_memory': 2048},
    }
    (root / 'hermes-home/config.yaml').write_text(json.dumps(config, indent=2))
    marker.touch()
elif not (root / 'hermes-home/config.yaml').is_file():
    sys.exit('Configuration marker exists but config.yaml is missing. Restore it or use another work directory.')
PY
# Apply this vision setting on reruns too; preserve other existing settings.
"$work_dir/bin/hermes" config set agent.image_input_mode native
"$work_dir/bin/hermes" chat --help >/dev/null
printf 'Hermes installed: %s/bin/hermes\n' "$work_dir"
printf 'Next: verify the local model connection and Docker sandbox using the Learning Path checks.\n'
