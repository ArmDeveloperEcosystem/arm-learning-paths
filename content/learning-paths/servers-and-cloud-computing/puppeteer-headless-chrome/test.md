---
title: "Write and run Puppeteer tests against a Hugo site"
description: "Fork the Ecosystem Dashboard for Arm, install Puppeteer inside the repository, start a local Hugo development server, and run three Puppeteer test scripts that assert page content, validate a documentation link, and capture a screenshot."

weight: 4

layout: "learningpathall"
---

## Fork and clone the repository

The following tests run against the [Ecosystem Dashboard for Arm](https://github.com/ArmDeveloperEcosystem/ecosystem-dashboard-for-arm). The dashboard is a public Hugo site that tracks the Arm compatibility status of open-source packages. You need your own fork so that you can commit the test scripts and wire them into GitHub Actions.

### Authenticate with GitHub

Install the `gh` CLI and authenticate before cloning. This sets up credentials for both the clone and later `git push` commands.

Install `git` and `gh`:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu 24.04" language="bash" >}}
sudo apt-get install -y git gh
  {{< /tab >}}
  {{< tab header="Amazon Linux 2023" language="bash" >}}
sudo dnf install -y git
sudo dnf install -y 'dnf-command(config-manager)'
sudo dnf config-manager --add-repo https://cli.github.com/packages/rpm/gh-cli.repo
sudo dnf install -y gh
  {{< /tab >}}
{{< /tabpane >}}

Log in using the browser-based device flow. You don't need a token:

```bash
gh auth login
```

Select **GitHub.com**, **HTTPS**, and authenticate using the browser.

If this is a new server, also configure your git identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### Fork and clone the repository

To fork and clone the repository:

1. Go to [https://github.com/ArmDeveloperEcosystem/ecosystem-dashboard-for-arm](https://github.com/ArmDeveloperEcosystem/ecosystem-dashboard-for-arm).
2. Select **Fork** and follow the prompts to create a fork under your account.
3. Clone your fork on your Arm server, replacing `your-github-username` with your actual username:

  ```bash
  cd $HOME
  git clone https://github.com/your-github-username/ecosystem-dashboard-for-arm
  ```

After forking and cloning the repository, change into the cloned directory:

  ```bash
  cd ecosystem-dashboard-for-arm
  ```

## Set up the Puppeteer project

Create a `puppeteer-tests` directory inside the repository, initialize a Node.js project, and install `puppeteer-core`:

```bash
mkdir puppeteer-tests
cd puppeteer-tests
npm init -y
npm install puppeteer-core
```

`puppeteer-core` skips the automatic download of a bundled browser binary. It uses the system-installed Chrome that you set up earlier. This keeps the install fast and avoids a duplicate browser on disk.

Add a `.gitignore` file inside `puppeteer-tests` to exclude `node_modules` from version control:

```bash
echo "node_modules/" > .gitignore
```

## Install Hugo and start the dev server

The test scripts target the dashboard served locally by Hugo. 

Install Hugo first:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu 24.04" language="bash" >}}
sudo apt-get install -y hugo
  {{< /tab >}}
  {{< tab header="Amazon Linux 2023" language="bash" >}}
curl -L "https://github.com/gohugoio/hugo/releases/download/v0.159.2/hugo_extended_0.159.2_linux-arm64.tar.gz" -o hugo.tar.gz
tar -xzf hugo.tar.gz hugo
sudo mv hugo /usr/local/bin/
  {{< /tab >}}
{{< /tabpane >}}

Verify the installation:

```bash
hugo version
```

The output is similar to:

```output
hugo v0.123.7+extended linux/arm64 BuildDate=2025-07-18T03:41:49Z VendorInfo=ubuntu:0.123.7-1ubuntu0.3
```

The exact version will vary depending on what your package manager installs. Any recent version works.

Start the Hugo development server from the repository root:

```bash
cd $HOME/ecosystem-dashboard-for-arm
hugo server --port 1313 &
```

The `&` runs the server in the background. Wait a few seconds, then confirm that it's ready:

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:1313/linux/
```

You should see `200`. Leave the server running while you work through the tests.

## Create Puppeteer tests

With the server running and the project ready, you can now create the following three tests.

{{< notice Note >}}
All three test scripts pass `--no-sandbox` and `--disable-setuid-sandbox` to Chrome. These flags are required when Chrome runs as a non-root user on a Linux server that hasn't been configured with user namespaces. Cloud instances and CI runners typically fall into this category. Without these flags, Chrome exits immediately with a sandbox initialization error. Including them makes your scripts portable across server environments without any code change.
{{< /notice >}}

### Assert that an NGINX package row is present

The test navigates to the Linux page of the dashboard and checks that the NGINX package row is rendered. It uses the `data-title` attribute that the dashboard sets on each table row to identify packages.

Navigate to the `puppeteer-tests` directory before creating the test files:

```bash
cd $HOME/ecosystem-dashboard-for-arm/puppeteer-tests
```

Create `test-package-status.mjs`:

```javascript
import puppeteer from 'puppeteer-core';

const browser = await puppeteer.launch({
  executablePath: '/usr/bin/google-chrome',
  args: ['--no-sandbox', '--disable-setuid-sandbox'],
  headless: true,
});

const page = await browser.newPage();
await page.goto('http://localhost:1313/linux/', { waitUntil: 'networkidle0' });

// Find the row whose data-title matches "nginx" (case-insensitive)
const row = await page.evaluateHandle(() => {
  const rows = Array.from(document.querySelectorAll('tr[data-title]'));
  return rows.find(r => r.getAttribute('data-title').toLowerCase() === 'nginx') ?? null;
});

const found = await page.evaluate(el => el !== null, row);

if (found) {
  console.log('PASS: NGINX package is present in the rendered dashboard');
  await browser.close();
  process.exit(0);
} else {
  console.error('FAIL: NGINX package row not found');
  await browser.close();
  process.exit(1);
}
```

Run the test:

```bash
node test-package-status.mjs
```

The expected output is:

```output
PASS: NGINX package is present in the rendered dashboard
```

### Validate the official documentation link

This test clicks the NGINX row of the dashboard to expand its sub-row. It waits for the official documentation link to appear and extracts its URL. The test navigates to the URL and asserts that the server returns HTTP `200`.

Create `test-doc-link.mjs`:

```javascript
import puppeteer from 'puppeteer-core';

const browser = await puppeteer.launch({
  executablePath: '/usr/bin/google-chrome',
  args: ['--no-sandbox', '--disable-setuid-sandbox'],
  headless: true,
});

const page = await browser.newPage();
await page.goto('http://localhost:1313/linux/', { waitUntil: 'networkidle0' });

// Click the NGINX row to expand the sub-row containing resource links
const nginxRowIndex = await page.evaluate(() => {
  const rows = Array.from(document.querySelectorAll('tr[data-title]'));
  const idx = rows.findIndex(r => r.getAttribute('data-title').toLowerCase() === 'nginx');
  if (idx === -1) return -1;
  rows[idx].click();
  return idx;
});

if (nginxRowIndex === -1) {
  console.error('FAIL: could not find and click the NGINX row');
  await browser.close();
  process.exit(1);
}

// Wait for the official docs link to become visible in the expanded sub-row
await page.waitForSelector('a[data-source-type="official-docs"]', { timeout: 5000 });

// Scope the link to the sub-row that follows the NGINX row
const docsHref = await page.evaluate((idx) => {
  const allRows = Array.from(document.querySelectorAll('tr'));
  const dataRows = allRows.filter(r => r.hasAttribute('data-title'));
  const nginxRow = dataRows[idx];
  // The sub-row is the next sibling tr after the NGINX row in the full table
  let sibling = nginxRow.nextElementSibling;
  while (sibling) {
    const link = sibling.querySelector('a[data-source-type="official-docs"]');
    if (link) return link.href;
    if (sibling.hasAttribute('data-title')) break; // hit the next package row
    sibling = sibling.nextElementSibling;
  }
  return null;
}, nginxRowIndex);

if (!docsHref) {
  console.error('FAIL: official docs link not found in the NGINX sub-row');
  await browser.close();
  process.exit(1);
}

const response = await page.goto(docsHref);
const status = response.status();

if (status === 200) {
  console.log(`PASS: docs link ${docsHref} returned HTTP ${status}`);
  await browser.close();
  process.exit(0);
} else {
  console.error(`FAIL: docs link ${docsHref} returned HTTP ${status}`);
  await browser.close();
  process.exit(1);
}
```

Run the test:

```bash
node test-doc-link.mjs
```

The expected output is:

```output
PASS: docs link https://www.nginx.com/resources/wiki/start/ returned HTTP 200
```

The exact URL in the output depends on what the dashboard stores for the NGINX official docs entry.

### Capture a screenshot

This test sets a 1920×1080 viewport, navigates to the Linux page, and saves a screenshot as `dashboard.png`.

Create `screenshot.mjs`:

```javascript
import puppeteer from 'puppeteer-core';

const browser = await puppeteer.launch({
  executablePath: '/usr/bin/google-chrome',
  args: ['--no-sandbox', '--disable-setuid-sandbox'],
  headless: true,
});

const page = await browser.newPage();
await page.setViewport({ width: 1920, height: 1080 });
await page.goto('http://localhost:1313/linux/', { waitUntil: 'networkidle0' });
await page.screenshot({ path: 'dashboard.png' });

console.log('Screenshot saved to dashboard.png');
await browser.close();
```

Run the test:

```bash
node screenshot.mjs
```

The expected output is:

```output
Screenshot saved to dashboard.png
```

You'll find `dashboard.png` in your `puppeteer-tests` directory. Copy it to your local machine to view it:

```bash
scp user@your-server-ip:~/ecosystem-dashboard-for-arm/puppeteer-tests/dashboard.png .
```

## Run all three tests

From the `puppeteer-tests` directory, run each script in sequence:

```bash
node test-package-status.mjs
node test-doc-link.mjs
node screenshot.mjs
```

A clean run produces three lines of output, one per script:

```output
PASS: NGINX package is present in the rendered dashboard
PASS: docs link https://www.nginx.com/resources/wiki/start/ returned HTTP 200
Screenshot saved to dashboard.png
```

## What you've accomplished and what's next

You've written and run Puppeteer scripts on the Ecosystem Dashboard for Arm. The scripts check package content, validate a documentation link, and capture a screenshot of the dashboard. 

Next, you'll automate these scripts with GitHub Actions on an Arm runner.
