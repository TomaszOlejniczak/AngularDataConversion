from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read()

setup(
    name='rms',
    version='1.0.0',
    description='D',
    packages=find_packages(exclude='docs'),
    platforms='Posix; MacOS X; Windows',
    include_package_data=False,
    zip_safe=False,
    install_requires=requirements,
)
