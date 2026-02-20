---
title: Set up OpenTelemetry environment and application on Arm64
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## OpenTelemetry environment and application setup

In this section, you prepare an arm64-based SUSE Linux virtual machine with container tooling and deploy an instrumented Python Flask microservice that emits OpenTelemetry traces and metrics.

## Architecture overview

This setup includes a lightweight application and telemetry flow as shown below:

```text
Flask Microservice (Arm64)
        |
        | OpenTelemetry SDK
        v
OpenTelemetry Collector
```

The Flask application generates telemetry data using the OpenTelemetry SDK and sends it to an OpenTelemetry Collector for further processing and visualization.

## Network and firewall requirements

Ensure the following ports are open on your VM firewall:

| Service           | Port  | Purpose                    |
| ----------------- | ----- | -------------------------- |
| Prometheus        | 9090  | Metrics dashboard UI       |
| Jaeger UI         | 16686 | Distributed tracing UI     |
| Collector Metrics | 8889  | Prometheus scrape endpoint |
| OTLP gRPC         | 4317  | Telemetry ingestion (gRPC) |
| OTLP HTTP         | 4318  | Telemetry ingestion (HTTP) |

These ports enable telemetry ingestion and provide web interfaces for monitoring metrics and traces.

## Enable the SUSE Containers module

Enable the SUSE Containers Module to ensure that Docker and container-related tools are fully supported.

```bash
sudo SUSEConnect -p sle-module-containers/15.5/arm64
sudo SUSEConnect --list-extensions | grep Containers
```

Verify that the output shows the Containers module as **Activated**.

## Install Docker on SUSE Arm64

Docker is required to run containerized services on the Arm-based VM.

```bash
sudo zypper refresh
sudo zypper install -y docker
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER
newgrp docker
```

### Verify Docker installation

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

### Verify Docker Compose installation

```bash
docker-compose --version
```

Docker Compose v2 is now installed and ready to manage multi-service deployments.

## Create project workspace

Create a dedicated directory for the OpenTelemetry demo application.

```bash
mkdir ~/otel-demo
cd ~/otel-demo
```

This directory will store the Flask application code, dependencies, and container configuration.

## Build an instrumented Flask application

This Flask service is integrated with the OpenTelemetry SDK to emit distributed traces and metrics.

Create a file `app.py` in `~/otel-demo` with the following content:

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

## Define Python dependencies

Create a file `requirements.txt` in `~/otel-demo` to list all required Python packages:

```text
flask
opentelemetry-api
opentelemetry-sdk
opentelemetry-exporter-otlp
opentelemetry-instrumentation-flask
```

This ensures all OpenTelemetry and Flask libraries are installed consistently inside the container.

## Create the application Docker image

Build an Arm-compatible container image for the Flask service.

Create a file `Dockerfile` in `~/otel-demo` with the following content:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
```

This Dockerfile packages the instrumented Flask application into a lightweight Arm64-compatible container.

## What you've accomplished and what's next

You've successfully:

- Set up Docker and Docker Compose on your Google Axion C4A Arm64 virtual machine
- Built an instrumented Python Flask microservice that emits OpenTelemetry traces and metrics
- Created a containerized application ready for deployment

Next, you'll deploy the OpenTelemetry Collector and observability stack to receive, process, and visualize the telemetry data.
