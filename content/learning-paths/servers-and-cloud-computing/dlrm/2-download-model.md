---
title: Download model weights and data
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Before building the model, you need to obtain the data and model weights. Start by creating directories for the two in your cloud instance.

## Install rclone and

```bash
cd $HOME
mkdir data
mkdir model
```

Install `rclone` using the bash script.

```bash
curl https://rclone.org/install.sh | sudo bash
```

You should see a similar output if the tools installed successfully.
```output
rclone v1.69.1 has successfully installed.
Now run "rclone config" for setup. Check https://rclone.org/docs/ for more details.
```

Configure the credentials as instructed.

```bash
rclone config create mlc-inference s3 provider=Cloudflare \
    access_key_id=f65ba5eef400db161ea49967de89f47b \
    secret_access_key=fbea333914c292b854f14d3fe232bad6c5407bf0ab1bebf78833c2b359bdfd2b \
    endpoint=https://c2686074cb2caf5cbaf6d134bdba8b47.r2.cloudflarestorage.com
```

You will now download the data and model weights. This process takes an hour or more depending on your internet connection.
```bash
rclone copy mlc-inference:mlcommons-inference-wg-public/dlrm_preprocessed $HOME/data  -P
rclone copy mlc-inference:mlcommons-inference-wg-public/model_weights $HOME/model/model_weights -P
```

Once it finishes, you should see that the `model` and `data` directories are populated.

* Overview of Dataset Used in MLPerf DLRM
* Steps to Download and Prepare the Data
* Preprocessing Data for Training and Inference

## Build DLRM image

You will use a branch of the the `Tool-Solutions` repository. This branch includes releases of PyTorch which enhance the performance of ML frameworks.

```bash
cd $HOME
git clone https://github.com/ARM-software/Tool-Solutions.git
cd $HOME/Tool-Solutions/
git checkout ${1:-"pytorch-aarch64--r24.12"}
```

A setup script runs which installs docker and builds a PyTorch image for a specific commit hash. Finally, it runs the MLPerf container which is used for the benchmark in the next section. This script takes around 20 minutes to finish.

```bash
cd ML-Frameworks/pytorch-aarch64/
./build.sh
```

You now have everything set up to analyze the performance. Proceed to the next section to run the benchmark and inspect the results.