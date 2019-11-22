#!/bin/bash
PROJECT_ROOT="$(git rev-parse --show-toplevel)"
DOCS_DIR="doc"
cd ${PROJECT_ROOT}
if [[ -d "${PROJECT_ROOT}/${DOCS_DIR}" ]]
then
    echo "Generating docs"
    python setup.py build_sphinx
fi
echo "Creating sdist"
python setup.py sdist --formats=gztar
echo "Creating wheel package"
python setup.py bdist_wheel
echo "Uploading via twine"
twine upload dist/*
