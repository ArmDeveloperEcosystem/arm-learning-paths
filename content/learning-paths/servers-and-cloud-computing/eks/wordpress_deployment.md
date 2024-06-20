---
title: "Deploy WordPress"
weight: 3
layout: learningpathall
---

## Create the WordPress deployment files

You can use three yaml files and `kubectl` to deploy WordPress. The three file names are `kustomization.yaml`, `mysql-deployment.yaml`, and `wordpress-deployment.yaml`.

Use a text editor to copy the contents of each file and save the result. 

Copy the information below into `kustomization.yaml`:

```console
secretGenerator:
- name: mysql-pass
  literals:
  - password=YourPassword
resources:
  - mysql-deployment.yaml
  - wordpress-deployment.yaml  
```

The `kustomization.yaml` file sets the password for the MySQL database. The resources section selects which files these kustomizations apply to. Information on working with kustomizations is in the [Kubernetes documentation](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/).

Copy the information below into the second file, `mysql-deployment.yaml`:

```console
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mysql-pv-volume
  labels:
    type: local
spec:
  storageClassName: manual
  capacity:
    storage: 20Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/tmp/mysql/data"
  persistentVolumeReclaimPolicy: Recycle
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mysql-pv-claim
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi
---
apiVersion: v1
kind: Service
metadata:
  name: wordpress-mysql
  labels:
    app: wordpress-mysql
spec:
  ports:
  - port: 3306
  selector:
    app: wordpress-mysql
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wordpress-mysql
  labels:
    app: wordpress-mysql
spec:
  selector:
    matchLabels:
      app: wordpress-mysql
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: wordpress-mysql
    spec:
      containers:
      - image: mysql:oracle
        name: mysql
        env:
        - name: MYSQL_DATABASE
          value: wordpress
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

The `mysql-deployment.yaml` file deploys a pod with a MySQL container. 

There are three objects defined:
- The first object is a service object. It creates a service called wordpress-mysql. The service is assigned to be the front end to the MySQL pod through the use of a selector. When a pod within the cluster wants to communicate with the MySQL pod, it communicates using the wordpress-mysql service name.
- The next object is a Persistent Volume Claim (PVC). This object mounts storage inside the MySQL pod. A key point to understand is that the PVC object is not what creates the storage. It is a declaration of a type of storage that you want available to the cluster.
- The last object created is a deployment. Inside the deployment spec there are selector labels. These labels match the labels in the service object. This match assigns the wordpress-mysql service to the MySQL pod. Within the deployment spec, there is also a pod spec which configures the MySQL container to deploy. 

Copy the information below into the last file, `wordpress-deployment.yaml`:

```console
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: wp-pv-volume
  labels:
    type: local
spec:
  storageClassName: manual
  capacity:
    storage: 20Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/tmp/wp/data"
  persistentVolumeReclaimPolicy: Recycle
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: wp-pv-claim
  labels:
    app: wordpress
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi
---
apiVersion: v1
kind: Service
metadata:
  name: wordpress
  labels:
    app: wordpress
    tier: frontend
spec:
  ports:
    - port: 80
  selector:
    app: wordpress
    tier: frontend
  type: LoadBalancer
---
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wordpress
  labels:
    app: wordpress
    tier: frontend
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
        - image: wordpress:6.0.1-php7.4
          name: wordpress
          env:
            - name: WORDPRESS_DB_HOST
              value: wordpress-mysql
            - name: WORDPRESS_DB_NAME
              value: wordpress
            - name: WORDPRESS_DB_USER
              value: root
            - name: WORDPRESS_DB_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: mysql-pass
                  key: password
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

Similar to the MySQL yaml, this file also creates three objects: 
- First, there is a service object named wordpress. This service exposes port 80 and is a load balancer.
- The second object is a PVC, similar to the MySQL yaml.
- The last object is a deployment. In the pod spec, set the MySQL user and password to match the MySQL non-root user and password in the MySQL yaml file. This password provides WordPress permission to read/write to the MySQL database pod.

## Deploy WordPress 

Run the following command to apply the above configuration:

```console
kubectl apply -k .
```

After applying the configuration, check the volume claims by running the following command:

```console
kubectl get pvc
```

Wait for the status to be "Bound". The output is similar to:

```output
NAME             STATUS   VOLUME            CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
mysql-pv-claim   Bound    mysql-pv-volume   20Gi       RWO            manual         <unset>                 88s
wp-pv-claim      Bound    wp-pv-volume      20Gi       RWO            manual         <unset>                 88s
```

Next, check the WordPress and MySQL pods by running the following command:

```console
kubectl get pods
```

After a brief start up, the pods will be running and the output will be similar to: 

```output
NAME                               READY   STATUS    RESTARTS   AGE
wordpress-55b7946887-9qzmw         1/1     Running   0          2m13s
wordpress-mysql-68cb45cc44-x2lzw   1/1     Running   0          2m13s
```

To get the external IP address of the WordPress deployment run the following command.

```console
kubectl get svc
```

The output shows the load balancer line which includes the external DNS name. 

```output
NAME              TYPE           CLUSTER-IP       EXTERNAL-IP                                                              PORT(S)        AGE
kubernetes        ClusterIP      10.100.0.1       <none>                                                                   443/TCP        17m
wordpress         LoadBalancer   10.100.166.194   ad53d835cdf0343378594f1188fe957d-136333022.us-east-1.elb.amazonaws.com   80:32689/TCP   2m57s
wordpress-mysql   ClusterIP      10.100.54.182    <none>                                                                   3306/TCP       2m57s
```

Use a browser to visit the external IP, `ad53d835cdf0343378594f1188fe957d-136333022.us-east-1.elb.amazonaws.com` for the output above, and see the WordPress welcome screen as shown below:

![eks #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/7202e08e-b403-4360-81bd-0331f3df0d03)

Click Continue, set the site parameters and set up the administrator password (make sure to save the password you enter).

Click Install WordPress to finish the setup. 

The WordPress site it now available on the external IP using the DNS name. You can also access the admin dashboard by adding `wp-admin/` to the DNS name,`ad53d835cdf0343378594f1188fe957d-136333022.us-east-1.elb.amazonaws.com/wp-admin/` in the example above.

You have created a Kubernetes cluster and installed an application using the EKS managed Kubernetes service and running on AWS Graviton processors. 

## Delete the AWS resources

If you don't want to keep the application running, make sure to clean up the resources you created. 

Everything can be deleted by running: 

```console
eksctl delete cluster --name demo-eks
```
