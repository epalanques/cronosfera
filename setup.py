from pip._vendor import pytoml
from setuptools import setup, find_packages

with open('Pipfile', 'r') as _pipfile:
    _PIPFILE_CONTENTS = pytoml.load(_pipfile)

setup(
    name='cronosfera',
    version='0.0',
    url='https://nanoporetech.com',
    author='Eric Palanques',
    author_email='eric.palanques@gmail.com',
    description='Project to visualise the history of the world',
    long_description='Locate events in three dimensions: eras, location and biology',
    packages=find_packages(
        exclude=[],
        include=['time*']),
    data_files=[('.', ['Pipfile']), ],
    install_requires=list(_PIPFILE_CONTENTS['packages'].keys()))
