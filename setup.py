import os
from setuptools import setup, find_packages

packages = find_packages()
packages.remove('sample_project')

classifiers = """
Topic :: Internet :: WWW/HTTP :: Dynamic Content
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Programming Language :: Python
Topic :: Software Development :: Libraries :: Python Modules
Development Status :: 4 - Beta
"""

setup(
    name='django-pagelets',
    version='0.5',
    author='Caktus Consulting Group',
    author_email='solutions@caktusgroup.com',
    packages=packages,
    install_requires = [],
    include_package_data = True,
    exclude_package_data={
        '': ['*.sql', '*.pyc'],
        'pagelets': ['media/*'],
    },
    url='http://http://github.com/caktus/django-pagelets',
    license='LICENSE.txt',
    description='Simple, flexible app for integrating static, unstructured '
                'content in a Django site',
    classifiers = filter(None, classifiers.split("\n")),
    long_description=open('README.rst').read(),
)
