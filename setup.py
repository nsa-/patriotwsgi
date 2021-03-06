import os
from setuptools import setup, find_packages


def read(fname):
    try:
        with open(os.path.join(os.path.dirname(__file__), fname)) as fh:
            return fh.read()
    except IOError:
        return ''

requirements = read('REQUIREMENTS').splitlines()
tests_requirements = read('REQUIREMENTS-TESTS').splitlines()

setup(
    name="patriotwsgi",
    version="0.0.1",
    description="A WSGI Middleware that sends requests and responses to a datacenter somewhere in the US.",
    long_description=read('README.rst'),
    url='https://github.com/nsa-/patriotwsgi',
    license="NSL - National Security License",
    author='NSA',
    author_email='developers@nsa.gov',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'License :: Free To Use But Restricted'
    ],
    install_requires=requirements,
    tests_require=tests_requirements,
)
