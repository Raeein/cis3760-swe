---
layout: post
category: K8s
---

Kubernetes is a container orchestration tool that helps us in scaling our application and meeting with customer needs. Our template app was deployed using Kubernetes and can be accessed from anywhere. In this post, we will go learn a little about Kubernetes and we will be setting up a basic Node.JS application. 

---
<h1 align="center">Key Terms in K8s</h1>
---

Here's a list of fundamental terms that are related to K8s:

**Pods:** Think of pods as the elemental building blocks in Kubernetes. They house one or more containers and share the same network and volume space.

**Node:** Nodes are the individual machines at the core of a Kubernetes cluster. They host pods, managing their execution and overseeing available resources

**Replica Set:** A Replica Set watches over your pods and ensures a set number of identical pod replicas are always running, automatically replacing any that fail.

**Deployment:** Deployments define how many pods and replica sets should exist. They facilitate continuous application availability, scalability, and application updates.

**Services:** Act as an abstraction layer to enable communication between different components in a Kubernetes cluster. Various types include:
- ClusterIP: Internal-only service, accessible within the cluster.
- NodePort: Exposes a service on a static port on each node, making it externally accessible.
- Load Balancer: Distributes traffic across multiple nodes, enhancing availability and reliability.

**Secrets:** Secrets in Kubernetes store confidential data like passwords or tokens, ensuring secure access to resources. 

**Ingress:** Ingress manages external access to services within your cluster. It uses rules to direct external traffic to specific services, serving as the gateway.

![K8s terms]({{site.baseurl}}/assets/img/k8s-terms.png)

Grasping these terms lays a good foundation for exploring the world of container orchestration and application management.

---
<h1 align="center">Setting up a local cluster with Minikube</h1>
---

[Minikube](https://minikube.sigs.k8s.io/docs/) is an essential tool for local Kubernetes development, offering a convenient way to experiment with and test clusters on your machine before deploying on a larger scale. It simplifies the process by creating a single-node Kubernetes cluster, allowing you to run, manage, and test your applications locally.

### Deployment Overview

In this section, we'll deploy two Node.js applications—a basic arithmetic calculator and a calculator history tracker—within a cluster. These applications communicate using cluster IPs, with the calculator performing arithmetic operations and the calculator-history app keeping a record of these operations. The two application have their images online in a docker hub repository, all we have to do is pull these images inside our pods when creating a deployment. The code for the two applications can be found at the very end of this post. 

> Before we get started, make sure to have Minikube installed and running. Use this [link](https://minikube.sigs.k8s.io/docs/start/) to setup Minikube on your local machine.

### Setting up The Cluster:

1. **Start minikube:**

```
minikube start
```

> Additionally, you can also view a dashboard using ```minikube dashboard```

2. **Create deployments ([guide](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)):**

Create a new file names `deployments.yaml` file.  We will use this file to create our deployments. Add the following content to the file:

```yaml
# Deployment 1: calculator-deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: calculator-deployment
spec:
  replicas: 1			# Number of pods to create
  selector:
    matchLabels:
      app: calculator		# Labels to match with the pod
  template:
    metadata:
      labels:
        app: calculator
    spec:
      containers:
      - name: calculator
        image: amerch/calculator:calculator	# Docker image to pull in the pods
        ports:
        - containerPort: 3000			# Port the container exposes
        env:					# Environment variables to use
          - name: HISTORY_SERVICE_ADDRESS
            value: http://history-service:4000

---
# Deployment 2: calculator-history-deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: calculator-history-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: calculator-history
  template:
    metadata:
      labels:
        app: calculator-history
    spec:
      containers:
      - name: calculator-history
        image: amerch/calculator:calculator-history
        ports:
        - containerPort: 4000
```

Apply the deployments using:

```
kubectl apply -f deployments.yaml
```

Check deployments status:

```
kubectl get deployments
```

The output should look like:

```
NAME                            READY   UP-TO-DATE   AVAILABLE   AGE
calculator-deployment           1/1     1            1           4m30s
calculator-history-deployment   1/1     1            1           4m30s
```


3. **Create services ([guide](https://kubernetes.io/docs/concepts/services-networking/service/)):**

Create a new services.yaml file with:

```yaml
# Service 1: calculator-service
apiVersion: v1
kind: Service
metadata:
  name: calculator-service
spec:
  selector:
    app: calculator		# Labels to match with the pod
  ports:
  - port: 3000			# Port to use for the service
    targetPort: 3000		# Port from the pods

---
# Service 2: history-service
apiVersion: v1
kind: Service
metadata:
  name: history-service
spec:
  selector:
    app: calculator-history
  ports:
  - port: 4000
    targetPort: 4000
```

Apply the services using:

```
kubectl apply -f services.yaml
```

Check deployments status:

```
kubectl get services
```

The output should look like:
```
NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
calculator-service   ClusterIP   10.111.219.32   <none>        3000/TCP   2m28s
history-service      ClusterIP   10.107.55.166   <none>        4000/TCP   2m28s
kubernetes           ClusterIP   10.96.0.1       <none>        443/TCP    36m
```

4. **Create ingress server ([guide](https://kubernetes.io/docs/concepts/services-networking/ingress/)):**

Now that we are done sertting up our services on minikube, let's access them. There is an easy way to access your services by typing ```minikube service 'service-name' --url``` which gives you a url than you can curl to get your results. For this tutorial, let's setup an ingress service to access our application from outside the cluster.

Before we create the ingress, let's run this command to enable ingress on minikube:

```
minikube addons enable ingress
```

Create ingress.yaml file and paste the following content:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: calculator-ingress
  labels:
    name: calculator-ingress
spec:
  rules:
  - http:
      paths:
      - pathType: Prefix
        path: "/"
        backend:
          service:
            name: calculator-service	# Use the following service at path '/'
            port: 
              number: 3000		# Port number of the service
      - pathType: Prefix
        path: "/history"
        backend:
          service:
            name: history-service
            port: 
              number: 4000
```

To apply this deployment to our project, type in the following command in your terminal:

```
kubectl apply -f ingress.yaml
```

To check if the pods are running, run:

```
kubectl get ingress
```

The output should look something like:

```
NAME                 CLASS   HOSTS	ADDRESS        PORTS   AGE
calculator-ingress   nginx   *  	192.168.49.2   80      10s
```


5. **Test the application:**

Our ingress is setup, we can access it using the minikube [tunnel](https://minikube.sigs.k8s.io/docs/commands/tunnel/), which will redirect any localhost calls to point to the minikube ip. Run the follwing command in a terminal (may not be required in linux):

```
minikube tunnel
```

And then you should be able to call the api:

```
curl localhost/history/all
curl -X POST -H "Content-Type: application/json" -d '{\"num1\": 5, \"num2\": 3}' http://localhost/add
curl localhost/history/all
curl -X POST -H "Content-Type: application/json" -d '{}' localhost/history/clear
```

The Output should look like this:

```
{"history":[]}
{"result":8}
{"history":[{"operation":"5 + 3","result":8}]}
{"message":"History cleared"}
```

6. **Delete Minikube:**

Once done, delete the Minikube container by running:

```
minikube delete
```

---
<h1 align="center">Conclusion</h1>
---

In this section, we successfully set up a local Kubernetes cluster using Minikube, deployed two Node.js applications, established communication between them, and enabled external access through Ingress. These steps provide a foundation for further exploration and testing of Kubernetes features and functionalities.

---
<h1 align="center">Reference code</h1>
---

Here is the code for our calculator and history apps:

```javascript
const express = require('express');
const axios = require('axios');
const app = express();
const port = 3000;

// Middleware to parse JSON in request body
app.use(express.json());

const history_service = process.env.HISTORY_SERVICE_ADDRESS ? process.env.HISTORY_SERVICE_ADDRESS : 'http://localhost:4000';

// function to log history
function logHistory(operation, result) {
    axios.post(
        `${history_service}/history/new`, 
        { operation, result },
        headers = {
            'Content-Type': 'application/json'
        }
    )
    .then(response => console.log(response.data.message))
    .catch(error => console.error('Error logging to history:', error.message));
}

// Define endpoints for basic math operations
// Addition
app.post('/add', (req, res) => {
  const { num1, num2 } = req.body;
  const result = num1 + num2;
  logHistory(`${num1} + ${num2}`, result);
  res.json({ result });
});

// Subtraction
app.post('/subtract', (req, res) => {
  const { num1, num2 } = req.body;
  const result = num1 - num2;
  logHistory(`${num1} - ${num2}`, result);
  res.json({ result });
});

// Multiplication
app.post('/multiply', (req, res) => {
  const { num1, num2 } = req.body;
  const result = num1 * num2;
  logHistory(`${num1} x ${num2}`, result);
  res.json({ result });
});

// Division
app.post('/divide', (req, res) => {
  const { num1, num2 } = req.body;
  if (num2 === 0) {
    return res.status(400).json({ error: 'Cannot divide by zero' });
  }
  const result = num1 / num2;
  logHistory(`${num1} / ${num2}`, result);
  res.json({ result });
});


app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});
```

```javascript
const express = require('express');
const app = express();
const port = 4000;

// Middleware to parse JSON in request body
app.use(express.json());

// Array to store the history of operations
let history = [];

// Endpoint to get the history
app.get('/history/all', (req, res) => {
  res.json({ history });
});

// Endpoint to add a new operation to the history
app.post('/history/new', (req, res) => {
  const { operation, result } = req.body;
  history.push({ operation, result });
  res.json({ message: 'Operation added to history' });
});

// Endpoint to clear the history
app.post('/history/clear', (req, res) => {
  history = [];
  res.json({ message: 'History cleared' });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});
```


