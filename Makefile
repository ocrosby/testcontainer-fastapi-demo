.PHONY: install lint freeze

# Set the default task to lint
.DEFAULT_GOAL := lint


install:
	@echo "Upgrading pip..."
	@pip install --upgrade pip

	@echo "Installing dependencies..."
	@pip install -r requirements.txt


lint:
	@echo "Running linters..."
	@echo "Running flake8..."
	@flake8 .
	@echo "Running pylint..."
	@pylint --rcfile=setup.cfg $(shell find . -name "*.py" -not -path "./.venv/*")

freeze:
	@pip freeze > requirements.txt


