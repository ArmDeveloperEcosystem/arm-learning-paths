---
# User change
title: "Setting Up Amazon Q"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

Before you can use Amazon Q to assist with your Arm development, you need to set it up in your environment. This section covers the different ways to access and configure Amazon Q.

## Access options for Amazon Q

Amazon Q is available through multiple interfaces:

1. **AWS Management Console**: Access Amazon Q directly in the AWS console
2. **IDE plugins**: Use Amazon Q in your development environment
3. **Command line interface**: Interact with Amazon Q from your terminal
4. **Web interface**: Access through a dedicated web portal

For Arm development, the IDE plugins and command line interface are particularly useful.

## Setting up Amazon Q in your IDE

Amazon Q offers plugins for popular IDEs including VS Code, JetBrains IDEs, and Visual Studio. Here's how to set up the VS Code extension:

1. Open VS Code and navigate to the Extensions view (Ctrl+Shift+X)
2. Search for "Amazon Q"
3. Click "Install" on the Amazon Q extension
4. Once installed, click "Sign in to AWS" and follow the authentication prompts
5. After authentication, Amazon Q is ready to use in your IDE

## Setting up Amazon Q CLI

For command line access, which is useful for scripting and automation:

```bash
# Install the AWS CLI if you haven't already
curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# Configure AWS credentials
aws configure

# Install Amazon Q CLI
pip install amazon-q-cli

# Verify installation
q --version
```

## Configuring Amazon Q for Arm development

To optimize Amazon Q for Arm development:

1. Create a `.amazonq` configuration file in your project root:

```json
{
  "architecture": "arm64",
  "preferredLanguages": ["c", "cpp", "python", "rust"],
  "optimizationLevel": "performance"
}
```

2. This configuration helps Amazon Q provide more relevant suggestions for Arm architecture.

## Testing your setup

Let's verify that Amazon Q is correctly set up and ready to assist with Arm development:

1. In your IDE with the Amazon Q extension, open a new file
2. Type a comment asking for help with an Arm-specific task:

```python
# Generate a function to check if the current system is running on Arm architecture
```

3. Invoke Amazon Q (usually with Ctrl+Space or through the Amazon Q panel)
4. Amazon Q should respond with relevant code for detecting Arm architecture

If you're using the CLI:

```bash
q "How can I detect if my code is running on an Arm processor?"
```

You should receive a helpful response with code examples specific to Arm architecture.

Now that you have Amazon Q set up, let's explore how to use it for code generation and optimization for Arm architecture.
