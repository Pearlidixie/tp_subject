# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='tp-subject',
    version='1',
    author=u'Pearl Malapeng',
    author_email='pmalapeng@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/Pearlidixie/tp_subject',
    license='GPL license, see LICENSE',
    description='Determine subject consent and other subject personal information',
    long_description=README,
    zip_safe=False,
    keywords='django tp_subject',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
