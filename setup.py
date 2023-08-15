from setuptools import setup

VERSION = '1.0' 
DESCRIPTION = 'A package to generate fake footballer data'
LONG_DESCRIPTION = 'A package to generate fake footballer data and statistics for data science training purpose'

setup(
    name='footballfakedata',
    version='1.0',
    description='A package to generate fake footballer data and statistics',
    author='Marek Zarzycki',
    author_email='contact@mazarzycki.com',
    author_website='https://mazarzycki.com/',
    packages=['footballfakedata'],
    install_requires=[
        'pandas',
    ],
)
