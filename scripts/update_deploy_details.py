import json
import subprocess
import time

from model_registry import ModelRegistry

DEPLOY_DETAILS_FILE = "deploy_details.json"


def start_port_forward():
    cmd = ["kubectl", "port-forward", "svc/model-registry-service", "-n", "kubeflow", "8081:8080"]
    process = subprocess.Popen(cmd)
    return process


def get_best_version(registry: ModelRegistry) -> str:
    name = "boston-housing"
    best_version = None

    for version in registry.get_model_versions(name):
        mse = version.custom_properties["mse"]
        if best_version is None:
            best_version = {"mse": mse, "version": version.name}
        elif mse < best_version["mse"]:
            best_version = {"mse": mse, "version": version.name}

    model_artifact = registry.get_model_artifact(name, best_version["version"])
    best_version["uri"] = model_artifact.uri

    return best_version


def _get_deploy_details() -> dict:
    with open(DEPLOY_DETAILS_FILE, "r") as f:
        return json.load(f)


def update_deploy_model(best_version: dict):
    details = _get_deploy_details()
    updated_details = dict()
    updated_details["old_model"] = details["new_model"]
    updated_details["prod_model"] = details["prod_model"]

    if details["new_model"]["mse"] > best_version["mse"]:
        updated_details["new_model"] = {
            "mse": best_version["mse"],
            "version": best_version["version"],
            "uri": best_version["uri"],
        }
        with open(DEPLOY_DETAILS_FILE, "w") as f:
            json.dump(updated_details, f)
        print(f"Updated deploy file! {updated_details}")


def main():
    # Start port-forwarding in background
    port_forward_process = start_port_forward()

    # Wait a bit for port-forward to establish
    time.sleep(5)

    try:
        registry = ModelRegistry(server_address="http://localhost", port=8081, author="wei", is_secure=False)
        best_version = get_best_version(registry)
        update_deploy_model(best_version)
    finally:
        # Clean up port-forward process
        port_forward_process.terminate()
        port_forward_process.wait()


if __name__ == "__main__":
    main()
