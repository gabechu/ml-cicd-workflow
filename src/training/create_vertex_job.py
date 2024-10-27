from google.cloud import aiplatform
from kfp import dsl

PROJECT_ID="ml-ops-439823"


def create_custom_job(project_id: str, location: str, container_uri: str, parameters: dict):
    aiplatform.init(project_id=project_id, location=location)

    job = aiplatform.CustomJob(
        display_name="xgboost-katib-training",
        worker_pool_specs=[{
            "machine_spec": {
                "machine_type": "n1-standard-4",
            },
            "replica_count": 1,
            "container_spec": {
                "image_uri": container_uri,
                "args": [
                    "--n-estimators", str(parameters["n_estimators"])
                ]
            }
        }]
    )

    return job


def training_pipeline():
    hp_tuning_job = 