import argparse
import logging
import os
import uuid
from datetime import datetime

import joblib
import numpy as np
import pandas as pd
from model_registry import ModelRegistry
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

logging.basicConfig(level=logging.INFO)


registry = ModelRegistry(
    server_address="http://model-registry-service.kubeflow.svc.cluster.local", port=8080, author="wei", is_secure=False
)


def _load_data() -> tuple[np.ndarray, np.ndarray]:
    raw_df = pd.read_csv("boston.csv", sep="\s+", skiprows=22, header=None)
    X = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    y = raw_df.values[1::2, 2]
    return X, y


def _persist_model(model):
    # Generate unique model filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_id = str(uuid.uuid4())[:8]
    model_filename = f"random_forest_model_{timestamp}_{unique_id}.joblib"

    # Save model to PVC
    model_path = os.path.join("/mnt/models", model_filename)
    joblib.dump(model, model_path)
    return model_filename


def train_random_forest(n_estimators: int, max_depth: int, min_samples_split: int, min_samples_leaf: int) -> float:
    X, y = _load_data()

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Select model: Random Forest Model
    rf_model = RandomForestRegressor(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        random_state=42,
    )

    # Train the model
    rf_model.fit(X_train, y_train)

    # Evalaute the model
    y_pred = rf_model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    print(f"mse={mse:.3f}")

    model_filename = _persist_model(rf_model)
    registry.register_model(
        "boston-housing",
        model_filename,
        model_format_name="joblib",
        model_format_version="1",
        version=f"v0.1.0_{str(uuid.uuid4())[:8]}",
        description="Random Forest model for Boston Housing",
        metadata={
            "mse": mse,
            "framework": "scikit-learn",
        },
    )
    return mse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train Random Forest model for Boston Price Prediction")
    parser.add_argument("--n-estimators", type=int, default=100, help="Number of trees in the forest")
    parser.add_argument("--max-depth", type=int, default=None, help="Maximum depth of the trees")
    parser.add_argument(
        "--min-samples-split", type=int, default=2, help="Minimum samples required to split an internal node"
    )
    parser.add_argument("--min-samples-leaf", type=int, default=1, help="Minimum samples required to be at a leaf node")
    args = parser.parse_args()

    train_random_forest(
        n_estimators=args.n_estimators,
        max_depth=args.max_depth,
        min_samples_split=args.min_samples_split,
        min_samples_leaf=args.min_samples_leaf,
    )
