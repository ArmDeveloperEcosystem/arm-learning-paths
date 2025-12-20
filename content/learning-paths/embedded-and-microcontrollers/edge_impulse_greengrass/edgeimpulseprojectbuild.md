---
title: 2. Edge Impulse Project Setup
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Creating our Edge Impulse Environment

The next step is to create our Edge Impulse environment. Edge Impulse provides a simple solution to creating and building a ML model for specific edge devices focused on specific tasks.  Lets get started. 

### 1. Create Edge Impulse Account

Lets create our account in Edge Impulse. Navigate to https://studio.edgeimpulse.com and select "Sign Up" down in the right hand corner:

![Sign Up](./images/EI_SignUp_1.png)

Next, fill in the requested information and press "Sign Up":

![Complete Information](./images/EI_SignUp_2.png)

If successful, you will be promoted as follows. Press "Click here to build your first ML model":

![Successful Sign Up](./images/EI_SignUp_3.png)

You will be presented with a wizard to create a new default project:

![Intro Wizard To create ML Model](./images/EI_SIgnUp_4.png)

You can dismiss the wizard by pressing the "-" in the upper right hand corner... this will reveal your current new default project:

![New Project](./images/EI_SignUp_5.png)

Next, we will clone an existing project that has a model that has already been created for you and which we will use for this workshop. On to the next step!

### 2. Clone Project Into Your Account

Next, we are going to clone an existing project into our own space. Navigate to this public project: 

https://studio.edgeimpulse.com/studio/524106

![Public Project](./images/EI_Clone_1.png)

Press the "Clone this project" button in the upper right. You will be presented with a dialog that will initiate the clone:

![Clone Project](./images/EI_Clone_2.png)

Leave everything defaulted and press "Clone Project" in the lower right. The cloning process will commence:

![Start Project Clone](./images/EI_Clone_3.png)

The cloning process will take about 12 minutes to complete. When it is complete:

![Completed Clone](./images/EI_Clone_4.png)

Next, click "Dashboard" to view your project... it should look something like this:

![My Cloned Project](./images/EI_Clone_5.png)

OK! We now have the project we will use for the workshop... lets continue by exploring the project a bit and creating a deployment for our own edge device. Onward!

### 3. Build your project's deployment

Let's have a look at some of the features in Edge Impulse studio. From a high level, Edge Impulse studio provides a solution to build, train, optimize, and deploy ML models for any edge device:

![Edge Impulse](./images/EI_Project_1.png)

Key in this is the "Impulse".  On the left side of the dashboard, our "Impulse" has been created for us and is called "Cat and Dog Detector". Click on "Create Impulse". You will see that there are 3 main parts of a "Impulse":  The pre-processing block, the model block, and the post-processing block:

![Edge Impulse](./images/EI_Project_2.png)

Clicking on "Object Detection" on the left, you will see some detail on the model that has been utilized in our Impulse:

![Edge Impulse](./images/EI_Project_3.png)

In our project, the "Impulse" is fully created, trained, and optimized so we won't have to walk through those steps.  Edge Impulse has a ton of [examples and documentation](https:://docs.edgeimpulse.com) to walk you through your first "Impulse" creation:

![Edge Impulse](./images/EI_Project_4.png)

What we want to do now is to deploy our model to a specific edge device type.  Depending on the specific hardware you are using in this workshop, you can choose from the following deployment edge device choices:

![Edge Impulse](./images/EI_Project_5.png)

Please select the appropriate choice and press "Build" (Example, for Raspberry Pi, choose "Linux(AARCH64)" to run the model on the CPU of the RPi:

![Edge Impulse](./images/EI_Project_6.png)

	NOTE:  For these edge device choices, please select the "int8" option 
	prior to pressing "Build". 

	NOTE: The "Linux(AARCH64)" is suitable for many Linux-class ARM-based 
	64bit devices where only the CPU will be used to run the model. 

Now that we have built our deployment, we are ready to move on to the next step - creating an API Key. Lets do this!

### 4. Create your project API key

Lastly, lets create our API key for our project. We'll use this key to connect our Greengrass component's environment to our Edge Impulse project. Click on the "Dashboard"  on the left hand side of our project:

![Edge Impulse Dashboard](./images/EI_Key_1.png)

Press "Keys":

![Edge Impulse Dashboard](./images/EI_Key_2.png)

Press "Add new API key" on the upper right side. Provide a name for the key. The role should be "admin" and "Set as development key" should be selected. Press "Create API key":

![Edge Impulse Dashboard](./images/EI_Key_3.png)

You will then be presented with the API key. Make a copy of this key as this will be the only time you will be able to see the full key for copying. We will place this key into AWS Secret Manager shortly so be sure to save it now!!

OK!  We are making good progress!  Next up, we are going to install AWS IoT Greengrass into our edge device. Lets go!