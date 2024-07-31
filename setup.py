from setuptools import setup, find_packages

setup(
    name="testcontainer-fastapi-demo",
    version="0.1.0",
    description="An example project using testcontainers along with FastAPI.",
    author="Omar Crosby",
    author_email="omar.crosby@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pytest",
        "pytest-bdd",
        "testcontainers",
        "sqlalchemy",
        "pydantic",
    ],
    extras_require={
        "dev": [
            "black",
            "isort",
            "flake8",
        ],
    },
    python_requires=">=3.7",
)