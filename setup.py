#!/usr/bin/env python


import os

# allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# if __name__ == "__main__":
import setuptools

setuptools.setup(
    name='staff_management_models',
    version='1.1.0',
    packages=setuptools.find_packages(),
    # install_requires=[
    #     'staff-models @ git+https://github.com/reimibeta/django-staff-models.git@993fd6e1a081f077a7f37ae2a7ad263b3db14d18',
    # ]
    # scripts=['manage.py']
)
