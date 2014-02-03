#!/usr/bin/env python3
from distutils.core import setup

setup(
    name='jinja-hamlike',
    version='HEAD',
    description='A minimalistic indentation-sensitive markup preprocessor',
    author='pyos',
    author_email='pyos100500@gmail.com',
    url='https://github.com/pyos/jinja-hamlike',
    packages=['hamlike'],
    package_dir={'hamlike': '.'},
    package_data={'hamlike': ['*.dg']}
)
