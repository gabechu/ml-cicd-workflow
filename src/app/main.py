import os
from pathlib import Path

import numpy as np
from fastapi import FastAPI, HTTPException
from joblib import load

from src.app.schemas import HousePredictionInput, HousePredictionOutput

app = FastAPI(title="Boston House Price Prediction API")


def load_model(model_file_name):
    # Get model file name from environment variable
    MODEL_FILE_NAME = os.getenv("MODEL_FILE_NAME")
    if not MODEL_FILE_NAME:
        raise ValueError("MODEL_FILE_NAME environment variable is required")

    model_path = Path(f"local_bucket/{MODEL_FILE_NAME}")
    return load(model_path)


@app.post("/predict", response_model=HousePredictionOutput)
async def predict(input_data: HousePredictionInput):
    try:
        features = np.array(
            [
                [
                    input_data.CRIM,
                    input_data.ZN,
                    input_data.INDUS,
                    input_data.CHAS,
                    input_data.NOX,
                    input_data.RM,
                    input_data.AGE,
                    input_data.DIS,
                    input_data.RAD,
                    input_data.TAX,
                    input_data.PTRATIO,
                    input_data.B,
                    input_data.LSTAT,
                ]
            ]
        )
        model = load_model("local_bucket/random_forest_model_20241027_235910_19892a47.joblib")
        prediction = model.predict(features)[0]
        return HousePredictionOutput(predicted_price=float(prediction))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
