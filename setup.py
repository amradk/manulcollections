from setuptools import setup

setup(
    name='mylibrary',
    packages=['mylibrary'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
