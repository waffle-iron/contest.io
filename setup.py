from setuptools import setup

setup(
    name='contest.io',
    packages=['server'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)