---
title: Verify connectivity to the Cobalt 100 VM
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Connect over SSH and test the open port

On the **Overview** page of the VM, copy the **Public IP address**. Open a terminal on your local machine, and SSH to the VM (replace *azureuser* if you chose a different admin username):

```bash
ssh -i [path to your pem file] azureuser@[public IP]
```

Replace `[public IP]` with your VM's public IP address, and `[path to your pem file]` with the path to your SSH private key file.

When prompted, confirm the connection to add the VM to your *known_hosts* file.

### Start a temporary HTTP server

If you don't already have an application listening on TCP 8080, you can start one temporarily:

```bash
sudo apt update -y && sudo apt install -y python3
python3 -m http.server 8080
```

Leave this terminal open – the server runs in the foreground.

### Test from your local machine

In a second local terminal run `curl` to confirm that you can reach the server through the NSG rule you created:

```bash
curl http://[public IP]:8080
```

Replace `[public IP]` with your VM's public IP address.

You should see an HTML directory listing (or your application response). A successful response confirms that TCP port 8080 is open and the VM is reachable from the public internet.

To stop the server, press `Ctrl + C`.

You now have an Arm-based Cobalt 100 VM with port 8080 open and ready to receive external traffic. You can use it to run any test server or deploy your own application. 

To learn about optimizing .NET workloads on Cobalt, check out [Migrating a .NET application to Azure Cobalt](../../dotnet-migration/).