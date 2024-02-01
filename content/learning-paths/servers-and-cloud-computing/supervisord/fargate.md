---
# User change
title: "Access the container running in AWS"
weight: 4

layout: "learningpathall"

---

You can use the same technique to access a container running in AWS, without opening any port for SSH access.

There are many ways to run containers using cloud services which demonstrate this, but AWS ECS with a Fargate launch type is shown below. You can adapt the example for any container runtime environment. 

The instructions below are similar to [How to use AWS Graviton processors on AWS Fargate with Copilot](/learning-paths/servers-and-cloud-computing/aws-copilot/). You can use the AWS Copilot CLI to launch a container and then SSH to it using Remote.It.

# Launch the container in AWS using AWS Copilot CLI

Install `copilot` using the [AWS Copilot CLI install guide](/install-guides/aws-copilot/).

You should be in the directory with the `Dockerfile` and `supervisord.conf` from the previous section.

Start a container in AWS ECS using the `copilot` command:

```console
copilot init --app test-container        \
--name debug                             \
--type 'Load Balanced Web Service'     \
--dockerfile './Dockerfile'            \
--env test                             \
--port 80                              \
--deploy
```

It will take some time to start the container in AWS.

When the `copilot` command completes, the URL of the load balancer is printed. 

You can open this URL in a browser and see the Apache welcome screen as in the previous sections.

There are 2 issues with this container:
- It is using the `amd64` architecture 
- No Remote.It registration code was provided so you cannot connect with SSH

# Update the container

To fix the 2 issues edit the file `copilot/debug/manifest.yml` and add a Remote.It registration code and change the platform to `linux/arm64`.

Make sure you substitute your registration code for the one shown below.

```console
platform: linux/arm64

variables:                    # Pass environment variables as key value pairs.
  R3_REGISTRATION_CODE: 416ED829-D9D8-532C-B1FE-13548929B2A1
```

After making the changes to `manifest.yml` update the container: 

```console
copilot svc deploy
```

A new container image will be built for the `arm64` architecture and deployed with the Remote.It registration code. 

After the update is complete, look in your Remote.It dashboard to see your new device. 

You can now SSH directly into the container just like you did in the previous section using `ubuntu` for the username and password.

Make sure to change the values to match your endpoint from your Remote.It dashboard.

```console
ssh ssh://ubuntu@proxy18.rt3.io:32443
```

Once you connect with SSH you can edit the file `/var/www/html/index.html` to simulate making a change and reload the page in your browser to see the update. 

Supervisor is useful to start multiple services in a container and useful for accessing containers without opening any ports. 

