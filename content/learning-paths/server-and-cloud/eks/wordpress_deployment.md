---
title: "Deploy WordPress example"
weight: 3
layout: learningpathall
---

## Prerequisites

* [An EKS cluster](/learning-paths/server-and-cloud/eks/cluster_deployment/)

## WordPress Deployment Files
We use three yaml files to deploy WordPress: kustomization.yaml, mysql-deployment.yaml, and wordpress-deployment.yaml.
Using an editor of your choice, create these files and copy the contents into them as shown.

Lets start with `kustomization.yaml`
```console
secretGenerator:
- name: mysql-pass
  literals:
  - password=YourPasswordHere
resources:
  - mysql-deployment.yaml
  - wordpress-deployment.yaml
```

This file allows us to set passwords for the MySQL database. The resources section selects which files these kustomizations apply to. Information on working with kustomizations is in the [Kubernetes documentation](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/).

The next file is `mysql-deployment.yaml`.
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
  storageClassName: gp2
  resources:
    requests:
      storage: 5Gi
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

This file will deploy a pod with a MySQL container. There are three objects defined. The first object (line 2) is a Service object. This will create a service called wordpress-mysql. This service will be assigned to be the front end to the MySQL pod through the use of a selector. Therefore, whenever a pod within the cluster wants to communicate with the MySQL pod, it will communicate using the wordpress-mysql service name.

The next object defined (line 16) is a Persistent Volume Claim (PVC). This object is used to mount storage inside the MySQL pod. A key point to understand is that the PVC object is not what creates the storage. It is a declaration of a type of storage that we want available to the cluster. As shown above, we are declaring that we need 5GiB of storage.

The last object created (line 30) is a Deployment. Inside the deployment spec (line 35), we have some selector labels (lines 36-39). Notice that these labels match the labels in the Service object (lines 10-12). This match is what assigns the wordpress-mysql service to the MySQL pod. Within the deployment spec, there is also a pod spec (line 47), where we configure the MySQL container we want deployed in the pod.

The last file is `wordpress-deployment.yaml` which is shown below.
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
  storageClassName: gp2
  resources:
    requests:
      storage: 5Gi
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

Similar to the MySQL yaml, this file creates three objects. First, there is a Service object (line 2) that is named wordpress (line 4). This service exposes port 80 (line 9) and has its type set to LoadBalancer.

The second object is a PVC (line 17). This is similar to what was explained for the MySQL yaml.

The last object is a Deployment (line 31). In the pod spec (line 48), we set the MySQL user and password to match the MySQL non-root user and password in the MySQL yaml file. This password is how WordPress has permission to read/write to the MySQL database pod.

## WordPress Deployment
Navigate to the directory that contains kustomization.yaml, mysql-deployment.yaml, and wordpress-deployment.yaml. Enter the following command to apply above configuration.
```console
kubectl apply -k .
```

It takes some time for everything to become ready. Let us first check on the volume claims by running the following command.
```console
kubectl get pvc
```

Eventually the volume claims will be bounded to the cluster and appear similar to the image below.

![image](https://user-images.githubusercontent.com/87687468/203515130-83c5604b-fc85-49e9-8f1a-1da2f00066b6.png)

Next, we can check on the WordPress and MySQL pods by running the following command.
```console
kubectl get pods
```

It may take a little while for the pods to be created and get into the running state. Eventually the pods should look like the image below.

![image](https://user-images.githubusercontent.com/87687468/203515032-0d6bd00f-068a-4848-b3f9-75e86e895ec9.png)

To verify WordPress is working, we can connect to WordPress through a browser. To get the external IP address of the WordPress deployment run the following command.
```console
kubectl get svc
```

![image](https://user-images.githubusercontent.com/87687468/203515908-db800aa4-602c-4e80-ae70-d7fc44c8e16b.png)

At this point, we can point a browser to the external IP address (in this case, it's 3.145.125.76) and see the WordPress welcome screen as shown below.

![image](https://user-images.githubusercontent.com/87687468/203516285-2e700357-0adb-4520-9fcc-ae22444529a2.png)
