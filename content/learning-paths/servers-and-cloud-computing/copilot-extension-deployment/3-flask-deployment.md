---
title: Deploying Flask
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How do I deploy my Copilot Extension Flask app to my newly created EC2 instance?

In the first GitHub Copilot Extension Learning Path, you created a Flask app in the section titled "[How can I create my own private GitHub Copilot Extension?](http://localhost:1313/learning-paths/servers-and-cloud-computing/gh-copilot-simple/run-python/)".

You will now deploy this Flask app on your newly created EC2 instance. First, retrieve your EC2 instance ID:

```bash
aws ec2 describe-instances --filters "Name=tag:Name,Values=CopilotExtensionDeploymentStack/LaunchTemplate" --query "Reservations[*].Instances[*].InstanceId" --output text
```

Next, use this ID to log in with AWS SSM.  Because your instance is in a private subnet for security purposes, you must use SSM. 

The SSM agent running on the instance creates a secure tunnel that lets you SSH in with the following command:

```bash
aws ssm start-session --target [your instance ID]
```

You can now follow the steps in "[How can I create my own private GitHub Copilot Extension?](http://localhost:1313/learning-paths/servers-and-cloud-computing/gh-copilot-simple/run-python/)" to create your Flask app, set up a Python virtual environment, and install the necessary packages.

The only two changes that you need to make are:

* Add a health check endpoint for the Application Load Balancer (ALB).
* Run your app on `0.0.0.0` port `8080`, which the ALB is configured to listen on.

First, add the following endpoint to your main Flask file:

```Python
@app.route('/health')
def health():
    return Response(status=200)
```

Next, add the `host` argument to the `app.run` call at the end of the file and update the port number. 

The final result should look like this:

```Python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

This exposes your app to the port that the ALB listener is monitoring.

Run the simple extension:

```Python
python ./simple-extension.py
```

Now, if you navigate to your API subdomain in a browser, you should see:

```text
"Hello! Welcome to the example GitHub Copilot Extension in Python!"
```

Your API is now complete and ready to be configured in your GitHub Application.