# rexec_sweet - Remote Sweet Benchmark Execution Tool

A tool for running Go benchmarks using Sweet on remote GCP instances and comparing results.

## Installation

### Python Environment Setup

#### Installing pyenv

```bash
# macOS (using Homebrew)
brew update
brew install pyenv

# Linux
sudo apt-get -y update

sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev

curl https://pyenv.run | bash

# Add to your shell configuration (.bashrc, .zshrc, etc.)
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```

Restart your shell or run `source ~/.bashrc` (or your appropriate shell config file).

#### Setting up Python 3.9.22 with pyenv and virtualenv

```bash
# Install Python 3.9.22
pyenv install 3.9.22

# Create a virtualenv for this project
pyenv virtualenv 3.9.22 rexec-sweet-env

# Activate the virtualenv
pyenv activate rexec-sweet-env
# Or navigate to the project directory and set local Python version
cd /path/to/project
pyenv local rexec-sweet-env
```

#### Installing the package

```bash
# Install from the project directory
pip install -e .
```

## Usage

```bash
# Run the tool
rexec-sweet

# Run with specific benchmark and instances
rexec-sweet --benchmark markdown --instance1 c4-96 --instance2 c4-64

# Generate report from existing benchstat file
rexec-sweet --report results/benchstat.results --output-dir ./my-report
```

## Project Structure

```
rexec_sweet/
├── __init__.py          # Package exports
├── benchmark_runner.py  # Benchmark execution logic
├── benchstat_report.py  # Report generation
├── cli.py               # Command-line interface
├── config.py            # Configuration management
├── gcp_utils.py         # GCP interaction utilities
└── visualization.py     # Data visualization

tests/                   # Test suite
```

## Running Tests

```bash
# Install development dependencies
make dev

# Run tests
make test

# Run tests with coverage
make test-cov
```

## Requirements

- Python 3.9+
- Google Cloud SDK
- Go with benchstat tool installed
- Sweet benchmarking tool