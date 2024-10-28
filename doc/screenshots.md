# [CI/CD Pipeline Execution Screenshots](https://github.com/gabechu/ml-cicd-workflow/blob/main/.github/workflows/deploy-trained-model.yml)
1. Setup Kubernetes with Minikube
1. Install Katib and Model Registry
1. Mount Artifact Storage
1. Activate Model Training
1. Compare Training Results
    - If the new model demonstrates better performance, proceed with the following steps:
        1. Deploy Model Service
        1. Test Prediction Endpoint
    - Else jump to step 6
1. Clean Up

![alt text](github_cicd.png)
![alt text](test_deployed_endpoint.png)

# Katib Parallel Run Screenshot
![alt text](parallel_trail_run.png)
![alt text](katib_job.png)
