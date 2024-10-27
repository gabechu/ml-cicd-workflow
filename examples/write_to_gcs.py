import json

from google.cloud.storage import Client as StorageClient


def write_to_gcs(storage_client: StorageClient):
    bucket_name = "my-bucket"
    try:
        bucket = storage_client.create_bucket(bucket_name)
        print(f"Bucket {bucket_name} created successfully.")
    except Exception as e:
        print(f"Bucket {bucket_name} already exists or there was an error: {e}")
        bucket = storage_client.bucket(bucket_name)

    # Define the blob path
    blob_path = "boston_house/model_performance.json"
    blob = bucket.blob(blob_path)

    # Upload the file
    try:
        blob.upload_from_string(json.dumps(data), content_type="application/json")
        print(f"File {blob_path} uploaded successfully to {bucket_name}")
    except Exception as e:
        print(f"Error uploading file: {e}")


if __name__ == "__main__":
    data = {
        "new_model": {"mse": 0.72, "model_version": "0.1.0"},
        "current_model": {"mse": 0.83, "model_version": "0.2.0"},
    }
    project_id = "ml-ops-439823"
    storage_client = StorageClient(project=project_id)
    write_to_gcs(storage_client)
