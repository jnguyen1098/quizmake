# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Setup module for setuputils-esque tools that support it.

I don't really know how these work.
"""

import setuptools

with open("README.rst", "r") as fd:
    long_description = fd.read()

with open("LICENSE") as fd:
    license = fd.read()

setuptools.setup(
    name="quizmake",
    version="0.1.5",
    author="jnguyen1098",
    description="Question generator package for Moodle",
    install_requires=["wheel", "pyparsing"],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/jnguyen1098/quizmake",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Education",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3",
        "Topic :: Education :: Testing",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="moodle",
    python_requires=">=3.7",
)
