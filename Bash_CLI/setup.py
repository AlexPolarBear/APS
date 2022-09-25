from setuptools import setup, find_packages

setup(
    name='Bash command line interface',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bash_cli = src.main:main',
        ]
    },
)
