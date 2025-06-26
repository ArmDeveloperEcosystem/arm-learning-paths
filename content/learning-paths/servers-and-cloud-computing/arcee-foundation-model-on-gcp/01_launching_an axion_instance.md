---
title: Launching an Axion c4a instance
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## System Requirements

  - A Google Cloud account with billing enabled

  - Quota for c4a instances in your preferred region

  - A Linux or MacOS host

  - A c4a-standard-4 or larger instance

  - At least 128GB of storage

## Google Cloud Console Steps

Follow these steps to launch your Compute Engine instance using the Google Cloud Console:

### Step 1: Launch Compute Engine Instance

1. **Navigate to Google Cloud Console**

   - Go to the [Google Cloud Console](https://console.cloud.google.com)

   - Make sure you're in the correct project

   - In the left navigation menu, click "Compute Engine" > "VM instances"

2. **Create Instance**

   Click "CREATE INSTANCE" button

3. **Configure Instance Details**

   - **Name**: Enter `arcee-axion-instance`

   - **Region**: Select a region where c4a instances are available (e.g., us-central1, us-east1, europe-west1)

   - **Zone**: Select any zone in the chosen region

   - **Machine family**: Select "General urpose"

   - **Series**: Select "C4A"

   - **Machine type**: Select `c4a-standard-32` or larger
     - This provides 32 vCPUs and 128 GB memory

4. **Configure OS and Storage**

   In the left menu, click on "OS and storage"

   - Click "Change".

   - **Size (GB)**: Set to `128`

   - Click "Select"

5. **Configure Networking**

   In the left menu, click on "Networking"

   - Click 

   - **Important**: We'll configure SSH access through IAP (Identity-Aware Proxy) for security

7. **Create Instance**

   - Review all settings

   - Click "Create" at the bottom of the screen.

### Step 3: Connect to Your Instance

  After a minute or so, the instance should be available.

   - In the VM instances list, locate the instance name (`arcee-axion-instance`) and click on "SSH"

   - This opens a browser-based SSH terminal. You may need to accept some security message

   - No additional configuration is needed

   - You should now be connected to your Ubuntu instance

### Important Notes

- **Region Selection**: Ensure you're in a region where c4a instances are available

- **Quota**: Make sure you have sufficient quota for c4a instances in your selected region

- **Security**: The browser-based SSH connection is more secure as it uses Google's Identity-Aware Proxy

- **Storage**: The 128GB boot disk is sufficient for the Arcee model and dependencies

- **Cost**: Monitor your usage in the Google Cloud Console billing section

- **Backup**: Consider creating snapshots for backup purposes