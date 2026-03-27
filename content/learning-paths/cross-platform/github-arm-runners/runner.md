---
title: "Create a new Arm-hosted runner for private repositories"

weight: 4

layout: "learningpathall"
---

## Can I use Arm-hosted runners for private repositories?

Yes, you can use Arm-hosted runners in private repositories.

You must have a Team or Enterprise Cloud plan to use Arm-hosted runners.

Two types of GitHub-hosted runners are available; standard runners, and larger runners. Larger runners are differentiated from standard runners because users can control the amount of RAM, the number of CPUs, and configure the allocated disk space. Larger runners have additional options for a static IP address and the ability to group runners and control settings across the runner group. Currently, Arm-hosted runners are a type of larger runner.

## How can I create an Arm-hosted runner?

Arm-hosted runners are created at the organization level.

Navigate to your organization and select the `Settings` tab. On the left pane, select `Actions->Runners`.

On the `Runners` page, select the `New runner` drop-down on the top right, and then select `New GitHub-hosted runner`.

![Screenshot of GitHub organization Settings showing the Runners page with a New runner dropdown menu expanded, highlighting the New GitHub-hosted runner option which initiates the Arm-hosted runner creation workflow#center](_images/new-runner.png "GitHub runner creation dropdown menu")


Specify a name for the runner, this is the `runs-on` field in your workflows so make the name clear for others who use it.

Choose Linux ARM64 for the platform and click `Save`.

![Screenshot showing GitHub-hosted runner platform selection with Linux ARM64 option selected, which configures the runner to use Arm architecture instead of x86 for workflow jobs#center](_images/platform.png "Platform selection for Arm-hosted runner")

Specify the operating system image for the runner, select `Ubuntu 22.04 by Arm Limited`, and click `Save`.

![Screenshot of runner image selection showing Ubuntu 22.04 by Arm Limited option, which determines the base operating system and software environment available to GitHub Actions workflows on the Arm-hosted runner#center](_images/image.png "Operating system image selection for runner")

Select the size of the runner, choose the 2-core option for this Learning Path, and click `Save`.

![Screenshot showing runner specifications with size options including 2-core, 4-core, and larger configurations, allowing selection of CPU and memory resources allocated to the Arm-hosted runner for workflow execution#center](_images/specifications.png "Runner size and resource specifications")

The `Capacity` section includes the maximum concurrency, which is the number of jobs to run at the same time. Specify at least two for this Learning Path.

You can also set the runner group for this runner. The runner group controls the settings for this runner. Pay attention to the runner group as you may need to return to the runner group settings if any configuration changes are needed.

![Screenshot of runner capacity configuration showing maximum concurrency settings, which determines how many workflow jobs can execute simultaneously on this Arm-hosted runner, and runner group assignment options#center](_images/capacity.png "Runner capacity and concurrency settings")

Finally, click `Create runner`.

Your new Arm-hosted runner is now ready to use. Remember the runner name for use in the next section: `ubuntu-22.04-arm`. 
