---
title: "Deploy with Copilot"
weight: 3

layout: "learningpathall"
---

# Deploy the application with Copilot

You can deploy the application with a single command:

```console
copilot init --app go-arch               \
  --name api                             \
  --type 'Load Balanced Web Service'     \
  --dockerfile './Dockerfile'            \
  --env test                             \
  --port 8080                            \
  --deploy
```

The default architecture is `amd64`. The `copilot` command builds the container on your local machine for `amd64`, pushes it to the container registry (Amazon ECR), and creates everything needed to run the application on AWS Fargate. 

You can also specify an existing container image using `--image` instead of `--dockerfile`. Make sure the image is a multi-architecture image supporting both `arm64` and `amd64`.

While you are waiting for the command to complete you can look in your AWS account and see the resources created in AWS S3, CloudFormation, and ECS.

When the `copilot` command completes, the URL of the load balancer is printed.

Visit the URL in your browser and see the printed message.

To access the application from the command line, run `curl` with the URL (your URL will be different). 

For example:

```console
curl -w '\n' http://go-arc-Publi-UvaFr7DQF5ud-988490958.us-west-2.elb.amazonaws.com
```

The output is:

```output
Hello from CPU PLATFORM:linux/amd64
```

You can also check running status using:

```console
copilot svc status
```

The output is similar to:

```output
Found only one deployed service api in environment test
Task Summary

  Running   ██████████  1/1 desired tasks are running
  Health    ██████████  1/1 passes HTTP health checks
            ██████████  1/1 passes container health checks

Tasks

  ID        Status      Revision    Started At     Cont. Health  HTTP Health
  --        ------      --------    ----------     ------------  -----------
  7779652d  RUNNING     1           7 minutes ago  HEALTHY       HEALTHY
```

# Migrate to Graviton

To move from `amd64` to `arm64` edit the file `copilot/api/manifest.yml` and change the `platform` entry from `linux/x86_64` to `linux/arm64`.

If you don't have a `platform` entry, add one after the existing entries. Either way, you should have this line in your `manifest.yml` file:

```yaml
platform: linux/arm64
```

You are now ready to run on Graviton2.

Save the file and redeploy the application using:

```console
copilot svc deploy 
```

Copilot rebuilds the container image for the `arm64` architecture, pushes the image to the container registry and deploys the new image.

If you look in your AWS console and visit the task configuration in ECS, you will see the task now shows `ARM64` as the architecture.

Visit the URL again using a browser or the same `curl` command and the message prints `arm64`.

```output
Hello from CPU PLATFORM:linux/arm64
```

# Open a shell in the container

If you need to troubleshoot a container, you can use Copilot to connect.

```console
copilot svc exec
```

Answer yes to install the Session Manager plugin, and you have a shell into the running container. 

```output
Starting session with SessionId: ecs-execute-command-0f1f212e5ff00ec05
/ # 
```

You can make changes to the container and do any needed investigation. Copilot is an easy way to connect to running containers. 

# Summary 

You have deployed a containerized application on Fargate running AWS Graviton2 processors using Copilot. The Copilot CLI makes it much easier to create the required resources and easily make changes using the `manifest.yml` file. 

There doesn't seem to be a way to specify `arm64` on the initial `copilot init` command, but it would be a useful enhancement. 

# Clean up the AWS resources

Delete the resources created by Copilot by running:

```console
copilot app delete
```

