---
title: Set up a GitHub Self-Hosted Runner
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

This section showsyou how to deploy a GitHub Actions self-hosted runner on your Arm64 Google Axion C4A instance. You will install Git and GitHub CLI, authenticate with GitHub, and register the runner so CI/CD workflows run on Arm infrastructure.

## Set up your development environment

Start by installing the required dependencies using the `apt` package manager:

```console
sudo apt update
sudo apt install -y git gh vim
```

Configure your Git identity:

```bash
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

Now you are ready to connect the machine to GitHub. The command below is used to authenticate the GitHub CLI with your GitHub account. It allows you to securely log in using a web browser or token, enabling the CLI to interact with repositories, actions, and other GitHub features on your behalf.

Authenticate with GitHub:

```console
gh auth login
```

Follow the prompts and accept the defaults.

![Login to GitHub alt-text#center](./images/gh-auth.png "Screenshot of GitHub authentication prompt")

{{% notice %}}
If you get an error opening the browser on your virtual machine, you can navigate to the following URL on the host machine and enter the device code displayed in the CLI of the virtual machine: 
```
https://github.com/login/device
```
{{% /notice %}}

When authentication succeeds, you will see a confirmation screen in your browser:

![GitHub UIalt-text#center](./images/login-page.png "Screenshot of successful GitHub login confirmation")

## Test GitHub CLI and Git

The command below creates a new public GitHub repository named **test-repo** using the GitHub CLI. It sets the repository visibility to public, meaning that anyone can view it:

```console
gh repo create test-repo --public
```
You should see an output similar to:
```output
✓ Created repository <your-github-account>/test-repo on GitHub
  https://github.com/<your-github-account>/test-repo
  ```


  ## Configure the self-hosted runner

  In your repository, go to **Settings** → **Actions** → **Runners** and select **Add runner**, or view existing self-hosted runners.

  {{% notice Note %}}
  If the **Actions** tab is not visible, enable Actions under **Settings** → **Actions** → **General** by selecting **Allow all actions and reusable workflows**.
  {{% /notice %}}

  ![runner](./images/newsh-runner.png)

  Then, click on the **New self-hosted runner** button. In the **Add new self-hosted runner** section. Select Linux for the operating system, and choose ARM64 for the architecture. This will generate commands to set up the runner. Copy and run them on your Google Axion C4A virtual machine.

  ![new-runner](./images/new-runner.png)

  The final command links the runner to your GitHub repo using a one-time registration token.

  During the command’s execution, you will be prompted to provide the runner group, the name of the runner, and the work folder name. You can accept the defaults by pressing **Enter** at each step. The output will resemble as below:

  ```output
  --------------------------------------------------------------------------------
  |        ____ _ _   _   _       _          _        _   _                      |
  |       / ___(_) |_| | | |_   _| |__      / \   ___| |_(_) ___  _ __  ___      |
  |      | |  _| | __| |_| | | | | '_ \    / _ \ / __| __| |/ _ \| '_ \/ __|     |
  |      | |_| | | |_|  _  | |_| | |_) |  / ___ \ (__| |_| | (_) | | | \__ \     |
  |       \____|_|\__|_| |_|\__,_|_.__/  /_/   \_\___|\__|_|\___/|_| |_|___/     |
  |                                                                              |
  |                       Self-hosted runner registration                        |
  |                                                                              |
  --------------------------------------------------------------------------------

  # Authentication

  √ Connected to GitHub
  # Runner Registration
  Enter the name of the runner group to add this runner to: [press Enter for Default]
  Enter the name of runner: [press Enter for lpprojectubuntuarm64]
  This runner will have the following labels: 'self-hosted', 'Linux', 'ARM64'
  Enter any additional labels (ex. label-1,label-2): [press Enter to skip]
  √ Runner successfully added
  √ Runner connection is good
  ```

  Finally, start the runner by executing:
  ```console
  ./run.sh
  ```
  You should see an output similar to:

  ```output
  √ Connected to GitHub

  Current runner version: '2.326.0'
  2025-07-15 05:51:13Z: Listening for Jobs
  ```
  The runner will now be visible in the GitHub actions:

  ![final-runner](./images/final-runner.png)

  For now, you can terminate the `./run.sh` command with `Ctrl+C`. Move on to the next section to set up a simple web server using the runner.
](./images/gh-auth.png)

{{% notice %}}
If you get an error opening the browser on your virtual machine, you can navigate to the following URL on the host machine.
```
https://github.com/login/device
```
From there, you can enter the code displayed in the CLI of the virtual machine.
{{% /notice %}}

If the log in was successful, you will see the following confirmation in your browser window.

![GitHub UI](./images/login-page.png)

### Test GitHub CLI and Git

The command below creates a new public GitHub repository named **test-repo** using the GitHub CLI. It sets the repository visibility to public, meaning anyone can view it

```console
gh repo create test-repo --public
```
You should see an output similar to:
```output
✓ Created repository <your-github-account>/test-repo on GitHub
  https://github.com/<your-github-account>/test-repo
  ```


  ### Configure the Self-Hosted Runner

  * Go to your repository's **Settings > Actions**, and under the **Runners** section
  * Click on **Add Runner** or view existing self-hosted runners.

  {{% notice Note %}}
  If the **Actions** tab is not visible, ensure Actions are enabled by navigating to **Settings > Actions > General**, and select **Allow all actions and reusable workflows**.
  {{% /notice %}}

  ![runner](./images/newsh-runner.png)

  Then, click on the **New self-hosted runner** button. In the **Add new self-hosted runner** section. Select Linux for the operating system, and choose ARM64 for the architecture. This will generate commands to set up the runner. Copy and run them on your Google Axion C4A virtual machine.

  ![new-runner](./images/new-runner.png)

  The final command links the runner to your GitHub repo using a one-time registration token.

  During the command’s execution, you will be prompted to provide the runner group, the name of the runner, and the work folder name. You can accept the defaults by pressing **Enter** at each step. The output will resemble as below:

  ```output
  --------------------------------------------------------------------------------
  |        ____ _ _   _   _       _          _        _   _                      |
  |       / ___(_) |_| | | |_   _| |__      / \   ___| |_(_) ___  _ __  ___      |
  |      | |  _| | __| |_| | | | | '_ \    / _ \ / __| __| |/ _ \| '_ \/ __|     |
  |      | |_| | | |_|  _  | |_| | |_) |  / ___ \ (__| |_| | (_) | | | \__ \     |
  |       \____|_|\__|_| |_|\__,_|_.__/  /_/   \_\___|\__|_|\___/|_| |_|___/     |
  |                                                                              |
  |                       Self-hosted runner registration                        |
  |                                                                              |
  --------------------------------------------------------------------------------

  # Authentication

  √ Connected to GitHub
  # Runner Registration
  Enter the name of the runner group to add this runner to: [press Enter for Default]
  Enter the name of runner: [press Enter for lpprojectubuntuarm64]
  This runner will have the following labels: 'self-hosted', 'Linux', 'ARM64'
  Enter any additional labels (ex. label-1,label-2): [press Enter to skip]
  √ Runner successfully added
  √ Runner connection is good
  ```

  Finally, start the runner by executing:
  ```console
  ./run.sh
  ```
  You should see an output similar to:

  ```output
  √ Connected to GitHub

  Current runner version: '2.326.0'
  2025-07-15 05:51:13Z: Listening for Jobs
  ```
  The runner will now be visible in the GitHub actions:

  ![final-runner](./images/final-runner.png)

  For now, you can terminate the `./run.sh` command with `Ctrl+C`. Move on to the next section to set up a simple web server using the runner.
