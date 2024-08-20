# https://fastapi.tiangolo.com/deployment/docker
# https://sentry.io/answers/understand-the-purpose-of-uvicorn-in-fastapi-applications/
# https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface
# https://gunicorn.org/
# https://sentry.io/answers/number-of-uvicorn-workers-needed-in-production/
# https://fastapi.tiangolo.com/deployment/server-workers/

# Use the official Python image from the Docker Hub
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /code

# Install dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev postgresql-dev

# Copy the requirements file into the container
COPY ./requirements.txt /code/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir uvicorn && \
    pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the required files into the container
COPY ./app /code/app
COPY ./LICENSE /code/LICENSE
COPY ./VERSION /code/VERSION

# the find_root_dir function needs this file
COPY setup.py /code/setup.py

# Expose the port the app runs on
EXPOSE 80

# Command to run the application using environment variables with shell form
CMD uvicorn app.main:api --host 0.0.0.0 --port 80
