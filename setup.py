# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf8') as f:
    long_description = f.read()

with open(path.join(here, 'src/pydips/version.py'), encoding='utf8') as f:
    exec(f.read())

setup(
    name='pydips',
    version=__version__,
    description='Multi-criteria Cantonese segmentation with dashes, intermediates, pipes, and spaces.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ayaka14732/cantoseg',
    author='Kevin Xiang Li',
    author_email='kevinx.li@outlook.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
        'Natural Language :: Cantonese',
        'Natural Language :: Chinese (Traditional)',
        'Operating System :: MacOS :: MacOS X',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ],
    keywords='cantonese chinese natural-language-processing',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={
        'pydips': ['../models/electra-small-6-layers-q4_0.gguf', '../binaries/macos/libbert.dylib'],
    },
    include_package_data=True,
    python_requires='>=3.10, <4',
    entry_points={},
    project_urls={
        'Bug Reports': 'https://github.com/AlienKevin/dips/issues',
        'Source': 'https://github.com/AlienKevin/dips',
    }
)