from distutils.core import setup

import sys

if sys.version_info.major < 3:
    print("bjoern-doc is python 3 only")
    print("installation failed")
    sys.exit(1)

setup(
    name='bjoern-doc',
    version='0.1',
    packages=['bjoerndoc'],
    scripts=['scripts/bjoerndoc'],
    url='',
    license='GPLv3',
    author='Alwin Maier',
    author_email='amaier@gwdg.de',
    description='Documentation tool for bjoern'
)
