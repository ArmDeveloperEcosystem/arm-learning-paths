---
title: Create Resource Class in CircleCI
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a resource class for a self-hosted runner in CircleCI
This section explains how to create a resource class in the CircleCI web dashboard for a self-hosted runner.

A resource class is a unique identifier that links your self-hosted runner to your CircleCI organization (namespace). It defines the *machine type* that CircleCI jobs can target, ensuring that only authorized jobs run on your managed infrastructure, which in this case is your SUSE Linux Arm64 VM on Google Cloud C4A (Axion).

### Steps

1. Open the CircleCI Web Dashboard
   - Login or Create a new account at [CircleCI](https://app.circleci.com/home)
   - In the left-hand navigation panel, click Self-Hosted Runners.
   - If this is your first time setting up runners, you’ll be prompted to accept the Terms of Use.
     Check “Yes, I agree to the terms” to enable runner functionality for your organization.
   - After accepting, click Self-Hosted Runners again to continue the setup process.

![CircleCI dashboard showing the Self-Hosted Runners section. The main panel displays options to add a new runner and manage existing ones. The left navigation menu highlights Self-Hosted Runners. The environment is a web interface with a neutral, professional tone. Visible text includes Self-Hosted Runners and related setup instructions. alt-text#center](images/shrunner0.png "Self-Hosted Runners")

## Create a New Resource Class

On your CircleCI Dashboard, click Create Resource Class.

Fill in the following details:

  * Namespace: Your CircleCI organization or username (e.g., circleci)
  * Resource Class Name: A clear, descriptive identifier for your runner (e.g., arm64)
  * Once complete, click Create Resource Class to generate it.

![Self-Hosted Runners alt-text#center](images/shrunner1.png "Figure 2: Create Resource Class ")

![Self-Hosted Runners alt-text#center](images/shrunner2.png "Figure 3: Details Resource Class & Namespace")

3. Save and Copy the Token

 After creating the resource class, CircleCI automatically generates a Resource Class Token, a secure authentication key used to register your runner. Copy this token immediately and store it in a secure location.
You’ll need this token in the next step to connect your SUSE Arm64 runner on the Google Cloud C4A (Axion) VM to CircleCI.

![Self-Hosted Runners alt-text#center](images/shrunner3.png "Figure 4: Resource Class Token")
   
Now that your resource class and token are generated, proceed to the next section to set up the CircleCI self-hosted runner.
