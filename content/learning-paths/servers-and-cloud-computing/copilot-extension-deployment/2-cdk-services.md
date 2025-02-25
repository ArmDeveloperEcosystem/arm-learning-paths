---
title: Deploying AWS services
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Which AWS Services do I need?

In the first GitHub Copilot Extension Learning Path, [Build a GitHub Copilot Extension in Python](learning-paths/servers-and-cloud-computing/gh-copilot-simple), you ran a GitHub Copilot Extension on a single Linux computer, with the public URL provided by an ngrok tunnel to your localhost.

For a production environment, you require:

* A domain that you own with DNS settings under your management, for example, through AWS Route 53.
* A load balancer (AWS ALB).
* An auto-scaling cluster (AWS ASG) in a private virtual cloud subnet (AWS VPC) that you can adjust based on the load.

In order to use your custom domain with your ALB, you will also need a custom TLS certificate so the ALB can terminate TLS before forwarding the packets to your ASG instances.

The following sections walk you through setting up all these services in AWS CDK.

## Imports

Inside the `copilot-extension-deployment` directory, there is an auto-generated folder named `copilot_extension_deployment` that contains a file called `copilot_extension_deployment_stack.py`.

Open this file, and add the following import lines:

```python
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_elasticloadbalancingv2 as elbv2,
    aws_autoscaling as autoscaling,
    aws_iam as iam,
    CfnOutput,
    aws_certificatemanager as acm,
    aws_route53 as route53,
    aws_route53_targets as targets
)
```

Then, within the generated class (`class CopilotExtensionDeploymentStack(Stack):`), incorporate all the AWS services you need for your Extension deployment as described below.

## Virtual Private Cloud (VPC)

The code below creates a VPC with one public subnet and one private subnet. Each subnet has a CIDR mask of 24, which means you will get 256 total IPs in each subnet. 

If you need more than this, adjust accordingly:

```python
vpc = ec2.Vpc(self, "FlaskStackVPC",
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Private",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    name="Public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                )
            ]
            )
```

You also need a security group for your EC2 instances:

```python
security_group = ec2.SecurityGroup(self, "EC2SecurityGroup",
                                           vpc=vpc,
                                           allow_all_outbound=True,
                                           description="Security group for EC2 instances"
                                           )
```

## EC2

Once you have set up your VPC templates, you can use them in your EC2 templates.

First, create a User Data script for all the EC2 templates that will launch in your auto-scaling group. 

This installs an SSM agent and the AWS CLI, for future convenience:

```python
user_data = ec2.UserData.for_linux()
user_data.add_commands(
    "apt-get update",
    # Install SSM agent
    "sudo snap install amazon-ssm-agent --classic",
    "sudo systemctl enable snap.amazon-ssm-agent.amazon-ssm-agent.service",
    "sudo systemctl start snap.amazon-ssm-agent.amazon-ssm-agent.service",
    # Install AWS CLI v2
    "apt install unzip",
    'curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"',
    "unzip awscliv2.zip",
    "sudo ./aws/install",
    # add any additional commands that you'd like to run on instance launch here
)
```

After the launch template, get the latest Ubuntu 24.04 Arm AMI:

```python
ubuntu_arm_ami = ec2.MachineImage.lookup(
    name="ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-arm64-server-*",
    owners=["099720109477"],  # Canonical's AWS account ID
    filters={"architecture": ["arm64"]}
)
```

Next, create an IAM role that allows your EC2 instances to use the SSM agent, write logs to CloudWatch, and access AWS S3:

```Python
ec2_role_name = "Proj-Flask-LLM-ALB-EC2-Role"
ec2_role = iam.Role(self, "EC2Role",
                    assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
                    managed_policies=[
                        iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore"),
                        iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchAgentServerPolicy"),
                        iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchLogsFullAccess"),
                        iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess")
                    ],
                    role_name=ec2_role_name,
                    )
```

Now pull all these elements together in the launch template that the ASG will use:

```Python
launch_template = ec2.LaunchTemplate(self, "LaunchTemplate",
                                        instance_type=ec2.InstanceType("c8g.xlarge"),
                                        machine_image=ubuntu_arm_ami,
                                        user_data=user_data,
                                        security_group=security_group,
                                        role=ec2_role,
                                        detailed_monitoring=True,
                                        block_devices=[
                                            ec2.BlockDevice(
                                                device_name="/dev/sda1",
                                                volume=ec2.BlockDeviceVolume.ebs(
                                                    volume_size=50,
                                                    volume_type=ec2.EbsDeviceVolumeType.GP3,
                                                    delete_on_termination=True
                                                )
                                            )
                                        ]
                                        )
```

Finally, create the ASG, specifying the launch template you just created as the launch template for the EC2 instances within the ASG:

```Python
asg = autoscaling.AutoScalingGroup(self, "ASG",
                                    vpc=vpc,
                                    vpc_subnets=ec2.SubnetSelection(
                                        subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
                                    launch_template=launch_template,
                                    min_capacity=1,
                                    max_capacity=1,
                                    desired_capacity=1
                                    )
```

Use a private subnet for security, and start with a single instance. You can scale manually later on, or create an autoscaling function, depending on your needs.

## Application Load Balancer (ALB)

First, create an ALB using the VPC resources that you previously specified, within the `PUBLIC` subnet:

```Python
alb = elbv2.ApplicationLoadBalancer(self, "ALB",
                                vpc=vpc,
                                internet_facing=True,
                                vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
                                )
```

Next, add a custom certificate. Make sure you generate the certificate in advance. 

If you want to do this from the AWS console, see [Getting Started with AWS Certificate Manager](https://aws.amazon.com/certificate-manager/getting-started/).

Then replace `ACM_CERTIFICATE_ARN` with the ARN of your newly-created certificate:

```Python
certificate = acm.Certificate.from_certificate_arn(
    self,
    "Certificate",
    os.environ["ACM_CERTIFICATE_ARN"]
)
```

Next, configure a listener for the ALB that uses the certificate and adds the ASG as a target, listening on port 8080. 

This is where you will serve your Flask app:

```Python
# Add a listener to the ALB with HTTPS
listener = alb.add_listener("HttpsListener",
                            port=443,
                            certificates=[certificate],
                            ssl_policy=elbv2.SslPolicy.RECOMMENDED)

# Add the ASG as a target to the ALB listener
listener.add_targets("ASGTarget",
                        port=8080,
                        targets=[asg],
                        protocol=elbv2.ApplicationProtocol.HTTP,
                        health_check=elbv2.HealthCheck(
                            path="/health",
                            healthy_http_codes="200-299"
                        ))
```

## Custom domain setup in Route 53

The final step in setting up your AWS services is to add an ALB-linked A record to the hosted zone for your domain. This makes sure that when GitHub invokes your API, the DNS is pointed to the IP of your ALB. You will need to replace `HOSTED_ZONE_DOMAIN_NAME` with your hosted zone domain, and replace `SUBDOMAIN_NAME` with the subdomain that maps to the ACM certificate that you generated and used in your ALB.

```Python
hosted_zone = route53.HostedZone.from_lookup(self, "HostedZone",
                                                domain_name=os.environ["HOSTED_ZONE_DOMAIN_NAME"],
                                                )

# Create an A record for the subdomain
route53.ARecord(self, "ALBDnsRecord",
                zone=hosted_zone,
                record_name=os.environ["SUBDOMAIN_NAME"],
                target=route53.RecordTarget.from_alias(targets.LoadBalancerTarget(alb))
                )
```

## How do I deploy?

After you have added all the required sections to your `copilot_extension_deployment_stack.py` file, you can deploy your services to AWS. 

Before you do, make sure your AWS environment is *bootstrapped*, meaning that the AWS CDK has created all necessary resources, such as IAM roles, an ECR repository, and artifact buckets.

This bootstrap process is typically a one-time setup, and can be run by entering:

```bash
cdk bootstrap aws://123456789012/us-east-1
```

Replace the AWS account and region with your account and region.

{{% notice Note %}}
If your organization has governance rules in place regarding naming conventions you will need a custom bootstrap yaml. To learn more about custom bootstrapping, see the [AWS guide  on Bootstrapping your environment for use with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping-env.html).
{{% /notice %}}

After bootstrapping your environment, navigate to the directory containing your stack file and run:

```bash
cdk deploy
```

This deployment might take a few minutes as CloudFormation deploys your resources.
