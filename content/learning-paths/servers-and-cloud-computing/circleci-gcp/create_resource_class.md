---
title: Create a resource class
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview
This section explains how to create a resource class in the CircleCI web dashboard for a self-hosted runner.

## What is a resource class? 

A resource class is a unique identifier that links your self-hosted runner to your CircleCI organization (namespace). It defines the *machine type* that CircleCI jobs can target, ensuring that only authorized jobs run on your managed infrastructure, which in this case is your SUSE Linux Arm64 VM on Google Cloud C4A (Axion).

## Create a resource class for a self-hosted Arm runner

To create a resource class for a self-hosted Arm runner in CircleCI, use the web dashboard and follow these steps:

- Go to the [CircleCI dashboard](https://app.circleci.com/home) and sign in, or create a new account if you don't have one.
- In the left navigation menu, select **Self-Hosted Runners**.
- If prompted, review and accept the Terms of Use by checking **Yes, I agree to the terms**. This enables runner functionality for your organization.
- After accepting, select **Self-Hosted Runners** again to continue setup.

{{% notice Note %}}
If you don't see the **Self-Hosted Runners** option, make sure your account has the required permissions or check that your organization is selected in the dashboard.
{{% /notice %}}


![CircleCI dashboard showing the Self-Hosted Runners section. The main panel displays options to add a new runner and manage existing ones. The left navigation menu highlights Self-Hosted Runners. The environment is a web interface with a neutral, professional tone. Visible text includes Self-Hosted Runners and related setup instructions. alt-text#center](images/shrunner0.png "Self-Hosted Runners")

## Create a new resource class

On the CircleCI dashboard, select **Create Resource Class**.

Enter the following information:

- **Namespace**: Enter your CircleCI organization or username, for example, `circleci`.
- **Resource Class Name**: Provide a clear, descriptive name for your runner, such as `arm64`.

After entering the details, select **Create Resource Class** to generate the resource class.

![CircleCI dashboard showing the Create Resource Class form. The main panel displays fields for Namespace and Resource Class Name, with labels and input boxes. A button labeled Create Resource Class appears below the form. The left navigation menu highlights Self-Hosted Runners. The environment is a clean, professional web interface designed for clarity and ease of use. Visible text includes Namespace, Resource Class Name, and Create Resource Class. The tone is neutral and instructional. alt-text#center](images/shrunner1.png "Create Resource Class")


![CircleCI dashboard displaying the details of a resource class and namespace. The main panel shows labeled fields for Namespace and Resource Class Name, each with input boxes containing example values. A button labeled Create Resource Class appears below the form. The left navigation menu highlights Self-Hosted Runners. The environment is a clean, professional web interface designed for clarity and accessibility. Visible text includes Namespace, Resource Class Name, and Create Resource Class. The tone is neutral and instructional. alt-text#center](images/shrunner2.png "Details Resource Class & Namespace")

## Save and copy the token

After creating the resource class, CircleCI automatically generates a Resource Class Token, a secure authentication key used to register your runner. Copy this token immediately and store it in a secure location. You’ll need this token in the next step to connect your SUSE Arm64 runner on the Google Cloud C4A (Axion) VM to CircleCI.

![CircleCI dashboard displaying the Resource Class Token section. The main panel shows a generated token in a text field labeled Resource Class Token with a Copy button next to it. Instructional text explains that this token is required to register a self-hosted runner. The environment is a clean, professional web interface with a focus on security and clarity. Visible text includes Resource Class Token and instructions to copy and store the token securely. The tone is neutral and informative. alt-text#center](images/shrunner3.png "Resource class token")

## What you've accomplished and what's next

Great job! You've successfully created a resource class and secured your token. You're making solid progress. Next, you'll set up the CircleCI self-hosted runner to connect your SUSE Arm64 VM on Google Cloud.
