import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pypiece",
    version = "0.1.0",
    author = "Kirill Borisov",
    author_email = "lensvol@gmail.com",
    description = ("Wrapper around pip for flakey connections."),
    license = "MIT",
    keywords = "pip",
    url = "https://github.com/lensvol/pypiece",
    packages=['pypiece'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
