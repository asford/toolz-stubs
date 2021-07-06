"""
Setup for toolz type annotations.
"""


from setuptools import setup
import os

setup(
    name="toolz-stubs",
    version="0.11.0.dev0",
    description="A collection of toolz stub files",
    long_description=(
        open("README.rst").read() if os.path.exists("README.rst") else ""
    ),
    url="https://github.com/zero323/toolz-stubs",
    packages=["toolz-stubs", "toolz-stubs.sandbox", "toolz-stubs.curried",],
    package_data={"": ["*.pyi", "py.typed"]},
    install_requires=["toolz>=0.11.0,<0.12.0"],
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Typing :: Typed",
    ],
)
