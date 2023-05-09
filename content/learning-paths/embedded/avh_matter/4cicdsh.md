---
# User change
title: "Manage development in a CI/CD workflow with Self-Hosted Runner"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
In this section you will learn how to manage ongoing development in an automated CI/CD workflow, using [GitHub Actions](https://github.com/features/actions) and self-hosted runner.

In the `lighting-app` console, stop the app (`Ctrl+C`) if still running.

## Prepare repository for workflows

The Matter repository from where the examples are sourced contains very many workflows for rebuilding different configurations. For the convenience of time, let us remove these, and install only the new workflow.

In the `lighting-app` console, navigate to the `.github/workflows` directory, and delete all.
```console
cd ~/connectedhomeip/.github/workflows
rm -rf *.yaml
rm -rf *.yml
ls
```
Create a `.yml` textfile, and copy the below to that file.
```yml
name: Matter_CICD_Demo

on:
  push:
  workflow_dispatch:

jobs:
  rebuild_lighting_app:
    runs-on: self-hosted
    steps:
     - uses: actions/checkout@v2
     
     - name: submodules
       run: ./scripts/checkout_submodules.py --shallow --platform linux
       
     - name: bootstrap and build
       run: |
         ./scripts/build/gn_bootstrap.sh
         source scripts/activate.sh
         git clone https://github.com/project-chip/zap.git ./zap
         cd ./zap
         sudo src-script/install-packages-ubuntu
         npm ci
         export ZAP_DEVELOPMENT_PATH=$PWD
         cd ../examples/lighting-app/linux
         gn gen out/debug
         ninja -C out/debug
         
  run_lighting_app:
    needs: rebuild_lighting_app
    runs-on: self-hosted
    steps:
      - name: Run lighting-app for 3 minutes
        run: |
          cd examples/lighting-app/linux
          timeout 180s ./out/debug/chip-lighting-app || code=$?; if [[ $code -ne 124 && $code -ne 0 ]]; then exit $code; fi
```

## Create GitHub self-hosted runner

Browse to the forked Matter repository in your personal GitHub space.

Navigate to `Settings` > `Actions` > `Runners`, and then click on `New self-hosted runner`.

Configure for `Linux` host on `ARM64` Architecture (the `host` of the runner will be the `lighting-app` Virtual Raspberry Pi 4 instance).

You will see a set of commands (unique to you) to download and configure the `runner`.

In the `lighting-app` console, return to your home directory:
```console
cd ~
```
Copy and paste the `Download` and `Configure` commands (from GitHub) for your `self-hosted runner`.

It is OK to select the default options when prompted during configuration.

To keep the console available for later use, run the `self-hosted runner agent` as a background service (if started, first stop with `Ctrl+C`):
```console
sudo ./svc.sh install pi
sudo ./svc.sh start
sudo ./svc.sh status
```
In your GitHub repository, you will see your runner listed (`Settings` > `Actions` > `Runners`), with `Idle` status.

## Make a code change

In the `lighting-app` console, make a code change, for example, editing the output message when light is toggled.

This is in a source file named `on-off-server.cpp`.
```console 
cd ~/connectedhomeip
nano src/app/clusters/on-off-server/on-off-server.cpp
```
Locate the `Toggle on/off` message (if using `nano`, use `Ctrl+_` to jump to line `175`):
```C
    emberAfOnOffClusterPrintln("Toggle ep%x on/off from state %x to %x", endpoint, currentValue, newValue);
```
Edit to give a new output message, for example:
```C
    emberAfOnOffClusterPrintln("HELLO WORLD! Toggle ep%x on/off from state %x to %x", endpoint, currentValue, newValue);
```
Exit (`Ctrl+X`) and save your change.

## Push changes to GitHub repository and invoke workflow

The workflow contains the below, which tells GitHub to invoke this workflow whenever there is a `push` to the repository.
```yml
on:
  push:
```
To push the changes, in `lighting-app` console, first enter your GitHub credentials.
```console
git config --global user.name "YOUR_GITHUB_USERNAME"
git config --global user.email YOUR_EMAIL_ADDRESS
```
Ensure you are pushing these changes to your personal forked repository.
```console
git remote -v 
```
Commit the changes to your repository.
```console
cd ~/connectedhomeip
git add .
git commit -m "delete other workflows, update output message"
git push
```
You will be prompted for your GitHub username and `Personal Access Token` (password).

The workflow contains two `jobs`, which rebuild, and then run `lighting-app`:
```yml
jobs:
  rebuild_lighting_app:
...
  run_lighting_app:
```
Note that `rebuild_lighting_app` will take a few minutes to complete, as it must repeat all the initialization steps for the Matter build system.

## Follow the workflow progress in GitHub Actions

The workflow does not output on the target, but rather logs to GitHub.

You can follow the workflow steps, and see the output logs in your GitHub repository, under the `Actions` tab.

After `lighting-app` is initialized, you can toggle the light with your `chip-tool` instance as before:
```console
./out/debug/chip-tool onoff on 0x11 1
./out/debug/chip-tool onoff off 0x11 1
```
Observer your new message in the `run_lighting_app` log, for example:
```output
[TIMESTAMP][INSTANCEID] CHIP:ZCL: HELLO WORLD! Toggle ep1 on/off from state 1 to 0
```
The workflow will cleanly terminate `lighting-app` after 120 seconds.
