Setting up your remote server

Install Helm: https://helm.sh/docs/intro/install/
Install Ingress-nginx if not already in the kluster (if using RKE2, it should already be installed): 
https://docs.nginx.com/nginx-ingress-controller/installation/installation-with-helm/

Steps to create gitlab credentials.

1. Settings -> Access Tokens -> Create new token with read permissions
2. In your command line, type in "kubectl create secret docker-registry regcred --docker-server=registry.socs.uoguelph.ca --docker-username=<UoG_username> --docker-password=<Token>"

Optional:
3. To create a yaml file that you can apply to your cluster, "kubectl get secret regcred --output=yaml"
4. Now that you have this file, you can easily reapply the setting to any cluster and it will allow you to fetch images straight from your UoG gitlab repository.

Full guide can be found here: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/

When creating your pods or deployments:
Use the following template:
```
apiVersion: v1
kind: Pod
metadata:
  name: private-reg
spec:
  containers:
  - name: private-reg-container
    image: registry.socs.uoguelph.ca/<username>/<registry>:<tag>
  imagePullSecrets:
  - name: regcred
```

