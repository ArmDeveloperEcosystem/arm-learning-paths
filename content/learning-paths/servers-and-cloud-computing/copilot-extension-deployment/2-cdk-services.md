---
title: Deploying AWS services
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## What AWS services do I need?

In [the first GitHub Copilot Extension Learning Path](learning-paths/servers-and-cloud-computing/gh-copilot-simple) you ran a GitHub Copilot Extension from a single Linux computer, with the public URL being provided by an ngrok tunnel to your localhost.

In an actual production environment, you'll want:

* A domain that you own with DNS settings that you control (you can get this through AWS Route 53)
* A load balancer (AWS ALB)
* An auto-scaling cluster (AWS ASG) in a private virtual cloud subnet (AWS VPC) that you can adjust the size of based on load

In order to use your custom domain with your ALB, you'll also need a custom TLS certificate in order to allow the ALB to do TLS termination before the ALB forwards the packets to your ASG instances.

The following sections will walk you through setting up all these required services in AWS CDK.

## Imports

You will have an auto-generated folder called `copilot_extension_deployment` within the `copilot-extension-deployment` that you previously created. It will contain a file called `copilot_extension_deployment_stack.py`. Open this file, and add the following import lines:

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

Then, within the generated class, add the services denoted in the sections below.

## Virtual Private Cloud (VPC)

This will create a VPC with a public and private subnet. These subnets have a CIDR mask of 24, which means you'll get 256 total IPs in each subnet. If you need more than this, adjust accordingly.

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

You'll also need a security group for the EC2 instances, along with egress on port 5000:

```python
security_group = ec2.SecurityGroup(self, "EC2SecurityGroup",
                                           vpc=vpc,
                                           allow_all_outbound=True,
                                           description="Security group for EC2 instances"
                                           )
security_group.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(5000), "Allow incoming traffic on port 5000")
```

## EC2

Once you have your VPC templates set up, you can use them in your EC2 templates.

First, create a User Data script for all the EC2 templates that will launch in your auto-scaling group. This will install an SSM agent and the AWS CLI, for later convenience:

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

After the launch template, you'll want to get the latest Ubuntu 24.04 Arm AMI:

```python
ubuntu_arm_ami = ec2.MachineImage.lookup(
    name="ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-arm64-server-*",
    owners=["099720109477"],  # Canonical's AWS account ID
    filters={"architecture": ["arm64"]}
)
```

Next create an IAM role that will allow your EC2 instances to use the SSM agent, write logs to CloudWatch, and access AWS S3:

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

As you can see, you'll want the instances inside your private subnet for security, and you only need one instance to begin with. You can scale manually later on, or create an autoscaling function, depending on your needs.

## Application Load Balancer (ALB)

First, create an ALB using the VPC resources you previously specified, within the PUBLIC subnet:

```Python
alb = elbv2.ApplicationLoadBalancer(self, "ALB",
                                vpc=vpc,
                                internet_facing=True,
                                vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
                                )
```

Next add a custom certificate. You'll need to generate this certificate beforehand. If you want to do this from the AWS console, see [Getting Started with AWS Certificate Manager](https://aws.amazon.com/certificate-manager/getting-started/).

Replace `ACM_CERTIFICATE_ARN` with the ARN of your newly created certificate:

```Python
certificate = acm.Certificate.from_certificate_arn(
    self,
    "Certificate",
    os.environ["ACM_CERTIFICATE_ARN"]
)
```

Next configure a listener for the ALB that uses the certificate and adds the ASG as a target, listening on port 8080 (this is where you'll serve your Flask app):

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

## Route 53

