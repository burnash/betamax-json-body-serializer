#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(filename):
    with open(filename) as f:
        content = f.read()
        return content


setup(
    name='betamax-json-body-serializer',
    author='Anton Burnashev',
    version='0.0.1',
    url='https://github.com/burnash/betamax-json-body-serializer',
    py_modules=['betamax_json_body_serializer'],
    install_requires=['betamax >= 0.3.2'],
    description=(
        'A third-party serializer for Betamax '
        'that includes a JSON version of the body.'
    ),
    keywords='betamax serializer',
    license=read('LICENSE'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
