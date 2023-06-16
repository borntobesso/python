#!/bin/bash
python3 -m pip install --upgrade pip setuptools wheel
python3 setup.py sdist bdist_wheel
pip install ./dist/my_minipack-1.0.0.tar.gz