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

![GitLab new project creation screen showing options for blank project and templates alt-txt#center](_images/new-project.png "GitLab new project creation screen")

Provide a project name (for example, `arm-runner-demo`) and select your preferred project URL. Select **Create Project**:

![GitLab project information entry screen with fields for project name and URL alt-txt#center](_images/project-info.png "GitLab project information entry screen")

Your new project is ready:

![GitLab project creation success screen showing project dashboard alt-txt#center](_images/project-done.png "GitLab project creation success screen")

With your project created, you can now add application files and configure the CI/CD pipeline to use Arm64 runners.
