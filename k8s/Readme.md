Steps to create gitlab credentials.

1. Settings -> Access Tokens -> Create new token with read permissions
2. In your command line, type in "kubectl create secret docker-registry regcred --docker-server=registry.socs.uoguelph.ca --docker-username=<UoG_username> --docker-password=<Token>

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



Steps to setup flux:

1. Install flux using eith choco or brew or linux
2. Create an access token
3. run the following command: echo "<Your access Token>" | flux bootstrap gitlab --owner=amerch04 --repository=springtemplate --branch=main --path=k8s --hostname=gitlab.socs.uoguelph.ca
4. Follow the rest of the instructions on: https://docs.gitlab.com/ee/user/clusters/agent/gitops/flux_tutorial.html#create-a-personal-access-token

