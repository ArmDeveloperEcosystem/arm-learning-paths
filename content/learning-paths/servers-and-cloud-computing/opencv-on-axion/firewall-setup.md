---

title: Create a firewall rule for OpenCV Browser Visualization

weight: 3
 
### FIXED, DO NOT MODIFY

layout: learningpathall

---
 
Create a firewall rule in Google Cloud Console to expose the required port for OpenCV browser-based visualization.
 
{{% notice Note %}}

For help with GCP setup, see the Learning Path [Getting started with Google Cloud Platform](/learning-paths/servers-and-cloud-computing/csp/google/).

{{% /notice %}}
 
## Configure the firewall rule
 
Navigate to the [Google Cloud Console](https://console.cloud.google.com/), go to **VPC Network > Firewall**, and select **Create firewall rule**.
 
![Google Cloud Console VPC Network Firewall page showing the Create firewall rule button in the top menu bar#center](images/firewall-rule.png "Create a firewall rule in Google Cloud Console")
 
Next, create the firewall rule that exposes the required port for OpenCV visualization.
 
Set the **Name** of the new rule to "allow-opencv-port". Select your network that you intend to bind to your VM.
 
Set **Direction of traffic** to "Ingress".  

Set **Allow on match** to "Allow".  

Set **Targets** to "Specified target tags".  

Enter "allow-opencv" in the **Target tags** field.  

Set **Source IPv4 ranges** to "0.0.0.0/0".
 
![Google Cloud Console Create firewall rule form configured for OpenCV with Ingress and Allow settings#center](images/network-rule.png "Configuring the OpenCV firewall rule")
 
## Configure port
 
Under **Protocols and ports**, select **Specified protocols and ports**.
 
Select the **TCP** checkbox and enter:
 
```text
8000
```

Then select **Create**.

![Google Cloud Console Protocols and ports section showing TCP checkbox selected with port 8000 configured for OpenCV Browser Visualization#center](images/network-port.png "Setting Ray ports in the firewall rule")

## What you've accomplished and what's next
In this section, you:

* Created a firewall rule for OpenCV visualization
* Enabled external browser access to your VM
* Exposed port 8000 for real-time pipeline outputs

Next, you'll:

* Run image and video pipelines
* Integrate ML models with OpenCV
* Optimize performance on Arm-based systems
