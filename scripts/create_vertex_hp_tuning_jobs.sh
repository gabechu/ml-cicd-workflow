#!/bin/bash

# Set variables
REGION="australia-southeast1"
DISPLAY_NAME="train-model"
MAX_TRIALS=12
PARALLEL_TRIALS=3
CONFIG_PATH="manifests/vertex-hp-config.yaml"

# Execute the command
gcloud ai hp-tuning-jobs create \
    --region="$REGION" \
    --display-name="$DISPLAY_NAME" \
    --max-trial-count="$MAX_TRIALS" \
    --parallel-trial-count="$PARALLEL_TRIALS" \
    --config="$CONFIG_PATH"

# Check if command was successful
if [ $? -eq 0 ]; then
    echo "Successfully created hyperparameter tuning job"
else
    echo "Failed to create hyperparameter tuning job"
    exit 1
fi