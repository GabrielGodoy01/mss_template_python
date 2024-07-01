from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt') as req_file:
        return req_file.read().splitlines()

setup(
    name='core',
    version='0.1.0',
    package_dir={'core': '.'},
    packages=['core'],
    # install_requires=read_requirements(),
)