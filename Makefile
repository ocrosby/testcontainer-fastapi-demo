.PHONY: install lint freeze

# Set the default task to lint
.DEFAULT_GOAL := run

# Define variables
IMAGE_NAME = testcontainer-fastapi-demo
IMAGE_TAG = latest

venv:
	@echo "Creating virtual environment..."
	@python3 -m venv .venv

install:
	@echo "Upgrading pip..."
	@python3 -m pip install --upgrade pip

	@echo "Installing dependencies..."
	@python3 -m pip install -r requirements.txt

	@echo "Checking if .env file exists..."
	@if [ ! -f .env ]; then \
	 echo "Copying example.env to .env..."; \
	 cp example.env .env; \
	fi

clean:
	@echo "Cleaning up..."
	@rm -f *.log
	@find . -name "junit.xml" -type f -delete
	@find . -name "report" -type d -exec rm -rf {} +
	@find . -name "__pycache__" -type d -exec rm -rf {} +
	@find . -name "*.pyc" -type f -delete
	@find . -name "*.pyo" -type f -delete
	@find . -name "*.pyd" -type f -delete
	@find . -name "*.pyz" -type f -delete
	@find . -name "app.log" -type f -delete

lint:
	@echo "Running linters..."
	@echo "Running flake8..."
	@flake8 .
	@echo "Running pylint..."
	@pylint --rcfile=setup.cfg $(shell find . -name "*.py" -not -path "./.venv/*")

test: clean lint
	@echo "Running Unit Tests..."
	@coverage run -m pytest -m unit -v
	@echo "Done"

freeze:
	@pip freeze > requirements.txt


build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) --quiet .


# Note: The HOST and PORT environment variables are used to set the host and port for the FastAPI server
# Note: The -p flag is used to map the host port to the container port
#       The format is -p <host_port>:<container_port>

run: build
	@echo "Server is running on http://localhost:8080/docs"
	docker run -e HOST=0.0.0.0 -e PORT=80 -p 8080:80 $(IMAGE_NAME):$(IMAGE_TAG)

#	@echo "To stop the server, run 'docker ps' to get the container ID and then run 'docker stop <container_id>'"