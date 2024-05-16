---
# User change
title: "Running CI/CD pipeline"

weight: 4

layout: "learningpathall"
---

## Objective
In this section you will run the CI/CD pipeline and verify that it deploys the Docker image to the Docker Hub repository

## CI/CD pipeline
The CI/CD pipeline is declared under the .github/workflows/asp-net-ci.cd.yml file. This YAML configuration defines a CI/CD pipeline for an ASP.NET project using GitHub Actions. It specifies actions to be triggered on push or pull request events to the main branch. This is indicated at the top of the YAML declaration:
```XML
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
```

The pipeline consists of two jobs: build and build-and-push-docker-image. Both jobs run on a self-hosted runner. Specifically, the build job is declared as follows:

```XML
jobs:
  build:
    runs-on: self-hosted

    steps:
    - uses: actions/checkout@v3

    - name: Setup .NET
      uses: actions/setup-dotnet@v1      
   
    - name: Build
      run: dotnet build -c Release
```

This job has three steps, which include:
1. Checking out the code using actions/checkout@v3.
2. Setting up .NET using actions/setup-dotnet@v1.
3. Building the project in Release configuration using the dotnet build -c Release command

Then, the YAML declares the build-and-push-docker-image job:
```XML
build-and-push-docker-image:
  needs: build
  runs-on: self-hosted
    
  steps:
  - uses: actions/checkout@v3
        
  - name: Set up Docker Buildx
    uses: docker/setup-buildx-action@v1
    
  - name: Login to DockerHub
    uses: docker/login-action@v1
    with:
      username: ${{ secrets.DOCKER_USERNAME }}
      password: ${{ secrets.DOCKER_PASSWORD }}
    
  - name: Build and push
    uses: docker/build-push-action@v2
    with:
      context: .
      file: ./Dockerfile
      push: true
      tags: ${{ secrets.DOCKER_USERNAME }}/sampleapp:latest
      platforms: linux/arm64
    
  - name: Logout of DockerHub
    run: docker logout
``` 

This job depends on the successful completion of the build job. This means that the build-and-push-docker-image will run after the build job. Again, the job uses self-hosted runner, and has the following steps:
1. Checking out the code again.
2. Setting up Docker Buildx using docker/setup-buildx-action@v1.
3. Logging in to DockerHub with credentials stored in GitHub secrets (DOCKER_USERNAME and DOCKER_PASSWORD).
4. Building and pushing the Docker image to DockerHub using docker/build-push-action@v2. The image is tagged as latest under the user's DockerHub account and is built for the linux/arm64 platform.
5. Logging out of DockerHub.

This pipeline automates the process of building the .NET application and packaging it into a Docker image, which is then pushed to DockerHub. It leverages GitHub secrets for secure authentication to DockerHub

## Running the pipeline
To run the above pipeline, we need to make modifications to the source code and commit these changes to the main branch. Follow the steps below to proceed:
1. Navigate to your GitHub repository, and open the Pages/index.cshtml file in edit mode by clicking the pencil icon in the top right corner.
2. Modify line 8 of this file to change the header text. Replace the existing line with the following code
```HTML
<h1 class="display-4">Hello, Arm Developers!</h1>
```

This change updates the page's main header to greet Arm developers specifically.

![img11](Figures/11.png)

3. Below the file editor, find and click the Commit changes button. This action opens the Commit changes window.

4. In the Commit changes window, you have the option to add a commit message describing your changes. After reviewing your message, click Commit changes to finalize the update:

![img12](Figures/12.png)

Committing these changes to the main branch will automatically trigger the CI/CD pipeline. You can monitor the progress of this pipeline under the Actions tab of your GitHub repository:

![img13](Figures/13.png)

Upon completion of the second job, which builds and pushes the Docker image, you can find the updated Docker image in your Docker Hub repository. The new image will be tagged as latest and will reflect the changes made to the index.cshtml file:

![img14](Figures/14.png)

This process demonstrates how code changes in your repository can seamlessly integrate with GitHub Actions to automate the build and deployment of your application, including updating Docker images in Docker Hub.

## Summary
In this learning path, we automated a CI/CD pipeline for an ASP.NET application using GitHub Actions. We began by setting up a self-hosted runner on an Arm64-powered machine to highlight the importance of this architecture for building and running applications specifically designed for Arm64 platforms. We then manually installed essential software on the self-hosted runner, including Docker and the .NET SDK. This ensured that the runner was equipped with all the necessary tools to build the .NET application and package it into a Docker container.

The runner was registered and configured within a GitHub repository to respond to specific events, such as push or pull requests to the main branch, enabling it to execute workflows defined in the GitHub Actions CI/CD pipeline. With the self-hosted runner prepared, we automated the build process of the .NET application to occur upon code changes. Following this build, a second job in the pipeline was tasked with building and pushing a Docker image of the application to Docker Hub, demonstrating the seamless integration of build and deployment processes.

Triggering the CI/CD pipeline was achieved by modifying the application's source code (index.cshtml) and committing these changes to the main branch, illustrating how code alterations can automatically initiate the build and deployment process via GitHub Actions. The successful completion of the pipeline updated the Docker image on Docker Hub, tagged as 'latest'. This image, incorporating the recent changes, is now ready for deployment in Arm64 architecture environments.

This workflow not only underscored the capabilities of GitHub Actions in automating CI/CD pipelines but also showcased the setup and use of a self-hosted runner on Arm64 architecture, enhancing compatibility and performance for application development and deployment.
