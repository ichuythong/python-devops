# Install minikube on Ubuntu
$ wget https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64  
$ chmod +x minikube-linux-amd64  
$ sudo mv minikube-linux-amd64 /usr/local/bin/minikube  
$ minikube version

# Install kubectl on Ubuntu
$ curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl  
$ chmod +x ./kubectl  
$ sudo mv ./kubectl /usr/local/bin/kubectl  
$ kubectl version -o json  --client

# Starting minikube on Ubuntu
$ minikube start

# Minikube Basic operations
$ kubectl cluster-info  
$ kubectl config view  
$ kubectl get nodes  
$ kubectl get pods  
$ kubectl get rs  
$ kubectl delete pod myfirstpod  

## Access minikube VM using ssh
$ minikube ssh  
$ sudo su -

## To stop a running local kubernetes cluster
$ minikube stop  

## To delete a local kubernetes cluster
$ minikube delete  

$ minikube status  

# Enable Kubernetes Dashboard
$ minikube addons list  
$ minikube addons enable portainer  
$ minikube dashboard  
$ minikube dashboard --url  
$ minikube ip

$ ssh docker@[ip]

$ kubectl create -f pod.yaml  
$ kubectl get pods  
$ kubectl delete pod myfirstpod  

$ kubectl create -f replica.yml  
$ kubectl get rs  

$ kubectl create -f deployment.yml  
$ kubectl get deploy  

$ kubectl apply -f deployment.yml  
$ kubectl get pods  

