---
title: Configure GitHub Actions for CI/CD
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why use GitHub Actions for MCP testing?

GitHub Actions provide automated CI/CD directly in your repository. For MCP server testing, it offers:

- **Arm runner support**: GitHub provides native Arm64 runners for building and testing.
- **Docker integration**: Runners come with Docker pre-installed.
- **Automatic triggers**: Tests run on every push and pull request.
- **Parallel execution**: Multiple jobs can run simultaneously.

## Create the workflow file

Create a GitHub Actions workflow file at `.github/workflows/integration-tests.yml`:

```yaml
name: Integration Tests

on:
  push:
  pull_request:

jobs:
  integration-tests:
    runs-on: ubuntu-24.04-arm
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: pip

      - name: Install test dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r mcp-local/tests/requirements.txt

      - name: Build MCP Docker image
        run: docker buildx build -f mcp-local/Dockerfile -t arm-mcp .

      - name: Run integration tests
        env:
          MCP_IMAGE: arm-mcp:latest
        run: pytest -v mcp-local/tests/test_mcp.py
```

## Understand the workflow configuration

The workflow uses the `ubuntu-24.04-arm` runner, which is a GitHub-hosted Arm64 runner. This ensures that both the Docker build and the tests execute natively on Arm hardware.

Key aspects of the configuration:

### Trigger events

```yaml
on:
  push:
  pull_request:
```

This configuration triggers the workflow on every push to any branch and on pull request events. You can restrict this to specific branches if needed:

```yaml
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
```

### Python caching

```yaml
- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: "3.11"
    cache: pip
```

The `cache: pip` option caches Python packages between runs, significantly speeding up subsequent workflow executions.

### Environment variables

```yaml
- name: Run integration tests
  env:
    MCP_IMAGE: arm-mcp:latest
  run: pytest -v mcp-local/tests/test_mcp.py
```

The `MCP_IMAGE` environment variable tells the test suite which Docker image to use. The test code reads this with:

```python
image = os.getenv("MCP_IMAGE", constants.MCP_DOCKER_IMAGE)
```

## Add test result artifacts

Enhance the workflow to save test results as artifacts for debugging:

```yaml
      - name: Run integration tests
        env:
          MCP_IMAGE: arm-mcp:latest
        run: pytest -v mcp-local/tests/test_mcp.py --junitxml=test-results.xml

      - name: Upload test results
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: test-results
          path: test-results.xml
```

The `if: always()` condition ensures test results upload even when tests fail.

## Add a build matrix for multiple platforms

To test on both Arm64 and x86_64, use a matrix strategy:

```yaml
jobs:
  integration-tests:
    strategy:
      matrix:
        runner: [ubuntu-24.04-arm, ubuntu-latest]
    runs-on: ${{ matrix.runner }}
    steps:
      # ... same steps as before
```

This runs the integration tests in parallel on both architectures.

## Monitor workflow runs

After pushing the workflow file, navigate to the Actions tab in your GitHub repository. Each workflow run shows:

- Build steps and their status
- Execution time for each step
- Log output for debugging failures
- Artifacts for download

## Troubleshoot common issues

If the workflow fails, check these common causes:

**Docker build timeout**: The initial image build can take 10+ minutes. GitHub Actions has a default timeout of 360 minutes per job, but individual steps might need explicit timeouts:

```yaml
- name: Build MCP Docker image
  timeout-minutes: 30
  run: docker buildx build -f mcp-local/Dockerfile -t arm-mcp .
```

**Container startup issues**: If tests fail with timeout errors, the MCP server might not be starting correctly. Add debug output:

```yaml
- name: Run integration tests
  env:
    MCP_IMAGE: arm-mcp:latest
  run: |
    docker run --rm arm-mcp:latest echo "Container starts successfully"
    pytest -v -s mcp-local/tests/test_mcp.py
```

**Rate limiting**: If tests query external services, you might encounter rate limits. Consider adding retry logic or using mock responses for CI environments.

## What you've accomplished and what's next

In this section:
- You created a GitHub Actions workflow for automated testing.
- You learned how to use Arm64 runners for native execution.
- You added test artifacts and multi-platform support.
- You explored troubleshooting techniques for CI failures.

You now have a complete CI/CD pipeline that automatically tests your MCP server on every code change. 

## Summary

In this Learning Path, you learned how to:

- Set up testcontainers for Docker-based integration testing.
- Write pytest tests that communicate with MCP servers over stdio transport.
- Parse MCP JSON-RPC responses and validate tool outputs.
- Configure GitHub Actions with Arm64 runners for automated testing.

These techniques apply to any MCP server implementation, not just the Arm MCP Server. Use this foundation to build comprehensive test suites that ensure your MCP tools work correctly across updates and deployments.
