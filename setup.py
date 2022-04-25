#/usr/bin/env python
from setuptools import find_packages, setup

project = "hello-world"

version = "0.0.1"

setup(
    name=project,
    version=version,
    description="Basic python console app template",
    author="Andrey Shuster",
    author_email="andrey@shuster.im",
    url="",
    install_requires=[
        "click",
    ],
    setup_requires=[
        "pytest>=6.2.4",
        "isort>=5.8.0",
    ],
    entry_points={
        "console_scripts": [],
    },
    tests_require=[
        "coverage",
    ],
    extras_require=dict(
        lint=[],
        test=[],
        typehinting=[],
    ),
)
