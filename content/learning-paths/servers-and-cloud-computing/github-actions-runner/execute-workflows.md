---
# User change
title: "Execute GitHub Actions workflows on Arm runners"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

After having installed RunsOn, you can start executing jobs on Arm-based runners by modifying your GitHub Actions workflow files.

For example, the following workflow will run on an Arm-based runner:

```yaml
name: CI

on: [push]

jobs:
  build:
    runs-on:
      - runs-on
      - runner=2cpu-linux-arm64
      - run-id=${{ github.run_id }}
    steps:
      - run: echo "Hello from arm!"
```
```

That's it! After ~30s, you should see the job running on an Arm-based runner from your AWS account where RunsOn is installed.

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

If you want to further customize the CPU count, RAM, disk sizes, etc., you can review the [job labels](https://runs-on.com/configuration/job-labels/) available.