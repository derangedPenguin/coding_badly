from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Flow Fields',
    ext_modules=cythonize("flow_fields.py"),
)