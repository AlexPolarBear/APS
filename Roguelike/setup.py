from setuptools import setup, find_packages

setup(
    name='Our roguelike game',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'play_rog = src.main:main',
        ]
    },
)
