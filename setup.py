from setuptools import setup

VERSION = '1.0' 
DESCRIPTION = 'A package to generate fake footballer data'
LONG_DESCRIPTION = 'A package to generate fake footballer data'

setup(
    name='fake_footballer_generator',
    version='1.0',
    description='A package to generate fake footballer data',
    author='Marek Zarzycki',
    author_email='contact@mazarzycki.com',
    author_website='https://mazarzycki.com/',
    packages=['fakefootballer'],
    install_requires=[
        'pandas',
    ],
)
