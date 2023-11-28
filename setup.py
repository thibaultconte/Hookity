from setuptools import setup, find_packages

setup(
    name='hookity',
    author="Thibault Conte",
    author_email="thibault1.conte@epitech.eu",
    description="Improve branch and commit message authorization for collaborator"
    version='0.1',
    packages=find_packages(),
    package_data={'hookity': ['resources/*']},
    install_requires=[
        'jq',
    ],
    entry_points={
        'console_scripts': [
            'hookity = lib.core:main',
        ],
    },
)