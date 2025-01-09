---
title: "Configure a Git provider"
weight: 4

layout: "learningpathall"
---

If you plan to use Daytona to work on code in your GitHub account, you can set up a Git provider. 

{{% notice Note %}}
This step is optional. If you want to run the example project without making any changes, you don't need to configure a Git provider. 
{{% /notice %}}

## How do I configure GitHub as a Git Provider for Daytona?

Daytona allows you to integrate with various Git providers to manage your code repositories. You can add GitHub as a Git provider using a GitHub Personal Access Token.

See the [Daytona documentation](https://www.daytona.io/docs/configuration/git-providers/) for other Git providers. 

### How do I create a Personal Access Token on GitHub?

1. Log in to your GitHub account.

2. Navigate to **Settings** > **Developer settings** > **Personal access tokens** > **Tokens (classic)**.

3. Click on **Generate new token**.

4. Provide a note for the token, select the required scopes, `repo` and `user`, and click **Generate token**.

5. Copy the generated token and save it securely. You will need it in the next step.


### How do I configure Daytona to use the GitHub Token?

Make sure the Daytona server is running on your computer. 

To configure GitHub, run the command below:

```console
daytona git-providers add
```

Select GitHub from the list using the arrow keys. 

Paste your GitHub token and enter your GitHub username. 

### How do I verify the GitHub Configuration?

To verify that Daytona is configured correctly to use GitHub, run the following command:

```console
daytona git-provider list
```

The output displays GitHub as one of the configured Git providers with your GitHub username.

```output

    Name                       Alias                           Username
    ─────────────────────────────────────────────────────────────────────────────────────────────────────────────
    GitHub                     jasonrandrews                   jasonrandrews
```

You have now successfully configured GitHub as a Git provider for Daytona.

You can now use Daytona to manage your code repositories hosted on GitHub.
