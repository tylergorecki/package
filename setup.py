from setuptools import setup

setup(
    name = 'PackageName', 
    version = '1.0.0', 
    url = 'https://github.com/tylergorecki/package', 
    author = 'Tyler Gorecki', 
    author_email = 'ttg6nx@virginia.edu', 
    description = 'Package description', 
    long_description = open('README.txt').read(), 
    install_requires = ['pandas']
)
