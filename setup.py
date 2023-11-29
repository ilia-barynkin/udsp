from setuptools import setup, find_packages

setup(
    name='udsp',
    version='0.0.1',
    author='Ilia Barynkin',
    description='Digital signal processing playground',
    packages=find_packages(),
    install_requires=[
        'numpy >= 1.26.0',
        'matplotlib >= 3.8.0',
        'pandas >= 2.1.0'
    ],
)