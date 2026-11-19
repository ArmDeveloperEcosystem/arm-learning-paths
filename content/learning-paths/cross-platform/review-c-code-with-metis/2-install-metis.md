---
title: Install and configure Metis
description: Install a tested Metis release and configure a model provider with an API key.
weight: 3
layout: "learningpathall"
---

## Install system tools

The commands in this Learning Path use a Unix-like shell. Use Terminal on macOS, a Linux terminal, or an existing Ubuntu/Debian terminal running under WSL2 on Windows. Native Windows PowerShell and Command Prompt are not covered.

Select your platform and install the compiler, Git, and command-line utilities used to fetch code, apply patches, and inspect reports:

{{< tabpane code=true >}}
  {{< tab header="macOS" language="bash">}}
xcode-select --install
  {{< /tab >}}
  {{< tab header="Ubuntu Linux or WSL2" language="bash">}}
sudo apt-get update
sudo apt-get install -y build-essential ca-certificates curl git grep patch sed
  {{< /tab >}}
{{< /tabpane >}}

If the Xcode Command Line Tools are already installed, macOS reports that no installation is needed. On WSL2, use the Linux filesystem for this exercise and avoid creating the workspace under `/mnt/c`.

## Install uv and Python

Metis requires Python 3.12 or later. This Learning Path uses `uv` to install Python 3.12 and create an isolated Metis environment:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Load the shell environment created by the installer and confirm that `uv` is available:

```bash
source "$HOME/.local/bin/env"
uv --version
```

Install Python 3.12 using `uv`:

```bash
uv python install 3.12
uv python find 3.12
```

The second command prints the path to the managed Python 3.12 executable.

Check that all command-line tools used by the exercises are available:

```bash
for tool in curl git grep patch sed uv; do
  command -v "$tool" >/dev/null || echo "Missing: $tool"
done
```

The command prints nothing when all required tools are available. Install any tools that are missing.

## Create the exercise workspace

Create one workspace in your home directory for Metis, the review targets, and generated reports. On WSL2, `$HOME` is inside the Linux filesystem:

```bash
mkdir -p "$HOME/metis-security-review/results"
cd "$HOME/metis-security-review"
```

## Clone and install Metis

Clone the Metis repository at the tested [2.0.0 release](https://github.com/arm/metis/releases/tag/metis-v2.0.0):

```bash
git clone --branch metis-v2.0.0 --depth 1 \
  https://github.com/arm/metis.git \
  "$HOME/metis-security-review/metis"

cd "$HOME/metis-security-review/metis"

uv sync --no-dev --python 3.12
source "$HOME/metis-security-review/metis/.venv/bin/activate"

command -v metis
metis --version
git rev-parse HEAD

cd "$HOME/metis-security-review"
```

`uv sync --no-dev --python 3.12` installs only the runtime dependencies needed to run the Metis CLI, using Python 3.12. It creates `metis/.venv` and installs Metis there. Activating the environment makes the `metis` command and the matching Python interpreter available in the current terminal.

The expected output from `metis --version` for this tag is:

```output
Metis 2.0.0
```

The `metis-v2.0.0` tag points to commit [`742b20d685b0aeb3216b36ddfc44bc5e05ace82c`](https://github.com/arm/metis/commit/742b20d685b0aeb3216b36ddfc44bc5e05ace82c). The output of `git rev-parse HEAD` should match this commit. Record the version and commit when comparing runs.

If you open a new terminal, return to the exercise workspace and reactivate the Metis environment before continuing:

```bash
cd "$HOME/metis-security-review"
source "$HOME/metis-security-review/metis/.venv/bin/activate"
command -v metis
```

The path printed by `command -v` should end with `metis-security-review/metis/.venv/bin/metis`. If it points elsewhere, open a new terminal or run `deactivate`, then run the activation command again.

## Configure the model provider

A model provider is the hosted service or local server that runs the language model Metis uses to review code. Hosted services typically require an API key, which authenticates your account and authorizes API usage. You also need access to a model and enough quota to run the reviews.

Follow the [Metis 2.0.0 provider setup instructions](https://github.com/arm/metis/blob/metis-v2.0.0/README.md#2-set-up-llm-provider), linked in the prerequisites, to configure your chosen provider. The provider guide explains which credentials, environment variables, and optional dependencies it needs. Make those credentials available in the same terminal that will run Metis. For a local provider, start its model server as described in the guide.

Keep credentials out of `.metis.md`, `metis-review.yaml`, shell history, source control, and report files.

Create a provider configuration outside the review targets. This example uses OpenAI and its public API base URL:

```bash
cat > "$HOME/metis-security-review/metis-review.yaml" <<'EOF'
llm_provider:
  name: openai
  model: gpt-6.1-sol
  base_url: https://api.openai.com/v1
EOF
```

The review commands load this file with `--config`. Adapt `llm_provider` to your provider's guide, including its `name`, available `model`, and any required connection settings. An OpenAI-compatible proxy uses `name: openai` with the API base URL supplied by its administrator and credentials issued for that service. It must support the OpenAI Responses API.

The captured runs used `gpt-6.1-sol` through an OpenAI-compatible proxy. Select a model available to your account or local server; model choice can change the findings.

## Confirm that the command starts

Display the command help before starting a model-backed review. Metis 2.0.0 runs its full workflow by default, including automated triage. The exercises use `--interactive` to run review-only commands; Metis initializes each target automatically.

```bash
metis --help
```

The help output should include `--codebase-path`, `--config`, `--interactive`, and `--output-file`. Repeat `--output-file` to request more than one format.

## Verify model access

Run a small review to check the configured provider before starting the exercises. This uses the same Metis commands for any configured provider and makes model calls that can consume API quota.

Create a tiny C file and start Metis with your provider configuration:

```bash
mkdir -p "$HOME/metis-security-review/provider-check"
printf 'int main(void) { return 0; }\n' > "$HOME/metis-security-review/provider-check/check.c"

metis \
  --interactive \
  --codebase-path "$HOME/metis-security-review/provider-check" \
  --config "$HOME/metis-security-review/metis-review.yaml"
```

At the Metis prompt, review the file, wait for the review to complete, then exit:

```console
review_file check.c
exit
```

Access is working when the review completes without provider errors and Metis prints a token-usage summary. Zero findings is a valid result for this test file.

If the check fails, use the error and your provider guide to check credentials, model access, API quota, and connection settings. For a local provider, also confirm that its server is running and the model is loaded. Resolve these errors before reviewing the larger examples.

## What you've accomplished and what's next

You installed the tested Metis 2.0.0 release and set it up with your model provider. Next, you will review a small C program and compare the report with defects that are intentionally present in its source.
