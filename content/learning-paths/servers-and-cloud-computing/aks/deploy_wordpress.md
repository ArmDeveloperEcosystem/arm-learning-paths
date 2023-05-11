---
# User change
title: "Deploy a WordPress Example"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Before you begin

You should have an AKS cluster already running from the previous topic. 

You can use the cluster to deploy an example application, WordPress.

## Deploy WordPress Example

### Create Terraform files

The yaml files below are a modified version of the [Kubernetes WordPress Tutorial](https://kubernetes.io/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/) in the Kubernetes documentation. 

You will use three yaml files to deploy WordPress on your AKS cluster:

- `kustomization.yaml`
- `mysql-deployment.yaml`
- `wordpress-deployment.yaml`

1. Use a text editor to create the file `kustomization.yaml` with the code below: 

```console
secretGenerator:
- name: mysql-pass
  literals:
  - password=YourPasswordHere
resources:
  - mysql-deployment.yaml
  - wordpress-deployment.yaml
```

2. Use a text editor to create the file `mysql-deployment.yaml` with the code below: 

```console
apiVersion: v1
kind: Service
metadata:
  name: wordpress-mysql
  labels:
    app: wordpress
spec:
  ports:
    - port: 3306
  selector:
    app: wordpress
    tier: mysql
  clusterIP: None
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mysql-pv-claim
  labels:
    app: wordpress
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: managed-csi
  resources:
    requests:
      storage: 20Gi
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wordpress-mysql
  labels:
    app: wordpress
spec:
  selector:
    matchLabels:
      app: wordpress
      tier: mysql
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: wordpress
        tier: mysql
    spec:
      containers:
      - image: mysql:8.0.30
        name: mysql
        env:
        - name: MYSQL_DATABASE
          value: wordpressdb
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-pass
              key: password
        - name: MYSQL_USER
          value: mysqluser
        - name: MYSQL_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-pass
              key: password
        ports:
        - containerPort: 3306
          name: mysql
        volumeMounts:
        - name: mysql-persistent-storage
          mountPath: /var/lib/mysql
      volumes:
      - name: mysql-persistent-storage
        persistentVolumeClaim:
          claimName: mysql-pv-claim
```

3. Use a text editor to create the file `wordpress-deployment.yaml` with the code below: 

```console
apiVersion: v1
kind: Service
metadata:
  name: wordpress
  labels:
    app: wordpress
spec:
  ports:
    - port: 80
  selector:
    app: wordpress
    tier: frontend
  type: LoadBalancer
  loadBalancerSourceRanges: ["0.0.0.0/0"]
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: wp-pv-claim
  labels:
    app: wordpress
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: managed-csi
  resources:
    requests:
      storage: 20Gi
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wordpress
  labels:
    app: wordpress
spec:
  selector:
    matchLabels:
      app: wordpress
      tier: frontend
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: wordpress
        tier: frontend
    spec:
      containers:
      - image: wordpress:6.0.2-apache
        name: wordpress
        env:
        - name: WORDPRESS_DB_HOST
          value: wordpress-mysql
        - name: WORDPRESS_DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql-pass
              key: password
        - name: WORDPRESS_DB_NAME
          value: wordpressdb
        - name: WORDPRESS_DB_USER
          value: mysqluser
        ports:
        - containerPort: 80
          name: wordpress
        volumeMounts:
        - name: wordpress-persistent-storage
          mountPath: /var/www/html
      volumes:
      - name: wordpress-persistent-storage
        persistentVolumeClaim:
          claimName: wp-pv-claim
```

### Apply the Terraform files 

Run `kubectl apply` to update the configuration:

```console
kubectl apply -k ./
```

The output is similar to:

```output
secret/mysql-pass-9mftfh2cbc created
service/wordpress created
service/wordpress-mysql created
persistentvolumeclaim/mysql-pv-claim created
persistentvolumeclaim/wp-pv-claim created
deployment.apps/wordpress created
deployment.apps/wordpress-mysql created
```

### Confirm WordPress is running

1. Check on volume claims to confirm the 20 Gb of storage has been created for MySQL and WordPress:

```console
kubectl get pvc
```

The output is similar to:

```output
NAME             STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
mysql-pv-claim   Bound    pvc-b5ed7959-9a05-4759-a178-86f7e1393be0   20Gi       RWO            managed-csi    107s
wp-pv-claim      Bound    pvc-cb03c97b-adab-4e4f-ad91-fcfaa69b1a30   20Gi       RWO            managed-csi    107s
```

2. Verify the WordPress and MySQL pods are running:

```console
kubectl get pods
```

The output is similar to:

```output
NAME                               READY   STATUS    RESTARTS   AGE
wordpress-6c5db6d5d7-zznww         1/1     Running   0          5m11s
wordpress-mysql-75467487bf-zs5vk   1/1     Running   0          5m11s
```

3. Verify that the persistent volumes have been attached:

```console
kubectl get volumeattachments
```

The output is similar to:

```output
NAME                                                                   ATTACHER             PV                                         NODE                               ATTACHED   AGE
csi-643e8fc7abcd16d5e98eeffcb0cff690c20aa2fb90a55c38889a570295fa07d2   disk.csi.azure.com   pvc-b5ed7959-9a05-4759-a178-86f7e1393be0   aks-demopool-85935132-vmss000001   true       5m52s
csi-eecaead981dd085e638d388afaa2a325019fcda81bfcda91e867b69d41fc4482   disk.csi.azure.com   pvc-cb03c97b-adab-4e4f-ad91-fcfaa69b1a30   aks-demopool-85935132-vmss000001   true       5m52s
```

4. Get the external IP address of the WordPress deployment:

```console
kubectl get svc
```

The output is similar to:

```output
NAME              TYPE           CLUSTER-IP   EXTERNAL-IP     PORT(S)        AGE
kubernetes        ClusterIP      10.0.0.1     <none>          443/TCP        21m
wordpress         LoadBalancer   10.0.69.21   20.10.212.247   80:31829/TCP   7m23s
wordpress-mysql   ClusterIP      None         <none>          3306/TCP       7m22s
```

The IP address in the `EXTERNAL-IP` column is the one to use.

5. Open the external IP in a browser.

The WordPress welcome screen will be displayed. 

![homescreen_screenshot](https://user-images.githubusercontent.com/67620689/200745521-1e004de9-f982-4b6d-b7e7-638569da2aec.PNG)

You have successfully installed WordPress on your Arm-based AKS cluster.

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```

Answer `yes` at the prompt to destroy all resources. 
