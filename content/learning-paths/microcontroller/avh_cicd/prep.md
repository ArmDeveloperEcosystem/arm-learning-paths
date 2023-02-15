---
# User change
title: "Prepare GitHub repository for CI/CD development"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
You will learn how to prepare a GitHub repository to be used in a CI/CD development flow.

## Prerequisites

A valid [GitHub](https://github.com) account.

GitHub requires that a [Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) be set. If you do not have this on your account already, navigate to `Settings` > `Developer Settings` > `Personal Access Tokens`, click on `Generate new token`, and save the token locally.

A valid [AWS](https://aws.amazon.com/) account is required. Launch the Arm Virtual Hardware AMI. For full instructions see [here](/install-tools/avh#corstone).

## Fork (copy) the example repository

As we shall be making modifications to the reference example, you must make your own copy (`fork`) of the repository.

In a web browser, navigate to the repository at:
```console
https://github.com/ARM-software/AVH-TFLmicrospeech/fork
```
and create a fork in your own personal repository store (you must be logged into GitHub).

It is assumed below that you have used the same repository name (`AVH-TFLmicrospeech`) for your fork.

## Clone this repository

In your Arm Virtual Hardware terminal, clone the fork of the repository, and navigate into its directory.
```console
git clone https://github.com/<Your_GitHub_Username>/AVH-TFLmicrospeech
cd AVH-TFLmicrospeech/Platform_FVP_Corstone_SSE-300_Ethos-U55
```
## Build the example (optional)

If you wish to verify the project behaves as expected, rebuild the project:
```console
cbuild.sh --pack microspeech.Example.Reference.cprj
```
To run on the Virtual Hardware, use the provided script:
```console
./run_example.sh
```
Observe the output:
```
Heard yes (146) @1000ms
Heard no (145) @5600ms
...
```
## Modify the example

Edit `command_responder.cc` source file, which defines the output message.
```console
nano ../micro_speech/src/command_responder.cc
```
For example, change `Heard` to `The word was` in the `TF_LITE_REPORT_ERROR()` function.
```C
    TF_LITE_REPORT_ERROR(error_reporter, "The word was %s (%d) @%dms", found_command,
                         score, current_time);
```
## Rebuild and rerun
Rebuild and rerun the example.
```console
cbuild.sh microspeech.Example.cprj
./run_example.sh
```
Observe that the output has changed as expected.
```
The word was yes (146) @1000ms
The word was no (145) @5600ms
...
```
## Update the GitHub repository

Set your GitHub login details in your Virtual Hardware instance
```console
git config --global user.name "<GitHub_Username>"
git config --global user.email <Email>
```
Verify that the repository fork is referenced:
```console
git remote -v
```
Commit and push changed file(s) to the repository:
```console
git add ../micro_speech/src/command_responder.cc
git commit -m "changed output message"
git push
```
You will be prompted for your GitHub username and Personal Access Token (password).

Refresh your browser and observe that your fork of the repository has been updated appropriately.
