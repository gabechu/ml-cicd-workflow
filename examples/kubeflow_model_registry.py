from model_registry import ModelRegistry

registry = ModelRegistry(server_address="http://localhost", port=8081, author="wei", is_secure=False)

rm = registry.register_model(
    "mnist",
    "https://github.com/tarilabs/demo20231212/raw/main/v1.nb20231206162408/mnist.onnx",
    model_format_name="onnx",
    model_format_version="1",
    version="v0.1",
    description="lorem ipsum mnist",
    metadata={
        "accuracy": 3.14,
        "license": "apache-2.0",
    },
)

model = registry.get_registered_model("minst")
print("Registered Model:", model, "with ID", model.id)
