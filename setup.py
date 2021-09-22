#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
@Project: rulesHandler
@File: setup.py.py
@Author: Symoon
@Date: 2021/9/14 下午5:27
"""

from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()
setup(
    name="python-validation-rules",
    packages=["ValidationRules"],
    version="0.1.13",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Symoon",
    author_email="symoon.gao@gmail.com",
    url="https://github.com/Gaoshengyue/validationRules",
    download_url="https://github.com/Gaoshengyue/validationRules/releases/tag/v0.1.13",
    keywords=["python-validation-rules", "validation-rules"],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent"

    ], install_requires=['pydantic >=1.5.1']
)
