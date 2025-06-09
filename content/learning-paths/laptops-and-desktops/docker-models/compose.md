---
title: "Run a containerized AI chat app with Docker Compose"
weight: 3
layout: "learningpathall"
---

Docker Compose makes it easy to run multi-container applications, and it can also include those that include local AI inference services.

In this section, you'll use Docker Compose to deploy a simple web-based AI chat application. The frontend is a Flask web app, and the backend uses Docker Model Runner to serve AI responses.

## Clone the example project

Clone the [docker-model-runner-chat](https://github.com/jasonrandrews/docker-model-runner-chat) repository from GitHub. This project provides a simple web interface to interact with local AI models such as Llama 3.2 or Gemma 3.

```console
git clone https://github.com/jasonrandrews/docker-model-runner-chat.git
cd docker-model-runner-chat
```

## Review the Docker Compose file

The `compose.yaml` file defines defines how Docker Compose sets up and connects the services.

It sets up two services:

- **ai-chat**: A Flask-based web application that provides the chat user interface. It is built from the local directory, exposes port 5000 for browser access, mounts the project directory as a volume for live code updates, loads environment variables from `vars.env`, and waits for the `ai-runner` service to be ready before starting.
- **ai-runner**: This service uses the Docker Model Runner provider to run the selected AI model (for example, `ai/gemma3`). The configuration under `provider` tells Docker to use the model runner extension and specifies which model to load.

The setup allows the web app to communicate with the model runner service as if it were an OpenAI-compatible API, making it easy to swap models or update endpoints by changing environment variables or compose options.

Review the `compose.yaml` file to see the two services.

```yaml
services:
  ai-chat:
    build:
      context: .
    ports:
      - "5000:5000"
    volumes:
      - ./:/app
    env_file:
      - vars.env
    depends_on:
      - ai-runner
  ai-runner:
    provider:
      type: model
      options:
        model: ai/gemma3
```

## Start the application

From the project directory, start the app with:

```console
docker compose up --build
```

Docker Compose builds the web app image and starts both services.

## Access the chat interface

Once running, open your browser and copy-and-paste the local URL below: 

```console
http://localhost:5000
```

You’ll see a simple chat UI. Enter a prompt and get real-time responses from the AI model.

![Compose #center](compose-app.png "Docker Model Chat")

## Configure the model

You can change the AI model or endpoint by editing the `vars.env` file before starting the containers. The file contains environment variables used by the web application:

- `BASE_URL`: The base URL for the AI model API. By default, it is set to `http://model-runner.docker.internal/engines/v1/`, which allows the web app to communicate with the Docker Model Runner service. This is the default endpoint setup by Docker to access the model. 
- `MODEL`: The AI model to use (for example, `ai/gemma3` or `ai/llama3.2`).

The `vars.env` file is shown below. 

```console
BASE_URL=http://model-runner.docker.internal/engines/v1/
MODEL=ai/gemma3
```

To use a different model or API endpoint, change the `MODEL` value. For example:

```console
MODEL=ai/llama3.2
```

Be sure to also update the model name in the `compose.yaml` under the `ai-runner` service. 

## Optional: customize generation parameters

You can edit `app.py` to adjust parameters such as:

* `temperature`: controls randomness (higher is more creative)
* `max_tokens`: controls the length of responses 

## Stop the application

To stop the services, press `Ctrl+C` in the terminal.

You can also run the command below in another terminal to stop the services.

```console
docker compose down
```

## Troubleshooting

Use the steps below if you have any issues running the application:

* Ensure Docker and Docker Compose are installed and running
* Make sure port 5000 is not in use by another application
* Check logs with:

```console
docker compose logs
```

## What you've learned 
In this section, you learned how to use Docker Compose to run a containerized AI chat application with a web interface and local model inference from Docker Model Runner. 
