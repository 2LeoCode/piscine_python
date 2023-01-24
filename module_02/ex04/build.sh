#!/bin/bash

if [ $1 == "--clean" ]; then
	rm -rf build dist *.egg-info
	exit 0
fi

pip install --upgrade pip
python setup.py sdist bdist_wheel
