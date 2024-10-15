---
# User change
title: "Execute GitHub Actions workflows on Arm runners"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

After installing RunsOn, you can execute jobs on Arm-based runners by modifying your GitHub Actions workflow files.

If you have existing GitHub Actions workflow files, you can simply change the `runs-on` setting.

For example, if you have a workflow file with:

```output
  runs-on: ubuntu-22.04
```

You can change the `runs-on` value as shown below to invoke a new runner in your AWS account.

```output
  runs-on:
    - runs-on
    - runner=1cpu-linux-arm64
    - run-id=${{ github.run_id }}
```

The runner is now an AWS EC2 Arm instance with 1 vCPU running Ubuntu 22.04.

That's it! After about 30 seconds, you should see the job running on an Arm-based runner from your AWS account.

### Specify other EC2 instance types

You can also select other instance types, such as Graviton3 or Graviton4, by using the `family` parameter:

```yaml
jobs:
  build:
    runs-on:
      - runs-on
      - runner=2cpu-linux-arm64
      - family=r8g # Graviton4
      - run-id=${{ github.run_id }}
```

You can learn more about the supported Linux runners in the [official documentation](https://runs-on.com/runners/linux/).

If you would like to further customize the CPU count, RAM, disk sizes, and more, you can review the [job labels](https://runs-on.com/configuration/job-labels/).

## A complete GitHub Actions example

If you don't have existing workflow files or want to try RunsOn by creating a new repository, you can run the commands below at a shell prompt. You will need Git (`git`) and the GitHub CLI (`gh`) installed. Refer to the [GitHub CLI installation instructions](https://cli.github.com/) if you don't have the `gh` command installed.

Create a new directory for the repository:

```console
mkdir actions-test ; cd actions-test
git init
mkdir -p .github/workflows
```

Use a text editor to save the workflow file below as a file named `test.yml` in the `.github/workflows/` directory:

```yaml
name: test

on: 
  push:
  workflow_dispatch:

jobs:  
  build:    
    runs-on:      
      - runs-on      
      - runner=1cpu-linux-arm64      
      - run-id=${{ github.run_id }}    
    steps:      
      - run: echo "Hello from your Arm runner!"

```

Add the workflow file to the repository, and commit the changes:

```console
git add .github/workflows/test.yml
git commit -m "initial commit for actions test"
```
Authorize GitHub so you can access your account from the command line:

```console
gh auth login
```

Use a browser or authentication token to authorize your GitHub account.

Create the repository:

```console
gh repo create actions-test --private --source=. --remote=origin
```

Save the project to GitHub:

```console
git push -u origin master
```

The `git push` command will trigger the GitHub Action to run. 

You can use a browser to view the Actions tab for the repository and see the job. 

You can also see the result from the command line:

```console
gh run list
```

Look at the output and find the ID. The output will be similar to:

```output
STATUS  TITLE                            WORKFLOW  BRANCH  EVENT  ID           ELAPSED  AGE                
✓       initial commit for actions test  test      master  push   10777854144  43s      about 6 minutes ago
```

Print the log for the run. Substitute your job ID for the example ID shown below.

```console
gh run view 10777854144 --log
```

You will see numerous details about the run, including architecture, instance name, region, instance type, and the name of the AMI (disk image).

You will also see that the instance is a spot instance (for lowest price).

```output
build	Set up job	2024-09-09T17:05:20.0155475Z Current runner version: '2.319.1'
build	Set up job	2024-09-09T17:05:20.0163810Z Runner name: 'runs-on--i-03421942a716b3f2a--vPaXOcNxGv'
build	Set up job	2024-09-09T17:05:20.0164922Z Runner group name: 'Default'
build	Set up job	2024-09-09T17:05:20.0165868Z Machine name: 'ip-10-1-44-45'
build	Set up job	2024-09-09T17:05:20.0187255Z ##[group]Runner Instance
build	Set up job	2024-09-09T17:05:20.0188268Z |       INFO        |                      VALUE                      |
build	Set up job	2024-09-09T17:05:20.0189375Z |-------------------|-------------------------------------------------|
build	Set up job	2024-09-09T17:05:20.0190247Z | SSH               | ssh runner@XX.XX.XXX.XX                         |
build	Set up job	2024-09-09T17:05:20.0191195Z | DefaultAdmins     | []                                              |
build	Set up job	2024-09-09T17:05:20.0194359Z | Region            | us-west-2                                       |
build	Set up job	2024-09-09T17:05:20.0195723Z | AvailabilityZone  | us-west-2c                                      |
build	Set up job	2024-09-09T17:05:20.0196761Z | Version           | v2.5.0                                          |
build	Set up job	2024-09-09T17:05:20.0197751Z | Runner            | runs-on--i-03421942a716b3f2a--vPaXOcNxGv        |
build	Set up job	2024-09-09T17:05:20.0198675Z | InstanceId        | i-03421942a716b3f2a                             |
build	Set up job	2024-09-09T17:05:20.0199804Z | InstanceType      | m7g.medium                                      |
build	Set up job	2024-09-09T17:05:20.0200853Z | InstanceLifecycle | spot                                            |
build	Set up job	2024-09-09T17:05:20.0201845Z | InstanceRAM       | 3810.47 MiB                                     |
build	Set up job	2024-09-09T17:05:20.0202929Z | InstanceCPU       | 1 cores                                         |
build	Set up job	2024-09-09T17:05:20.0203988Z | InstanceDisk1     | /=/dev/nvme0n1p1                                |
build	Set up job	2024-09-09T17:05:20.0204948Z |                   | Free=31.16GiB Used=7.41GiB                      |
build	Set up job	2024-09-09T17:05:20.0205963Z | ImageId           | ami-0657d9a6ae629cc71                           |
build	Set up job	2024-09-09T17:05:20.0207032Z | ImageName         | runs-on-v2.2-ubuntu22-full-arm64-20240907064532 |
build	Set up job	2024-09-09T17:05:20.0208066Z | Platform          | linux                                           |
build	Set up job	2024-09-09T17:05:20.0209048Z | Architecture      | arm64                                           |
build	Set up job	2024-09-09T17:05:20.0210029Z | Has preinstall    | false                                           |
build	Set up job	2024-09-09T17:05:20.0211070Z | PrivateIp         | 10.1.44.45                                      |
build	Set up job	2024-09-09T17:05:20.0212487Z | Debug             | false                                           |
build	Set up job	2024-09-09T17:05:20.0213565Z | BucketCacheName   | runs-on-s3bucketcache-wdz50kvdwgnk              |
build	Set up job	2024-09-09T17:05:20.0214516Z ##[endgroup]
build	Set up job	2024-09-09T17:05:20.0215051Z ##[group]Timings
build	Set up job	2024-09-09T17:05:20.0215788Z |         TIME         |         STEP         |  DIFF   | TOTAL  |
build	Set up job	2024-09-09T17:05:20.0216832Z |----------------------|----------------------|---------|--------|
build	Set up job	2024-09-09T17:05:20.0217838Z | 2024-09-09T17:04:45Z | workflow-job-created | 0ms     | 0.0s   |
build	Set up job	2024-09-09T17:05:20.0218934Z | 2024-09-09T17:04:48Z | webhook-received     | 3400ms  | 3.40s  |
build	Set up job	2024-09-09T17:05:20.0219949Z | 2024-09-09T17:04:48Z | instance-launched    | 26ms    | 3.43s  |
build	Set up job	2024-09-09T17:05:20.0221067Z | 2024-09-09T17:04:50Z | instance-pending     | 1572ms  | 5.00s  |
build	Set up job	2024-09-09T17:05:20.0222055Z | 2024-09-09T17:05:08Z | agent-booting        | 18683ms | 23.68s |
build	Set up job	2024-09-09T17:05:20.0223051Z | 2024-09-09T17:05:08Z | agent-metadata       | 21ms    | 23.70s |
build	Set up job	2024-09-09T17:05:20.0224084Z | 2024-09-09T17:05:08Z | agent-userdata       | 215ms   | 23.92s |
build	Set up job	2024-09-09T17:05:20.0225112Z | 2024-09-09T17:05:08Z | runner-env           | 37ms    | 23.96s |
build	Set up job	2024-09-09T17:05:20.0226129Z | 2024-09-09T17:05:08Z | runner-setup-hooks   | 0ms     | 23.96s |
build	Set up job	2024-09-09T17:05:20.0227166Z | 2024-09-09T17:05:10Z | runner-disk-setup    | 1091ms  | 25.05s |
build	Set up job	2024-09-09T17:05:20.0228160Z | 2024-09-09T17:05:10Z | runner-setup-agent   | 48ms    | 25.10s |
build	Set up job	2024-09-09T17:05:20.0229734Z | 2024-09-09T17:05:10Z | runner-chown-user    | 0ms     | 25.10s |
build	Set up job	2024-09-09T17:05:20.0230634Z ##[endgroup]
build	Set up job	2024-09-09T17:05:20.0248725Z Testing runner upgrade compatibility
build	Set up job	2024-09-09T17:05:20.6787659Z ##[group]GITHUB_TOKEN Permissions
build	Set up job	2024-09-09T17:05:20.6789958Z Contents: read
build	Set up job	2024-09-09T17:05:20.6790702Z Metadata: read
build	Set up job	2024-09-09T17:05:20.6791251Z Packages: read
build	Set up job	2024-09-09T17:05:20.6791826Z ##[endgroup]
build	Set up job	2024-09-09T17:05:20.6796044Z Secret source: Actions
build	Set up job	2024-09-09T17:05:20.6796849Z Prepare workflow directory
build	Set up job	2024-09-09T17:05:20.7586035Z Prepare all required actions
build	Set up job	2024-09-09T17:05:20.7901878Z Complete job name: build
build	Set up runner	2024-09-09T17:05:20.9495781Z A job started hook has been configured by the self-hosted runner administrator
build	Set up runner	2024-09-09T17:05:21.0909000Z ##[group]Run '/opt/runs-on/pre.sh'
build	Set up runner	2024-09-09T17:05:21.0944129Z shell: /usr/bin/bash --noprofile --norc -e -o pipefail {0}
build	Set up runner	2024-09-09T17:05:21.0944878Z ##[endgroup]
build	Run echo "Hello from your Arm runner!"	2024-09-09T17:05:21.1884436Z ##[group]Run echo "Hello from your Arm runner!"
build	Run echo "Hello from your Arm runner!"	2024-09-09T17:05:21.1885273Z echo "Hello from your Arm runner!"
build	Run echo "Hello from your Arm runner!"	2024-09-09T17:05:21.1914580Z shell: /usr/bin/bash -e {0}
build	Run echo "Hello from your Arm runner!"	2024-09-09T17:05:21.1915072Z env:
build	Run echo "Hello from your Arm runner!"	2024-09-09T17:05:21.1915428Z   RUNS_ON_AGENT_ARCH: arm64
build	Run echo "Hello from your Arm runner!"	2024-09-09T17:05:21.1916056Z   RUNS_ON_RUNNER_NAME: runs-on--i-03421942a716b3f2a--vPaXOcNxGv
build	Run echo "Hello from your Arm runner!"	2024-09-09T17:05:21.1916751Z   RUNS_ON_AGENT_USER: runner
build	Run echo "Hello from your Arm runner!"	2024-09-09T17:05:21.1917378Z   RUNS_ON_S3_BUCKET_CACHE: runs-on-s3bucketcache-wdz50kvdwgnk
build	Run echo "Hello from your Arm runner!"	2024-09-09T17:05:21.1918075Z   RUNS_ON_AWS_REGION: us-west-2
build	Run echo "Hello from your Arm runner!"	2024-09-09T17:05:21.1918665Z   ACTIONS_RUNNER_HOOK_JOB_STARTED: /opt/runs-on/pre.sh
build	Run echo "Hello from your Arm runner!"	2024-09-09T17:05:21.1919277Z ##[endgroup]
build	Run echo "Hello from your Arm runner!"	2024-09-09T17:05:21.2054907Z Hello from your Arm runner!
build	Complete job	2024-09-09T17:05:21.2297627Z Cleaning up orphan processes
```

You are now able to run GitHub Actions workflows on Graviton-based EC2 instances in your AWS account.
