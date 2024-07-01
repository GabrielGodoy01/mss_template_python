from setuptools import setup, find_packages

setup(
    name='core',
    version='0.1',
    package_dir={'shared': 'shared'},
    packages=['shared'],
    include_package_data=True,
    install_requires=[
        # Lista de dependências do core application, ou
        # você pode ler de requirements.txt se preferir
        # 'requests', 'flask', etc.
    ],
)