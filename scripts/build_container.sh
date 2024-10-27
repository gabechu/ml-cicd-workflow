#!/bin/bash

# Set project ID
PROJECT_ID=ml-ops-439823

# Build the container
docker build -t gcr.io/ml-ops-439823/train-model:latest -f docker/Dockerfile.train-model .

# Push to GCR
docker push gcr.io/${PROJECT_ID}/train-model:latest