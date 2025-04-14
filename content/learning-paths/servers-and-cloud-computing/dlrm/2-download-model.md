---
title: Download model weights and data
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Before building the model, you'll need to obtain the data and model weights. 

Start by creating directories for the data and model weights on your cloud instance.

```bash
cd $HOME
mkdir data
mkdir model
```
## Install rclone

You'll use `rclone` to [download the data and model weights](https://github.com/mlcommons/inference/tree/master/recommendation/dlrm_v2/pytorch#download-preprocessed-dataset).

Install `rclone` using the bash script:

```bash
curl https://rclone.org/install.sh | sudo bash
```

You should see a similar output if the tools installed successfully:

```output
rclone v1.69.1 has successfully installed.
Now run "rclone config" for setup. Check https://rclone.org/docs/ for more details.
```

Configure the following credentials for rclone:

```bash
rclone config create mlc-inference s3 provider=Cloudflare \
    access_key_id=f65ba5eef400db161ea49967de89f47b \
    secret_access_key=fbea333914c292b854f14d3fe232bad6c5407bf0ab1bebf78833c2b359bdfd2b \
    endpoint=https://c2686074cb2caf5cbaf6d134bdba8b47.r2.cloudflarestorage.com
```

Run the commands below to download the data and model weights. This process can take 30 minutes or more depending on the internet connection in your cloud instance.

```bash
rclone copy mlc-inference:mlcommons-inference-wg-public/dlrm_preprocessed $HOME/data  -P
rclone copy mlc-inference:mlcommons-inference-wg-public/model_weights $HOME/model/model_weights -P
```

Once it finishes, you should see that the `model` and `data` directories are populated. With the data in place, you can proceed to run the benchmark in order to measure the performance of the downloaded DLRM model.

