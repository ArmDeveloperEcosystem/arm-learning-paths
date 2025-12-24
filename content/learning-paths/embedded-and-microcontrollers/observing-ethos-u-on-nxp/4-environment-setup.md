---
# User change
title: "Enviroment Setup"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

For detailed instructions on setting up your ExecuTorch build environment, please see the official PyTorch documentation: [Environment Setup](https://docs.pytorch.org/executorch/stable/using-executorch-building-from-source.html#environment-setup)

{{% notice macOS %}}

Use a Docker container to build ExecuTorch:
* The [Arm GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain) currently does not have a "AArch64 GNU/Linux target" for macOS
* You will use this toolchain's `gcc-aarch64-linux-gnu` and `g++-aarch64-linux-gnu` compilers on the next page of this learning path

1. Install and start [Docker Desktop](https://www.docker.com/)

2. Create a directory for building a `ubuntu-24-container`:

   ```bash
   mkdir ubuntu-24-container
   ```

3. Create a `dockerfile` in the `ubuntu-24-container` directory:

   ```bash
   cd ubuntu-24-container
   touch Dockerfile
   ```

4. Add the following commands to your `Dockerfile`:

   ```dockerfile
   FROM ubuntu:24.04

   ENV DEBIAN_FRONTEND=noninteractive

   RUN apt update -y && \
       apt install -y \
       software-properties-common \
       curl vim git
   ```

   The `ubuntu:24.04` container image includes Python 3.12, which will be used for this learning path.

5. Create the `ubuntu-24-container`:

   ```bash
   docker build -t ubuntu-24-container .
   ```

6. Run the `ubuntu-24-container`:

   ```bash { output_lines = "2-3" }
   docker run -it ubuntu-24-container /bin/bash
   # Output will be the Docker container prompt
   ubuntu@<CONTAINER ID>:/#
   ```

   [OPTIONAL] If you already have an existing container:
   - Get the existing CONTAINER ID:
     ```bash { output_lines = "2-4" }
     docker ps -a
     # Output
     CONTAINER ID  IMAGE                    COMMAND      CREATED        STATUS                       PORTS  NAMES
     0123456789ab  ubuntu-24-container  "/bin/bash"  27 hours ago   Exited (255) 59 minutes ago.        container_name
     ```
   - Log in to the existing container:
     ```bash
     docker start 0123456789ab
     docker exec -it 0123456789ab /bin/bash
     ```

{{% /notice %}}

After logging in to the Docker container, navigate to the ubuntu home directory:

```bash
cd /home/ubuntu
```

1. **Install dependencies:**

   ```bash { output_lines = "1" }
   # Use "sudo apt ..." if you are not logged in as root
   apt update
   apt install -y \
     python-is-python3 python3.12-dev python3.12-venv \
     gcc g++ \
     make cmake \
     build-essential \
     ninja-build \
     libboost-all-dev
   ```

2. Clone ExecuTorch:
   ```bash
   git clone https://github.com/pytorch/executorch.git
   cd executorch
   git fetch --tags
   git checkout v1.0.0
   git submodule sync
   git submodule update --init --recursive
   ```

3. Create a Virtual Environment:
   ```bash { output_lines = "3" }
   python3 -m venv .venv
   source .venv/bin/activate
   # Your prompt will prefix with (.venv)
   ```

4. Configure your git username and email globally:
   ```bash
   git config --global user.email "you@example.com"
   git config --global user.name "Your Name"
   ```
