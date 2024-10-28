#!/bin/bash
export MODEL_FILE_NAME=$1
poetry run uvicorn src.app.main:app --host 0.0.0.0 --port 8005