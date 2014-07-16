# coding=utf-8

from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="pygwr",
    version="0.1.0",
    description="A simple GWR in Python",
    author="mkordi",
    author_email="maryam.kordi@gmail.com",
    maintainer="Olof Sjöbergh",
    maintainer_email="olofsj@gmail.com",
    url="https://github.com/olofsj/pygwr",
    license="GPLv3",
    packages=[
        "pygwr",
    ],
    long_description=read("README.md"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
)
