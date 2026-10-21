---
title: "Automate Puppeteer tests with GitHub Actions on an Arm runner"
description: "Create a GitHub Actions workflow that starts a local Hugo server and runs Puppeteer tests on an Arm runner on pull requests or manual runs."

weight: 5

layout: "learningpathall"
---

## Run tests on pull requests

You can run Puppeteer tests automatically on pull requests to check changes before merging them. The workflow you'll create here checks out the repository, starts Hugo, and runs all three Puppeteer scripts whenever a pull request targets the main branch. If any script exits with a non-zero code, the workflow fails.

Using a native arm64 runner means Chrome runs at full native speed, the same as on your Arm server.

## Commit the test scripts to your fork

The GitHub Actions workflow expects the `puppeteer-tests` directory and its scripts to be present in the repository. Commit everything you created in the previous section:

```bash
cd $HOME/ecosystem-dashboard-for-arm
git add puppeteer-tests/
git commit -m "Add Puppeteer headless tests"
git push origin main
```

## Create the workflow file

Create the `.github/workflows/` directory and the workflow file:

```bash
mkdir -p .github/workflows
```

Create `.github/workflows/puppeteer-test.yml` with the following content:

```yaml
name: Puppeteer pre-publish tests

on:
  pull_request:
    branches: [main]
  workflow_dispatch:

jobs:
  test:
    runs-on: ubuntu-24.04-arm

    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Hugo
        uses: peaceiris/actions-hugo@v3
        with:
          hugo-version: '0.147.0'
          extended: true

      - name: Start Hugo development server
        run: hugo server --port 1313 &

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install Chrome
        run: |
          wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_arm64.deb
          sudo apt install -y ./google-chrome-stable_current_arm64.deb

      - name: Install Puppeteer
        run: npm install puppeteer-core
        working-directory: puppeteer-tests

      - name: Wait for Hugo server
        run: npx wait-on http://localhost:1313 --timeout 30000

      - name: Test — assert NGINX package is present
        run: node test-package-status.mjs
        working-directory: puppeteer-tests

      - name: Test — validate official documentation link
        run: node test-doc-link.mjs
        working-directory: puppeteer-tests

      - name: Test — capture screenshot
        run: node screenshot.mjs
        working-directory: puppeteer-tests

      - name: Upload screenshot artifact
        uses: actions/upload-artifact@v4
        with:
          name: dashboard-screenshot
          path: puppeteer-tests/dashboard.png
```

Commit and push the workflow file to trigger it on your next pull request:

```bash
git add .github/workflows/puppeteer-test.yml
git commit -m "Add Puppeteer GitHub Actions workflow"
git push origin main
```

To verify the workflow immediately, open your fork on GitHub and select **Actions**. Select **Puppeteer pre-publish tests**, then select **Run workflow**. Choose the `main` branch and select **Run workflow** to start the tests.

### What each step does

- `actions/checkout@v4` — clones the repository onto the runner.
- `peaceiris/actions-hugo@v3` — installs the Hugo extended binary at the pinned version. The `extended: true` flag is required because the dashboard uses Hugo Pipes for asset processing.
- `hugo server --port 1313 &` — starts the development server in the background. The `&` is essential; without it the step never finishes.
- `actions/setup-node@v4` — installs Node.js 20 and adds `npm` to the path.
- Install Chrome — downloads the official Google arm64 `.deb` package and installs it with `apt`. This is the same package you installed on your server in the previous section.
- Install Puppeteer — runs `npm install puppeteer-core` inside the `puppeteer-tests` directory where your test scripts live.
- `npx wait-on` — polls `http://localhost:1313` until Hugo responds or the 30-second timeout expires. This prevents the test steps from starting before the server is ready.
- The three test steps run each script and let the exit code determine whether the step passes or fails.
- `actions/upload-artifact@v4` — saves `dashboard.png` so you can download and inspect the screenshot from the GitHub Actions run summary.

## The arm64 runner label

The `runs-on: ubuntu-24.04-arm` label selects a GitHub-hosted runner running Ubuntu 24.04 on 64-bit Arm hardware.

## Expected job outcome

When the workflow runs successfully on a pull request, the three test steps and the screenshot upload step show green check marks in the Actions tab. The job summary includes a downloadable artifact named `dashboard-screenshot`.

The expected output is:

```output
PASS: NGINX package is present in the rendered dashboard
PASS: docs link https://www.nginx.com/resources/wiki/start/ returned HTTP 200
Screenshot saved to dashboard.png
```

If any test step shows a red cross, expand the step log to see which assertion failed and which exit code the script returned. A `net::ERR_CONNECTION_REFUSED` error in the test logs usually means the Hugo server was not ready in time; increase the `--timeout` value passed to `wait-on`.

## What you've accomplished

You've created a GitHub Actions workflow that runs your Puppeteer scripts on an Arm runner and saves a dashboard screenshot as an artifact. You can extend the scripts to check other packages or adapt them to test your own web application.
