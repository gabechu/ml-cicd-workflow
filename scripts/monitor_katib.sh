#!/bin/bash

while true; do
  status_running=$(kubectl get experiments train-model -n kubeflow -o jsonpath='{.status.conditions[?(@.type=="Running")].status}')
  status_succeeded=$(kubectl get experiments train-model -n kubeflow -o jsonpath='{.status.conditions[?(@.type=="Succeeded")].status}')
  
  if [ "$status_running" != "True" ] && [ "$status_succeeded" == "True" ]; then
    echo "Experiment completed successfully"
    exit 0
  elif [ "$status_running" != "True" ] && [ "$status_succeeded" != "True" ]; then
    echo "Experiment failed"
    exit 1
  fi
  
  echo "Experiment still running..."
  sleep 300
done