---
title: "Install Daytona providers"

weight: 5

layout: "learningpathall"

---

Daytona allows you to use various cloud providers to manage your development environments. Installing providers does not require any configuration input. The details of using a provider are required when a Daytona target is configured. 

To add providers, run: 

```console
daytona provider install
```

Docker is already installed. 

Select the providers you want to install using the arrow keys.

Select **No** when you are asked about creating a target. You can enter the details later when a new target is created. 

To verify providers are installed, run the following command:

```console
daytona provider list
```

The output should display the list of providers you installed. 

The output below shows the Docker, AWS, and Azure providers installed:

```output

    Provider                                 Name                                            Version
    ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
    Docker                                   docker-provider                                 v0.12.6

    AWS                                      aws-provider                                    v0.3.6

    Azure                                    azure-provider                                  v0.3.6
```


You can remove providers using the uninstall command:

```console
daytona provider uninstall
```

Select the provider you want to uninstall. 

You are now ready to use Daytona to manage your development environments.
