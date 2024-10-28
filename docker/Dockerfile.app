FROM python:3.11-slim

# Define build argument
ARG MODEL_FILE_NAME
ENV MODEL_FILE_NAME=$MODEL_FILE_NAME

WORKDIR /app

# Copy requirements and install dependencies
COPY poetry.lock .
COPY pyproject.toml .

RUN pip install poetry
RUN poetry install --without dev

# Copy app
COPY ./src/app ./src/app
COPY ./local_bucket ./local_bucket

CMD ["poetry", "run", "uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8005"]
