def objective(parameters):
    import time

    time.sleep(5)
    result = 4 * int(parameters["a"]) - float(parameters["b"]) ** 2
    print(f"result={result}")


import kubeflow.katib as katib

parameters = {"a": katib.search.int(min=10, max=20), "b": katib.search.double(min=0.1, max=0.2)}

katib_client = katib.KatibClient(namespace="kubeflow")

name = "tune-experiment"
katib_client.tune(
    name=name,
    objective=objective,
    algorithm_name="bayesianoptimization",
    parameters=parameters,
    objective_metric_name="result",
    max_trial_count=12,
    resources_per_trial={"cpu": "1"},
)

katib_client.wait_for_experiment_condition(name=name)

print(katib_client.get_optimal_hyperparameters(name))
