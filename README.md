<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">ML-CICD-WORKFLOW</h1></p>
<p align="center">
	<em>Streamline ML deployment with precision and speed.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/gabechu/ml-cicd-workflow?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/gabechu/ml-cicd-workflow?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/gabechu/ml-cicd-workflow?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/gabechu/ml-cicd-workflow?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

The ml-cicd-workflow project simplifies the continuous integration and deployment process for machine learning models. It streamlines model training, deployment, and monitoring using Docker containers, Kubeflow, and Google Cloud services. Ideal for data scientists and ML engineers, it enhances collaboration and efficiency in managing ML workflows.

---

##  Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes **Kubeflow** for managing ML workflows</li><li>Employs **Docker** for containerization</li><li>Defines **PersistentVolume** and **PersistentVolumeClaim** for storage</li><li>Integrates with **Google Cloud AI Platform** for custom training jobs</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Follows **PEP 8** coding standards</li><li>Utilizes **Black** for code formatting</li><li>Includes **Mypy** static type checking</li><li>Implements **Pytest** for automated testing</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive **Python** documentation</li><li>Includes **Poetry** for managing dependencies</li><li>Provides detailed **YAML** configuration files</li><li>Offers **JSON** files for deployment details</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with **Google Cloud** services</li><li>Utilizes **Kubeflow Model Registry** for model management</li><li>Includes **FastAPI** for building APIs</li><li>Incorporates **Scikit-learn** for machine learning tasks</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Separates concerns with **Pydantic** models</li><li>Organizes code into **src** directories</li><li>Encapsulates training logic in **train_model.py**</li><li>Defines API endpoints in **main.py**</li></ul> |
| 🧪 | **Testing**       | <ul><li>Automated testing with **Pytest**</li><li>Includes unit tests for critical components</li><li>Ensures code quality with test coverage</li><li>Validates input/output data with **Pydantic** models</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimizes hyperparameters with **Bayesian optimization**</li><li>Utilizes **XGBoost** for efficient model training</li><li>Ensures scalability with **Google Cloud AI Platform**</li><li>Efficiently deploys models with **Kubeflow**</li></ul> |
| 🛡️ | **Security**      | <ul><li>Follows best practices for **Google Cloud** security</li><li>Secures model storage with **PersistentVolumeClaim**</li><li>Implements secure API endpoints with **FastAPI**</li><li>Ensures data integrity and confidentiality</li></ul> |

---

##  Project Structure

```sh
└── ml-cicd-workflow/
    ├── .github
    │   └── workflows
    ├── LICENSE
    ├── deploy_details.json
    ├── docker
    │   ├── Dockerfile.app
    │   ├── Dockerfile.train-model
    │   └── app_entry_point.sh
    ├── examples
    │   ├── kubeflow_hyperparameter_tuning.py
    │   ├── kubeflow_model_registry.py
    │   ├── random_hyperparameter_search.yml
    │   ├── train_xgboost.py
    │   └── write_to_gcs.py
    ├── manifests
    │   ├── create_pv.yaml
    │   ├── create_pvc.yaml
    │   ├── train-model.yaml
    │   └── vertex-hp-config.yaml
    ├── poetry.lock
    ├── pyproject.toml
    ├── scripts
    │   ├── build_container.sh
    │   ├── create_vertex_hp_tuning_jobs.sh
    │   ├── monitor_katib.sh
    │   └── update_deploy_details.py
    ├── src
    │   ├── __init__.py
    │   ├── app
    │   └── training
    └── tests
        ├── __init__.py
        └── unit
```


###  Project Index
<details open>
	<summary><b><code>ML-CICD-WORKFLOW/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
				<td>Define project dependencies and versions using Poetry in pyproject.toml to manage Python packages and streamline the ML CI/CD workflow.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/deploy_details.json'>deploy_details.json</a></b></td>
				<td>- Manages deployment details for old, new, and production machine learning models<br>- Tracks model versions, mean squared error, and storage URIs.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- docker Submodule -->
		<summary><b>docker</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/docker/Dockerfile.app'>Dockerfile.app</a></b></td>
				<td>- Facilitates building and running a Python application within a Docker container<br>- Sets up the environment, installs dependencies, copies the application code, and specifies the command to start the application<br>- The Dockerfile.app plays a crucial role in containerizing the Python application and ensuring its smooth execution.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/docker/app_entry_point.sh'>app_entry_point.sh</a></b></td>
				<td>- Facilitates running the application with a specified model file<br>- Launches the app using Uvicorn with defined host and port settings.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/docker/Dockerfile.train-model'>Dockerfile.train-model</a></b></td>
				<td>- Builds a Docker image for training a machine learning model using Python dependencies and a specified training script and data<br>- The Dockerfile sets up the environment, installs project dependencies, and executes the training script upon container startup.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- examples Submodule -->
		<summary><b>examples</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/examples/kubeflow_model_registry.py'>kubeflow_model_registry.py</a></b></td>
				<td>- Registers and manages machine learning models in the Kubeflow Model Registry<br>- Allows for easy registration, retrieval, and management of models with metadata such as version, description, and accuracy<br>- Ideal for organizing and tracking models within the project architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/examples/random_hyperparameter_search.yml'>random_hyperparameter_search.yml</a></b></td>
				<td>- Define a hyperparameter search experiment for Kubeflow using a YAML file<br>- The file specifies parameters like learning rate and momentum ranges, trial configurations, and resource constraints for training a PyTorch model<br>- This setup enables efficient hyperparameter optimization within the Kubeflow ecosystem.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/examples/kubeflow_hyperparameter_tuning.py'>kubeflow_hyperparameter_tuning.py</a></b></td>
				<td>- Facilitates hyperparameter tuning using Katib in Kubeflow<br>- Defines an objective function, sets parameter ranges, and initiates tuning with Bayesian optimization<br>- Monitors experiment progress and retrieves optimal hyperparameters<br>- Enables efficient model optimization within the Kubeflow ecosystem.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/examples/train_xgboost.py'>train_xgboost.py</a></b></td>
				<td>- Optimize XGBoost hyperparameters using GridSearchCV on the Boston Housing dataset to find the best model for predicting house prices<br>- Splitting the data into training and testing sets, the code evaluates the model's performance by calculating the mean squared error on the test set.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/examples/write_to_gcs.py'>write_to_gcs.py</a></b></td>
				<td>- Creates a new bucket in Google Cloud Storage and uploads a JSON file with model performance data<br>- The code handles bucket creation, error checking, and file upload, ensuring seamless data storage and retrieval for machine learning models.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- scripts Submodule -->
		<summary><b>scripts</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/scripts/create_vertex_hp_tuning_jobs.sh'>create_vertex_hp_tuning_jobs.sh</a></b></td>
				<td>- Generates hyperparameter tuning jobs for training models in the specified Google Cloud region, with a set number of trials running in parallel<br>- The script uses a configuration file to define the tuning job parameters and checks for successful job creation.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/scripts/build_container.sh'>build_container.sh</a></b></td>
				<td>Builds and pushes a Docker container to Google Container Registry for the ML Ops project with the specified project ID.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/scripts/monitor_katib.sh'>monitor_katib.sh</a></b></td>
				<td>- Monitors the status of a Katib experiment in the Kubeflow namespace, checking for completion or failure<br>- If the experiment is successful, it exits with a success status; if it fails, it exits with a failure status<br>- Continuously checks the experiment status every 5 minutes until completion.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/scripts/update_deploy_details.py'>update_deploy_details.py</a></b></td>
				<td>- Updates deploy details with the best model version by starting port-forwarding, retrieving the best model version from the registry, and updating the deploy file accordingly<br>- This script ensures the deployment of the most optimal model version for the project.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- .github Submodule -->
		<summary><b>.github</b></summary>
		<blockquote>
			<details>
				<summary><b>workflows</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/.github/workflows/run-hp-tuning.yml'>run-hp-tuning.yml</a></b></td>
						<td>- Automates deployment to Minikube by setting up necessary components, building and deploying containers, comparing models, and deploying a model service with health checks<br>- It ensures efficient testing and deployment of machine learning models in a local Kubernetes environment.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/.github/workflows/tests.yml'>tests.yml</a></b></td>
						<td>- Automates Python testing workflow by setting up Python 3.11, installing Poetry, caching dependencies, and running unit tests using pytest<br>- This workflow ensures consistent testing on every push and pull request to the main branch.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- manifests Submodule -->
		<summary><b>manifests</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/manifests/train-model.yaml'>train-model.yaml</a></b></td>
				<td>Define experiment configuration for training a model using Kubeflow with Bayesian optimization algorithm, specifying parameters, trial template, and resource constraints.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/manifests/vertex-hp-config.yaml'>vertex-hp-config.yaml</a></b></td>
				<td>- Define study and trial configurations for hyperparameter optimization in the ML model training process<br>- Specify metrics, parameters, worker pool specifications, and container details for running experiments<br>- This file plays a crucial role in setting up the experimental environment and defining optimization goals within the project architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/manifests/create_pv.yaml'>create_pv.yaml</a></b></td>
				<td>- Defines a PersistentVolume named 'model-storage-pv' with 1Gi storage capacity, ReadWriteOnce access mode, and Retain reclaim policy<br>- It uses the 'standard' storage class and a hostPath at "/mounted-workspace" for Filesystem volume mode.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/manifests/create_pvc.yaml'>create_pvc.yaml</a></b></td>
				<td>Defines a PersistentVolumeClaim named 'model-storage' in the 'kubeflow' namespace with 1Gi storage capacity and ReadWriteOnce access mode.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- src Submodule -->
		<summary><b>src</b></summary>
		<blockquote>
			<details>
				<summary><b>app</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/src/app/schemas.py'>schemas.py</a></b></td>
						<td>Defines Pydantic models for input and output data for house price prediction in the project architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/src/app/main.py'>main.py</a></b></td>
						<td>- Enables Boston House Price Prediction API with model loading and prediction functionality based on input features<br>- Implements endpoints for predicting house prices and performing health checks.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>training</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/src/training/create_vertex_job.py'>create_vertex_job.py</a></b></td>
						<td>- Generates a custom training job for XGBoost model using Google Cloud AI Platform<br>- The job is configured with specified parameters and container image URI<br>- This code file plays a crucial role in orchestrating the training process within the ML Ops project structure.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/gabechu/ml-cicd-workflow/blob/master/src/training/train_model.py'>train_model.py</a></b></td>
						<td>- Trains a Random Forest model for Boston Price Prediction, evaluating its performance and registering the model in the Model Registry<br>- The code splits data, trains the model, calculates mean squared error, and saves the model to persistent storage<br>- The registered model includes metadata for tracking and versioning.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with ml-cicd-workflow, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Poetry


###  Installation

Install ml-cicd-workflow using one of the following methods:

**Build from source:**

1. Clone the ml-cicd-workflow repository:
```sh
❯ git clone https://github.com/gabechu/ml-cicd-workflow
```

2. Navigate to the project directory:
```sh
❯ cd ml-cicd-workflow
```

3. Install the project dependencies:


**Using `poetry`** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

```sh
❯ poetry install
```




###  Usage
Run ml-cicd-workflow using the following command:
**Using `poetry`** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

```sh
❯ poetry run python {entrypoint}
```


###  Testing
Run the test suite using the following command:
**Using `poetry`** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

```sh
❯ poetry run pytest
```


---
##  Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/gabechu/ml-cicd-workflow/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/gabechu/ml-cicd-workflow/issues)**: Submit bugs found or log feature requests for the `ml-cicd-workflow` project.
- **💡 [Submit Pull Requests](https://github.com/gabechu/ml-cicd-workflow/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/gabechu/ml-cicd-workflow
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/gabechu/ml-cicd-workflow/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=gabechu/ml-cicd-workflow">
   </a>
</p>
</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
