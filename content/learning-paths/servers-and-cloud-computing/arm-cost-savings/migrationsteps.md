---
title: How to Migrate an x86 Workload to Arm64 on AWS
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### 1. Assess Workload Compatibility

Before migrating, determine whether your applications can run on 64-bit Arm architecture. Most modern applications built with portable runtimes (e.g., Java, Go, Python, Node.js) can run seamlessly on 64-bit Arm with little or no modifications. Check your container images and dependencies for 64-bit Arm compatibility. Fortunately, our [pipelines-tutorial](https://www.google.com/url?q=https://github.com/openshift/pipelines-tutorial&sa=D&source=editors&ust=1749822472442265&usg=AOvVaw1m8Dc2XNThwRLw9jJ9AX-L) doesn't have these restrictions.

### 2. Enable Multi-Arch Support in Red Hat OpenShift

Red Hat OpenShift supports multi-architecture workloads, allowing you to run both 64-bit x86 and 64-bit Arm based nodes in the same cluster. Red Hat OpenShift's [documentation](https://www.google.com/url?q=https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/postinstallation_configuration/configuring-multi-architecture-compute-machines-on-an-openshift-cluster%23multi-architecture-verifying-cluster-compatibility_creating-multi-arch-compute-nodes-aws&sa=D&source=editors&ust=1749822472444182&usg=AOvVaw3zaXidSPcmXJdpHXRLF8jq) will be your guide for this process.

### 3. Add 64-bit Arm MachineSets

To migrate to Graviton-based EC2 instances:

Ensure that the Red Hat Openshift cluster is using the multi-arch release payload.

```
$oc adm release info -o jsonpath="{ .metadata.metadata}"
{"release.openshift.io/architecture":"multi","url":"https://access.redhat.com/errata/xxx"}$

```

* Decide on a scheduling strategy. Manual with Taints/Tolerations, or [Multiarch Tuning O](https://www.google.com/url?q=https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/postinstallation_configuration/configuring-multi-architecture-compute-machines-on-an-openshift-cluster%23multiarch-tuning-operator&sa=D&source=editors&ust=1749822472450131&usg=AOvVaw1zslJ0RW8K9Lq_t6bf9Jrt)[perator](https://www.google.com/url?q=https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/postinstallation_configuration/configuring-multi-architecture-compute-machines-on-an-openshift-cluster%23multiarch-tuning-operator&sa=D&source=editors&ust=1749822472450917&usg=AOvVaw1QxXa3syc7ziLPLvut2YZv).
    Since we have 1 workload (our build pipeline) we'll go the Taint and Toleration routes. We've added this taint to our new Arm machine sets:

```   
  taints:

    - effect: NoSchedule

        key: newarch

        value: arm64
```
This prevents existing x86 workloads from being scheduled to the Arm nodes.

* Reimport needed imagestreams with import-mode set to 'PreserveOriginal'

```
    oc import-image php -n openshift --all --confirm --import-mode='PreserveOriginal'
    oc import-image python -n openshift --all --confirm --import-mode='PreserveOriginal'
```

### 4. Rebuild and Verify Container Images

Note: Red Hat OpenShift only supports native architecture container builds. Cross-architecture container builds are not supported.

To build 64-bit Arm compatible images, we've modified the openshift-pipelines tutorial to patch deployments with the Tekton Task's podTemplate information. This will allow us to pass a podTemplate for building and deploying our newly built application on the target architecture. It also makes it easy to revert back to 64-bit x86 by re-running the pipeline without the template.

Create a podTemplate defining a toleration and a node affinity to make the builds deploy on arm machines:

arm64.yaml
```
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

            * "arm64"

        - key: "kubernetes.io/os"

            operator: "In"

            values:

            - "linux"
```

Next we update 02\_update\_deployment\_task.yaml
This includes extract patching to include the podTemplate's nodeAffinity/tolerations.

02\_update\_deployment\_task.yaml
```
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
And we need to update 04\_pipeline.yaml to pass the taskrun-name to the update-deployment task:

```
- name: update-deployment

    taskRef:

    name: update-deployment

    params:

    - name: deployment

        value: $(params.deployment-name)

    - name: IMAGE

        value: $(params.IMAGE)

    - name: taskrun-name //add these

        value: $(context.taskRun.name) //lines
```

Now we can redeploy the UI and API using the arm64.yaml podTemplate. This will force all parts of the build pipeline and deployment to our tainted 64-bit Arm nodes.
```
tkn pipeline start build-and-deploy \\\\

--prefix-name build-deploy-api-pipelinerun-arm64 \\\\

-w name=shared-workspace,volumeClaimTemplateFile=https://raw.githubusercontent.com/openshift/pipelines-tutorial/master/01\_pipeline/03\_persistent\_volume\_claim.yaml \\\\

-p deployment-name=pipelines-vote-api \\\\

-p git-url=https://github.com/openshift/pipelines-vote-api.git \\\\

-p IMAGE=image-registry.openshift-image-registry.svc:5000/pipelines-tutorial/pipelines-vote-api-arm64

--use-param-defaults \\\\
--pod-template arm64.yaml
```
```
tkn pipeline start build-and-deploy \\\\

--prefix-name build-deploy-ui-pipelinerun-arm64 \\\\

-w name=shared-workspace,volumeClaimTemplateFile=https://raw.githubusercontent.com/openshift/pipelines-tutorial/master/01\_pipeline/03\_persistent\_volume\_claim.yaml \\\\

-p deployment-name=pipelines-vote-ui \\\\

-p git-url=https://github.com/openshift/pipelines-vote-ui.git \\\\

-p IMAGE=image-registry.openshift-image-registry.svc:5000/pipelines-tutorial/pipelines-vote-ui-arm64 \\\\

--use-param-defaults \\\\
--pod-template arm64.yaml
```

Once the pods are up and running, you can safely remove the x86 worker nodes from the cluster, and remove the taints from the Arm worker nodes (if you choose to do so).


