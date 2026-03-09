---
title: Set up your Edge Impulse project
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create an Edge Impulse account

Edge Impulse is an ML platform that lets you build, train, optimize, and deploy models for edge devices. In this section, you create an account, clone a pre-built project, build a deployment for your Arm device, and generate an API key.

Navigate to [Edge Impulse Studio](https://studio.edgeimpulse.com) and select **Sign Up** in the upper-right corner:

![Edge Impulse Studio login page with the Sign Up button in the upper-right corner#center](./images/ei_signup_1.png "Edge Impulse sign-up page")

Fill in the requested information and select **Sign Up**:

![Edge Impulse sign-up form with fields for name, email, and password#center](./images/ei_signup_2.png "Complete the sign-up form")

After a successful sign-up, a confirmation message appears. Select **Click here to build your first ML model**:

![Confirmation message after successful Edge Impulse account creation#center](./images/ei_signup_3.png "Successful sign-up confirmation")

A wizard appears to help you create a default project:

![Edge Impulse new project wizard showing initial setup options#center](./images/ei_signup_4.png "New project wizard")

You can dismiss the wizard by selecting the **-** button in the upper-right corner. This reveals your new default project:

![Edge Impulse dashboard showing a newly created default project#center](./images/ei_signup_5.png "New default project")

Now that your account is ready, clone an existing project that already has a trained model. You'll use this model throughout the Learning Path.

## Clone the project into your account

Navigate to this public project:

https://studio.edgeimpulse.com/studio/524106

![Edge Impulse public project page for the Cat and Dog Detector model#center](./images/ei_clone_1.png "Public project page")

Select the **Clone this project** button in the upper-right corner. A dialog appears to confirm the clone:

![Clone project dialog with default settings and a Clone Project button#center](./images/ei_clone_2.png "Clone project dialog")

Leave the default settings and select **Clone Project** in the lower-right corner. The cloning process starts:

![Progress indicator showing the project clone in progress#center](./images/ei_clone_3.png "Cloning in progress")

The cloning process takes about 12 minutes to complete. When it finishes, a completion message appears:

![Completion message indicating the project clone finished successfully#center](./images/ei_clone_4.webp "Clone complete")

Select **Dashboard** to view the cloned project. It should look similar to the following:

![Edge Impulse dashboard showing the cloned Cat and Dog Detector project with model details#center](./images/ei_clone_5.webp "Cloned project dashboard")

You now have the project you'll use for this Learning Path.

## Build your project deployment

Edge Impulse Studio provides a workflow to build, train, optimize, and deploy ML models. Take a moment to explore the project dashboard:

![Edge Impulse Studio dashboard showing the project overview with data, impulse, and deployment sections#center](./images/ei_project_1.png "Project dashboard overview")

Central to Edge Impulse is the concept of an *Impulse*, which is a pipeline that defines how sensor data is processed, what model runs on it, and how results are interpreted. Your cloned project already has an Impulse called "Cat and Dog Detector". Select **Create Impulse** on the left sidebar to see the three main parts: the pre-processing block, the model block, and the post-processing block:

![Create Impulse view showing the three pipeline blocks: pre-processing, model, and post-processing#center](./images/ei_project_2.webp "Impulse pipeline structure")

Select **Object Detection** on the left sidebar to see details about the model used in the Impulse:

![Object Detection page showing the model architecture and training results#center](./images/ei_project_3.webp "Object Detection model details")

The Impulse in this project is already created, trained, and optimized, so you don't need to walk through those steps. Edge Impulse provides extensive [examples and documentation](https://docs.edgeimpulse.com) to guide you through creating your own Impulse from scratch:

![Edge Impulse documentation page showing available guides and tutorials#center](./images/ei_project_4.webp "Edge Impulse documentation")

Now deploy the model to your specific edge device type. Depending on the hardware you selected earlier, choose the matching deployment target:

![Deployment page showing available target device options including Linux AARCH64 and other platforms#center](./images/ei_project_5.webp "Deployment target options")

Select the appropriate target for your device and select **Build**. For example, if you're using a Raspberry Pi 5 or an EC2 Graviton instance, choose **Linux (AARCH64)** to run the model on the CPU:

![Build dialog with the Linux AARCH64 target selected and the Build button highlighted#center](./images/ei_project_6.webp "Build deployment")

{{% notice Note %}}
For these edge device targets, select the **int8** quantization option before selecting **Build**. The **Linux (AARCH64)** target is suitable for many Linux-class Arm-based 64-bit devices where the CPU runs the model.
{{% /notice %}}

With the deployment built, the next step is to create an API key that connects the Greengrass component to your Edge Impulse project.

## Create your project API key

The Edge Impulse Runner on your device uses an API key to authenticate with your project and download the model. Select **Dashboard** on the left sidebar:

![Edge Impulse project dashboard with the Dashboard link highlighted in the left sidebar#center](./images/ei_key_1.webp "Project dashboard")

Select **Keys**:

![Dashboard view with the Keys tab visible in the project settings area#center](./images/ei_key_2.webp "Keys tab")

Select **Add new API key** in the upper-right corner. Enter a name for the key, set the role to **admin**, and confirm that **Set as development key** is selected. Then select **Create API key**:

![API key creation dialog with fields for name, role set to admin, and the development key checkbox selected#center](./images/ei_key_3.webp "Create API key")

The API key appears on the screen. Copy and save it immediately — this is the only time the full key is visible. You'll store this key in AWS Secrets Manager in a later step.

## What you've accomplished

In this section, you created an Edge Impulse account, cloned a pre-built Cat and Dog Detector project, built a deployment for your Arm device, and generated an API key. In the next section, you install AWS IoT Greengrass on your edge device.