import json

from model_registry import ModelRegistry

DEPLOY_DETAILS_FILE = "deploy_details.json"


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

    if details["new_model"]["mse"] > best_version["mse"]:
        updated_details["new_model"] = {
            "mse": best_version["mse"],
            "version": best_version["version"],
            "uri": best_version["uri"],
        }
        with open(DEPLOY_DETAILS_FILE, "w") as f:
            json.dump(updated_details, f)
        print("Updated deploy file!")


if __name__ == "__main__":
    registry = ModelRegistry(server_address="http://localhost", port=8081, author="wei", is_secure=False)
    best_version = get_best_version(registry)
    update_deploy_model(best_version)
