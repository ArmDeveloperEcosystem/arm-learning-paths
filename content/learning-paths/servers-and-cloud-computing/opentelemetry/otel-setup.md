---
title: OpenTelemetry Environment & Application Setup on ARM64
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## OpenTelemetry Environment & Application Setup

In this guide, you will prepare an **Arm64-based SUSE Linux virtual machine** with container tooling and deploy an **instrumented Python Flask microservice** that emits OpenTelemetry traces and metrics. This forms the foundation for building a complete observability pipeline in the upcoming steps.

## Architecture Overview

This setup includes a lightweight application and telemetry flow as shown below:

```text
Flask Microservice (ARM64)
        |
        | OpenTelemetry SDK
        v
OpenTelemetry Collector
```
The Flask application generates telemetry data using the OpenTelemetry SDK and sends it to an OpenTelemetry Collector for further processing and visualization.

## Network & Firewall Requirements
Ensure the following port is open on your VM firewall:

| Service   | Port | Purpose                     |
|-----------|------|-----------------------------|
| Flask App | 8080 | Application HTTP traffic   |


Opening port **8080** allows external access to the Flask microservice running inside the container.

## Install Docker on SUSE ARM64

Docker is required to run containerized services on the ARM-based VM.

```bash
sudo zypper refresh
sudo zypper install -y docker
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER
newgrp docker
```

### Verify Installation

```bash
docker --version
```

Docker Engine is now installed and configured to run without sudo for the current user.



## Install Docker Compose (v2)

Docker Compose is used to orchestrate multi-container applications.

```bash
sudo curl -L https://github.com/docker/compose/releases/download/v2.27.0/docker-compose-linux-aarch64 \
  -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```

### Verify Installation

```bash
docker-compose --version
```

Docker Compose v2 is now installed and ready to manage multi-service deployments.

## Create Project Workspace
Create a dedicated directory for the OpenTelemetry demo application.

```bash
mkdir ~/otel-demo
cd ~/otel-demo
```

This directory will store the Flask application code, dependencies, and container configuration.

## Build an Instrumented Flask Application
This Flask service is integrated with the OpenTelemetry SDK to emit distributed traces and metrics.

```bash
vi app.py
```

### File: app.py

```python
from flask import Flask
import time

from opentelemetry import trace, metrics
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.trace.export import BatchSpanProcessor

resource = Resource.create({
    "service.name": "flask-arm-service"
})

trace_provider = TracerProvider(resource=resource)
trace.set_tracer_provider(trace_provider)

trace_exporter = OTLPSpanExporter(endpoint="otel-collector:4317", insecure=True)
trace_provider.add_span_processor(
    BatchSpanProcessor(trace_exporter)
)

metric_exporter = OTLPMetricExporter(endpoint="otel-collector:4317", insecure=True)

metric_reader = PeriodicExportingMetricReader(
    metric_exporter,
    export_interval_millis=5000
)

meter_provider = MeterProvider(
    resource=resource,
    metric_readers=[metric_reader]
)

metrics.set_meter_provider(meter_provider)

meter = metrics.get_meter(__name__)

request_counter = meter.create_counter(
    name="demo_requests_total",
    description="Total number of requests"
)

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

@app.route("/")
def hello():
    request_counter.add(1)
    time.sleep(0.2)
    return "Hello OpenTelemetry!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```

The Flask service now automatically generates traces for HTTP requests and custom metrics for request counts.

## Define Python Dependencies
Create a file to list all required Python packages.

```bash
vi requirements.txt
```

### File: requirements.txt

```
flask
opentelemetry-api
opentelemetry-sdk
opentelemetry-exporter-otlp
opentelemetry-instrumentation-flask
```

This ensures all OpenTelemetry and Flask libraries are installed consistently inside the container.



## Create Application Docker Image

Build an ARM-compatible container image for the Flask service.

```bash
vi Dockerfile
```

### File: Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
```

This Dockerfile packages the instrumented Flask application into a lightweight ARM64-compatible container.

## What You Have Accomplished

- Installed Docker and Docker Compose on an ARM64 SUSE VM
- Created an OpenTelemetry-instrumented Flask microservice
- Defined application dependencies
- Built a container-ready application image

### What’s Next

In the next section, you will deploy the **OpenTelemetry Collector and observability stack** to receive, process, and visualize the telemetry data generated by this application.
