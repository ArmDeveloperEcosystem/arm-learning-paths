---
# User change
title: "Deploy Arm based VMs using the console"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Generate an SSH key pair

Generate an SSH key pair (public key, private key) using `ssh-keygen` to use for Arm VMs access. To generate the key pair, follow this [documentation](/install-guides/ssh#ssh-keys).

{{% notice Note %}}
If you already have an SSH key pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}

## Deploy Arm based VMs via GUI
Log in to your Google account and in the Google Cloud console, go to the [VM instances page](https://console.cloud.google.com/compute/instances?_ga=2.159262650.1220602700.1668410849-523068185.1662463135) ( you may need to enable the API the first time).

![image](https://user-images.githubusercontent.com/67620689/202090364-2946214c-2347-4538-b2b0-3a36f45caee0.PNG)

Select your project

![image](https://user-images.githubusercontent.com/67620689/202095985-103deaa4-610d-45ea-a84c-65af2bbfec41.PNG)

Click on Create instance

![image](https://user-images.githubusercontent.com/67620689/202090934-aa0aa2da-e0f7-4aea-b8db-bc4988b781b2.PNG)

Specify a Name for your VM. For more information, see [Resource naming convention](https://cloud.google.com/compute/docs/naming-resources#resource-name-format).

![image](https://user-images.githubusercontent.com/67620689/202098830-532b5dc8-f6b5-4cff-931c-ec41edd08516.PNG)

Choose a Zone for this VM that supports [Tau T2A](https://cloud.google.com/compute/docs/general-purpose-machines#t2a_machines). Tau T2A is only available in select regions and zones. Check the [available regions and zones](https://cloud.google.com/compute/docs/regions-zones#available) information to find out which regions offer Tau T2A.

![image](https://user-images.githubusercontent.com/67620689/202097168-6208b6ae-3627-47b3-a397-7783769e6727.PNG)

Select `GENERAL-PURPOSE` from the Machine family options. Select `T2A` from the Series and a `T2A` Machine type from the drop-down menu.

![image](https://user-images.githubusercontent.com/67620689/203740482-d820ced1-5eeb-4c07-99a3-18a7a7511966.PNG)

In the Boot disk section, click Change.

![image](https://user-images.githubusercontent.com/67620689/204448755-f1259724-a386-4dc3-9b88-8ece7057d4de.PNG)

Then on the `PUBLIC IMAGES` tab, choose the following:
 * The default Debian-11-Arm64 image or any other supported Arm OS. Here Ubuntu 22.04 LTS is chosen.
 * Boot disk type
 * Boot disk size

Then click on select.

![image](https://user-images.githubusercontent.com/67620689/204448774-b75b0c07-5cc3-4aa2-8d5d-0e0ced437e22.PNG)

Now expand the Advance options section then click on Security. Expand VM access and add the public key by clicking on `ADD ITEM`.

![image](https://user-images.githubusercontent.com/67620689/225616099-8fc7791a-24b3-4195-b957-154eaca43080.PNG)

To create and start the VM, click Create.

![image](https://user-images.githubusercontent.com/67620689/202098038-7bfb0b6c-af18-4d5c-92a8-ca90a57bc25b.PNG)

## SSH into the launched instance
Run following command to connect to VM through SSH:

```
ssh <username>@<Public IP>
```
{{% notice Note %}}
Replace `<username>` with the user name that created the SSH key you have uploaded. The `<Public IP>` can be retrieved from the console when the instance is online.
{{% /notice %}}

Output should be similar to:

```output
The authenticity of host '34.91.147.54 (34.91.147.54)' can't be established.
ECDSA key fingerprint is SHA256:xwUGlczMr7M0ekr3g4axqREera7wUsCc1vEWpeENUAo.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '34.91.147.54' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 22.04.2 LTS (GNU/Linux 5.15.0-1030-gcp aarch64)
```
