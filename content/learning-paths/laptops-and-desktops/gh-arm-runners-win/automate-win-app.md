---
title: Automate the Build of Windows Applications

weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
In this section, you will learn how to automate the build process of a Windows application using GitHub Arm-hosted runners. You will use the application in the [Optimize Windows applications using Arm Performance Libraries] Learning Path.

### Overview of the Windows Application

A basic overview of the application is provided here but for details on building the application refer to the [Optimize Windows applications using Arm Performance Libraries Learning Path](https://learn.arm.com/learning-paths/laptops-and-desktops/windows_armpl/2-multithreading/).

The source code for the application that renders a rotating 3D cube to perform the calculations using different programming options is provided in this GitHub repository. 

```console
https://github.com/odincodeshen/SpinTheCubeInGDI.git
```

The application implements a spinning cube and consists of four key components:
- **Shape Generation**: Generates vertices for a sphere using a golden ratio-based algorithm.
- **Rotation Calculation**: Uses a rotation matrix to rotate the 3D shape around the X, Y, and Z axes.
- **Drawing**: Draws the transformed vertices of the shapes on the screen using a Windows API.
- **Performance Measurement**: Measures and displays the number of transforms per second.

The code has two options to calculate the rotation:

1. Multithreading: the application utilizes multithreading to improve performance by distributing the rotation calculations across multiple threads.
2. Arm Performance Libraries: the application utilizes optimized math library functions for the rotation calculations.

You will learn how to automate the build process for this application by using GitHub Actions that leverages the Arm-hosted Windows runners.

### Automate the Build Process

This GitHub Actions workflow [`msbuild.yml`](https://github.com/odincodeshen/SpinTheCubeInGDI/blob/main/.github/workflows/msbuild.yml) that automates the build process for this project using MSBuild for Windows on Arm is included in this repository.

Below is an explanation of the steps in the workflow:

**Trigger Events**: The workflow runs when there is a push or pull_request event on the main branch.
**Job Definition**: A single job named build is defined. It runs on the GitHub Arm-hosted Windows runner (`windows-11-arm`) as shown:
```console
jobs:
  build:
    runs-on: windows-11-arm
```
**Checkout Repository**: Uses the `actions/checkout@v4` action to fetch the code.
**Add MSBuild to PATH**: Adds MSBuild tools for the build process using `microsoft/setup-msbuild@v1.0.2`.
**Restore Dependencies**: Runs `nuget restore` to restore NuGet packages required by the solution.
**Create Download Directory**: Creates a directory to store downloaded files and verifies the Python version.
**Download ARM Performance Libraries**: Downloads the Windows installer for ARM Performance Libraries (APL) and verifies the downloaded files.
**Install ARM Performance Libraries**: Installs the downloaded ARM Performance Libraries using `msiexec.exe` with a quiet mode and logs the process.
**Check Installation Success**: Verifies the success of the APL installation by checking the exit code and logs.
**Build the Solution**: Runs MSBuild to build the solution with the specified configuration (Debug) and platform (ARM64).
**Upload Build Artifact**: Uploads the built executable as an artifact using `actions/upload-artifact@v4`.

This workflow automates the process of dependency management, environment setup, building your Windows on Arm project, and storing the final artifact all using GitHub Arm-hosted runner.

