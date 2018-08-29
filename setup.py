# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
    name              = 'tacrypto',
    packages          = ['tacrypto'],
    version           = '0.1.11',
    description       = 'Technical Analysis Library in Python for Cryptocurrency',
    long_description  = 'Analyze Cryptocurrency technical analysis performance',
    author = 'Avinash Barnwal',
    author_email = 'avinash@inncretech.com',
    url = 'https://github.com/avinashbarnwal/tacrypto',
    maintainer='Avinash Barnwal',
    maintainer_email='avinash@inncretech.com',
    install_requires=[
        'numpy',
        'pandas'
    ],
    download_url = 'https://github.com/avinashbarnwal/tacrypto/tarball/0.1.11',
    keywords = ['technical analysis', 'python3', 'pandas','Cryptocurrency'],
    license='The MIT License (MIT)',
    classifiers = [],
)
