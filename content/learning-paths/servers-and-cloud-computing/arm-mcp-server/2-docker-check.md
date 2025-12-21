---
title: Direct AI Chat
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Checking Base Images for Arm Compatibility

This section demonstrates just one example of using direct AI chat with the Arm MCP Server. You can use similar natural language prompts to check library compatibility, search for Arm documentation, or analyze code for migration issues.

A common first step when migrating a containerized application to Arm is verifying that the base container images support the arm64 architecture. The Arm MCP Server simplifies this process by allowing you to ask this question directly using a natural language prompt, without manually inspecting image manifests or registry metadata. 

## Example: Legacy CentOS 6 Application

Consider an application built on CentOS 6, a legacy Linux distribution that has reached end of life (EOL). This example represents a typical x86-optimized, compute-heavy benchmark application that you might encounter when migrating older workloads.

Before examining the Dockerfile, note that it contains several x86-specific elements that need attention during migration: the `centos:6` base image (which might lack arm64 support), the `-mavx2` compiler flag for x86 AVX2 SIMD instructions, and C++ source files with x86 intrinsics.

Copy this Dockerfile into VS Code using GitHub Copilot or another agentic IDE connected to the Arm MCP Server:

```dockerfile
FROM centos:6

# CentOS 6 reached EOL, need to use vault mirrors
RUN sed -i 's|^mirrorlist=|#mirrorlist=|g' /etc/yum.repos.d/CentOS-Base.repo && \
    sed -i 's|^#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-Base.repo

# Install EPEL repository (required for some development tools)
RUN yum install -y epel-release && \
    sed -i 's|^mirrorlist=|#mirrorlist=|g' /etc/yum.repos.d/epel.repo && \
    sed -i 's|^#baseurl=http://download.fedoraproject.org/pub/epel|baseurl=http://archives.fedoraproject.org/pub/archive/epel|g' /etc/yum.repos.d/epel.repo

# Install Developer Toolset 2 for better C++11 support (GCC 4.8)
RUN yum install -y centos-release-scl && \
    sed -i 's|^mirrorlist=|#mirrorlist=|g' /etc/yum.repos.d/CentOS-SCLo-scl.repo && \
    sed -i 's|^mirrorlist=|#mirrorlist=|g' /etc/yum.repos.d/CentOS-SCLo-scl-rh.repo && \
    sed -i 's|^# baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-SCLo-scl.repo && \
    sed -i 's|^# baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-SCLo-scl-rh.repo

# Install build tools
RUN yum install -y \
    devtoolset-2-gcc \
    devtoolset-2-gcc-c++ \
    devtoolset-2-binutils \
    make \
    && yum clean all

# Set working directory
WORKDIR /app

# Copy all header files
COPY *.h ./

# Copy all C++ source files
COPY *.cpp ./

# Build the application with optimizations using devtoolset-2 (GCC 4.8)
# AVX2 intrinsics are used in the code for x86-64 platforms
RUN scl enable devtoolset-2 "g++ -O2 -mavx2 -o benchmark \
    main.cpp \
    matrix_operations.cpp \
    hash_operations.cpp \
    string_search.cpp \
    memory_operations.cpp \
    polynomial_eval.cpp \
    -std=c++11"

# Create a startup script
COPY start.sh .
RUN chmod +x start.sh

# Run the application
CMD ["./start.sh"]
```

## Using the Arm MCP Server to Check Compatibility

With the Arm MCP Server connected to your AI assistant, you can quickly verify base image compatibility using a simple natural language prompt:

```text
Check this base image for Arm compatibility
```

The AI assistant will use the `check_image` or `skopeo` tool to inspect the image and return a report. For `centos:6`, you'd discover that this legacy image doesn't support `arm64` architecture.

## What you've accomplished and what's next

In this section, you've used direct AI chat with the Arm MCP Server to check Docker base images for Arm compatibility. You've seen how a simple natural language prompt can quickly identify compatibility issues without manually inspecting image manifests.

In the next section, you'll migrate x86 SIMD code to Arm using a fully agentic workflow with prompt files.
