---
title: Use Veraison Service for CCA Attestation
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Use Your AWS Deployment to Verify a CCA Attestation Token
Now that your Veraison services are deployed into AWS and initialized with endorsements for the CCA reference platform, you are ready to make use of the verification service to verify a CCA attestation token.

To do this, you should follow the steps set out in the Learning Path [Get Started with CCA Attestation and Veraison](/learning-paths/servers-and-cloud-computing/cca-veraison/). Follow the steps in this Learning Path exactly, except you'll use your AWS-hosted Veraison deployment instead of Linaro's service.

The URL for the Veraison server provided by Linaro is `https://veraison.test.linaro.org:8443`.

Instead of this URL, use the one for your own Veraison service, which will be of the form `https://services.example-veraison.com:8443`, although you need to replace `example-veraison.com` with your AWS domain.

Apart from this URL change, you also need to use a newer versions of `evcli`.

When cloning `evcli` source code use commit:
``` bash
git -C evcli checkout 0e253e8
```


## Cleanup

Once you are done with your AWS services for this learning path, you can clean things up to save on AWS costs. Back on the Ubuntu host:

```bash
cd $HOME/cca_veraison/services/deployments/aws

# Confirm that we still have the correct environment (both should be set prior)
echo $AWS_REGION
echo $VERAISON_DEB

# Delete all AWS resources we created in this learning path (from veraison repo readme)
./bin/veraison delete-stack services
./bin/veraison delete-stack rds
./bin/veraison delete-image keycloak
./bin/veraison delete-image services
./bin/veraison delete-image sentinel
./bin/veraison delete-signing-key
./bin/veraison delete-key-pair
./bin/veraison delete-deb

# Force delete the Cloud Formation stacks
aws cloudformation delete-stack --stack-name veraison-support
aws cloudformation wait stack-delete-complete --stack-name veraison-support || \
aws cloudformation delete-stack --stack-name veraison-support --deletion-mode FORCE_DELETE_STACK

aws cloudformation delete-stack --stack-name veraison-vpc
aws cloudformation wait stack-delete-complete --stack-name veraison-vpc || \
aws cloudformation delete-stack --stack-name veraison-vpc --deletion-mode FORCE_DELETE_STACK

# Force delete the secret without deletion delay
aws secretsmanager delete-secret \
    --secret-id veraison-ear-signer \
    --force-delete-without-recovery \
    --region ${AWS_REGION}

# Clean up the local cache
state_dir="${XDG_DATA_HOME:-$HOME/.local/share}/veraison/aws"
state_backup="${state_dir}.backup-$(date +%Y%m%d-%H%M%S)"
cp -a -- "$state_dir" "$state_backup"
for entry in key vpc support services images signer-key-arn; do
  ./bin/veraison --deployment-name veraison cache --delete "$entry" || break
done
```

{{% notice Note %}}
The above deletion steps will delete most of the AWS resources created by this learning path. However, any failed deployments may partially/wholly remain and will require manual deletion from the AWS console. Be sure to double check via the AWS console including examining AWS dashboardds for:  Cloud Formation, ElastiCache, RDS and Aurora, Secrets Manager, and EC2 for any residual resources that might be dangling after the above deletions.
{{% /notice %}}
