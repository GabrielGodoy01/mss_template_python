from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt') as req_file:
        return req_file.read().splitlines()

setup(
    name='core',
    version='0.1',
    package_dir={'shared': 'src/shared'},
    packages=['shared'],
    include_package_data=True,
    # install_requires=read_requirements(),
)