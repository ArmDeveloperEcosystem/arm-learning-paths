---

title: Create a firewall rule for OpenCV browser visualization

weight: 3
 
### FIXED, DO NOT MODIFY

layout: learningpathall

---

## Expose port for OpenCV browser-based visualization

Create a firewall rule in Google Cloud Console to allow browser access to your OpenCV output on port 8000.
 
{{% notice Note %}}

For help with Google Cloud Platform setup, see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).

{{% /notice %}}
 
### Configure the firewall rule

Configure the firewall rule using the Google Cloud Console:
 
1. Open the [Google Cloud Console](https://console.cloud.google.com/), navigate to **VPC Network > Firewall**, and select **Create firewall rule**.
 
![Google Cloud Console VPC Network Firewall page showing the Create firewall rule button in the top menu bar#center](images/firewall-rule.png "Create a firewall rule in Google Cloud Console")
 
2. Set the **Name** of the new rule to **allow-opencv-port**. Select the network that you intend to bind to your VM.
 
3. For **Direction of traffic**, select **Ingress**.  

4. For **Allow on match**, select **Allow**.  

5. For **Targets**, select **Specified target tags**.  

6. For **Target tags**, enter **allow-opencv**.  

7. Set **Source IPv4 ranges** to your current machine's public IP address. Run the following command in a terminal on your local machine to find the address:

```bash
curl -4 ifconfig.me
```

The `-4` flag forces an IPv4 response. Take the returned address and append `/32` to convert it to CIDR notation, for example `203.0.113.42/32`. Restricting access to your own IP prevents port 8000 from being exposed to the public internet.

{{% notice Note %}}If your IP address changes or you need to access the visualization from a different machine, update this field with the new IP address. Using `0.0.0.0/0` opens the port to all traffic and is not recommended.{{% /notice %}}
 
![Google Cloud Console Create firewall rule form configured for OpenCV with Ingress and Allow settings#center](images/network-rule.png "Configuring the OpenCV firewall rule")
 
 
8. For **Protocols and ports**, select **Specified protocols and ports**.
 
9. Select the **TCP** checkbox and, for **Ports**, enter **8000**.
 
10. Select **Create**.

![Google Cloud Console Protocols and ports section showing TCP checkbox selected with port 8000 configured for OpenCV browser visualization#center](images/network-port.png "Setting ports in the firewall rule")

## What you've accomplished and what's next

You've now created a firewall rule for OpenCV visualization that enables external browser access to your VM and exposes port 8000 for real-time pipeline outputs.

Next, you'll create a Google Axion virtual machine to host your OpenCV application.
