from setuptools import setup, find_packages


setup(
    name="optativa_pycicd",
    version="1.0.0",
    author="Boussoufi Amin",
    author_email="boussoufiamin@seup.net",
    description="Descripción de tu proyecto",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "flake8",
    ],
)