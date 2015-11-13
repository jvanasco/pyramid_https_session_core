"""pyramid_https_session_core installation script.
"""
import os

from setuptools import setup
from setuptools import find_packages

try:
    here = os.path.abspath(os.path.dirname(__file__))
    README = open(os.path.join(here, "README.md")).read()
    README = README.split("\n\n", 1)[0] + "\n"
except:
    README = ''

requires = [
    "pyramid",
]

setup(
    name="pyramid_https_session_core",
    version="0.0.2",
    description="provides for a 'session_https' secure session interface",
    long_description=README,
    classifiers=[
        "Intended Audience :: Developers",
        "Framework :: Pyramid",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="web pyramid beaker",
    packages=['pyramid_https_session_core'],
    author="Jonathan Vanasco",
    author_email="jonathan@findmeon.com",
    url="https://github.com/jvanasco/pyramid_https_session_core",
    license="MIT",
    include_package_data=True,
    zip_safe=False,
    tests_require = requires,
    install_requires = requires,
    test_suite='tests',
)