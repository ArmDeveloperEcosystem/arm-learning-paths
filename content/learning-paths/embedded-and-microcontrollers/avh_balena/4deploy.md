---
title: "Deploy an application to your device"
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Deploy from Balena Hub

You can build and deploy your own custom applications on Balena OS, or use a pre-built application from [Balena Hub](https://hub.balena.io/). 

As an example, you can deploy a Grafana dashboard from Balena Hub that will show the state of your Balena OS device.

Open Balena Hub in a new tab by clicking on the Balena Hub button on the top right corner of your Balena Cloud dashboard.

![Balena Cloud dashboard header showing the Balena Hub button in the top right corner next to other navigation elements#center](balena_hub_button.png "Balena Hub button location")

On the Balena Hub, click `Apps` in the top navigation bar, then search for `balena-app`. This is a pre-built dashboard backed by Grafana and served by Nginx.

![Balena Hub Apps page displaying search results for balena-app, showing the application card with description and deployment options#center](balena_hub_app.webp "balena-app in Balena Hub")

Click on the app to open the details page.

Look for the `Deploy` button in the upper-right corner of the page.

Clicking this button takes you back to your Balena Cloud dashboard with a dialog to deploy `balena-app` to a fleet.

![Deployment dialog showing fleet selection options with AVH-Testing fleet highlighted and advanced configuration settings collapsed#center](balena_app_deploy.png "Deploy balena-app to fleet")

Select `Use an existing fleet instead` and choose the `AVH-Testing` fleet.

You don't need to do any advanced configuration for this app. Click the `Deploy to fleet` button to begin the deployment.

{{% notice Note %}}
If you have more than one device in your fleet, this process deploys the selected application to all devices in your fleet simultaneously.
{{% /notice %}}

Once the deployment finishes, click on your device in Balena Cloud dashboard to open up the device page. You'll see that the Grafana and Nginx services have been deployed to and are running on your device.

![Balena Cloud device page showing active services with Grafana and Nginx containers running, including service status indicators and log output#center](balena_app_running.webp "balena-app services running on device")

You'll also be able to see the system logs from your device, and optionally get access to the device's terminal from this Balena Cloud screen.

## Access your Grafana dashboard

Your application is now running, but it's not accessible from the outside world. To view your Grafana dashboard in your browser, you need to tell Balena to make your device accessible from a public URL. 

Toggle the `Public Device URL` switch to the `On` position.

A link appears next to the switch, click on it to open the newly created public URL.

![Balena-app login screen showing username and password fields over a dark background with the Grafana logo and branding#center](balena_app_login.webp "balena-app login page")

This opens the `balena-app` on your device in your browser. You're presented with a log in screen, use the default username `admin` and password `admin` to log in. You'll be prompted to set a new password for the `admin` user before continuing.

![Grafana dashboard showing real-time system metrics including CPU usage, memory consumption, network traffic, and container status for the Balena OS device#center](balena_app_dashboard.webp "balena-app dashboard with system metrics")

You now see the Grafana dashboard monitoring your Balena OS installation on this device, including the containers running Grafana and Nginx.
