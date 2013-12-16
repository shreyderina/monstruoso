from setuptools import find_packages, setup

setup(
    name='monstruoso',
    version='0.1',
    description='RESTful API testing framework',
    long_description='',
    author='Igor Pavlov',
    author_email='nwlunatic@yandex.ru',
    packages=find_packages(),
    install_requires=[
        'human_curl',
        'nose',
    ],
)