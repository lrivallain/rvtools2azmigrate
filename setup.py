#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.md") as history_file:
    history = history_file.read()

requirements = [
    "coloredlogs",
    "Click",
    "openpyxl",
    "rich",
]

setup_requirements = []

test_requirements = []

description = "Convert an RVTools export to an Azure Migrate CSV inventory file"
# In case of long description
# description +=

setup(
    author="Ludovic Rivallain",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description=description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "rvtools2azmigrate=rvtools2azmigrate.cli:cli",
            "rv2azm=rvtools2azmigrate.cli:cli",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="rvtools2azmigrate",
    name="rvtools2azmigrate",
    packages=find_packages(include=["rvtools2azmigrate", "rvtools2azmigrate.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/lrivallain/rvtools2azmigrate",
    version="0.1.2",
    zip_safe=False,
)
