"""
FileSort Pro — Setup Configuration
Cherry Computer Ltd.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="filesort-pro",
    version="1.0.0",
    author="Dr. Ahmad M. Ishanzai",
    author_email="ahmad@cherrycomputer.ltd",
    description="A lightweight Python CLI tool for intelligent directory organisation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Infinite-Networker/FileSort-Pro",
    py_modules=["filesort_pro"],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Utilities",
        "Topic :: System :: Filesystems",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
    ],
    entry_points={
        "console_scripts": [
            "filesort-pro=filesort_pro:main",
        ],
    },
    keywords="file sorting directory organisation cli tool filesystem",
)
