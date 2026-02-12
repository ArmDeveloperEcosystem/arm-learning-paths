---
title: Create a GitLab project
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Before you begin, log in to your [GitLab account](https://gitlab.com/) or create a new one.

You need a GitLab project to store your application code and CI/CD configuration. You can either create a new project or use an existing one.

{{% notice Note %}}
If you're using an existing project, skip to the next section.
{{% /notice %}}

## Create a new project

Navigate to **Projects** in the left sidebar and select **New Project**:

![Gitlab-Projects #center](_images/gitlab-projects.png)

Choose **Create blank project** or **Create from template** (select **GitLab CI/CD components** if using a template):

![New-Project #center](_images/new-project.png)

Provide a project name (for example, `arm-runner-demo`) and select your preferred project URL. Select **Create Project**:

![Project-Info #center](_images/project-info.png)

Your new project is ready:

![Project-Done #center](_images/project-done.png)

With your project created, you can now add application files and configure the CI/CD pipeline to use Arm64 runners.
