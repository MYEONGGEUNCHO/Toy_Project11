from setuptools import find_packages, setup

setup(
    name='app',
    version='2.2.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)