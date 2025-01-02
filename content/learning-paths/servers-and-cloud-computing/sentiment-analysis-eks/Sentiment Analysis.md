---
title: Cluster monitoring with Prometheus and Grafana in Amazon EKS
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

You will need an [AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html). Create an account if needed. 

Four tools are required on your local machine. Follow the links to install each tool.

* [Kubectl](/install-guides/kubectl/)
* [AWS CLI](/install-guides/aws-cli/)
* [Docker](/install-guides/docker/)
* [Terraform](/install-guides/terraform/)

To use the AWS CLI, you will need to generate AWS access keys and configure the CLI. Follow the [AWS Credentials](/install-guides/aws_access_keys/) install guide for instructions. 

## Setup sentiment analysis

Take a look at the [GitHub repository](https://github.com/koleini/spark-sentiment-analysis) then clone it on your local computer:

```console
git clone https://github.com/koleini/spark-sentiment-analysis.git
cd spark-sentiment-analysis
```

Edit the file `eks/variables.tf` if you want to change the default AWS region.

The default value is at the top of the file and is set to `us-east-1`.

```output
variable "AWS_region" {
  default     = "us-east-1"
  description = "AWS region"
}
```

Execute the following commands to create the Amazon EKS cluster:

```console
terraform init
terraform apply --auto-approve
```

Update the `kubeconfig` file to access the deployed EKS cluster with the following command:

If you want to use an AWS CLI profile not named `default`, change the profile name before running the command. 

```console
aws eks --region $(terraform output -raw region) update-kubeconfig --name $(terraform output -raw cluster_name) --profile default
```

Create a service account for Apache spark

```console
kubectl create serviceaccount spark
kubectl create clusterrolebinding spark-role --clusterrole=edit --serviceaccount=default:spark --namespace=default
```

## Build the sentiment analysis JAR file

Navigate to the `sentiment_analysis` folder and create a JAR file for the sentiment analyzer:

```console
cd sentiment_analysis
sbt assembly
```

A JAR file is created at the following location:

```console
sentiment_analysis/target/scala-2.13/bigdata-assembly-0.1.jar
```

## Create a Spark container image

Create a repository in Amazon ECR to store the docker images. You can also use Docker Hub.

The Spark repository contains a script to build the container image you need to run inside the Kubernetes cluster. 

Execute this script on your Arm-based computer to build the arm64 image.

In the current working directory, clone the `apache spark` github repository prior to building the image

```console
git clone https://github.com/apache/spark.git
cd spark
git checkout v3.4.3
```

Build the docker container using the following commands. Substitute the name of your container repository before running the commands.

```console
cp ../sentiment_analysis/target/scala-2.13/bigdata-assembly-0.1.jar jars/
bin/docker-image-tool.sh -r <your-docker-repository> -t sentiment-analysis build
bin/docker-image-tool.sh -r <your-docker-repository> -t sentiment-analysis push
```

## Run Spark computation on the cluster

Execute the `spark-submit` command within the Spark folder to deploy the application. The following commands will run the application with two executors, each with 12 cores, and allocate 24GB of memory for both the executors and driver pods.

Set the following variables before executing the `spark-submit` command:

```console
export MASTER_ADDRESS=<K8S_MASTER_ADDRESS>
export ES_ADDRESS=<IP_ADDRESS_OF_ELASTICS_SEARCH>
export CHECKPOINT_BUCKET=<BUCKET_NAME>
export EKS_ADDRESS=<EKS_REGISTERY_ADDRESS>
```

Execute the `spark-submit` command:

```console
bin/spark-submit \
      --class bigdata.SentimentAnalysis \
      --master k8s://$MASTER_ADDRESS:443 \
      --deploy-mode cluster \
      --conf spark.executor.instances=2 \
      --conf spark.kubernetes.container.image=532275579171.dkr.ecr.us-east-1.amazonaws.com/spark:sentiment-analysis \
      --conf spark.kubernetes.driver.pod.name="spark-twitter" \
      --conf spark.kubernetes.namespace=default \
      --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark \
      --conf spark.driver.extraJavaOptions="-DES_NODES=4$ES_ADDRESS -DCHECKPOINT_LOCATION=s3a://$CHECKPOINT_BUCKET/checkpoints/" \
      --conf spark.executor.extraJavaOptions="-DES_NODES=$ES_ADDRESS -DCHECKPOINT_LOCATION=s3a://$CHECKPOINT_BUCKET/checkpoints/" \
      --conf spark.executor.cores=12 \
      --conf spark.driver.cores=12 \
      --conf spark.driver.memory=24g \
      --conf spark.executor.memory=24g \
      --conf spark.memory.fraction=0.8 \
      --name sparkTwitter \
      local:///opt/spark/jars/bigdata-assembly-0.1.jar
```

Use `kubectl get pods` to check the status of the pods in the cluster.

```output
NAME                                        READY   STATUS    RESTARTS   AGE
sentimentanalysis-346f22932b484903-exec-1   1/1     Running   0          10m
sentimentanalysis-346f22932b484903-exec-2   1/1     Running   0          10m
spark-twitter                               1/1     Running   0          12m
```

## Twitter sentiment analysis

Create a twitter(X) [developer account](https://developer.x.com/en/docs/x-api/getting-started/getting-access-to-the-x-api) and create a `bearer token`. 

Use the following commands to set the token and fetch the Tweets:

```console
export BEARER_TOKEN=<BEARER_TOKEN_FROM_X>
python3 scripts/xapi_tweets.py
```

You can modify the script `xapi_tweets.py` with your own keywords. 

Here is the code which includes the keywords: 

```output
query_params = {'query': "(#onArm OR @Arm OR #Arm OR #GenAI) -is:retweet lang:en",
                'tweet.fields': 'lang'}
```
