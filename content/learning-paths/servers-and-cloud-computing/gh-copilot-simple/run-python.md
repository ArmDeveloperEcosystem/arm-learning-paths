---
title: Run a private GitHub Copilot Extension using Python
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How can I create my own private GitHub Copilot Extension?

You can create a simple extension in Python to get started learning how Copilot connects to extensions.

Use a text editor to save the Python code below to a file named `simple-extension.py` on Linux computer with Python installed.

```python
import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello! Welcome to the example GitHub Copilot Extension in Python!"

@app.route("/", methods=["POST"])
def handle_post():
    # Identify the user, using the GitHub API token provided in the request headers.
    token_for_user = request.headers.get("X-GitHub-Token")
    user_response = requests.get("https://api.github.com/user", headers={"Authorization": f"token {token_for_user}"})
    user = user_response.json()
    print("User:", user['login'])

    # Parse the request payload and log it.
    payload = request.json
    print("Payload:", payload)

    # Insert a special pirate-y system message in our message list.
    messages = payload['messages']
    messages.insert(0, {
        "role": "system",
        "content": "You are a helpful assistant that replies to user messages with a focus on software development. Don't answer questions that are not related to software or computing."
    })
    messages.insert(0, {
        "role": "system",
        "content": f"Start every response with the user's name, which is @{user['login']}"
    })

    # Use Copilot's LLM to generate a response to the user's messages, with
    # our extra system messages attached.
    copilot_response = requests.post(
        "https://api.githubcopilot.com/chat/completions",
        headers={
            "Authorization": f"Bearer {token_for_user}",
            "Content-Type": "application/json"
        },
        json={
            "messages": messages,
            "stream": True
        },
        stream=True
    )

    # Stream the response straight back to the user.
    return app.response_class(copilot_response.iter_content(), mimetype='application/json')

port = int(os.environ.get("PORT", 3000))
if __name__ == "__main__":
    app.run(port=port)

```

You may need to install the following Python packages:

```console
sudo apt update
sudo apt install python3-pip python-is-python3 python3-venv -y
```

Create a Python virtual environment to run the extension:

```console
python -m venv venv
source venv/bin/activate
```

Your shell prompt now includes `(venv)` indicating the virtual environment is active. 

Install the required Python packages:

```console
pip install flask requests
```

Run the extension using Python:

```console
python ./simple-extension.py
```

The output is similar to the text below:

```output
* Serving Flask app 'simple-extension'
* Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on http://127.0.0.1:3000
Press CTRL+C to quit
```

Your extension is running, but needs to be connected to Copilot. Continue to learn how to share it with Copilot.