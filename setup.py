import sys

try:
    # noinspection PyUnresolvedReferences
    from setuptools import setup
except ImportError:
    print("Test result reporter now needs setuptools in order to build. Install it using"
          " your package manager (usually python-setuptools) or via pip (pip"
          " install setuptools).")
    sys.exit(1)

__version__ = '0.0.1'
__author__ = 'dimorinny'

setup(
    name='py-rockyou',
    version=__version__,
    description='Brute force dictionary',
    author=__author__,
    author_email='didika914@gmail.com',
    package_dir={'rockyou': 'rockyou'},
    packages=['rockyou'],
    include_package_data=True
)
