---
# User change
title: "Self-hosted runner"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
In this section you will learn how to integrate Arm Virtual Hardware into a CI/CD development flow, and automate with GitHub Actions.

## Enable GitHub Actions

Open your browser, and navigate to your fork of the example repository.

Navigate to `Actions`. If prompted that `workflows` have been disabled, click the `I understand my workflows, go ahead and enable them` button.

## Create a Self-hosted Runner

Navigate to the repository `Settings` > `Actions` > `Runners`, and click on `New self-hosted runner`.

Set `Runner image` as `Linux`, and `Architecture` as `x64` (matching the AWS instance). A set of commands will be displayed to run to prepare the runner. These commands will be unique for your account and repository.

Create a Virtual Hardware terminal copy and paste these commands to launch the runner. When configuring, you can select the default options when prompted.

The runner will report that it is `Listening for Jobs`.

In your browser, if you return to `Settings` > `Actions` > `Runners`, you will see the runner exists, and is `Idle`.

## Modify the example sources

Return to the original terminal, and edit `command_responder.cc` source file for a different output message (e.g `The runner heard`).
```console
nano ../micro_speech/src/command_responder.cc
```
We will not rebuild and re-run at this step.

## Update the GitHub repository

Commit and push changed file(s) to the repository
```
git add ../micro_speech/src/command_responder.cc
git commit -m "another output message"
git push
```
You will be prompted for your GitHub username and Personal Access Token.

Refresh your browser and observe that your copy of the repository has been updated appropriately.

## Runner starts automatically

In the AVH runner terminal, you will see that it reports `Running job: ci_demonstration` (and eventually `Job ci_demonstration completed with result: Succeeded`).

In the browser, navigate to `Actions`, and observe that the `virtual_hardware_sh.yml` workflow has started (and eventually completes). Click on `ci_demonstration` to see the progress of the run, and a complete log of all outputs.

Under the `Run the microspeech example` step, you will find the output:
```output
The runner heard yes (146) @1000ms
The runner heard no (145) @5600ms
...
```
Workflows are defined in the `.github/workflows` folder of the repository. See the GitHub Actions [documentation](https://docs.github.com/en/actions) for more information.

Full instructions and further examples are given in the Arm Virtual Hardware [documentation](https://arm-software.github.io/AVH/main/examples/html/GetStarted.html).
