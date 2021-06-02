#!/usr/bin/env python


import os

# allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# if __name__ == "__main__":
import setuptools

setuptools.setup(
    name='staff_management_models',
    version='1.0.4',
    packages=setuptools.find_packages(),
    install_requires=[
        'staff-models @ git+https://github.com/reimibeta/django-staff-models.git@4a245b6b9804dd897e98ca3af748ee7f8aae294d',
    ]
    # scripts=['manage.py']
)
