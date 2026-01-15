---
title: Set up GCP Pub/Sub and IAM for ClickHouse real-time analytics on Axion
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Pub/Sub and IAM Setup on GCP (UI-first)
This section prepares the **Google Cloud messaging and access foundation** required for the real-time analytics pipeline.  
It focuses on **Pub/Sub resource creation and IAM roles**, ensuring Dataflow and the Axion VM can securely communicate.

### Create Pub/Sub Topic
The Pub/Sub topic acts as the **ingestion entry point** for streaming log events.

- Open **Google Cloud Console**
- Navigate to **Pub/Sub → Topics**
- Click **Create Topic**
- Enter:
   - **Topic ID:** `logs-topic`
- Leave encryption and retention as the default
- Click **Create**

This topic will receive streaming log messages from producers.

![Google Cloud Console showing Pub/Sub topic creation screen with logs-topic configured alt-txt#center](images/pub_sub1.png "Pub/Sub Topic")

### Create Pub/Sub Subscription

The subscription allows **Dataflow to pull messages** from the topic.

- Open the newly created `logs-topic`
- Click **Create Subscription**
- Configure:
   - **Subscription ID:** `logs-sub`
   - **Delivery type:** Pull
   - **Ack deadline:** Default (10 seconds)
- Click **Create**

![Google Cloud Console displaying Pub/Sub subscription configuration screen for logs-sub with Pull delivery alt-txt#center](images/pub_sub2.png "Pub/Sub Subscription")

This subscription will later be referenced by the Dataflow pipeline.

### Verify Pub/Sub Resources

Navigate to **Pub/Sub → Topics** and confirm:

- Topic: `logs-topic`
- Subscription: `logs-sub`

This confirms the messaging layer is ready.

![Google Cloud Console Pub/Sub topics list showing logs-topic and logs-sub subscription verified alt-txt#center](images/verify_pub_sub.png "Pub/Sub Resources")

### Identify Compute Engine Service Account

Dataflow and the Axion VM both rely on the **Compute Engine default service account**.

Navigate to:

**IAM & Admin → IAM**

Locate the service account in the format:

```bash
<PROJECT_NUMBER>-compute@developer.gserviceaccount.com
```

This account will be granted the required permissions.

### Assign Required IAM Roles

Grant the following roles to the **Compute Engine default service account**:

| Role | Purpose |
|----|----|
| Dataflow Admin | Create and manage Dataflow jobs |
| Dataflow Worker | Execute Dataflow workers |
| Pub/Sub Subscriber | Read messages from Pub/Sub |
| Pub/Sub Publisher | Publish test messages |
| Storage Object Admin | Read/write Dataflow temp files |
| Service Account User | Allow service account usage |

**Steps (UI):**
- Go to **IAM & Admin → IAM**
- Click **Grant Access**
- Add the service account
- Assign the roles listed above
- Save

![Google Cloud Console IAM page displaying assigned roles for Compute Engine service account including Dataflow and Pub/Sub permissions alt-txt#center](images/roles.webp "Required IAM Roles")

VM OAuth scopes are limited by default. IAM roles are authoritative.

### Create GCS Bucket for Dataflow (UI)

Dataflow requires a Cloud Storage bucket for staging and temp files.

- Go to **Cloud Storage → Buckets**
- Click **Create**
- Configure:
   - **Bucket name:** `imperial-time-463411-q5-dataflow-temp`
   - **Location type:** Region
   - **Region:** `us-central1`
- Leave defaults for storage class and access control
- Click **Create**

![Google Cloud Console showing Cloud Storage bucket creation screen with dataflow-temp bucket configured alt-txt#center](images/bucket.png "GCS Bucket")

### Grant Bucket Access

Ensure the Compute Engine service account has access to the bucket:

- Role: **Storage Object Admin**

This allows Dataflow workers to upload and read job artifacts.

### Validation Checklist

Before proceeding, confirm:

- Pub/Sub topic exists (`logs-topic`)
- Pub/Sub subscription exists (`logs-sub`)
- IAM roles are assigned correctly
- GCS temp bucket is created and accessible

With Pub/Sub and IAM configured, the environment is now ready for **Axion VM setup and ClickHouse installation** in the next phase.
