from setuptools import find_packages, setup

setup(
    name="Lab2",
    version="1.0",
    packages=find_packages(include=['modules', 'modules.*']),
    entry_points={
      'console_scripts': [
        'parser=modules.main:main',
      ],
    },
    install_requires=[
    'atomicwrites==1.4.0',
    'attrs==21.2.0',
    'colorama==0.4.4',
    'iniconfig==1.1.1',
    'packaging==21.0',
    'pluggy==1.0.0',
    'py==1.10.0',
    'pyparsing==2.4.7',
    'pytest==6.2.5',
    'PyYAML==5.4.1',
    'toml==0.10.2'

    ]
 )