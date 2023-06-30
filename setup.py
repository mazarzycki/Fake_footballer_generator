from setuptools import setup

VERSION = '1.0' 
DESCRIPTION = 'A package to generate fake footballer data'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

setup(
    name='fake-footballer-generator',
    version='1.0',
    description='A package to generate fake footballer data',
    author='Marek Zarzycki',
    author_email='contact@mazarzycki.com',
    author_website='https://mazarzycki.com/',
    packages=['fake_footballer'],
    install_requires=[
        'pandas',
    ],
)
