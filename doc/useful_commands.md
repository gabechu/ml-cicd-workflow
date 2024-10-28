1. Install minikube to create local K8s cluster
    - minikube start
    - minikube dashboard
1. Install Katib v0.17.0 for hyperparameter tuning
    - kubectl apply -k "github.com/kubeflow/katib.git/manifests/v1beta1/installs/katib-standalone?ref=v0.17.0"
    - kubectl apply -k "github.com/kubeflow/katib.git/manifests/v1beta1/installs/katib-standalone?ref=master"
    - kubectl port-forward svc/katib-ui -n kubeflow 8080:80
    - Open http://localhost:8080/katib/
1. Model registry
    - kubectl apply -k "https://github.com/kubeflow/model-registry/manifests/kustomize/overlays/db?ref=v0.2.3-alpha"
1. Model storage
    - kubectl apply -f manifests/create_pv.yaml
    - kubectl apply -f manifests/create-pvc.yaml
    - minikube mount /Users/gabechu/Code/interviews/ml-cicd-workflow/local_bucket:/local_bucket
1. Container registry
    - eval $(minikube docker-env)
    - docker build -t train-model:latest -f docker/Dockerfile.train-model .
    - docker push localhost:5001/xgboost-training:latest
1. Run Katib job
    - kubectl create -f manifests/train-model.yaml
    - kubectl get experiment train-xgboost-model -n kubeflow -o=jsonpath='{.status.currentOptimalTrial}'
1. Auth gcr
    - gcloud auth login
    - gcloud auth configure-docker
    - gcloud config set compute/region australia-southeast1
1. Build model service
    - docker build -t boston-housing-api -f docker/Dockerfile.app .
    - docker run -d -p 8005:8005 boston-housing-api
