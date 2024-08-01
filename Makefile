.PHONY: install lint freeze

# Set the default task to lint
.DEFAULT_GOAL := test


install:
	@echo "Upgrading pip..."
	@pip install --upgrade pip

	@echo "Installing dependencies..."
	@pip install -r requirements.txt


clean:
	@echo "Cleaning up..."
	@find . -name "junit.xml" -type f -delete
	@find . -name "report" -type d -exec rm -rf {} +

lint:
	@echo "Running linters..."
	@echo "Running flake8..."
	@flake8 .
	@echo "Running pylint..."
	@pylint --rcfile=setup.cfg $(shell find . -name "*.py" -not -path "./.venv/*")

test: clean lint
	@echo "Running Unit Tests..."
	@pytest -m unit -v
	@echo "Done"

freeze:
	@pip freeze > requirements.txt


