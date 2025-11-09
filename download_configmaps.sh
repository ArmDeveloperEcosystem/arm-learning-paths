#!/bin/bash

# Download nginx_arm configmap
kubectl get configmap nginx-arm -n nginx -o yaml > nginx_arm_configmap.yaml

# Download nginx_intel configmap  
kubectl get configmap nginx-intel -n nginx -o yaml > nginx_intel_configmap.yaml

echo "Downloaded configmaps:"
echo "- nginx_arm_configmap.yaml"
echo "- nginx_intel_configmap.yaml"
