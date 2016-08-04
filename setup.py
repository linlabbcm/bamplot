
import os

from setuptools import setup, find_packages



setup(
    name='bamplot',
    version='0.8.0',
    description='bamplot python package',
    long_description='program to make plots of bam read density at specific loci',
    url='https://github.com/linlabbcm/bamplot',
    download_url = 'https://github.com/linlabbcm/bamplot/tarball/v0.8.0',
    

    classifiers=[],

    keywords=['bioinformatics','bam','SEQ','plotting'],

    packages=find_packages(),
    package_data={
    'bamplot': ['annotation/*'],
        },

    install_requires=[],
    extras_require={},

    scripts=['scripts/bamplot_plotter.R'],

    entry_points={
            'console_scripts': [
                        'bamplot=bamplot:main',
                        ]
            },

)
