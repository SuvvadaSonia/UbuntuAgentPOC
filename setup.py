from setuptools import setup, find_packages

# to use consistent encoding
from codecs import open
from os import path


# the directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="remote-agent",
    version="0.1.0",
    description="Demo library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://medium-multiply.readthedocs.io/",
    author="Vinodh Kumar Adari",
    author_email="vinod.codes@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["connector"],
    include_package_data=True,
    install_requires=["paramiko",]
)
