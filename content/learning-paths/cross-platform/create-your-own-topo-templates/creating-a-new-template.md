---
title: Creating a new Topo Template
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create a Topo Template from scratch

You have already cloned and modified an existing Topo Template. In this section, you will create a new Template from an empty directory.

The Template you create serves a small web page with configurable text and color. It demonstrates the core parts of a Topo Template:

- A `compose.yaml` file with standard Compose services
- An `x-topo` metadata block
- Build arguments exposed as Topo clone-time parameters
- A container image built for Arm Linux targets

### Create the project directory

Create a new directory for the Template:

```bash
mkdir topo-message-card
cd topo-message-card
```

A Topo Template is a normal project directory. At minimum, it must contain a `compose.yaml` file. Most Templates also include a `Dockerfile` and application source code.

The directory you create in this section will have the following structure:

```output
topo-message-card/
├── compose.yaml
├── Dockerfile
└── src/
    └── index.html
```

### Create the web page

Create the application HTML file:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{CARD_TITLE}}</title>
    <style>
      body {
        margin: 0;
        min-height: 100vh;
        display: grid;
        place-items: center;
        font-family: Arial, sans-serif;
        background: #f3f6f8;
        color: #17212b;
      }

      main {
        width: min(720px, calc(100vw - 40px));
        border-top: 8px solid {{ACCENT_COLOR}};
        background: white;
        padding: 40px;
        box-shadow: 0 18px 40px rgba(15, 23, 42, 0.12);
      }

      h1 {
        margin: 0 0 16px;
        font-size: clamp(2rem, 6vw, 4rem);
      }

      p {
        margin: 0;
        font-size: 1.25rem;
        line-height: 1.5;
      }
    </style>
  </head>
  <body>
    <main>
      <h1>{{CARD_TITLE}}</h1>
      <p>{{CARD_MESSAGE}}</p>
    </main>
  </body>
</html>
```

The values wrapped in double braces are placeholders. The `Dockerfile` replaces them with values supplied by Topo.

### Create the Dockerfile

Create a `Dockerfile`:

```Dockerfile
FROM nginx:alpine

COPY src/index.html /usr/share/nginx/html/index.html

ARG CARD_TITLE="Hello from Topo"
ARG CARD_MESSAGE="This page was created from a Topo Template."
ARG ACCENT_COLOR="#0091bd"

RUN sed -i "s|{{CARD_TITLE}}|${CARD_TITLE}|g" /usr/share/nginx/html/index.html
RUN sed -i "s|{{CARD_MESSAGE}}|${CARD_MESSAGE}|g" /usr/share/nginx/html/index.html
RUN sed -i "s|{{ACCENT_COLOR}}|${ACCENT_COLOR}|g" /usr/share/nginx/html/index.html
```

Topo passes configuration values to templates through Docker build arguments. The `ARG` lines define the values consumed during the image build.

### Create the compose file

Create `compose.yaml`:

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/arm/topo-template-format/refs/heads/main/schema/topo-template-format.json
services:
  message-card:
    platform: linux/arm64
    build:
      context: .
      args:
        CARD_TITLE: "Hello from Topo"
        CARD_MESSAGE: "This page was created from a Topo Template."
        ACCENT_COLOR: "#0091bd"
    ports:
      - "8088:80"

x-topo:
  name: "Message Card"
  description: |
    A minimal web application Template that shows a configurable title,
    message, and accent color.
  type: "application"
  deploy_success_message: |
    Message Card is running. Open http://localhost:8088/ in your browser.
  args:
    CARD_TITLE:
      description: "The title to show on the message card"
      required: true
      example: "Hello from Arm"
    CARD_MESSAGE:
      description: "The message to show below the title"
      required: false
      default: "This page was created from a Topo Template."
      example: "Built once and deployed with Topo"
    ACCENT_COLOR:
      description: "The CSS color used for the card accent"
      required: false
      default: "#0091bd"
      example: "#00a3a3"
```

This file is both a Compose file and a Topo Template definition.

The `services` section is standard Compose. The service builds the local `Dockerfile`, publishes the web server on port `8088`, and sets `platform: linux/arm64` so the service targets Arm-based Linux systems.

The `x-topo` section is the Topo metadata block:

- `name` gives the Template a human-readable name.
- `description` explains what the Template does.
- `type` identifies this as an application Template.
- `deploy_success_message` prints a useful hint after deployment.
- `args` defines the values Topo prompts for when someone clones the Template.

The argument names in `x-topo.args` match the keys under `services.message-card.build.args`. When Topo resolves the arguments, it writes the selected values into the build arguments.

### Clone the local Template

Move to the parent directory and clone your local Template with Topo:

```bash
cd ..
topo clone dir:./topo-message-card ./message-card-demo \
  CARD_TITLE="Hello from Arm" \
  CARD_MESSAGE="Created from a new Topo Template" \
  ACCENT_COLOR="#00a3a3"
```

You can also omit the argument values and answer the interactive prompts:

```bash
topo clone dir:./topo-message-card ./message-card-demo
```

After cloning, inspect the generated project:

```bash
cd message-card-demo
sed -n '1,80p' compose.yaml
```

The `build.args` values should contain the values you provided:

```yaml
services:
  message-card:
    platform: linux/arm64
    build:
      context: .
      args:
        CARD_TITLE: "Hello from Arm"
        CARD_MESSAGE: "Created from a new Topo Template"
        ACCENT_COLOR: "#00a3a3"
```

### Deploy the new project

Deploy the cloned project to the host machine:

```bash
topo deploy --target localhost
```

When deployment completes, open `http://localhost:8088/` in your browser.

Confirm that the container is running:

```bash
topo ps --target localhost
```

The output should include the `message-card` service and port `8088`.

### Add hardware requirements

Only add `features` when your Template needs specific Arm hardware features. For example, a SIMD benchmark that requires SVE can declare:

```yaml
x-topo:
  name: "SIMD Visual Benchmark"
  description: |
    Visual demonstration of SIMD performance benefits on Arm processors.
  type: "application"
  features:
    - "SVE"
```

Topo can use these feature requirements when listing Templates against a target.

### Share the Template

To share your Template, publish the Template directory as a Git repository. Other users can then clone it with Topo:

```bash
topo clone https://github.com/<user-or-org>/topo-message-card.git
```

If the Template is intended to be reusable by the wider Topo community, include:

- `compose.yaml`
- Any Dockerfiles and source files required by the services
- A `README.md` with usage instructions
- A license file
- Clear `x-topo` metadata and argument descriptions

You now have a complete Topo Template created from scratch.
