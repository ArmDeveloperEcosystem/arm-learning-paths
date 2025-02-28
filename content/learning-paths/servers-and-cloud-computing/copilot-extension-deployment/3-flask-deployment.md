---
title: Deploying Flask
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How do I deploy my Copilot Extension Flask app to my newly created EC2 instance?

In the first GitHub Copilot Extension Learning Path you created a Flask app in the section titled "[How can I create my own private GitHub Copilot Extension?](../../gh-copilot-simple/run-python/)".

You will deploy this Flask app on your newly created EC2 instance. First, get your EC2 instance ID:

```bash
aws ec2 describe-instances --filters "Name=tag:Name,Values=CopilotExtensionDeploymentStack/LaunchTemplate" --query "Reservations[*].Instances[*].InstanceId" --output text
```

Then use that ID to log in with AWS SSM. You must use AWS SSM because your instance is in a private subnet for security purposes, but because the SSM agent is running on the instance, it creates a tunnel that allows you to SSH into the machine with the following command:

```bash
aws ssm start-session --target [your instance ID]
```

You should now be able to go through the steps in "[How can I create my own private GitHub Copilot Extension?](../../gh-copilot-simple/run-python/)" to create your Flask app, create a Python virtual environment, and install the appropriate packages.

The only two changes you'll make are to add a health check endpoint (for the ALB health check), and to run your app on 0.0.0.0 port 8080, which the ALB is listening for.

First, add the following endpoint to your main flask file:

```Python
@app.route('/health')
def health():
    return Response(status=200)
```

Next, add the `host` argument to the `app.run` call at the end of the file and update the port number. The final result should look like this:

```Python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

This will expose your app to the port that you set up your ALB listener to listen on.

Run the simple extension:

```Python
python ./simple-extension.py
```

You should now be able to navigate to your API subdomain from any browser and see

```text
"Hello! Welcome to the example GitHub Copilot Extension in Python!"
```

Your API is now complete and ready to be configured in your GitHub Application.