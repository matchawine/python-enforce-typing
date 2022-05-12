#!/usr/bin/env python

from os import path
from io import open
from setuptools import setup, find_packages
from enforce_typing import get_version

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

if __name__ == "__main__":
    setup(
        name="enforce-typing",
        version=get_version(),
        description=("An easy to use decorator to enforce static typing"
                     " for functions and dataclasses."),
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        author="Joshua Logan",
        author_email="joshua@matcha.wine",
        url="https://github.com/matchawine/python-enforce-typing",
        packages=find_packages(),
        license="GPL",
        keywords="decorators typing",
        python_requires=">=3.5",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Plugins",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU General Public License (GPL)",
            "Operating System :: OS Independent",
            "Natural Language :: English",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    )
