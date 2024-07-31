.PHONY: install lint freeze

# Set the default task to lint
.DEFAULT_GOAL := lint


install:
	@pip install --upgrade pip
	@pip install -r requirements.txt


lint:
	@flake8 .
	@pylint $(shell find . -name "*.py" -not -path "./.venv/*")

freeze:
	@pip freeze > requirements.txt
