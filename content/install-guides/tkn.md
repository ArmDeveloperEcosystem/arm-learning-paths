---
title: Tekton CLI (tkn)

author: Jason Andrews
official_docs: https://tekton.dev/docs/cli/

minutes_to_complete: 10
additional_search_terms:
- tekton
- pipelines
- ci/cd
- kubernetes
- openshift
- devops

layout: installtoolsall
multi_install: false
multitool_install_part: false
test_images:
- ubuntu:latest
test_maintenance: false
tool_install: true
weight: 1
---

The Tekton CLI, `tkn`, is a command-line interface for Tekton Pipelines. It allows you to create, manage, and interact with Tekton resources such as tasks, pipelines, and pipeline runs from your terminal.

Tekton CLI is available for macOS and Linux and supports the Arm architecture.

## What should I consider before installing the Tekton CLI?

This article provides a quick way to install the latest version of the Tekton CLI for Ubuntu on Arm and macOS with Apple Silicon.

Confirm you are using an Arm computer by running:

```bash { target="ubuntu:latest" }
uname -m
```

If you are on Arm Linux the output should be:

```output
aarch64
```

If you are on macOS with Apple Silicon the output should be:

```output
arm64
```

## How do I download and install the Tekton CLI?

You can install the Tekton CLI in multiple ways. The following methods download the latest stable release directly from GitHub.

### Install on Arm Linux

To install the Tekton CLI on Arm Linux:

```bash { target="ubuntu:latest" }
TKN_VERSION=$(curl -s https://api.github.com/repos/tektoncd/cli/releases/latest | grep tag_name | cut -d '"' -f 4)
curl -LO https://github.com/tektoncd/cli/releases/download/${TKN_VERSION}/tektoncd-cli-${TKN_VERSION#v}_Linux-ARM64.deb
sudo apt install ./tektoncd-cli-${TKN_VERSION#v}_Linux-ARM64.deb
```

{{% notice Tip %}}
If the version query fails, you can manually set `TKN_VERSION` to a known stable version like `v0.41.0`.
{{% /notice %}}

### Install on macOS

To install the Tekton CLI on macOS with Apple Silicon:

```console
TKN_VERSION=$(curl -s https://api.github.com/repos/tektoncd/cli/releases/latest | grep tag_name | cut -d '"' -f 4)
curl -LO https://github.com/tektoncd/cli/releases/download/${TKN_VERSION}/tkn_${TKN_VERSION#v}_Darwin_all.tar.gz
tar -xzf tkn_${TKN_VERSION#v}_Darwin_all.tar.gz
sudo mv tkn /usr/local/bin/
rm tkn_${TKN_VERSION#v}_Darwin_all.tar.gz README.md LICENSE
```

Alternatively, you can install using Homebrew on macOS:

```console
brew install tektoncd-cli
```

## How do I verify the Tekton CLI installation?

Verify the Tekton CLI is installed by checking the version:

```bash { target="ubuntu:latest" }
tkn version
```

The output shows the client version information:

```output
Client version: 0.41.0
```

You can also check that the command is working by displaying the help:

```bash { target="ubuntu:latest" }
tkn help
```

This displays the main command groups and options:

```output
CLI for tekton pipelines

Usage:
  tkn [flags]
  tkn [command]

Available Commands:
  bundle              Manage Tekton Bundles
  chain               Manage Chains
  clustertask         Manage ClusterTasks
  clustertriggerbinding Manage ClusterTriggerBindings
  completion          Prints shell completion scripts
  eventlistener       Manage EventListeners
  help                Help about any command
  hub                 Interact with tekton hub
  pipeline            Manage pipelines
  pipelinerun         Manage pipeline runs
  resource            Manage pipeline resources
  task                Manage Tasks
  taskrun             Manage TaskRuns
  triggerbinding      Manage TriggerBindings
  triggertemplate     Manage TriggerTemplates
  version             Prints version information

Flags:
  -h, --help   help for tkn

Use "tkn [command] --help" for more information about a command.
```

## How do I get started with the Tekton CLI?

To use the Tekton CLI effectively, you need access to a Kubernetes cluster with Tekton Pipelines installed. You can check if Tekton is available in your cluster:

```console
tkn pipeline list
```

If Tekton Pipelines is not installed, you might see an error message. In that case, you need to install Tekton Pipelines on your cluster first.

### Common Tekton CLI commands

Below are some common commands to get you started.

List pipelines:

```console
tkn pipeline list
```

List pipeline runs:

```console
tkn pipelinerun list
```

List tasks:

```console
tkn task list
```

List task runs:

```console
tkn taskrun list
```

Start a pipeline:

```console
tkn pipeline start <pipeline-name>
```

Show pipeline run logs:

```console
tkn pipelinerun logs <pipelinerun-name>
```

Describe a pipeline:

```console
tkn pipeline describe <pipeline-name>
```

You are now ready to use the Tekton CLI to manage your CI/CD pipelines with Tekton Pipelines on Kubernetes or OpenShift.
