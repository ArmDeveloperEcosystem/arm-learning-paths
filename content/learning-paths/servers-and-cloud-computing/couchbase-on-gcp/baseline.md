---
title: Perform Couchbase baseline testing
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Verify Couchbase cluster health and prepare a benchmarking bucket
This section guides you through verifying that Couchbase is installed and running on your GCP SUSE VM with Arm64 architecture. You'll set up your cluster, confirm your node is healthy, and use the web console to create a bucket. After completing these steps, your environment is ready for benchmarking.

## Set up the default cluster 
Once Couchbase is running, set up your default cluster for the first time.

Open the **Couchbase Web Console** in your browser using your VM's public IP address from the previous step:

```console
http://<VM-Public-IP>:8091
```

Select **Set up new cluster** to begin the initial configuration.

![Couchbase Web Console setup screen showing fields for cluster name, administrator password, and a button labeled Set up new cluster. The interface is clean and organized with a sidebar on the left and main setup form in the center. The environment appears welcoming and straightforward, designed to guide users through initial cluster configuration. Visible text includes Set up new cluster, Cluster Name, Administrator Password, and Set up new cluster button. alt-text#center](images/cluster-setup-1.png "Set up new cluster")

Provide a name for your cluster (for example, "my_cluster") and create a password for your administrator account (leaving the username as the default `Administrator`).

![Couchbase Web Console showing the cluster creation screen with fields for cluster name and administrator password. The main form is centered with a sidebar on the left. Visible text includes Set up new cluster, Cluster Name, Administrator Password, and Set up new cluster button. The interface is clean and welcoming, designed to guide users through initial cluster setup. alt-text#center](images/cluster-setup-2.png "Create cluster and admin count")
Check the **Accept Terms** box to agree to the license terms. Then select **Configure Disk Memory Services** to continue with the cluster setup.

![Couchbase Web Console showing the Accept Terms screen for cluster setup. The main form displays a checkbox labeled Accept Terms and a button labeled Configure Disk Memory Services. The interface is clean and organized with a sidebar on the left and the setup form centered. Visible text includes Accept Terms and Configure Disk Memory Services. The environment feels welcoming and guides users through the initial configuration process. alt-text#center](images/cluster-setup-3.png "Accept Terms")

Accept the defaults of your cluster configuration and select "Save & Finish".

![Couchbase Web Console showing the final configuration screen for cluster setup. The main form displays fields and buttons for finalizing cluster settings, including disk, memory, and services configuration. The sidebar is visible on the left, and the interface is organized and welcoming, designed to guide users through the last step of cluster setup. Visible text includes Finalize configuration, Configure Disk Memory Services, and Save Finish. The environment feels supportive and clear, helping users complete the initial Couchbase cluster configuration. alt-text#center](images/cluster-setup-4.png "Finalize configuration")
Your default cluster is now set up. Save the password you created for your Administrator account. You'll need this password for future steps, including verifying cluster health and creating your benchmarking bucket.

## Verify cluster nodes
Run the following command to verify that your Couchbase node is healthy. Replace `password` with the Administrator password you set earlier.

```console
/opt/couchbase/bin/couchbase-cli server-list \
  -u Administrator -p password --cluster localhost
```

The expected output is:

```output
ns_1@cb.local 127.0.0.1:8091 healthy active
```

If you see `healthy active`, your Couchbase node is running correctly and ready for benchmarking.

```console
/opt/couchbase/bin/couchbase-cli server-list \
  -u Administrator -p password --cluster localhost
```

```output
ns_1@cb.local 127.0.0.1:8091 healthy active
```

## Prepare a Couchbase bucket for benchmarking
Once the service is running, you can access the Couchbase Web Console to create a bucket for benchmarking.

Open the Couchbase Web Console in your browser. Enter your VM's public IP address from the previous step, followed by `:8091`. For example:

```console
http://<VM-Public-IP>:8091
```

Use the admin `username` (default is "Administrator") and `password` you created during Couchbase cluster setup in the previous step.

![Couchbase Dashboard showing cluster health, server statistics, and bucket status. The dashboard displays panels for cluster overview, server nodes, and buckets, with status indicators for health and activity. Text in the image includes Cluster Overview, Servers, Buckets, and Health. The interface is organized and visually clear, designed to help users monitor Couchbase performance and status. The environment feels professional and supportive, encouraging users to review system health and resource usage. alt-text#center](images/dashboard-1.png "Couchbase Dashboard")

On the left sidebar, select **Buckets** to view your bucket list.

In the upper right corner, select **Add Bucket** to start creating a new bucket for benchmarking.

![Couchbase Web Console showing the Add Bucket screen. The main form displays fields for bucket name, bucket type, and memory quota. The sidebar is visible on the left, and the Add Bucket button is highlighted in the upper right corner. Transcribed text includes Bucket Name, Bucket Type, Memory Quota, and Add Bucket. The interface is organized and welcoming, designed to guide users through bucket creation. The environment feels supportive and clear, encouraging users to set up a new Couchbase bucket for benchmarking. alt-text#center](images/create-bucket-1.png "Create Bucket")

Now name your bucket `benchmark`. For **Bucket Type**, select **Couchbase**. Set the **Memory Quota** to **512 MB**. These settings help ensure your benchmarking results are accurate and consistent on your Arm-based GCP VM.

![Couchbase Web Console displaying the Add Bucket form with fields for Bucket Name, Bucket Type, and Memory Quota. The user is entering benchmark as the bucket name, selecting Couchbase as the bucket type, and setting the memory quota to 512 MB. The Add Bucket button is visible in the upper right corner. The sidebar on the left shows navigation options. Transcribed text includes Bucket Name, Bucket Type, Memory Quota, and Add Bucket. The environment is organized and supportive, guiding users through the process of creating a new bucket for benchmarking. alt-text#center](images/create-bucket-2.png "Create Bucket")

| **Parameter** | **Value** |
|----------------|-----------|
| **Bucket Name** | benchmark |
| **Bucket Type** | Couchbase |
| **Memory Quota** | 512 MB |

You should now see that your bucket has been created:

![Couchbase Web Console showing the newly created benchmark bucket listed under Buckets. The main panel displays a table with columns for Bucket Name, Bucket Type, and Memory Quota. The benchmark bucket appears with type Couchbase and memory quota 512 MB. The sidebar on the left provides navigation options. Visible text includes Bucket Name, Bucket Type, Memory Quota, and benchmark. The environment is organized and supportive, confirming successful bucket creation and encouraging users to continue with benchmarking tasks. alt-text#center](images/create-bucket-3.png "Created Bucket")

## Understanding buckets in Couchbase

A bucket in Couchbase works like a database. It stores and organizes your data. In this guide, you created a benchmark bucket specifically for load testing and performance benchmarking. Setting the Memory Quota (RAM Quota) ensures Couchbase reserves enough memory for fast, in-memory data operations. This helps you get accurate performance results on your Arm-based GCP VM.

You can now proceed to the next section for benchmarking to measure Couchbase's performance.
