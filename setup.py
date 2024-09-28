"""
This script is used to package the project into a distributable format.
"""
import sys
from setuptools import setup, find_packages

try:
    from semantic_release import setup_hook
    setup_hook(sys.argv)
except ImportError:
    pass

setup(
    packages=find_packages(exclude=["tests"]),
)
