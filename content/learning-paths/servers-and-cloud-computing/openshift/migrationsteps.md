---
title: Migrate an x86 workload to Arm on AWS
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Migrating container workloads from x86 to Arm on AWS can help reduce cloud costs, improve energy efficiency, and enhance performance. This Learning Path shows you how to assess workload compatibility, enable multi-architecture support in Red Hat OpenShift, configure Arm64 nodes, rebuild and verify container images, and transition your deployments safely.

This example uses the [OpenShift Pipelines Tutorial](https://github.com/openshift/pipelines-tutorial) as the baseline and assumes it is running on x86 infrastructure.

## Assess workload compatibility

Before migrating, confirm that your applications can run on the Arm 64-bit (`arm64`) architecture. Most modern applications built with portable runtimes such as Java, Go, Python, or Node.js run on Arm with little or no changes. Check your container images and dependencies for compatibility.

Use the following tools to inspect container images for multi-architecture support:

- [KubeArchInspect](/learning-paths/servers-and-cloud-computing/kubearchinspect/): scans container images in your Kubernetes cluster.
- [Docker inspect script](/learning-paths/cross-platform/docker/check-images/): checks local image manifests for platform variants.

{{% notice Note %}}
The OpenShift Pipelines Tutorial supports `arm64` and has no architecture restrictions.
{{% /notice %}}


## Enable multi-architecture support in Red Hat OpenShift

OpenShift supports multi-architecture workloads, allowing you to run x86 and Arm nodes in the same cluster.

To check if your cluster is multi-architecture compatible, run:

```bash
oc adm release info -o jsonpath="{ .metadata.metadata }"
```

If the output includes:

```json
"release.openshift.io/architecture": "multi"
```

...then your cluster supports multi-architecture nodes.

If your cluster is not multi-architecture compatible, you must migrate it to use the multi-architecture release payload. This involves updating your OpenShift cluster to a version that supports multi-architecture and switching to the multi-architecture payload. For step-by-step instructions, see the OpenShift documentation on [migrating to a cluster with multi-architecture compute machines](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html-single/updating_clusters/#migrating-to-multi-payload). Once migration is complete, you can add compute nodes with different architectures.

## Add 64-bit Arm MachineSets

To take advantage of Arm-based compute, you need to add new MachineSets to your OpenShift cluster that use Arm (Graviton) EC2 instances. This step enables your cluster to schedule workloads on Arm nodes, allowing you to run and test your applications on the target architecture while maintaining your existing x86 nodes for a smooth migration.

## Decide on a scheduling strategy

When introducing Arm nodes into your OpenShift cluster, you need to control which workloads are scheduled onto these new nodes. There are two main approaches:

- **Manual scheduling with Taints and Tolerations:** by applying a taint to your Arm nodes, you ensure that only workloads with a matching toleration are scheduled there. This gives you precise control over which applications run on Arm, making it easier to test and migrate workloads incrementally.
- **Automated scheduling with the Multiarch Tuning Operator:** this operator helps automate the placement of workloads on the appropriate architecture by managing node affinity and tolerations for you. This is useful for larger environments or when you want to simplify multi-architecture workload management.

For manual scheduling, add the following taint:

```yaml
taints:
  - effect: NoSchedule
    key: newarch
    value: arm64
```

This prevents existing x86 workloads from being scheduled to the Arm nodes, ensuring only workloads that explicitly tolerate this taint will run on Arm.

## Reimport needed ImageStreams with import-mode set to PreserveOriginal

When running workloads on Arm nodes, you may need to ensure that the required container images are available for the arm64 architecture. OpenShift uses ImageStreams to manage container images, and by default, these may only include x86 (amd64) images.

To make arm64 images available, you should reimport the necessary ImageStreams with the `PreserveOriginal` import mode. This ensures that all available architectures for an image are imported and preserved, allowing your Arm nodes to pull the correct image variant.

For example, to reimport the `php` and `python` ImageStreams:

```bash
oc import-image php -n openshift --all --confirm --import-mode='PreserveOriginal'
oc import-image python -n openshift --all --confirm --import-mode='PreserveOriginal'
```

{{% notice Note %}}
This avoids image pull errors when deploying on Arm nodes.
{{% /notice %}}


## Rebuild and verify container images

To build 64-bit Arm compatible images, the OpenShift Pipelines Tutorial has been modified to patch deployments with the Tekton Task's podTemplate information. This will allow you to pass a podTemplate for building and deploying your newly built application on the target architecture. It also makes it easy to revert back to 64-bit x86 by re-running the pipeline without the template.

{{% notice Note %}}
Red Hat OpenShift only supports native builds. Cross-architecture builds are not supported.
{{% /notice %}}

## Define a podTemplate
Create a podTemplate defining a toleration and a node affinity to make the builds deploy on Arm machines.

Save the following as `arm64.yaml`:

```yaml
tolerations:
  - key: "newarch"
    value: "arm64"
    operator: "Equal"
    effect: "NoSchedule"
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
        - matchExpressions:
            - key: "kubernetes.io/arch"
              operator: "In"
              values:
                - "arm64"
            - key: "kubernetes.io/os"
              operator: "In"
              values:
                - "linux"
```

Next the `02_update_deployment_task.yaml` file needs to be updated. This includes extract patching to include the podTemplate's nodeAffinity/tolerations.

Modify the file `02_update_deployment_task.yaml` to contain the information below:

```yaml
apiVersion: tekton.dev/v1
kind: Task
metadata:
name: update-deployment
spec:
params:
- name: deployment
    description: The name of the deployment patch the image
    type: string
- name: IMAGE
    description: Location of image to be patched with
    type: string
- name: taskrun-name
    type: string
    description: Name of the current TaskRun (injected from context)
    steps:
    - name: patch
        image: image-registry.openshift-image-registry.svc:5000/openshift/cli:latest
        command: \["/bin/bash", "-c"\]
        args:
        - |-
            oc patch deployment $(inputs.params.deployment) --patch='{"spec":{"template":{"spec":{
            "containers":\[{
            "name": "$(inputs.params.deployment)",
            "image":"$(inputs.params.IMAGE)"
            }\]
            }}}}'
            \# Find my own TaskRun name
            MY\_TASKRUN\_NAME="$(params.taskrun-name)"
            echo "TaskRun name: $MY\_TASKRUN\_NAME"
            \# Fetch the podTemplate
            PODTEMPLATE\_JSON=$(kubectl get taskrun "$MY\_TASKRUN\_NAME" -o jsonpath='{.spec.podTemplate}')
            if \[ -z "$PODTEMPLATE\_JSON" \]; then
            echo "No podTemplate found in TaskRun...Remove tolerations and affinity."
            oc patch deployment "$(inputs.params.deployment)" \\\\
            --type merge \\\\
            -p "{\\"spec\\": {\\"template\\": {\\"spec\\": {\\"tolerations\\": null, \\"affinity\\": null}}}}"
            else
            echo "Found podTemplate:"
            echo "$PODTEMPLATE\_JSON"
            oc patch deployment "$(inputs.params.deployment)" \\\\
            --type merge \\\\
            -p "{\\"spec\\": {\\"template\\": {\\"spec\\": $PODTEMPLATE\_JSON }}}"
            fi
            \# issue: https://issues.redhat.com/browse/SRVKP-2387
            \# images are deployed with tag. on rebuild of the image tags are not updated, hence redeploy is not happening
            \# as a workaround update a label in template, which triggers redeploy pods
            \# target label: "spec.template.metadata.labels.patched\_at"
            \# NOTE: this workaround works only if the pod spec has imagePullPolicy: Always
            patched\_at\_timestamp=\`date +%s\`
            oc patch deployment $(inputs.params.deployment) --patch='{"spec":{"template":{"metadata":{
            "labels":{
            "patched\_at": '\\"$patched\_at\_timestamp\\"'
            }
            }}}}'
```

Finally the `04_pipeline.yaml` needs to be updated to pass the taskrun-name to the update-deployment task. The modifications are below:

```yaml
- name: update-deployment
  taskRef:
    name: update-deployment
  params:
    - name: deployment
      value: $(params.deployment-name)
    - name: IMAGE
      value: $(params.IMAGE)
    - name: taskrun-name
      value: $(context.taskRun.name)
```

Now the UI and API can be redeployed using the `arm64.yaml` podTemplate. This will force all parts of the build pipeline and deployment to the tainted Arm nodes.

Run the `tkn` command:

```bash
tkn pipeline start build-and-deploy --prefix-name build-deploy-api-pipelinerun-arm64 -w name=shared-workspace,volumeClaimTemplateFile=https://raw.githubusercontent.com/openshift/pipelines-tutorial/master/01_pipeline/03_persistent_volume_claim.yaml -p deployment-name=pipelines-vote-api -p git-url=https://github.com/openshift/pipelines-vote-api.git -p IMAGE=image-registry.openshift-image-registry.svc:5000/pipelines-tutorial/pipelines-vote-api-arm64 --use-param-defaults --pod-template arm64.yaml
```

Once the pods are up and running, you can safely remove the x86 worker nodes from the cluster, and remove the taints from the Arm worker nodes (if you choose to do so).

### Conclusion

Automating native builds for different architectures using Red Hat OpenShift Pipelines on Red Hat OpenShift 4.18 on AWS streamlines the development and deployment of versatile applications. 

By setting up distinct pipelines that leverage nodeSelector to build on x86 and Arm nodes, you ensure that your application components are optimized for their target environments. This approach provides a clear and manageable way to embrace multi-architecture computing in the cloud.