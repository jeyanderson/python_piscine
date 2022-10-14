python -m pip install --upgrade pip wheel setuptools
python setup.py sdist bdist_wheel
pip install ./dist/my_minipack-1.0.0-py3-none-any.whl