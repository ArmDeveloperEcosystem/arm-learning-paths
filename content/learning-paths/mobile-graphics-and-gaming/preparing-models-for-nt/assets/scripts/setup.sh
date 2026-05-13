cat > setup_executorch_min.sh <<'EOF'
#!/usr/bin/env bash
set -Eeuo pipefail

PYTHON_VERSION="${PYTHON_VERSION:-3.11.14}"
REPO_URL="${REPO_URL:-https://github.com/pytorch/executorch.git}"
REPO_PARENT="repo"
REPO_DIR="${REPO_PARENT}/executorch"
VENV_DIR="./venv"

have() {
  command -v "$1" >/dev/null 2>&1
}

OS="$(uname -s)"
case "${OS}" in
  Darwin) PLATFORM="macos" ;;
  Linux)  PLATFORM="linux" ;;
  *) echo "Unsupported OS: ${OS}" >&2; exit 1 ;;
esac

install_deps_macos() {
  if ! xcode-select -p >/dev/null 2>&1; then
    echo "Run: xcode-select --install" >&2
    exit 1
  fi

  if ! have brew; then
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  fi

  if [ -x "/opt/homebrew/bin/brew" ]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
  elif [ -x "/usr/local/bin/brew" ]; then
    eval "$(/usr/local/bin/brew shellenv)"
  fi

  brew update
  brew install openssl readline sqlite3 xz zlib tcl-tk libffi git curl wget pyenv cmake ninja pkg-config
}

install_deps_linux() {
  if have apt-get; then
    sudo apt-get update
    sudo apt-get install -y \
      make build-essential patch \
      libssl-dev zlib1g-dev \
      libbz2-dev libreadline-dev libsqlite3-dev \
      curl wget git \
      libncursesw5-dev xz-utils tk-dev \
      libxml2-dev libxmlsec1-dev \
      libffi-dev liblzma-dev \
      libgdbm-dev libgdbm-compat-dev \
      uuid-dev libnss3-dev \
      ca-certificates llvm cmake ninja-build pkg-config
  elif have dnf; then
    sudo dnf install -y \
      gcc gcc-c++ make patch \
      openssl-devel zlib-devel bzip2-devel \
      readline-devel sqlite-devel \
      curl wget git \
      ncurses-devel xz xz-devel tk-devel \
      libffi-devel gdbm-devel libuuid-devel nss-devel \
      ca-certificates llvm cmake ninja-build pkgconf-pkg-config
  elif have yum; then
    sudo yum install -y \
      gcc gcc-c++ make patch \
      openssl-devel zlib-devel bzip2-devel \
      readline-devel sqlite-devel \
      curl wget git \
      ncurses-devel xz xz-devel tk-devel \
      libffi-devel gdbm-devel libuuid-devel nss-devel \
      ca-certificates llvm cmake ninja-build pkgconfig
  else
    echo "Unsupported Linux package manager" >&2
    exit 1
  fi
}

ensure_pyenv() {
  export PYENV_ROOT="${HOME}/.pyenv"

  export PATH="${PYENV_ROOT}/bin:$PATH"

  if ! have pyenv; then
    echo "Installing pyenv..."
    curl -fsSL https://pyenv.run | bash
    export PATH="${PYENV_ROOT}/bin:$PATH"
  fi

  eval "$(pyenv init --path)"
  eval "$(pyenv init -)"
}

ensure_python() {
  pyenv install -s "${PYTHON_VERSION}"
  pyenv rehash
  PYENV_PYTHON="${PYENV_ROOT}/versions/${PYTHON_VERSION}/bin/python"
}

clone_repo() {
  mkdir -p "${REPO_PARENT}"
  if [ ! -d "${REPO_DIR}/.git" ]; then
    git clone "${REPO_URL}" "${REPO_DIR}"
  fi
}

create_venv() {
  rm -rf "${VENV_DIR}"
  "${PYENV_PYTHON}" -m venv "${VENV_DIR}"
}

main() {
  if [ "${PLATFORM}" = "macos" ]; then
    install_deps_macos
  else
    install_deps_linux
  fi

  ensure_pyenv
  ensure_python
  clone_repo
  create_venv

  echo "Done"
  echo "Repo: ${REPO_DIR}"
  echo "Venv: ${VENV_DIR}"
}

main "$@"
EOF

chmod +x setup_executorch_min.sh
bash setup_executorch_min.sh
