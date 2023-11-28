from setuptools import setup, find_packages

setup(
    name='hookity',
    version='0.1',
    packages=find_packages(),
    package_data={'hookity': ['resources/*']},
    entry_points={
        'console_scripts': [
            'hookity = lib.core:main',
        ],
    },
)