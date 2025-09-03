# Use official Python base image
FROM python:3.11-slim

ARG APP_PORT
ARG APP_HOST

ENV APP_HOST=0.0.0.0
ENV APP_PORT=80

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.2

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && apt-get clean

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Set work directory
WORKDIR /app

# Copy only the necessary files for dependency installation
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --only main

# Copy the rest of the application code
COPY . .

# Expose FastAPI port
EXPOSE ${APP_PORT}

RUN echo ${APP_PORT}

ENTRYPOINT ["sh", "-c"]

# Start the FastAPI app using Uvicorn
CMD ["uvicorn scripts.mock_dsp_api:app --host $APP_HOST --port $APP_PORT"]
