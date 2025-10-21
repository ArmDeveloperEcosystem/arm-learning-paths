## Setup and Configuration for Ubuntu-based EC2 instance

### Create Ubuntu EC2 Instance

AWS EC2 instances can be used to simulate edge devices when edge device hardware isn't available.  

We'll start by opening our AWS Console and search for EC2:

![AWS Console](../images/EC2_Setup_1.png)

We'll now open the EC2 console page:

![AWS EC2 Console](../images/EC2_Setup_2.png)

Select "Launch instance". Provide a Name for the EC2 instance and select the "Ubuntu" Quick Start option. Additionally, select "64-bit(Arm)" as the architecture type and select "t4g.large" as the Instance type:

![Create EC2 Instance](../images/EC2_Setup_3.png)

Additionally, please click on "Create new Key Pair" and provide a name for a new SSH key pair that will be used to SSH into our EC2 instance. Press "Create key pair":

![Create EC2 Keypair](../images/EC2_Setup_4.png)

>**_NOTE:_**
>You will notice that a download will occur with your browser. Save off this key (a .pem file) as we'll use it shortly.

Next, we need to edit our "Network Settings" for our EC2 instance... scroll down to "Network Settings" and press "Edit":

![Security Group](../images/EC2_Setup_4_ns.png)

Press "Add security group rule" and lets allow port tcp/4912:

![Security Group](../images/EC2_Setup_4_4912.png)

Lets also give the EC2 instance a bit more disk space. Please change the "8" to "28" here:

![Increase Diskspace](../images/EC2_Setup_5.png)

Finally, press "Launch instance". You should see your EC2 instance getting created:

![Launch Instance](../images/EC2_Setup_6.png)

Now, press "View all instances" and press the refresh button... you should see your new EC2 instance in the "Running" state:

![Running Instance](../images/EC2_Setup_7.png)

You can scroll over and save off your Public IPv4 IP Address. You'll need this to SSH into your EC2 instance. 

Lets now confirm that we can SSH into our EC2 instance. With the saved off pem file and our EC2 Public IPv4 IP address, lets ssh into our EC2 instance
  
>**_NOTE:_**
>In this example, my pem file is named	DougsEC2SimulatedEdgeDeviceKeyPair.pem and my EC2 instances' public IP address is 1.2.3.4

	chmod 600 DougsEC2SimulatedEdgeDeviceKeyPair.pem
	ssh -i ./DougsEC2SimulatedEdgeDeviceKeyPair.pem ubuntu@1.2.3.4

You should see a login shell now for your EC2 instance!

![Login Shell](../images/EC2_Setup_8.png)

Excellent! You can keep that shell open as we'll make use of it when we start installing Greengrass a bit later. 

Lastly, lets install the prerequisites that we need. Please run these commands to add some required dependencies:

	sudo apt update	
	sudo apt install -y curl unzip
	sudo apt install -y gcc g++ make build-essential nodejs sox gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps
	
Additionally, we need to install the prerequisites for AWS IoT Greengrass "classic":

	sudo apt install -y default-jdk  

Before we go to the next section, lets also save off this JSON - it will be used to configure our AWS Greengrass custom component a bit later:

#### Non-Camera configuration

	{     
	   "Parameters": { 
	      "node_version": "20.18.2",
	      "vips_version": "8.12.1",
	      "device_name": "MyEC2EdgeDevice",
	      "launch": "runner",
	      "sleep_time_sec": 10,
	      "lock_filename": "/tmp/ei_lockfile_runner",
	      "gst_args": "filesrc:location=/home/ggc_user/data/testSample.mp4:!:decodebin:!:videoconvert:!:videorate:!:video/x-raw,framerate=2200/1:!:jpegenc",
	      "eiparams": "--greengrass",
	      "iotcore_backoff": "-1",
	      "iotcore_qos": "1",
	      "ei_bindir": "/usr/local/bin",
	      "ei_sm_secret_id": "EI_API_KEY",
	      "ei_sm_secret_name": "ei_api_key",
	      "ei_poll_sleeptime_ms": 2500,
	      "ei_local_model_file": "/home/ggc_user/data/currentModel.eim",
	      "ei_shutdown_behavior": "wait_on_restart",
	      "ei_ggc_user_groups": "video audio input users system",
	      "install_kvssink": "no",
	      "publish_inference_base64_image": "no",
	      "enable_cache_to_file": "no",
	      "cache_file_directory": "__none__",
	      "enable_threshold_limit": "no",
	      "metrics_sleeptime_ms": 30000,
	      "default_threshold": 50,
	      "threshold_criteria": "ge",
	      "enable_cache_to_s3": "no",
	      "s3_bucket": "__none__" 
	   }  
	}

OK, Lets proceed to the next step and get our Edge Impulse environment setup!

[Next](../../edgeimpulseprojectbuild/)
