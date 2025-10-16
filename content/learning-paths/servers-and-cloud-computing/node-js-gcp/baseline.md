---
title: Node.js baseline testing on Google Axion C4A Arm Virtual machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


Since Node.js has been successfully installed on your GCP C4A Arm virtual machine, please follow these steps to make sure that it is running.

## Validate Node.js installation with a baseline test

### 1. Run a Simple REPL Test
The Node.js REPL (Read-Eval-Print Loop) allows you to run JavaScript commands interactively.

```console
node
```
Inside the REPL, type:

```console
console.log("Hello from Node.js");
```
You should see an output similar to:

```output
Hello from Node.js
undefined
```
This confirms that Node.js can execute JavaScript commands successfully.

### 2. Test a Basic HTTP Server
You can now create a small HTTP server to validate that Node.js can handle web requests.

Create `app.js`.  For example, you can type "vi app.js" in the SSH shell and then insert the following code:

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Baseline test successful!\n');
});

server.listen(3000, '0.0.0.0', () => {
  console.log('Server running at http://0.0.0.0:3000/');
});
```
 - This server listens on port 3000.
 - Binding to 0.0.0.0 allows connections from any IP, not just localhost.

Run the server in the background:

```console
node app.js &
```
You should see an output similar to:

```output
Server running at http://0.0.0.0:3000/
```
{{% notice Note %}}
Make sure your GCP firewall allows TCP traffic on port 3000. On SUSE Arm64, internal firewalls are usually disabled, so only the GCP firewall needs to be configured.

```console
sudo zypper install -y firewalld
sudo firewall-cmd --permanent --add-port=3000/tcp
sudo firewall-cmd --reload
```
{{% /notice %}}
#### Test Locally with Curl

```console
curl http://localhost:3000
```

You should see an output similar to:

```output
Baseline test successful!
```

#### Test from a Browser
Also, you can access it from the browser with your VM's public IP. Run the following command to print your VM’s public URL, then open it in a browser:

```console
echo "http://$(curl -s ifconfig.me):3000/"
```

You should see the following message in your browser, confirming that your Node.js HTTP server is running successfully:

![Node.js Browser alt-text#center](images/node-browser.png)

This verifies the basic functionality of the Node.js installation before proceeding to the benchmarking.
