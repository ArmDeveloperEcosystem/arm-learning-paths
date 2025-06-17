---
title: Verify connectivity to the Cobalt 100 VM
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Connect over SSH and test the open port

1. On the **Overview** page for the VM copy the **Public IP address**.
2. Open a terminal on your local machine and SSH to the VM (replace *azureuser* if you chose a different admin username):

```bash
ssh -i [path to your pem file] azureuser@[public IP]
```

Where `[public IP]` is your public IP and `[path to your pem file]` is the path to your SSH key file.

Accept the prompt to add the host to *known_hosts* the first time you connect.

### Start a simple HTTP server

If you do not already have an application listening on TCP 8080 you can start one temporarily:

```bash
sudo apt update -y && sudo apt install -y python3
python3 -m http.server 8080
```

Leave this terminal open – the server runs in the foreground.

### Test from your local machine

In a second local terminal run `curl` to confirm you can reach the server through the NSG rule you created:

```bash
curl http://[public IP]:8080
```

Where `[public IP]` is your public IP.

You should see an HTML directory listing (or your application response). Receiving a response verifies that TCP 8080 is open and the VM is reachable from the public internet.

Terminate the Python server when you are finished testing (press `Ctrl + C`).

You now have an Arm-based Cobalt 100 VM with an exposed port 8080 that you can use to run any test server. To learn about optimizing .NET workloads on Cobalt, check out [Migrating a .NET application to Azure Cobalt](../../dotnet-migration/).