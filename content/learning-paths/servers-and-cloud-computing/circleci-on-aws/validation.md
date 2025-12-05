---
title: Verify CircleCI Arm64 Self-Hosted runner
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Verify CircleCI Arm64 Self-Hosted Runner

This section walks you through validating your self-hosted CircleCI runner on an Arm64 machine by executing a simple workflow and a test computation. This ensures your runner is correctly configured and ready to process jobs.

## Create a test repository
Start by creating a GitHub repository dedicated to verifying your Arm64 runner:

```console
git clone https://github.com/<your_repo_name/aws-circleci/
cd aws-circleci
```
This repository serves as a sandbox to confirm that your CircleCI runner can pick up and run jobs for Arm64 workflows.

## Add a sample script
Create a minimal shell script to confirm your runner can execute commands:

```bash
echo 'echo "Hello from CircleCI Arm64 Runner!"' > hello.sh
chmod +x hello.sh
```

This script prints a message when run, helping you verify that your self-hosted runner is working as expected.

```console
echo 'echo "Hello from CircleCI Arm64 Runner!"' > hello.sh
chmod +x hello.sh
```

## Define the CircleCI configuration
Now create a `.circleci/config.yml` file to define the workflow that runs on your Arm64 runner:

```yaml
version: 2.1

jobs:
  test-Arm64:
    machine:
      enabled: true
    resource_class: your-namespace/Arm64-linux   # Replace with your actual resource class
    steps:
      - checkout
      - run:
          name: Verify Arm64 Runner
          command: |
            uname -m
            lscpu | grep Architecture
            ./hello.sh
      - run:
          name: Run sample computation
          command: |
            echo "Performing test on Arm64 runner"
            echo "CPU Info:" 
            lscpu
            echo "Success!"

workflows:
  test-workflow:
    jobs:
      - test-Arm64
```
This configuration does the following:

- Defines a single job called `test-Arm64` that uses a machine executor on your self-hosted Arm64 runner
- Verifies the runner's architecture by running `uname -m` and checking the output of `lscpu`
- Runs the `hello.sh` script to confirm the runner can execute commands
- Performs a sample computation step that displays CPU information and prints a success message

Each step helps you confirm that your CircleCI Arm64 runner is set up correctly and ready to process jobs.

## Commit and push to GitHub
After you create `hello.sh` and `.circleci/config.yml`, push your project to GitHub so CircleCI can build and verify your Arm64 runner:

```console
git add .
git commit -m "Initial CircleCI Arm64 test"
git branch -M main
git push -u origin main
```

Here's what each command does:
- git add . — stages all your files for commit
- git commit -m ... — saves your changes with a message
- git branch -M main — sets your branch to main (if it's not already)
- git push -u origin main — pushes your code to GitHub

Once your code is on GitHub, CircleCI can start running your workflow automatically.
## Start the CircleCI runner and run your job

Before you test your workflow, make sure your CircleCI runner is enabled and running. This lets your self-hosted runner pick up jobs from CircleCI:

```console
sudo systemctl enable circleci-runner
sudo systemctl start circleci-runner
sudo systemctl status circleci-runner
```
- Enable the runner so it starts automatically when your machine boots
- Start the runner and check its status to confirm it is running

After you push your code to GitHub, go to your CircleCI Dashboard and select Projects. Look for your test-Arm64 workflow and check that it is running on your self-hosted runner.

If everything is set up correctly, you’ll see your job running under the resource class you created.

## Output
Once the job starts running, CircleCI does the following:

- It verifies the Arm64 Runner:

  ![CircleCI self-hosted runner dashboard showing a successful Arm64 job execution. The main panel displays job status as successful with green check marks. The sidebar lists workflow steps including checkout, verify Arm64 runner, and run sample computation. The environment is a web interface with a clean, professional layout. The overall tone is positive and confirms successful validation of the self-hosted runner. alt-text#center](images/runnerv1.png "Self-Hosted Runners ")
  
- It runs a sample computation:

  ![CircleCI dashboard displaying the results of a sample computation job on a self-hosted Arm64 runner. The main panel shows the job status as successful with green check marks. Workflow steps listed in the sidebar include checkout, verify Arm64 runner, and run sample computation. The environment is a modern web interface with a clean, organized layout. On-screen text includes Success and CPU Info. The overall tone is positive, confirming the successful execution of the computation step on the Arm64 runner. alt-text#center](images/computation.png "Self-Hosted Runners ")

All CircleCI jobs have run successfully, the sample computation completed, and all outputs are visible in the CircleCI Dashboard.
