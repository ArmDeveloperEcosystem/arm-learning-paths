---
# User change
title: "Summary"

weight: 9

layout: "learningpathall"
---
## Summary
In this Learning Path, you automated a CI/CD pipeline for an ASP.NET application using GitHub Actions. You began by setting up a self-hosted runner on an Arm64-powered machine to highlight the importance of this architecture for building and running applications specifically designed for Arm64 platforms. You then manually installed essential software on the self-hosted runner, including Docker and the .NET SDK. This ensures that the runner was equipped with all the necessary tools to build the .NET application and package it into a Docker container.

The runner was registered and configured within a GitHub repository to respond to specific events, such as push or pull requests to the main branch, enabling it to execute workflows defined in the GitHub Actions CI/CD pipeline. With the self-hosted runner prepared, you automated the build process of the .NET application to occur upon code changes. Following this build, a second job in the pipeline was tasked with building and pushing a Docker image of the application to Docker Hub, demonstrating the seamless integration of build and deployment processes.

Triggering the CI/CD pipeline was achieved by modifying the application's source code (index.cshtml) and committing these changes to the main branch, illustrating how code alterations can automatically initiate the build and deployment process via GitHub Actions. The successful completion of the pipeline updated the Docker image on Docker Hub, tagged as 'latest'. This image, incorporating the recent changes, is now ready for deployment in Arm64 architecture environments.

This workflow not only underscored the capabilities of GitHub Actions in automating CI/CD pipelines, but also showcased the setup and use of a self-hosted runner on Arm64 architecture, enhancing compatibility and performance for application development and deployment.