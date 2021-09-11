"""setup.py file."""
from setuptools import setup, find_packages
import re
import pathlib

with open("README.md", "r") as readme_md:
    long_description = readme_md.read()

with open("requirements.txt", "r") as fs:
    requirements = [line for line in fs.read().splitlines() if
                    (len(line) > 0 and not line.startswith("#"))]


def find_version(lib_path, file_type):
    base_module = next(pathlib.Path(lib_path).glob(file_type))
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        base_module.read_text(),
        re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="pyisc",
    version=find_version("pyisc", "__init__.py"),
    author="Jonas Hallqvist",
    author_email="jonas.hallqvist@outlook.com",
    description="A module for manipulation of various ISC files.",
    license="Apache 2.0",
    url="https://github.com/jhallqvist/pyisc",
    packages=find_packages(exclude=("test*",)),
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License"
    ],
    install_requires=requirements,
)
