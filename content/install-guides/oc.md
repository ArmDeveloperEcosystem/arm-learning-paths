---
title: OpenShift CLI (oc)

draft: true

author: Jason Andrews

official_docs: https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/cli_tools/openshift-cli-oc#cli-getting-started
minutes_to_complete: 10

additional_search_terms:
- OpenShift
- Kubernetes

layout: installtoolsall
multi_install: false
multitool_install_part: false
test_images:
- ubuntu:latest
test_maintenance: false
tool_install: true
weight: 1
---

The OpenShift command-line interface (CLI), `oc`, allows you to work with OpenShift Container Platform projects from a terminal. You can use `oc` to create applications, manage OpenShift Container Platform projects, and perform administrative tasks.

The OpenShift CLI is a superset of the Kubernetes `kubectl` command. When you install `oc`, you get both the OpenShift-specific functionality and all standard Kubernetes `kubectl` commands in a single tool. This means you can use `oc` to manage both OpenShift and standard Kubernetes resources.

The OpenShift CLI is available for macOS and Linux and supports the Arm architecture.

## What should I consider before installing the OpenShift CLI?

This article provides a quick solution to install the latest version of the OpenShift CLI for Ubuntu on Arm and macOS with Apple Silicon.

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

## How do I download and install the OpenShift CLI?

There are multiple ways to install the OpenShift CLI. The methods below download the latest stable version directly from the OpenShift mirror.

### Install on Arm Linux

To install the OpenShift CLI on Arm Linux:

```bash { target="ubuntu:latest" }
curl -LO https://mirror.openshift.com/pub/openshift-v4/clients/ocp/stable/openshift-client-linux-arm64.tar.gz
tar -xzf openshift-client-linux-arm64.tar.gz
sudo mv oc kubectl /usr/local/bin/
rm openshift-client-linux-arm64.tar.gz README.md
```

### Install on macOS

To install the OpenShift CLI on macOS with Apple Silicon:

```console
curl -LO https://mirror.openshift.com/pub/openshift-v4/clients/ocp/stable/openshift-client-mac-arm64.tar.gz
tar -xzf openshift-client-mac-arm64.tar.gz
sudo mv oc kubectl /usr/local/bin/
rm openshift-client-mac-arm64.tar.gz README.md
```

Both installations include both `oc` and `kubectl` commands. The `oc` command provides the full OpenShift functionality, while the `kubectl` command gives you compatibility with standard Kubernetes clusters. Since `oc` is a superset of `kubectl`, you can use `oc` for all Kubernetes operations, but having both commands available gives you flexibility in your workflow.

## Understanding oc and kubectl

The OpenShift CLI (`oc`) is built as a superset of the Kubernetes CLI (`kubectl`). 

This means:

- You can use `oc` anywhere you would use `kubectl`
- OpenShift-specific features such as `oc login`, `oc new-project`, `oc new-app`, are available to manageme OpenShift resources

## How do I verify the OpenShift CLI installation?

Verify the OpenShift CLI is installed by checking the version:

```bash { target="ubuntu:latest" }
oc version --client
```

The output shows the client version information:

```output
Client Version: 4.19.3
Kustomize Version: v5.5.0
```

You can also verify that `kubectl` is available and shows the same version (since it's the same binary):

```bash { target="ubuntu:latest" }
kubectl version --client
```

The output shows the kubectl client version:

```output
Client Version: v1.32.1
Kustomize Version: v5.5.0
```

Both commands are now available for managing Kubernetes and OpenShift resources.

## How do I get started with the OpenShift CLI?

To get help with available commands, run:

```console
oc help
```

This displays the main command groups and options:

```output
OpenShift Client

This client helps you develop, build, deploy, and run your applications on any
OpenShift or Kubernetes cluster. It also includes the administrative
commands for managing a cluster under the 'adm' subcommand.

Usage:
  oc [flags]

Basic Commands:
  login           Log in to a server
  new-project     Request a new project
  new-app         Create a new application
  status          Show an overview of the current project
  project         Switch to another project
  projects        Display existing projects
  explain         Get documentation for a resource

Build and Deploy Commands:
  rollout         Manage the rollout of a resource
  rollback        Revert part of an application back to a previous deployment
  new-build       Create a new build configuration
  start-build     Start a new build
  cancel-build    Cancel running, pending, or new builds
  import-image    Import images from a Docker registry
  tag             Tag existing images into image streams

Application Management Commands:
  create          Create a resource from a file or from stdin
  apply           Apply a configuration to a resource by file name or stdin
  get             Display one or many resources
  describe        Show details of a specific resource or group of resources
  edit            Edit a resource on the server
  set             Commands that help set specific features on objects
  label           Update the labels on a resource
  annotate        Update the annotations on a resource
  expose          Expose a replicated application as a service or route
  delete          Delete resources by file names, stdin, resources and names, or by resources and label selector
  scale           Set a new size for a deployment, replica set, or replication controller
  autoscale       Autoscale a deployment or replica set
  secrets         Manage secrets
  serviceaccounts Manage service accounts in your project

Troubleshooting and Debugging Commands:
  logs            Print the logs for a resource
  rsh             Start a shell session in a pod
  rsync           Copy files between a local file system and a pod
  port-forward    Forward one or more local ports to a pod
  debug           Launch a new instance of a pod for debugging
  exec            Execute a command in a container
  proxy           Run a proxy to the Kubernetes API server
  attach          Attach to a running container
  run             Run a particular image on the cluster
  cp              Copy files and directories to and from containers
  wait            Experimental: Wait for a specific condition on one or many resources

Advanced Commands:
  adm             Tools for managing a cluster
  create          Create a resource from a file or from stdin
  replace         Replace a resource by file name or stdin
  patch           Update fields of a resource
  process         Process a template into list of resources
  export          Export resources so they can be used elsewhere
  extract         Extract secrets or config maps to disk
  observe         Observe changes to resources and react to them (experimental)
  policy          Manage authorization policy
  auth            Inspect authorization
  image           Useful commands for managing images
  registry        Commands for working with the registry
  idle            Idle scalable resources
  api-versions    Print the supported API versions on the server, in the form of "group/version"
  api-resources   Print the supported API resources on the server
  cluster-info    Display cluster information
  diff            Diff the live version against a would-be applied version
  kustomize       Build a kustomization target from a directory or URL

Settings Commands:
  logout          End the current server session
  config          Modify kubeconfig files
  whoami          Return information about the current session
  completion      Output shell completion code for the specified shell (bash, zsh, fish, or powershell)

Other Commands:
  help            Help about any command
  plugin          Provides utilities for interacting with plugins
  version         Print the client and server version information

Use "oc <command> --help" for more information about a given command.
Use "oc options" for a list of global command-line options (applies to all commands).
```

To connect to an OpenShift cluster, you need to log in using:

```console
oc login <cluster-url>
```

Replace `<cluster-url>` with your OpenShift cluster's URL. You will be prompted for your username and password.

You are now ready to use the OpenShift CLI to manage your OpenShift Container Platform projects and applications.
