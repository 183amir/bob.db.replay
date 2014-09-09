#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Sex 10 Ago 2012 14:22:33 CEST

from setuptools import setup, find_packages

# The only thing we do in this file is to call the setup() function with all
# parameters that define our package.
setup(

    name='bob.db.replay',
    version='2.0.0a0',
    description='Replay Attack Database Access API for Bob',
    url='http://pypi.python.org/pypi/bob.db.replay',
    license='GPLv3',
    author='Andre Anjos, Ivana Chingovska',
    author_email='andre.anjos@idiap.ch, ivana.chingovska@idiap.ch',
    long_description=open('README.rst').read(),

    # This line is required for any distutils based packaging.
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    install_requires=[
      'setuptools',
      'six',
      'antispoofing.utils',
      'bob.db.base',
    ],

    namespace_packages = [
      'bob',
      'bob.db',
      ],

    entry_points = {
      # bob database declaration
      'bob.db': [
        'replay = bob.db.replay.driver:Interface',
        ],

      # antispoofing database declaration
      'antispoofing.utils.db': [
        'replay = bob.db.replay.spoofing:Database',
        ],
      },

    classifiers = [
      'Development Status :: 4 - Beta',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'Topic :: Database :: Front-Ends',
      ],
)
